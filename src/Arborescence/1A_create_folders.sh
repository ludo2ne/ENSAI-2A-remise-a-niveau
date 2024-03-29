#!/bin/bash

input_file="folders_1A.csv"
#directory="$HOME/Cours1A"
directory="/p/Cours1A"

mkdir -p "$directory"

# Read the CSV file, skip the headers, and create the folders
while IFS=';' read -r folder_name td tp end; do
    # Create the main folder
    mkdir -p "$directory/$folder_name"
    mkdir -p "$directory/$folder_name/Annales"

    if [ "$td" = "true" ]; then        
        # Create the subfolder "TD"
        mkdir -p "$directory/$folder_name/TD"
    fi    

    if [ "$tp" = "true" ]; then        
        # Create the subfolder "TP"
        mkdir -p "$directory/$folder_name/TP"
    fi
    
done < <(tail -n +2 "$input_file")
