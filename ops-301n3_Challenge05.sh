 #!/bin/bash

# Script: 		    OPS 301 Challenge 05
# Author: 		    Lilian Mburu
# Last Revision: 	May 6rd 2023
# Purpose: 		    A script that clears log files for you.              
#     
# Variables
SYS_LOG="/var/log/syslog"
WTMP="/var/log/wtmp"
BACKUPS="/var/log/backups"
TIMESTAMP=$(date +"%Y%m%d%H%M%S")

# Functions

loop() {
    val=$1
    for file in "${val[@]}"; do
        # file size before compression
        FILE_SIZE=$(wc -c "$file" | awk '{print $1}')
        
        # Compress the contents of the log files listed below to a backup directory
        echo "Compressing $BACKUPS/$FILE_NAME-$TIMESTAMP.zip"
        FILE_NAME=$(basename "$file")
        sudo zip -r "$BACKUPS/$FILE_NAME-$TIMESTAMP.zip" $file

        # Clear the contents of the log file
        sudo cat /dev/null > "$file"

        # file size after compression
        COMPRESSED_FILE_SIZE=$(wc -c "$BACKUPS/$FILE_NAME-$TIMESTAMP.zip" | awk '{print $1}')
        
        # Compare the size of the compressed files to the size of the original log files
        echo "File size before compression: $FILE_SIZE"
        echo "File size after compression: $COMPRESSED_FILE_SIZE"

        if [[ $FILE_SIZE -gt $COMPRESSED_FILE_SIZE ]]; then 
            AMOUNT="$((FILE_SIZE - COMPRESSED_FILE_SIZE))"
            echo "Compression successful. File reduced by $AMOUNT bytes"
        else 
            echo "Compression unsuccessful."
        fi

    done
}
# Main

# Check if backups directory exists. If it doesn't exist, create one.
if [[ -d $BACKUPS ]]; then
  echo "Backup path $BACKUPS exists"
else 
  echo "Backup path $BACKUPS doesn't exist"
  ${sudo mkdir $BACKUPS}
fi


loop "$SYS_LOG"
loop "$WTMP"

# End