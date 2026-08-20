##Dictonary methods
student ={ "name":"Krish","age":21,"grade":"A"}
#Getting keys and values
keys=student.keys()
print(keys)
values=student.values()
print(values)

#Getting key value pairs
key_value_pair = student.items()
print(key_value_pair)

##Shallow copy (imp)
student_copy = student
print(student)
print(student_copy)

student_copy["name"] ="Krish2"
print(student_copy)                                                                                                                                  
print(student)

#this doesnt make a seperate copy hence when we are modifying the elements of student_copy it changes the original too

student_copy1 = student.copy()  #This will make a shallow copy 
student["name"] = "Krishna"
print(student)
print(student_copy1)