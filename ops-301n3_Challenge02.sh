# !/bin/bash

# Script: 		    OPS 301 Challenge 02
# Author: 		    Lilian Mburu
# Last Revision: 	April 29th 2023
# Purpose: 		    Change the permissions in system file/directories provided by an end user. 	The script will prompt and 	
#                   a user for the desired file/directory as well as the permission level desired. Permissions will be changed
#                   and upon successful change,  prints to the termnal.

# Variables
input_path=''
user=''
user_level=0
group=''
group_level=0
other=''
other_level=0
role=''


# Functions

set_perm() {
    sum=0
    read -p "Grant READ permission level? y/n  " val
    if [[ $val == "y" ]]; then
        sum=$((sum+4))
    fi
    read -p "Grant WRITE permission level? y/n " val
    if [[ $val == "y" ]]; then
        sum=$((sum+2))
    fi
    read -p "Grant EXECUTE permission level? y/n " val
    if [[ $val == "y" ]]; then
        sum=$((sum+1))
    fi 
}

repeat() {
    tries=0
    
    while [[ $tries -ne 2 ]]; do
        tries=$((tries+1))
        res=''
        echo "You have entered an invalid response. Please try again." 
        read -p "Do you want to change $1 permissions? y/n " res
        if [[ $res == "y" && $1 == "user" ]]; then
            set_perm
            user_level=$sum
            break
        elif [[ $res == "y" && $1 == "group" ]]; then 
            set_perm
            group_level=$sum
            break
        elif [[ $res == "y" && $1 == "other" ]]; then
            set_perm
            other_level=$sum
            break
        elif [[ $res == "n" ]]; then 
             echo "No permissions will be set at this level" 
             break
        elif [[ $tries -eq 2 ]]; then
            echo "You have exceed the number of allowed attempts. Exiting application"
            exit
        fi
    done 

}





# Main
echo  "Ready to change the permission level on you file or directory?..." 

read -p  "Please enter the directory or file you would like to change: " input_path

if [ -d "$input_path" ]; then
    echo "Looks like $input_path exists!"
elif [ -f "$input_path" ]; then 
    echo "Looks like $input_path exists!"
else 
    echo "The directory and/of file provided does not exist. Exiting application"
    exit
fi

read -p "Do you want to change USER permissions? y/n " user


if [[ $user == "y" ]]; then
    set_perm
    user_level=$sum
elif [[ $user == "n" ]]; then 
    echo "No permissions will be set at this level" 
else
    role="user"
    repeat $role
fi

read -p "Do you want to change GROUP permissions? y/n " group

if [[ $group == "y" ]]; then 
    set_perm
    group_level=$sum
elif [[ $group == "n" ]]; then 
    echo "No permissions will be set at this level" 
else
    role="group"
    repeat $role
fi

read -p "Great! Do you want to change OTHER permissions? y/n " other

if [[ $other == "y" ]]; then 
   set_perm
   other_level=$sum
elif [[ $other == "n" ]]; then 
    echo "No permissions will be set at this level" 
else
    role="other"
    repeat $role
fi

if [[ $user_level -eq 0 && $group_level -eq 0 && $other_level -eq 0 ]]; then 
    echo "Ummm.. Removing all read, write and execute permission is unsafe. Unable to complete this request. Exiting Application"
    exit
fi



echo "At this location: $input_path permission levels will be set to: $user_level$group_level$other_level"

if [ -d "$input_path" ]; then

    chmod -R $user_level$group_level$other_level "$input_path"

    for f in $input_path/*; do
        filename=$(basename $f)
        echo $(ls -l) $filename
    done

fi

# End
