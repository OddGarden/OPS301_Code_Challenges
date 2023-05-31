#!/usr/bin/env python3

# Script: 		    OPS 301 Challenge 10
# Author: 		    Lilian Mburu
# Last Revision: 	May 30th 2023
# Purpose: 		    This script uses file handling commands, create a Python script 
#                   that creates a new .txt file, appends three lines, prints to the 
#                   screen the first line, then deletes the .txt file.


# imports
import os


# variables

file_path = "challenge10_test.txt"
copy_path = "challenge10_copy.txt"
final_path = "challenge10_final.txt"
search_term = "Praesent"
replace_term= "Velit"

# Main

# creates a new .txt file, appends three lines
with open(file_path, 'a') as file:
    file.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n")
    file.write("Praesent vel nisi nec quam rhoncus convallis.\n")
    file.write("Nullam id neque quis libero euismod pretium.\n")

# prints to the screen the first line
with open(file_path, 'r') as file:
    content = file.read()
    first_line = file.readline()
    print("First line:", first_line)

# make a copy of the file
with open(copy_path, 'w') as file: 
    file.write(content)

# delete the .txt file
os.remove(file_path)


# Stretch Goal: Choosing to copy new file above to complete the goals in this section 
# as I do not have access to my lab kit at the time of completing this challenge.

# open the file & read all lines
with open(copy_path, 'r') as file:
    content = file.readlines()

# for each line, find the search_term and swap it with the replace_term
for i, line in enumerate(content):
    content[i] = line.replace(search_term, replace_term)

# Save the changes out to a new file name.
with open(final_path, 'w') as file:
    file.writelines(content)

# End