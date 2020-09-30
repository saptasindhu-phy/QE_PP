#Relaxation Post Processing Script for Quantum Espresso
#Version 1.0b
#Written by Saptasindhu <saptasindhu62@gmail.com> on 15-09-2019
#Last Updated on 16-09-2019
#Currently the script is in beta mode.
#This comes under GNU GPL v3.0.

print("")
print("    Relaxation Post Processing Script for Quantum Espresso")
print("    Version 1.0b")
print("    Written by Saptasindhu <saptasindhu62@gmail.com> on 15-09-2019")
print("    Last Updated on 16-09-2019")
print("    Currently the script is in beta mode.")
print("    This comes under GNU GPL v3.0.")
print("")

import numpy as np #Imports Numpy for data manipulation.
import csv #Imports CSV for Splitting data of QE output into words
from matplotlib import pyplot as plt

force = [] 

with open('G:/BAND/rel.out') as output:  #Reads QE relaxation Output. *****Improvement Needed****
    for line in output:
        if 'Total force' in line:
            force.append(line.rstrip('\n')) #Appends force data printed after each scf cycle convergence.
newdata = list(csv.reader(force, delimiter=' ')) #Initialising force list by CSV, splits words by words
newdata = np.array(newdata)                 #Stores CSV data as Numpy Array
force_correction = newdata[:,12]            #Extracts Force Correction Data
scf_correction = newdata[:,-1]              #Extracts SCF Correction Data
output_force=force_correction.astype(float)          #Changes type to floating point data
output_scf_correction=scf_correction.astype(float)   #Changes type to floating point data
with open ('G:/BAND/force_vs_iterations.txt', 'wb') as f:
    np.savetxt(f, output_force, newline=' \n', fmt='%.8f')
with open ('G:/BAND/scf_correction_vs_iterations.txt', 'wb') as f:
    np.savetxt(f, output_scf_correction, newline=' \n', fmt='%.8f')
print("ALL DONE");        