#!/usr/bin/env python3

# Script: 		    OPS 301 Challenge 09
# Author: 		    Lilian Mburu
# Last Revision: 	May 21th 2023
# Purpose: 		    This script focuses on working with python conditionals. In this exercise,
#                   the user will have one chance to guess a random number
# imports
import random

# variables
start = input("Enter starting range: ")
end = input("Enter ending range: ")

# Main

if start.isdigit() and end.isdigit():
    print("Acceptable values entered")

    if start != end:
        rand_num = random.randint(int(start), int(end))
        guess = input("Guess a number between " + start + " and " + end + ": ")
        mid = rand_num / 2
        if rand_num == int(guess):
            print("Lucky guess!")
        else:
            if int(rand_num) == 0:
                print("The random number is " + str(rand_num) + " which has no mid point")
            elif int(guess) < rand_num and int(guess) <= mid:
                print("Your guess " + guess + " is less than  random number " + str(rand_num))
                print("Your guess " + guess + " is also less than or equal to half of the random number " +str(mid) )
            elif int(guess) > rand_num and int(guess) >= mid:
                print("Your guess " + guess + " is greater than or random number " + str(rand_num))
                print("Your guess " + guess + " is also greater than or equal to half of the random number " +str(mid) )
            else:
                print("The guessed number is out of range ")   
    else:
        print("There is only one digit in the range: " + start + " - " + end)    
else:
    print("Unacceptable values entered")


# End