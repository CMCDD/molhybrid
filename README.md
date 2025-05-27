# Molhybrid
---
## About
Molecular hybridization is a powerful computational tool used in drug discovery that generates hybrids based on a given pharmacophore core structure. The tool randomly combines the pharmacophoric fragments from known bioactive compounts within an existing chemical space and thus generate a library of molecules. 

---
## Prerequisites and  Installation

- **Operating System:** Linux
- **Python Version:** Python 3.9 with the installation of dependencies, installed with command line conda install python = 3.9 , conda install anaconda-navigator
- **Required Python Packages:** ``
- **External Dependencies:** This requires the presence of openbabel and installed with the command conda install -c conda-forge openbabel
---
## Usage

In order to access the user manual, runn the following 
```bash
command molhybrid -h

###### Arguments

 -h, --help:
-duplicates {T,true,f,false} (T or true shows the duplicates available and f or false do not show the available duplicates)
                    
--opt {optimize, no_optimize) ( allows for optimization or no optimazation of the structures)
                    perform MMFF optimization(default off)
--NP, {Np} (The number of parallel threads)
--ouput_type {single,Multiple} (output file format)
