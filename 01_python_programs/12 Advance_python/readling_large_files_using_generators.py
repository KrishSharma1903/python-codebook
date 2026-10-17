##Reading large files using generators
'''Generators are particularly useful for reading large files because they allow you to process 
one line at a time without loading the entire file into memory.'''

def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line

file_path = "large_file.txt"

for line in read_large_file(file_path):
    print(line.strip())