# Molhybrid
---
## About
Molecular hybridization is a powerful computational tool used in drug discovery that generates hybrids based on a given pharmacophore core structure. The tool randomly combines the pharmacophoric fragments from known bioactive compounts within an existing chemical space and thus generate a library of molecules. 

---
## Prerequisites 

- **Operating System:** Linux
- **Python Version:** Python 3.9 with the installation of dependencies, installed with command line conda install python = 3.9 , conda install anaconda-navigator
- **Required Python Packages:** ``
- **External Dependencies:** This requires the presence of openbabel and installed with the command conda install -c conda-forge openbabel
---
## Usage

In order to access the user manual, runn the following command
```bash
   molhybrid -h

###### Arguments

 -h, --help:
-duplicates {T,true,f,false} (T or true shows the duplicates available and f or false do not show the available duplicates)
                    
--opt {optimize, no_optimize) ( allows for optimization or no optimazation of the structures)
                    perform MMFF optimization(default off)
--NP, {Np} (The number of parallel threads)
--ouput_type {single,Multiple} (output file format)


## Installation

### Internal Dependencies

To install the required internal dependencies, execute the following command in the terminal from the home directory:

Step 1: Set up a Conda environment named molhybrid

```

```bash
conda create --name molhybrid python=3.9

```
Step 2: Launch environment

```bash
conda activate molhybrid
```
Step 3: Go to the site-packages folder
Navigate to the directory where Python libraries are installed (typically under lib/python3.9/site-packages) within your Conda environment
`````

```bash
cd anaconda3/envs/molhybrid/lib/python3.9/site-packages/

```
Step 4: Download the Repository from GitHub
Use git to clone the T_SELEX software repository to your local computer

--bash
git clone https://github.com/CMCDD/T_SELEX.git

```
Step 5: Install Required Packages via Script
Run the provided Python script to automatically install all dependencies

```

--bash
python install_dependencies.py
```

Step 6: Make the Main Script Executable
Grant execution permissions to the molhybrid_program.py script

```
Step 7: Move Script to System Path for Global Use
Copy the script to a system-wide binary directory so it can be run from anywhere

```

--bash
sudo cp molhybrid_program.py /usr/local/bin/molhybrid_program
```
Step 8: Verify Installation
Run the command to confirm everything is working properly

--bash
molhybrid_program

```





