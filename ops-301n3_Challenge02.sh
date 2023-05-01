# !/bin/bash

# Script: 		    OPS 301 Challenge 02
# Author: 		    Lilian Mburu
# Last Revision: 	April 29th 2023
# Purpose: 		    Change the permissions in system file/directories provided by an end user. 	The script will prompt and 	
#                   a user for the desired file/directory as well as the permission level desired. Permissions will be changed
#                   and upon successful change,  prints to the termnal.

# Variables
underline=`tput smul`
nounderline=`tput rmul`
input_path=''
user=''
user_level=0
group=''
group_level=0
other=''
other_level=0
role=''


# Functions

# Set permission level for each group
set_perm() {
    sum=0
    sleep 1 
    echo -e ""
    read -p "   Grant READ permission level? y/n " val
    if [[ $val == "y" ]]; then
        sum=$((sum+4))
    fi
    sleep 1 
    echo -e " "
    read -p "   Grant WRITE permission level? y/n  " val
    if [[ $val == "y" ]]; then
        sum=$((sum+2))
    fi
    sleep 1 
    echo -e ""
    read -p "   Grant EXECUTE permission level? y/n " val
    if [[ $val == "y" ]]; then
        sum=$((sum+1))
    fi 
}

# validate user input provided regarding user, group & other roles. Exit if 3 attempts are unsuccessful.
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

repeat_sub() {
    tries=0
    
    while [[ $tries -ne 2 ]]; do
        tries=$((tries+1))
        res=''
        echo "You have entered an invalid response. All Permssion level must have correct responses. Please try again" 
        
        read -p "Grant $1 permission level? y/n  " res
        if [[ $res == "y" && $1 == "read" ]]; then
            set_perm
            user_level=$sum
            break
        elif [[ $res == "y" && $1 == "write" ]]; then 
            set_perm
            group_level=$sum
            break
        elif [[ $res == "y" && $1 == "execute" ]]; then
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
echo  -e "\n ${underline}CHANGE PERMISSION LEVEL SCRIPT ${nounderline} \n" 
sleep 2

read -p  "Please enter the directory or file you would like to change: " input_path


echo -e "\n Validating... \n"
sleep 2

# Check if the give path is a directory or file && it exists. Exit if it does not exist.
if [ -d "$input_path" ]; then
    echo -e "Great! looks like  $input_path directory exists! \n"
elif [ -f "$input_path" ]; then 
    
    echo -e "Great! looks like $input_path file exists! \n"
else 
    echo -e "Hmmm....The directory and/of file provided does not exist. \n"
    sleep 1 
    echo "This application will exit in"
    timer=3
    while [[ $timer -ne 0 ]]; do
        echo -e " $timer.... \n "
        timer=$((timer-1))
        sleep 1 
    done
    echo -e "GOODBYE! \n "
    exit
fi

# Determine if user permissions need to be set.
read -p "Do you want to change USER permissions? y/n " user
if [[ $user == "y" ]]; then
    set_perm
    user_level=$sum
elif [[ $user == "n" ]]; then 
    echo -e "No permissions will be set at this level \n " 
else
    role="user"
    repeat $role
fi

#  Determin if group permissions need to be set.
echo -e ""
read -p "Do you want to change GROUP permissions? y/n " group
if [[ $group == "y" ]]; then 
    set_perm
    group_level=$sum
elif [[ $group == "n" ]]; then 
    echo -e "No permissions will be set at this level \n " 
else
    role="group"
    repeat $role
fi

#  Determine if other permissions need to be set.
echo -e ""
read -p "Do you want to change OTHER permissions? y/n " other
if [[ $other == "y" ]]; then 
   set_perm
   other_level=$sum
elif [[ $other == "n" ]]; then 
    echo -e "No permissions will be set at this level \n " 
else
    role="other"
    repeat $role
fi

#  Exit if input request is to remove all permissions. Unsafe request. 
if [[ $user_level -eq 0 && $group_level -eq 0 && $other_level -eq 0 ]]; then 
    echo  -e "Ummm.. Removing all read, write and execute permission is unsafe. Unable to complete this request. \n "
    sleep 1 
    echo "This application will exit in"
    timer=3
    while [[ $timer -ne 0 ]]; do
        echo -e " $timer.... \n "
        timer=$((timer-1))
        sleep 1 
    done
    echo -e "GOODBYE! \n "
    exit
fi


echo -e "At this location: $input_path permission levels will be set to: $user_level$group_level$other_level \n "

echo -e "Please wait while I process this request \n "
timer=3
while [[ $timer -ne 0 ]]; do
    echo -e "  .... \n "
    timer=$((timer-1))
    sleep 1 
done

#  if path provided is a directory, change the permissions of all content
echo -e "Done. \n "

sleep 2

echo -e "The following files have been revised as follows: \n"

if [ -d "$input_path" ]; then
    
    chmod -R $user_level$group_level$other_level "$input_path"
    for f in $input_path/*; do
        sleep 2
        filename=$(basename $f)
        echo -e $(ls -l) $filename " \n "
    done
else 
    chmod $user_level$group_level$other_level "$input_path"

    echo -e $(ls -l) $input_path " \n "
fi

sleep 2

echo -e "Thank you for using this application. Any feedback is always welcome! \n "

echo -e "********** THE END! ******************** \n "

# End
