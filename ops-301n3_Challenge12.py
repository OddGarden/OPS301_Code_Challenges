# Script: 		    OPS 301 Challenge 12
# Author: 		    Lilian Mburu
# Last Revision: 	June 8th 2023
# Purpose: 		    This script uses python's `requests` library to 
#                  evaluate how a web server responds to outside requests.

#!/usr/bin/python3
import requests as req
import re

# Variables
options = ["GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS"]

# Functions

# This function take no arguments
# uses the `requests` library to run HTTP method to 
# a given url.
def execute():
  status = ""
  if uppercase_action == "GET":
    status = req.get(url)
  elif uppercase_action == "POST":
    status = req.post(url)
  elif uppercase_action == "PUT":
    status = req.put(url)
  elif uppercase_action == "DELETE":
    status = req.delete(url)
  elif uppercase_action == "HEAD":
    status = req.head(url)
  elif uppercase_action == "PATCH":
    status = req.patch(url)
  elif uppercase_action == "OPTIONS":
    status = req.options(url)
  else: 
    print("That is an invalid action")
  return status

# This function accepts an argument. 
# Translate the codes into plain terms that print to the screen
def evaluate_response(status):
  if status.status_code == 200: 
    print("Success!")
  elif status.status_code == 301: 
    print("Moved Permanently!")
  elif status.status_code == 400: 
    print("Bad Request!")
  elif status.status_code == 401: 
    print("Unauthorized!")
  elif status.status_code == 403: 
    print("Forbidden!")
  elif status.status_code == 404: 
    print("Not Found!")
  elif status.status_code == 405: 
    print("Method Not Allowed!")
  elif status.status_code == 500: 
    print("Internal Server Error!")
  elif status.status_code == 502: 
    print("Bad Gateway!")
  elif status.status_code == 503: 
    print("Service Unavailable!")
  else:
    print("An error has occurred.")
  
# Main

# Prompt the user to type a string input as the variable for your destination URL.
url = input("Please enter a website: ")
# remove whitespaces
url = url.strip()
# format url if missing valid protocol
if not re.match(r"^(http||https\ftp)://", url):
  url = "https://"+url
print("\n")
# Prompt the user to select a HTTP Method of the following options
action = input(f"What would you like to do  ({', '.join(options)}): ")
# convert respose to uppercase letters
uppercase_action = action.upper()
print("\n")
# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
proceed = input(f"You would like to {uppercase_action} {url}. Yes or No? ")
proceed = proceed.upper()
print("\n")
# Execute if user confirmed; else exit program
if proceed == "YES":
  status = execute()
else:
  print("GOODBYE")
# For the given URL, print response header information to the screen.
print(f"{url} Headers: \n \n {status.headers} \n")
# For the given header, translate the codes into plain terms that print to the screen
print(f"{url} response:")
evaluate_response(status)

# End
