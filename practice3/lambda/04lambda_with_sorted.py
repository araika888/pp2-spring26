#1
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

#2
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

#3
numbers = [5, 2, 9, 1, 7]
sort = sorted(numbers, key = lambda x : x)
print(sort)

#4
nums = [3, 8, 1, 6, 2]
s = sorted(nums, key = lambda x: x, reverse = True)
print(s)

#5
numbers = [-10, 5, -3, 2, -1]
ss = sorted(numbers, key = lambda x: abs(x))
print(ss)

#6
words = ["apple", "kiwi", "banana", "fig"]
ws = sorted(words, key = lambda x: len(x))
print(ws)

#7
words = ["cat", "dog", "bat", "apple"]
sw = sorted(words, key = lambda x: x[-1])
print(sw)

#8
students = [
    ("Ali", 85),
    ("Madina", 92),
    ("Arman", 78)
]
st = sorted(students, key = lambda x: x[1])
print(st)