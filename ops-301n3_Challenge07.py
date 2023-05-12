#!/usr/bin/env python3

# Script: 		    OPS 301 Challenge 07
# Author: 		    Lilian Mburu
# Last Revision: 	May 13th 2023
# Purpose: 		    This script generates all directories, sub-directories and files 
#                   for a user-provided directory path.
# Import libraries

import os
import subprocess
# Declaration of variables
user_response = ""
reserved_char = "<>|:&"
path = ()

# Declaration of functions

# Function validates user input for invalid characters in the path


### Declare a function here


def check_if_exists(value):
    # if path exists and value is a directory. Confirm
    if os.path.exists(value) and os.path.isdir(value):
        print("This item exists!")
        return True
    elif os.path.isfile(value):
        print("This file  exists")
        return True
    else:
        if os.path.isdir(value):
            print("This is a dir")
        
        if os.path.isfile(value):
            print("This is a file")


def create_location(path_type, value):
    if path_type == "dir":
        if input("This directory does not exist. Do you want to create one? ").lower() == "yes":
            os.makedirs(value)
        else: 
            print("existing applicaiton.. ")
            exit()
    
    if path_type == "file":
        if input("This file does not exist. Do you want to create an empty file? ").lower() == "yes":
            with open(value, 'w'):
                pass
        else: 
            print("existing applicaiton.. ")
            exit()


def traverse_path(value):
    this_dir= os.path.dirname(value)
    print("root" + this_dir)
    for (root, dirs, files) in os.walk(this_dir):
        ### Add a print command here to print ==root==
        print("Root folder is: " + root)
        ### Add a print command here to print ==dirs==
        print("Sub dir is: " , dirs)
        ### Add a print command here to print ==files==
        print("file is: " , files)

        # write the output to  a .txt file.
        with open("dir_output.txt", "w") as file:
            file.write("ROOT INFO \n")
            file.write(root)
            file.write("\n")
            file.write("DIRS INFO \n")
            file.writelines("\n".join(dirs))
            file.write("\n")
            file.write("FILES INFO \n")
            file.writelines("\n".join(files))
            file.write("\n")
# Main
# print script title
print('\033[4m'+"Directory Creation"+'\033[0m'+'\n')

# Get user input and print to screen

for i in range(3):
    if i == 0:
        user_response = input("Root directory name: ")
        path += (user_response,) 
        if not check_if_exists(os.path.join(*path)):
            create_location("dir", os.path.join(*path))
        
    elif i == 1:
        user_response =  input("Sub directory name: ")
        path += (user_response,)
        if not check_if_exists(os.path.join(*path)):
            create_location("dir", os.path.join(*path))
        
    else:
        user_response =  input("Filename: ")
        path += (user_response,) 
        if not check_if_exists(os.path.join(*path)):
            create_location("file", os.path.join(*path))
       

# print(user_response)
valid_path = os.path.join(*path)
traverse_path(valid_path)


# open the .txt file with Libre Office Writer.
subprocess.run("libreoffice", "--writer", "dir_output.txt")

# 

### Pass the variable into the function here

# End
