##Nested dictonaries
students = {
    "student1" :{"name":"Krish","age":21},
    "student2" :{"name":"Krishna","age":18}
}
print(students)

##Accessing nested dictonaries
print(students["student2"]["name"])
print(students["student2"]["age"])


#Iterating over nested dictonaries
for student_id, student_info in students.items():
    print(f"{student_id}:{student_info}")
    for key,value in student_info.items():
        print(f"{key}:{value}")


##Dictonary comprehension
squares ={x:x**2 for x in range(10)}
print(squares)

##Conditional dictonary comprehension
evens ={x:x**2 for x in range(10) if x%2==0}
print(evens)

##Merge 2 dictonaries into one
dict1={"a":1,"b":2}
dict2={"c":3,"c":4}

merge_dict = {**dict1,**dict2}
print(merge_dict)