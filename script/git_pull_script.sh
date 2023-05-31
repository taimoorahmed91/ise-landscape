#!/bin/bash

# Set the local directory paths
localDirectory1="/root/ise-landscape/mise"
localDirectory2="/var/www/html"

# Function to perform git pull
perform_git_pull() {
    local_directory="$1"

    # Change to the local directory
    cd "$local_directory" || exit

    # Get the default branch name
    default_branch=$(git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@')

    # Perform git pull
    git pull origin "$default_branch"
    if [ $? -eq 0 ]; then
        echo "Git pull in '$local_directory' completed successfully."
    else
        echo "Git pull in '$local_directory' failed."
    fi
}

# Perform git pull for local directory 1
perform_git_pull "$localDirectory1"

echo

# Perform git pull for local directory 2
perform_git_pull "$localDirectory2"

