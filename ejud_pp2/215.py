n = int(input())
names = []
for _ in range(n):
    name = input()
    names.append(name)

count = {}
for name in names:
    if name in count:
        count[name] += 1
    else:
        count[name] = 1

q = 0
for name in count:
    if count[name]!=0:
        q += 1

print(q)