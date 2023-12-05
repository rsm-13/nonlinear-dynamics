# Author: Radha Munver
# Date: 12/06/2023
# (AT) Nonlinear Dynamics
# main.py --> Newtons Method

import os
import sys
sys.path.append("../util")

from DEgraphics_Radha import *
from newtonsFractal import *
from colorTheory import *
from newtonsMethodUI import *
import subprocess

# install and import necessary libs
def resolveImports():
    libs = ['numpy', 'pydub']
    installCmds = [f'pip install {mod}' for mod in libs]

    for command in installCmds:
        subprocess.run(command, shell=True)
    
def main():
    resolveImports()
    os.system('python3 newtonsMethodUI.py')

main()