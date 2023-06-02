#!/usr/bin/env python3

# Script: 		    OPS 301 Challenge 11
# Author: 		    Lilian Mburu
# Last Revision: 	June 1st 2023
# Purpose: 		    This script uses Psutil to fetch system information.


# imports
import psutil as p

# variables

# Main
# cpu_times = p.cpu_times()
# print(cpu_times)
# Time spent by normal processes executing in user mode
print(f"Process time in user mode: {p.cpu_times().user}\n")

# Time spent by processes executing in kernel mode
print(f"Process time in kernel mode: {p.cpu_times().system}\n")

# Time when system was idle
print(f"Process time in idle: {p.cpu_times().idle}\n")

# Time spent by priority processes executing in user mode

# Get a list of all processes
all_processes = p.process_iter()
# Define the priority level (e.g., "high" priority)
priority_level = -10
# Filter processes by priority
priority_processes = [p for p in all_processes if p.nice() < priority_level]
# Fetch the time spent in user mode for each priority process
for process in priority_processes:
    process_id = process.pid
    cpu_times = process.cpu_times()
    print(f"Process ID: {process_id}, User Mode Time: {cpu_times.user} seconds")

# End