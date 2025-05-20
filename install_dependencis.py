import subprocess
import sys

def run_command(command):
    
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

def install_conda_packages():
    
    conda_commands = [
        "conda install rdkit::rdkit",
        "conda install numpy"
    ]
    
    for command in conda_commands:
        run_command(command)
        
        
        
        
        
if __name__ == "__main__":
    
    print('installing dependencies .............')
    install_conda_packages()
    print("All dependencies have been installed.")
