n=int(input())
name=[]
for i in range(n):
    names=input()
    name.append(names)
count={}

for i in range(n):
    w=name[i]
    if w not in count:
        count[w]=i+1
    
for i in sorted(count):
    print(i,count[i])

n=int(input())

