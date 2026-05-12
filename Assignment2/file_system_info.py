import os
import stat
import sys

def analyze_directory(target_path):
    # Check if the path actually exists
    if not os.path.exists(target_path):
        print(f"Error: The path '{target_path}' does not exist.")
        return

    print(f"\nListing files in: {target_path}\n")

    # Loop through all items in the directory
    for filename in os.listdir(target_path):
        
        # Create the full path to the item
        filepath = os.path.join(target_path, filename)
        
        # Check if it is a file (and not a subdirectory)
        if os.path.isfile(filepath):
            
            # Get file metadata using os.stat
            file_stats = os.stat(filepath)
            size = file_stats.st_size
            permissions = stat.filemode(file_stats.st_mode)
            
            # Basic output with line breaks
            print("File Name   :", filename)
            print("Size (bytes):", size)
            print("Permissions :", permissions)
            print() # Empty print to create a line break between files

if __name__ == "__main__":
    # Check if the user provided an argument in the terminal
    if len(sys.argv) > 1:
        path_input = sys.argv[1]
    else:
        # Default to the current directory if no argument is given
        print("No directory provided. Using current directory ('.').")
        path_input = "."
        
    # Call the function
    analyze_directory(path_input)