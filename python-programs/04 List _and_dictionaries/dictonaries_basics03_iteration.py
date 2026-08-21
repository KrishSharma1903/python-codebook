##iteration over dictonaries
#You can use loops to iterate over dictonaries, key , values or items

student ={ "name":"Krish","age":21,"grade":"A"}
#iterating over keys
for keys in student.keys():
    print(keys)

#iterate over values
for keys in student.values():
    print(keys)

#iterate over key value pairs
for i,values in student.items():
    print(i,values)