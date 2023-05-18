#!/bin/bash

# Step 1: Move to the specific folder
cd /root/ise-landscape

# Step 2: Run 'git add .'
git add .

# Step 3: Run 'git add *'
git add *

# Step 4: Run 'git commit' with a default message
git commit -m "Automatic commit"

# Step 5: Provide password
password="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"

# Step 6: Run 'git push' with the provided password
echo -e "protocol=https\nhost=github.com\nusername=taimoorahmed91\npassword=$password" | git credential-store store
git push -u origin main

# Optional: Clear the stored credentials after use (uncomment if desired)
# git credential-store erase

