##Inheritance in pyhton 
#parent class 
class Car:
    def __init__(self,windows,doors,enginetype):
        self.windows = windows
        self.doors = doors
        self.enginetype = enginetype

    def drive(self):
        print(f"The person will drive the {self.enginetype} car")

car1= Car(4,5,"Petrol")
car1.drive()

#single inheritance 
class Tesla(Car): #-> inheriting the properties of car class
    def __init__(self, windows, doors, enginetype,is_selfdriving):
        super().__init__(windows, doors, enginetype) #Calling the init from the parent class
        self.is_selfdriving =is_selfdriving

    def selfdriving(self):
        print(f"Tesla Supports self driving : {self.is_selfdriving}")

tesla1 = Tesla(4,5,"electric",True)
tesla1.selfdriving()

tesla1.drive()

##Multiple Inheritance
#When a class inherits from more than one base class

class Animal: #Base class 1
    def __init__(self,name):
        self.name=name

    def speak(self):
        print("Sub classes must implement this method")

class Pet:#Base class 2
    def __init__(self,owner):
        self.owner=owner

class Dog(Animal,Pet):
    def __init__(self, name,owner):
        # super().__init__(name)
        Animal.__init__(self,name)
        Pet.__init__(self,owner)

    def speak(self):
        return f"{self.name} says woof"

dog=Dog("Buddy","Krish")
print(dog.speak())
print(f"Owner {dog.owner}")
