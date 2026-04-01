n=int(input())
k=list(map(int,input().split()))
minn=100000000000
a=max(k)
for i in range(n):
    if minn>k[i]:
        minn=k[i]

for i in range(n):
    if a==k[i]:
        k[i]=minn
print(*k)
