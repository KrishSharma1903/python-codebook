##Class is a blue print for creating objects, attributes,methods
class Car:
    pass

audi=Car()
bmw=Car()
print(type(bmw))
print(audi)
print(bmw)

audi.windows=4 #defining attributes like this isnt a proper way 
print(audi.windows)

#Instance variable (attributes)
class Dog:
    ##Constructor 
    def __init__(self,name,age): #-> helps in defining initial attributes
        self.name = name #self variable is used to access the instance variable inside the class itself whenever we create an object 
        self.age = age

#creating the object 
dog1=Dog("Tommy",12)
print(dog1)
print(dog1.name)
print(dog1.age)

##instance Methods
#Define a class with instance methods 
class Dog: 
    def __init__(self,name,age):
        self.name = name 
        self.age = age

    def bark(self):
        print(f"{self.name} says woof")

dog1=Dog("Muku",4)
dog1.bark()

dog2=Dog("Buddy",3)
dog2.bark()
        

##EXAMPLE -> Modeling a bank account

##Define a class for bank account
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance += amount
        print(f"{amount} is deposited, New balance is {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Current balance {self.balance}")

    def get_balance(self):
        return self.balance

##create a bank account 
account = BankAccount("Krish",200)
account.deposit(500)
account.withdraw(1000)
account.withdraw(10)
print(account.get_balance())