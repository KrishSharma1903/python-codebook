# Encapsulation
'''Encapsulation is the concept of wrapping data (variables) and methods (functions) together as a single unit. 
It restricts direct access to some of the object's components, 
which is a means of preventing accidental interference and misuse of the data.'''

## Example for encapsulation
##Getter and setter method 
## IMP ACCESS Modifiers - Public, Protected,Private variables

#Public Acess Modifier 
class Person:
    def __init__(self,name,age):
        self.name = name #Public variables (can be used or called outside of this specific class)
        self.age = age #Public variable

def get_name(person):
    return person.name

person=Person("Krish", 34)
print(get_name(person))

# print(dir(person))


##Private Access modiifier 
class Person:
    def __init__(self,name,age,gender):
        self.__name = name #Private variables (can't be used or called outside of this specific class)
        self.__age = age #Private variable
        self.gender=gender

def get_name(person):
    return person.__name

person1 = Person("Krish",34,"Male")
# print(get_name(person1))
print(dir(person1))

##Protected access modifier  (can't be accessed from outside the class but can be derived from a derived/subclass)
class Person:
    def __init__(self,name,age,gender):
        self._name = name #Protected Variable 
        self._age = age #Protected variable
        self.gender=gender

class Employee(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

employee=Employee("Krish",34,"Male")
print(employee._name)


#Encapsulation with getter and setter
class Person:
    def __init__(self,name,age):
        self.__name = name #Private access modifier or variable 
        self.__age = age ##Private Variable

    ##Getter method for name
    def get_name(self):
        return self.__name

    ##Setter method
    def set_name(self,name):
            self.__name=name

    # Getter method for age
    def get_age(self):
            return self.__age
    
    # Setter method for age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age cannot be negative.")   

person = Person("Krish",21)

## Access and modify private variables using getter and setter
print(person.get_name())
print(person.get_age())

person.set_age(35)
print(person.get_age())

person.set_age(-5)
