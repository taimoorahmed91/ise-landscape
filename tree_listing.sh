#!/bin/bash

function list_files() {
    local file_path=$1
    local indentation=$2

    # Print current folder or file
    echo "${indentation}${file_path##*/}"

    if [ -d "$file_path" ]; then
        # If the path is a directory, recursively list its contents
        local sub_files=("$file_path"/*)
        local count=${#sub_files[@]}

        for ((i=0; i<count; i++)); do
            local sub_file=${sub_files[i]}
            local next_indentation=$indentation"│   "

            if [ $i -eq $((count-1)) ]; then
                next_indentation=$indentation"    "
            fi

            list_files "$sub_file" "$next_indentation"
        done
    fi
}

# Main entry point
if [ $# -eq 0 ]; then
    # If no directory provided, use the current directory
    directory="."
else
    directory="$1"
fi

echo "Listing files and folders in directory: $directory"
echo

list_files "$directory" ""

