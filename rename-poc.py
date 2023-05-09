"""
Python script that can do what you've described. It uses the os and shutil modules to navigate through the directories and rename the files.
"""

import os
import shutil

# Define the starting directory
starting_directory = "POC"

# Define a counter to keep track of how many files have been renamed
file_count = 0

# Define a function to rename the files in a directory
def rename_files(directory):
    global file_count
    # Get the directory name to use as a prefix for the renamed files
    prefix = os.path.basename(directory)
    # Get a list of all the files in the directory
    files = os.listdir(directory)
    # Sort the files alphabetically to ensure consistent naming
    files.sort()
    # Define a counter for the number of files renamed in this directory
    count = 0
    # Rename each file in the directory
    for file in files:
        # Check if the file is an image file
        if file.endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
            # Increment the file count
            file_count += 1
            # Get the file extension
            extension = os.path.splitext(file)[1]
            # Define the new filename
            new_filename = f"Fig.{count+1} {prefix}{extension}"
            # Get the full path to the file
            old_path = os.path.join(directory, file)
            new_path = os.path.join(directory, new_filename)
            # Rename the file
            shutil.move(old_path, new_path)
            # Increment the counter
            count += 1
    # Print the number of files renamed in this directory
    print(f"Renamed {count} files in {directory}")

# Define a function to traverse the directory tree and rename the files
def traverse_directory(directory):
    # Call rename_files on the current directory
    rename_files(directory)
    # Get a list of all the subdirectories in the current directory
    subdirectories = [os.path.join(directory, name) for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
    # Traverse each subdirectory
    for subdirectory in subdirectories:
        traverse_directory(subdirectory)

# Call the traverse_directory function on the starting directory
traverse_directory(starting_directory)

# Print the total number of files renamed
print(f"Renamed a total of {file_count} files")
