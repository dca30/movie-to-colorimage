import os

# Get the list of files in the current directory
files = os.listdir()

# Iterate through the list of files
for file in files:
  # Check if the file is a .mp4 file
  if file.endswith('.mp4'):
    # Extract the string before the ".mp4" extension
    file_name = file.split('.mp4')[0]
    print(f'The string before the ".mp4" extension is: {file_name}')