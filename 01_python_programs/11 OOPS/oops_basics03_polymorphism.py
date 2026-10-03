##Method overriding 
#Method overriding allows a child class to provide a specific implementation of a method that is already defined in its parent class

##Base class 
class Animal: 
    def speak(self):
        return "Sound of the animal"

class Dog(Animal): # -> derived class 1
    def speak(self):
        return "woof!" #Method overriding

class Cat(Animal):
    def speak(self):
        return "meow!"

##Function that demonstrates polymorphism
def animal_speak(animal):
    print(animal.speak())

dog=Dog()
print(dog.speak())

cat=Cat()
print(cat.speak())
animal_speak(dog)



##Polymorphism with functions and methods 
class Shape:
    def area(self):
        return "The area of the figure"

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


#Function to demonstrate polymorphism
def print_area(shape):
    print(f"The area is {shape.area()}")

rectangle=Rectangle(4,5)
circle=Circle(5)

print_area(rectangle)
print_area(circle)


##Polymorphism with abstract base classes

#abstract base class 
'''Abstract Base Classes (ABCs) are used to define common methods for a group of related objects. 
They can enforce that derived classes implement particular methods, promoting consistency across different implementations.'''

from abc import ABC, abstractmethod
## Define an abstract class
class Vechile(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vechile):
    def start_engine(self):
        return "Car engine started"

class MotorCycle(Vechile):
    def start_engine(self):
        return "Motorcycle engine started"

def start_vehicle(vehicle):
    print(vehicle.start_engine())
car=Car()
motorCycle=MotorCycle()

start_vehicle(car)