#1
class Person1:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person1("John", "Doe")
x.printname()

#2
class Person2:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student2(Person2):
    pass

x = Student2("Mike", "Olsen")
x.printname()

#3
class Person3:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student3(Person3):
    def __init__(self, fname, lname):
        Person3.__init__(self, fname, lname)

x = Student3("Mike", "Olsen")
x.printname()

#4
class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal makes sound"
    
class Dog(Animal):
    def bark(self):
        return "WOOF!"
    
dog1 = Dog("Aktos")
print(dog1.name)
print(dog1.speak())
print(dog1.bark())

#5
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def info(self):
        return f"Student name: {self.name} \nStudent age: {self.age} \nStudent major: {self.major}"
    
name = "Arai"
age = 18
major = "Information system"
studentinfo = Student(name, age, major)
print(studentinfo.info())