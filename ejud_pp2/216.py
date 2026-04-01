n=int(input())
s=list(map(int,input().split()))
count={}

for i in s:
    if i in count:
        print("NO")
        count[i]+=1
    else:
        print("YES")
        count[i]=1


n=int(input())
a=list(map(int,input().split()))
count={} 
for i in a:
    if i in count:
        print("NO")
        count[i]+=1
    else:
        print("YES")
        count[i]=1  