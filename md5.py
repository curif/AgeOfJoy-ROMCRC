import os
import hashlib

# Set the directory you want to read
directory = "./"

# Get a list of all the files in the directory
files = os.listdir(directory)

# Iterate over the files in the directory
for file in files:
  # Get the full path of the file
  file_path = os.path.join(directory, file)
  
  # Open the file in binary mode
  with open(file_path, "rb") as f:
    # Read the file's binary data
    data = f.read()
    
    # Compute the MD5 hash of the file's data
    md5_hash = hashlib.md5(data).hexdigest()
    
    # Print the file name and its MD5 hash
    print(f"{file}: {md5_hash}")

