#!/usr/bin/env python3

# Script: 		    OPS 301 Challenge 08
# Author: 		    Lilian Mburu
# Last Revision: 	May 18th 2023
# Purpose: 		    This script focuses on working with python lists.
#                
# Import libraries

# Declaration of variables

# Assign to a variable a list of ten string elements.
my_language_list = ["bash", "powershell", "python", "java", "C++", "javascript", "GO", "php", "typescript", "kotlin" ]

# Declaration of functions

# Main

# Print the fourth element of the list.
print("The 4th item on my list is: ", my_language_list[3], "\n")        

# # Print the sixth through tenth element of the list.
print("The 6th - 10th items on my list are: ", my_language_list[6:], "\n")

# # Change the value of the seventh element to “onion”.
print("The current value of the 7th item on my list is ", my_language_list[7], "\n")
my_original_seven = my_language_list[7]  
my_language_list[7] = "onion"
print("The modified value of the 7th item on my list is ", my_language_list[7], "\n")
print("***Length of my_language_list: ", len(my_language_list), "\n")

# append(): Add an item to the end of the list
my_language_list.append(my_original_seven)
print("New value added: ", my_language_list[-1], "\n")

# count(): Returns how many times an items appears in a list
my_language_list.append(my_original_seven)
print("***Length of my_language_list: ", len(my_language_list), "\n")
print("How many times does php appear? ", my_language_list.count('php'), "\n")

# index(): Return the index of the first matching value located on the list
print("What is index is php located at? ", my_language_list.index("php"), "\n")

# insert(): Insert an item at a specific index
my_language_list.insert(0, "perl")
print("What is index is perl located at? ", my_language_list.index("perl"), "\n")
print("***Length of my_language_list: ", len(my_language_list), "\n")

# reverse(): reverse the elements of the list
print("My current order: ", my_language_list, "\n")
my_language_list.reverse()
print("My reverse order: ", my_language_list, "\n")

# sort(): Sort items of the list

# copy(): Shallow copy of the list

# extend(): Extend the list by appending all the items from the iterable.

# clear(): Remove all items from the list
# pop(): Remove an item with or without specifying an index
# remove(): remove an item from the list




# End