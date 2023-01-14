from genericpath import isfile
from msilib import Directory
import os

program_files = input(os.path.join())

file_path = os.path.join(program_files)

print(os.path.isdir(file_path))

if isfile == os.path.isfile(file_path) or Directory == os.path.isdir(file_path):
    print("Provided path is not a folder.")
elif os.path.exists(file_path) == False:
    print("Provided path does not exist.")

# Nu inteleg de ce nu vrea sa mearga