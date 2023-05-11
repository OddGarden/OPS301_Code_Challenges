#!/usr/bin/env python3

# Script: 		    OPS 301 Challenge 06
# Author: 		    Lilian Mburu
# Last Revision: 	May 10th 2023
# Purpose: 		    Execute Linux terminal commands from within a Python script.              

# imports
import os 



# variables
who_val = "whoami"
addr_val = "ip a"
sys_val = "sudo lshw -short"

# Main
print("This executes Linux terminal commands from within a Python script \n")


print("Computer Name:")
os.system(who_val)
print("=====================\n ")

print("IP address:")
os.system(addr_val)
print("=====================\n ")


print("Hardware configuration:")
os.system(sys_val)
print("=====================\n ")


# End