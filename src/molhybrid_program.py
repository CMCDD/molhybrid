#!/usr/bin/env python3

import pandas as pd
import os
import argparse
from rdkit import Chem
from rdkit.Chem import AllChem
import random
import molhybrid
from molhybrid import src
from molhybrid.src import inputs, randomm, main, optimize 
from molhybrid.src.inputs import input_molecules, read_pharmacophores, read_linker, read_parameters
from molhybrid.src.randomm import validate_smiles, machanics, stores, combine_smiles, combine_multiple_molecules, hybridize_molecules, convert_mols_to_3d_sdf
from molhybrid.src.main import genarator, check_duplicates
from molhybrid.src.optimize import MoleculeOptimizer


def gen_hybrids(filename, duplicates=None, opt=None, NP=4, output_type=None):
    
    l, cleaned,structures = genarator(filename)
    if duplicates == 'T' or duplicates == 'True':
        rm_cleand = check_duplicates(cleaned)
    else:
        rm_cleand = cleaned
        
    if opt == 'optimize':
        optimizer = MoleculeOptimizer(rm_cleand, num_threads=NP)
        
        if output_type == 'Single' or output_type == 'single':
            w = convert_mols_to_3d_sdf(optimizer, output_file_prefix='output')
            
        elif output_type == 'Multiple' or output_type == 'multiple':
            w = Chem.SDWriter('./optimizedmolecules.sdf')
            for o in optimizer:
                w.write(o)
        else:
            raise ValueError("Incorrect input type argument. Please use 'single' for a single SDF output file and 'multiple' for multiple SDF outputs.")
            
    elif opt == 'no_optimize' or opt is None:
        
        if output_type == 'Single' or output_type == 'single':
            w = convert_mols_to_3d_sdf(rm_cleand, output_file_prefix='output')
            
        elif output_type == 'Multiple' or output_type == 'multiple':
            w = Chem.SDWriter('./optimizedmolecules.sdf')
            for o in rm_cleand:
                w.write(o)
        else:
            raise ValueError("Incorrect input type argument. Please use 'single' for a single SDF output file and 'multiple' for multiple SDF outputs.")
            
    else:
        raise ValueError("Incorrect opefault=t argument. Please use 'optimize' for optimization and 'no_optimize' for no optimization.")
    
    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Run Molhybrid program")
    parser.add_argument("filename", type=str, help="Input filename containing molecular data")
    parser.add_argument("--duplicates", type=str, choices=['T', 'True', 'F', 'False'], default='False', help="Check and remove duplicates")
    parser.add_argument("--opt", type=str, choices=['optimize', 'no_optimize'], default='no_optimize', help="Optimization flag")
    parser.add_argument("--NP", type=int, default=4, help="Number of parallel threads")
    parser.add_argument("--output_type", type=str, choices=['Single', 'Multiple'], default='Single', help="Output file format")
    
    args = parser.parse_args()
    gen_hybrids(args.filename, args.duplicates, args.opt, args.NP, args.output_type)
