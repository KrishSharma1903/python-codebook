## Abstraction
'''Abstraction is the concept of hiding the complex implementation details and showing only the necessary features of an object. 
This helps in reducing programming complexity and effort.'''

from abc import ABC, abstractmethod
##Abstract base class
class Vechile(ABC): #inheriting the ABC class for abstraction 
    def drive(self):
        print("The vechile is used for driving ")

    @abstractmethod #subclass must implement this function in their own way
    def start_engine(self):
        pass

class Car(Vechile):
    def start_engine(self):
        print("car engine started")


def operate_vehicle(vehicle):
    vehicle.start_engine()
    vehicle.drive()

car=Car()
operate_vehicle(car)