#creating dictonaries
empty_dict={}
print(type(empty_dict))

empty_dict=dict()
print(type(empty_dict))


#dictonary with key value pairs
student ={ "name":"Krish","age":21,"grade":"A"}
print(student)
print(type(student))

#Keys should be unique
student ={ "name":"Krish","age":21,"name":"A"}
print(student)

##acessing dictonary elements
student ={ "name":"Krish","age":21,"grade":"A"}
print(student["grade"])
print(student["age"])

print(student.get('grade'))
print(student.get('name'))
print(student.get('last_name'))
print(student.get('last_name',"Not Available"))

#Modifying dictonary elements
#Dictonary are mutuable, so you can add, update or delete elements
print(student)
#update the value
student["age"]=28
print(student)
#adding a new key and value 
student["address"]="India"
print(student)
#delete the key
del student['grade']
print(student)