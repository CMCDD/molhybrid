# Molhybrid
---
## About
Molecular hybridization is a powerful computational tool used in drug discovery that generates hybrids based on a given pharmacophore core structure. The tool randomly combines the pharmacophoric fragments from known bioactive compounts within an existing chemical space and thus generate a library of molecules. 

---
## System Requirements 

- **Operating System:** Linux
- **Python Version:** Python 3.9 with the installation of dependencies, installed with command line conda install python = 3.9 , conda install anaconda-navigator
- **Required Python Packages:**  rdkit==2024.03.5
- **External Dependencies:** This requires the presence of RDkit and openbabel which is installed with the command conda install -c conda-forge openbabel
---
## Usage

In order to access the user manual, run the following command
```bash
   molhybrid -h
```
The output should print the folling on the terminal:

```bash
###### Arguments

 -h, --help:
-duplicates {T,true,f,false} (T or true shows the duplicates available and f or false do not show the available duplicates)
                    
--opt {optimize, no_optimize) ( allows for optimization or no optimazation of the structures)
                    perform MMFF optimization(default off)
--NP, {Np} (The number of parallel threads)
--ouput_type {single,Multiple} (output file format)

```
In order the to run the molhbrid program, inputs parameters are required can be detailed in a configuration file with **.ini** extension. The molhbrid program uses a configuration file in .ini format to define the parameters and molecular components required for hybrid molecule generation. The configuration file consists of three main sections: **parameters**, **linkers**, and **pharmacophores**.The example of an input configuration is shown below.

```ini

///parameters
#max_hybrids = 20000
#max_asymble = 10

///Molecules

//linkers
#l1 CCO                                            : # Ethoxy group
#l2 CC(=O)O                                        : # Isopropyl group
#l3 CC(=O)CC                                       :  # Butyl group
#l4 C1=CC=CC=C1                                    : # Benzene ring
#l5 C1CCCCC1                                      :   # Cyclohexane ring
#l6 C@@C                                           :   # Stereochemistry notation
#l7 C#C                                            : # Triple bond

//pharmacophores
#P1 CNC1=C2C=CC(Cl)=CC2=NC=C1                      :  # Specific heterocyclic structure
#P2 c1(ccc(cc1)S(=O)(N)=O)N                        :  # Another aromatic sulfonamide group3
#P3 S(=O)(c1ccc(N)cc1)(=O)N(C)C                    :  # Another sulfonamide group
#P4 CN(S(c1ccc(cc1)N)(=O)=O)C                      :  # Another functionalized amide
#P5 N1C2NCC(=NC2C(NC=1N)=O)C                       :  # Another heterocyclic structure
#P6 CN[C@H]1CC(O[C@@H]1COC)N1C=C(C)C(=O)NC1=O     :  # Complex structure
#P7 CCC1=NC(N)=NC(N)=C1C                           :  # Another complex structure
#P8 CN1CCNCC1                                      :  # A cyclic amine
#P9 [H][C@@]1(C)CN(C)CCN1                          :  # Stereochemical notation with amines
#P10 [H]N1CCC[C@]2([H])CN(C)C[C@]12[H]              :  # Another stereochemically complex structure
#P11 CN1CCCC[C@@H](N)C1                             :  # Another cyclic structure with nitrogen
```

The parameters section includes global settings that control the behavior of the program. For this example, `max_hybrids` sets the maximum number of hybrid molecules to be generated (e.g., 20,000), and `max_asymble` limits the possible number of linker and pharmacophores that can be assembled per hybrid (e.g., 10). These parameters allow users to manage the scale and complexity of the output.
n the molecules section, users can define molecular building blocks used in the hybridization process. **Linkers** are identified with *#lX* are small chemical fragments such as ethoxy groups (CCO), benzene rings (C1=CC=CC=C1), or cyclohexane rings (C1CCCCC1). These fragments function as connectors between pharmacophores. **Pharmacophores** are identified with *#PX*, are more complex molecular structures that contribute specific functional or biological properties to the final hybrids. Examples include heterocyclic structures, sulfonamides, functionalized amides, and chiral amine rings, all represented in SMILES format.

Each entry starts with a comment character **(#)**, followed by a unique identifier (e.g., **#l1**, **#P3**), the SMILES string representing the molecule, and a description comment that explains the structure in simple terms. Descriptions following colons **(:)** are for user reference only and are ignored during execution.

## Installation

### Internal Dependencies

From your home directory, open a terminal and execute the command below to install the required internal components:

Step 1: Set up a Conda environment named molhybrid
```bash
conda create --name molhybrid python=3.9
```
Step 2: Launch/activate environment
```bash
conda activate molhybrid
```
Step 3: Go to the site-packages folder of you molhbrid anaconda enviroment
Navigate to the directory where Python libraries are installed (typically under lib/python3.9/site-packages) within your Conda environment
```bash
cd anaconda3/envs/molhybrid/lib/python3.9/site-packages/
```
Step 4: Download the Repository from GitHub
Use git to clone the T_SELEX software repository to your local computer
```bash
git clone https://github.com/CMCDD/molhybrid.git
```
Step 5: Install Required Packages via Script
Run the requirement.txt for installing the dependencies.

```bash
pip install -r requirements.txt
```
Step 6: Make the Main Script Executable
Grant execution permissions to the molhybrid_program.py script
```bash
sudo cp molhybrid_program.py /usr/local/bin/molhybrid
```
Step 7: Verify Installation
Run the command to confirm everything is working properly
```bash
molhybrid -h
```

```
## Examples

An example two pharmacophore core molecule is the



)


### Example 
You need to input two or more pharmacophore SMILES STRINGS along with linkers, such as functional groups, into the software, which will then generate a molecular library.
Linkers
'CCO', # Ethanol 'CC(=O)O', # Acetic acid, 'CC(C)C', # Isobutane

Pharmacophores
CNC1=C2C=CC(Cl)=CC2=NC=C1','CC1=C(C)C2=C(NN=C2)N=C1', 'c1(ccc(cc1)S(=O)(N)=O)N',

Generated molecules

```
![alt text](https://github.com/CMCDD/molhybrid/blob/main/graphics/Pharmacophore.png)

![alt text](https://github.com/CMCDD/molhybrid/blob/main/graphics/Ligandscleaned2.png)

