# !/bin/bash

# Script: 		    OPS 301 Challenge 03
# Author: 		    Lilian Mburu
# Last Revision: 	May 3rd 2023
# Purpose: 		    Continuously process or exist a request based on defined conditions.               
#     
# Variables
underline=`tput smul`
nounderline=`tput rmul`
val=0

# Functions

init_menu() {
    echo -e " \n Menu options: \n " 
    echo -e "   1. Hello World! \n " 
    echo -e "   2: Ping self \n "
    echo -e "   3. IP Info \n"
    echo -e "   4. Exit \n " 
    read -p "Please make a selection: " val
}

init_pause() {
    echo -e "Processing... \n "
    sleep 1
}

init_stop() {
    sleep 1
    echo -e "********************** Done! *********************** \n "
}

# Main

echo -e $underline CONDITIONALS IN MENU SYSTEM $nounderline " \n "



while [[ $val -ne 4 ]]; do
    init_menu
    sleep 1
    if [[ $val -eq 1 ]]; then 
        init_pause
        echo -e "          Hello World! \n" 
        init_stop
    elif [[ $val -eq 2 ]]; then 
        init_pause
        ping -c 2 127.0.0.1
        echo -e " \n "
        
    elif [[ $val -eq 3 ]]; then 
        init_pause
        echo -e $(sudo lshw -class network) " \n "
        init_stop
    elif [[ $val -eq 4 ]]; then
        init_pause 
        echo -e "Exiting application..."
        sleep 1
        echo -e "3... \n "
        sleep 1
        echo -e "2... \n "
        sleep 1
        echo -e "1... \n "
        init_stop
        exit
    else 
        init_pause
        echo -e "   Invalid response. Please try again \n "
    fi
done








# End