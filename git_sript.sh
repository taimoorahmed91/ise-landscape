#!/bin/bash

# Step 1: Move to a specific folder
cd /root/ise-landscape

# Step 2: Run 'git add .'
git add .

# Step 3: Run 'git add *'
git add *

# Step 4: Ask for comments
read -p "Enter commit comments: " comments

# Step 5: Run 'git commit -m' with the comments
git commit -m "$comments"

# Step 6: Run 'git push -u origin main'
git push -u origin main

# Step 7: Provide username
username="taimoorahmed91"

# Step 8: Provide password
password="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"

# Optional: Authenticate with Git using the provided credentials
git config --global credential.helper 'cache --timeout=3600'
echo -e "protocol=https\nhost=github.com\nusername=$username\npassword=$password" | git credential-store store

# Optional: Clear the stored credentials after use (uncomment if desired)
# git credential-store erase

