import sys
import os

id = sys.argv[1]
dstise = sys.argv[2]
print(f"Hello There: {id} and the destination ISE was {dstise}")

# Base directory path
base_dir = "/var/www/html/mise/v0.1/configs/ap/"

# Construct the file paths
file_path = os.path.join(base_dir, id)

# Open and read the file
try:
    with open(file_path, 'r') as file:
        file_contents = file.read()
        print("File contents:")
        print(file_contents)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred while opening the file: {e}")

# Print the file paths
print(f"File Path: {file_path}")
