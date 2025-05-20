

from rdkit import Chem
from rdkit.Chem import AllChem
import random
from .inputs import input_molecules, read_pharmacophores, read_linker, read_parameters
from .randomm import validate_smiles, machanics, stores, combine_smiles, combine_multiple_molecules, hybridize_molecules, convert_mols_to_3d_sdf

def genarator(file_name):
    
    smiles_input, len_linkers = input_molecules(file_name)
       
    replacements = smiles_input
    molecule_list = []
    num_molecules, num_hybrids = read_parameters(file_name)

    nums_ = list(range(num_molecules + 1))
    del nums_[0]  # Remove the first two elements
    del nums_[0]

    try:
        valid_smiles = validate_smiles(smiles_input)
        hybridized_molecules = hybridize_molecules(valid_smiles, num_hybrids=num_hybrids, num_molecules=len(nums_))
        
        # Convert hybridized SMILES to Mol objects
        cleaned_smiles = []
        structures = []
        
        for smi in hybridized_molecules:
            for replacement in replacements:
                smi_cleaned = smi.replace('.', replacement).replace('OO', 'O')
                cleaned_smiles.append(smi_cleaned)
                smi_cleaned = replacement + smi_cleaned  
                cleaned_smiles.append(smi_cleaned)
                
                for len_add in range(min(len_linkers + 1, len(replacements))):
                    first_add = replacements[len_add] + smi_cleaned 
                    cleaned_smiles.append(first_add)
                    second_add = smi_cleaned + replacements[len_add]
                    cleaned_smiles.append(second_add)
                    both_add = replacements[len_add] + smi_cleaned + replacements[len_add]
                    cleaned_smiles.append(both_add)
                
                mol = Chem.MolFromSmiles(smi_cleaned)
                if mol:
                    structures.append(mol)
                else:
                    print(f"Invalid SMILES: {smi_cleaned}")
        
        return hybridized_molecules, structures, cleaned_smiles
    
    except ValueError as e:
        print(e)
        return [], [], []
    
def check_duplicates(smiles_list):
    fingerprint_map = {} 
    unique_molecules = [] 
    smiles_ = []  
    unique = set()  
    mols = []  
    
    for smiles in smiles_list:
        
        mol = Chem.MolFromSmiles(smiles)

        if mol is None:  
            continue

        
        fingerprint = AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=2048)
        fp = fingerprint.ToBitString()

        
        if fp not in unique:
            unique.add(fp)
            unique_molecules.append(mol)  
            smiles_.append(smiles) 
            mols.append(mol) 
    return mols

if __name__ == "__main__":
    l, structures, cleaned = main()
    print("Done___________________________Done")
