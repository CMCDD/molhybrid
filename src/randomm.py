#!/usr/bin/env python3
from rdkit import Chem
from rdkit.Chem import AllChem
import random

def validate_smiles(smiles_list):
    """Validate SMILES strings and ensure there are at least 10 valid strings."""
    
    valid_smiles = []
    
    for smile in smiles_list:
        
        if Chem.MolFromSmiles(smile):
            
            valid_smiles.append(smile)
            
    if len(valid_smiles) < 10:
        
        raise ValueError("You must provide at least 10 valid SMILES strings.")
        
    return valid_smiles

def machanics(smiles):
    """Generate random variations of the given SMILES based on its substructures."""
    
    mols = []
    
    m = Chem.MolFromSmiles(smiles)
    
    if m:
        
        variations = Chem.MolToRandomSmilesVect(m, 100)
        
        for var in variations:
            
            mol = Chem.MolFromSmiles(var)
            
            if mol:
                
                mols.append(var)
    return mols

def stores(pharmacophores):
    
    """Store the random variations of each pharmacophore."""
    
    storage_pharms = []
    
    for pharm in pharmacophores:
        
        storage_pharms.append(machanics(pharm))
        
    return storage_pharms

def combine_smiles(smile1, smile2):
    
    """Combine two SMILES strings into a new hybrid."""
    
    mol1 = Chem.MolFromSmiles(smile1)
    mol2 = Chem.MolFromSmiles(smile2)
    
    if mol1 is None or mol2 is None:
        return None

    hybrid_mol = Chem.RWMol()
    atom_map = {}
    start_index = 0

    for mol in [mol1, mol2]:
        
        for atom in mol.GetAtoms():
            
            idx = hybrid_mol.AddAtom(atom)
            
            atom_map[atom.GetIdx() + start_index] = idx

        for bond in mol.GetBonds():
            
            hybrid_mol.AddBond(
                atom_map[bond.GetBeginAtomIdx() + start_index],
                atom_map[bond.GetEndAtomIdx() + start_index],
                bond.GetBondType()
            )
        
        start_index += mol.GetNumAtoms()

    return Chem.MolToSmiles(hybrid_mol)

def combine_multiple_molecules(molecule_list):
    """Combine multiple RDKit molecules into a new one."""
    
    hybrid_mol = Chem.RWMol()
    atom_map = {}
    start_index = 0

    for mol in molecule_list:
        
        for atom in mol.GetAtoms():
            
            idx = hybrid_mol.AddAtom(atom)
            atom_map[atom.GetIdx() + start_index] = idx

        for bond in mol.GetBonds():
            
            hybrid_mol.AddBond(
                atom_map[bond.GetBeginAtomIdx() + start_index],
                atom_map[bond.GetEndAtomIdx() + start_index],
                bond.GetBondType()
            )

        start_index += mol.GetNumAtoms()

    return Chem.MolToSmiles(hybrid_mol)

def hybridize_molecules(smiles_list, num_hybrids=5, num_molecules=2):
    
    """Generate hybridized molecules from given SMILES."""
    
    hybridized_smiles = []
    
    for _ in range(num_hybrids):
        
        selected_molecules = [Chem.MolFromSmiles(random.choice(smiles_list)) for _ in range(num_molecules)]
        
        combined_smiles = combine_multiple_molecules(selected_molecules)
        
        if combined_smiles:
            
            hybridized_smiles.append(combined_smiles)
    
    return hybridized_smiles


def try_embedding(mol, max_attempts=200):
    methods = [
        AllChem.ETKDG(),
        AllChem.ETKDGv3(),
        AllChem.ETKDGv2(),
        None,
        {'useRandomCoords': True},
    ]
    attempts = 0

    while attempts < max_attempts:
        for method in methods:
            try:
                if method is None:
                    status = AllChem.EmbedMolecule(mol)
                elif isinstance(method, dict):
                    status = AllChem.EmbedMolecule(mol, **method)
                else:
                    status = AllChem.EmbedMolecule(mol, method)

                if status == 0:
                    return True
            except:
                pass
        attempts += 1

    return False

def convert_mols_to_3d_sdf(mols, output_file_prefix='output'):
    output_file = f"{output_file_prefix}.sdf"
    #writer = Chem.SDWriter(output_file)

    for idx, mol in enumerate(mols):
        if mol is None:
            continue

        mol = Chem.AddHs(mol)

        if not try_embedding(mol):
            continue

        try:
            AllChem.UFFOptimizeMolecule(mol)
        except:
            continue
        writer = Chem.SDWriter(f'{output_file_prefix}_{idx + 1}.sdf')
        writer.write(mol)

    writer.close()
