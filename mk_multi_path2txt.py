import os

# Open the text file for reading
with open('list.txt', 'r') as f:
    lines = f.readlines()

# Create a dictionary to store the output filenames and contents
output_dict = {}

# Loop through each line in the text file
for line in lines:
    # Split the line by the '/' character
    parts = line.strip().split('/')
    
    # Check that there are at least two parts after splitting
    if len(parts) < 2:
        continue
    
    # Check if the first part (before the '/') is already a key in the output dictionary
    if parts[0] not in output_dict:
        # If not, create a new key and value in the dictionary
        output_dict[parts[0]] = []
    
    # Add the second part (after the '/') to the list of values for the current key
    output_dict[parts[0]].append(parts[1])

# Loop through the keys and values in the output dictionary
for key, values in output_dict.items():
    # Create a new file with the key as the filename and write the values to it
    with open(key + '.txt', 'w') as f:
        f.write('\n'.join(values))
    
# Delete the original text file
os.remove('list.txt')
