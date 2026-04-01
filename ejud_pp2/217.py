n=int(input())
name=[]
for i in range(n):
    names=input()
    name.append(names)
count={}
for i in name:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

q=0
for i in count:
    if count[i]==3:
        q+=1
print(q)