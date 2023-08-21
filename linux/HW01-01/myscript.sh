#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: myscript.sh </home/olivia/folder2> <nice>"
    exit 1 #  1 means a failure. check if there are 2 arguments $1 and $2
fi

echo arg0="$0"
echo arg1="$1"
echo arg2="$2"

folder_path="$1"
word="$2"
file_path="$folder_path/$word"

if [ ! -d "$folder_path" ]; then
    echo "Folder '$folder_path' does not exist."
    exit 1
fi

if [ -e "$file_path" ]; then
    read -p "File '$file_path' already exists. Do you want to create it again? [y/n]: " response
    if [ "$response" != "y" ]; then
        echo "No action taken."
        exit 0 # 0 means  successful
    fi
fi

touch "$file_path"
if [ $? -eq 0 ]; then  # $? is a variable holding the return value of the last command you ran.
    echo "File '$file_path' created successfully."
else
    echo "Error creating file."
fi
