import os
import random

def create_file_of_size(file_path, size_in_mb):
    # Convert size to bytes
    size_in_bytes = size_in_mb * 1024 * 1024
    
    with open(file_path, 'wb') as f:
        f.write(os.urandom(size_in_bytes))
        
    print(f"File '{file_path}' created with size {size_in_mb} MB.")

# Example usage:
file_path = 'C:\\111\\custom_size_file.bin'
size_in_mb = 1000  # Change this to the desired file size in MB
create_file_of_size(file_path, size_in_mb)
