#1 
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

#2
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

#3
numbers = [-3, 5, -1, 7, 0]
pos_nums = list(filter(lambda x : x > 0, numbers))
print(pos_nums)

#4
words = ["apple", "banana", "kiwi", "watermelon"]
s = list(filter(lambda x : len(x) > 5, words))
print(s)

#5
numbers = [3, 12, 7, 25, 9, 15]
g = list(filter(lambda x : x > 10, numbers))
print(g)

#6
words = ["apple", "banana", "orange", "grape", "avocado"]
a = list(filter(lambda x : x[0] == "a" or x[0] == "e" or x[0] == "o" or x[0] == "u" or x[0] == "i", words))
print(a)

#7
numbers = [3, 5, 9, 10, 12, 14]
t = list(filter(lambda x : x % 3 == 0, numbers))
print(*a)

#8
numbers = [-5, 1, 3, 8, 15, 25]
c = list(filter(lambda x : x >= 2 and x <=20, numbers))
print(c)

#9
prices = [500, 1500, 700, 2000, 300]
k = list(filter(lambda x : x > 1000, prices))
print(k)

#10
words = ["code", "python", "AI", "data", "science"]
f = list(filter(lambda x : len(x) > 4, words))
print(f)