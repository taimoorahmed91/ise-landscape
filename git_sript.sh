#!/bin/bash

# Step 1: Move to the specific folder
cd /root/ise-landscape

# Step 2: Run 'git add .'
git add .

# Step 3: Run 'git add *'
git add *

# Step 4: Run 'git commit' with a default message
git commit -m "Automatic commit"

# Step 5: Provide username and password
username="taimoorahmed91"
password="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"

# Step 6: Run 'git push' with the provided credentials
echo -e "$username\n$password" | git push origin main

