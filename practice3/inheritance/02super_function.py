#1
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)

#2
class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price

class DiscountedProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount
    
    def final_sum(self):
        return self.price - (self.price * self.discount)/100

name = "Shoes"
price = 42000
discount = 20
f = DiscountedProduct(name, price, discount)
print(f.final_sum())

#3
class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

class SavingAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    def newbalance(self):
        return f"New balance for {self.owner}: {int(self.balance +(self.balance * self.interest_rate)/100)}"
    
n = SavingAccount("Arai", 850000, 50)
print(n.newbalance())

#4
class Shape:
    def __init__(self, color):
        self.color = color

    def describe(self):
        return f"This shape is {self.color}."


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)   
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def info(self):
        return f"Circle color: {self.color}, Radius: {self.radius}"
    
c1 = Circle("Red", 5)

print(c1.describe())   
print(c1.info())       
print("Area:", c1.area())

#5
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal makes sound"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # ← Animal-дың __init__ шақыру
        self.breed = breed

    def bark(self):
        return "Woof!"

    def info(self):
        return f"Name: {self.name}, Breed: {self.breed}"
    
dog1 = Dog("Rex", "Labrador")

print(dog1.info())
print(dog1.speak())  
print(dog1.bark())    