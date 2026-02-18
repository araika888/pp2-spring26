#1
class MyClass1:
    x = 5

print(MyClass1)

#2
class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

#3
class Person1:
    name = "John"
    age = 36

print(Person1.name)

#4
class Person2:
    name = "John"
    age = 36

p1 = Person2()

print(p1.name)

#5
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old"
    
name = "Arai"
age = 18
p1 = Person(name, age)
print(p1.introduce())