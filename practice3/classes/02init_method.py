#1
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def info(self):
        return f"{self.title} — {self.author} ({self.pages} pages)"

title = "Gauhartas"
author = "Dulat Isabekov"
page = 87
p1 = Book(title, author, page)

print(p1.info())

#2
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
width = 20
height = 45

p = Rectangle(width, height)
print("Area:", p.area())
print("Perimeter:", p.perimeter())

#3
class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def is_honor(self):
        return self.gpa >= 3.5

name = "Madina"
major = "Information System"
gpa = 3.19

f = Student(name, major, gpa)
print(f.is_honor())

#4
class Car():
    def __init__(self, brand, year, model, current_year):
        self.brand = brand
        self.year = year
        self.model = model
        self.current_year = current_year

    def age(self):
        return self.current_year - self.year
    
brand = "Hyundai"
model = "Hyundai Elantra"
year = 2026
current_year = 2026

c = Car(brand, year, model, current_year)
print(c.age())

#5
class PointCoordinates():
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def show(self):
        return f"({x1}, {y1})"

    def move(self):
        return f"({x2}, {y2})"
    
    def euclidean(self):
        dict = ((self.x3-self.x2)**2 + (self.y3-self.y2)**2)**0.5
        return dict

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
p = PointCoordinates(x1, y1, x2, y2, x3, y3)
print(p.show())
print(p.move())
print(f"{p.euclidean():.2f}")

#6
class Account():
    def __init__(self, b, w):
        self.b = b
        self.w = w

    def wamount(self):
        if w > b:
            return "Insufficient Funds"
        else:
            return (b-w)
        
b, w = map(int, input().split())
p = Account(b, w)
print(p.wamount())

#7
class Circle():
    def __init__(self, pi, r):
        self.pi = pi
        self.r = r
    
    def area(self):
        return pi * (r**2)

r = int(input())
pi = 3.14159
p = Circle(pi, r)
print(f"{p.area():.2f}")

#8
class Person():
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
    
    def display(self):
        return f"Student: {name}, GPA: {gpa}"

name, gpa = input().split()
gpa = float(gpa)
p = Person(name, gpa)
print(p.display())

#9
class Pair():
    def __init__(self, a1, b1, a2, b2):
        self.a1 = a1
        self.b1 = b1
        self.a2 = a2
        self.b2 = b2
    
    def psum(self):
        a_sum = self.a1 + self.a2
        b_sum = self.b1 + self.b2
        return f"Result: {a_sum} {b_sum}"
    
a1, b1, a2, b2 = map(int, input().split())
p = Pair(a1, b1, a2, b2)
print(p.psum())