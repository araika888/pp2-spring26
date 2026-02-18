#1
class Animal:
    def speak(self):
        return "Animal makes sound"


class Dog(Animal):
    def speak1(self):
        return "Woof!"


a = Animal()
d = Dog()
print("1)", a.speak())  
print("1)", d.speak()) 

#2
class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


s = Shape()
r = Rectangle(4, 5)
print("2)", s.area())  # 0
print("2)", r.area())  # 20

#3
class Employee:
    def __init__(self, name):
        self.name = name

    def get_role(self):
        return "Employee"


class Manager(Employee):
    def get_role1(self):
        return "Manager"


e = Employee("Ali")
m = Manager("Madina")
print("3)", e.name, "-", e.get_role()) 
print("3)", m.name, "-", m.get_role())

#4
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            return "Amount must be positive"
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrawn: {amount}. Balance: {self.balance}"


class PremiumAccount(Account):
    FEE_RATE = 0.05  

    def withdraw(self, amount):
        if amount <= 0:
            return "Amount must be positive"

        fee = amount * self.FEE_RATE
        total = amount + fee

        if total > self.balance:
            return "Insufficient funds (including fee)"

        self.balance -= total
        return f"Withdrawn: {amount}, Fee: {fee}. Balance: {self.balance}"


acc = Account("Aruzhan", 1000)
pacc = PremiumAccount("Dias", 1000)
print("4)", acc.withdraw(200))   
print("4)", pacc.withdraw(200))  

#5 
class Notification:
    def send(self):
        return "Notification sent"


class EmailNotification(Notification):
    def __init__(self, email):
        self.email = email

    def send2(self):
        return f"Email sent to {self.email}"


n = Notification()
en = EmailNotification("user@mail.com")
print("5)", n.send())
print("5)", en.send())

#6
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Hi, I am {self.name}"


class Student(Person):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major

    def introduce(self):
        return f"Hi, I am {self.name} and I study {self.major}"


p = Person("Ali")
st = Student("Madina", "Information Systems")
print("6)", p.introduce())
print("6)", st.introduce())

#7
class Vehicle:
    def start(self):
        return "Vehicle started"


class Car(Vehicle):
    def start2(self):
        return "Car engine started"


v = Vehicle()
c = Car()
print("7)", v.start())
print("7)", c.start())