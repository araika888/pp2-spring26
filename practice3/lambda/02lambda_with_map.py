#1
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

#2
nums = [85, 741, 9, 54, 41]
newm = list(map(lambda x: x * x, nums))
print(newm)

#3
numbers = [1, 2, 3]
n = list(map(lambda x : str(x), numbers))
print(n)

#4
temps = [0, 20, 30]
f = list(map(lambda x : x * 9/5 + 32, temps))
print(f)

#5
words = ["apple", "banana", "kiwi"]
lw = list(map(lambda x : len(x), words))
print(lw)