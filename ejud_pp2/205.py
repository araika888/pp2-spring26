n=int(input())
m=list(map(int,input().split()))
a=m[0]
for i in range(n):
    if a<m[i]:
        a=m[i]
print(a)