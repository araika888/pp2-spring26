#1
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

#2
def get_greeting():
    return "Hello from a function"

message = get_greeting()
print(message)

#3
def func():
    return "Salem, Alem!"

print(func())

#4
def pifagor(a,b):
    return (a**2 + b**2)**0.5

a = 3
b = 4
c = int(pifagor(a, b))

print(c)

#5
def ToUpper(word):
    return word.upper()

s = "Hello World"
print(ToUpper(s))