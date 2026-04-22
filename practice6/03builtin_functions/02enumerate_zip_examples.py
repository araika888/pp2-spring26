#1
fruits=['apple','banana','cherry']
for i, fruit in enumerate(fruits):
    print(f"{i}:{fruit}")
print("Total fruits: ",len(fruits))
print()
#2
numbers=[5,10,15]
for i,num in enumerate(numbers):
    print(f"Index {i}={num}")
print("Sum of numbers: ",sum(numbers))
print()
#3
nums=[8,3,12,5]
for i, n in enumerate(nums):
    print(f"{i}->{n}")
print("Min: ",min(nums))
print("Max: ",max(nums))
#4
items=['dog','cat','bird','fish']
for i,item in enumerate(sorted(items)):
    print(f"{i}:{item}")
print()
#5
names=['Arman','Zarina','Anna']
ages=[24,46,32]
for i,(name,age) in enumerate(zip(names,ages)):
    print(f"{i}:{name} is {age} years old")