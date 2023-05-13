import os
import sys
import datetime

def create_folder_with_versioning(folder_name):
    folder_path = os.path.abspath(folder_name)

    if os.path.exists(folder_path):
        # Generate timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

        # Append timestamp to folder name
        new_folder_name = f"{folder_name}_{timestamp}"
        new_folder_path = os.path.join(os.path.dirname(folder_path), new_folder_name)

        try:
            os.makedirs(new_folder_path)
            print(f"Folder '{new_folder_path}' created with versioning.")
        except OSError:
            print(f"Failed to create versioned folder '{new_folder_path}'.")
    else:
        os.makedirs(folder_path)
        print(f"New folder '{folder_path}' created.")

# Example usage
if len(sys.argv) < 2:
    print("Please provide the folder name as a command-line argument.")
else:
    folder_name = sys.argv[1]
    create_folder_with_versioning(folder_name)

