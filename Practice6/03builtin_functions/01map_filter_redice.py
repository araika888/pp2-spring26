#1
from functools import reduce
numbers=[1,2,3,4,5]
squares=list(map(lambda x:x**2,numbers))
print("Squares: ",squares)
#2
number=list(map(str,numbers))
print("string is:",number)
#3
evens=list(filter(lambda x:x%2==0,numbers))
print("Even number:",evens)
#4
big_number=list(filter(lambda x:x>3,numbers))
print("numbers where greater than 3: ",big_number)
#5
total=reduce(lambda x,y:x+y,numbers)
print("oxerall sum is: ",total)