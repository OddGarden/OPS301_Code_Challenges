# !/bin/bash

# Script: 		OPS 301 Challenge 01
# Author: 		Lilian Mburu
# Last Revision: 	April 26th 2023
# Purpose: 		Copies files to the current working directory. The current date and time 		
#			is appended to the new filename


# Variables
source="/var/log/syslog"
filename=syslog_$(date +%Y%m%d%H%M%S).txt


# Main

# copy contents from source path to new fle located current working directory
cp $source $filename

# Echo statements provides the source, destination and filename to end user.
echo `date +%A` `date +%Y-%m-%d` `date +%H:%M:%S` 
echo File located at directory: $source was copied to current directory at: $(pwd)
echo To view the content please open up the file named: $filename

# End
