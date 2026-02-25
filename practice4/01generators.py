#1
def square(n):
    for i in range(1,n+1):
        yield i*i
n = int(input())
for i in square(n):
    print(i)
#2
def even(n):
    for i in range(0, n+1):
        if i % 2 == 0:
            yield i

n = int(input())
for i in even(n):
    if i != 0:
        print(",", end="")
    print(i, end="")

#3
def calc(n):
    for i in range(0,n+1):
        if i%3==0 and i%4==0:
            yield i
n=int(input())
for i in calc(n):
    print(i)

#4
def sqr(a,b):
    for i in range(a,b+1):
        yield i*i
a=int(input())
b=int(input())
for i in sqr(a,b):
    print(i)

#5
def num(n):
    for i in range(0,n+1):
        yield i
n=int(input())
for i in num(n):
    print(i)