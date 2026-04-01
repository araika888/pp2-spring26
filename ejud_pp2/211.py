n,l,r=map(int,input().split())
m=list(map(int,input().split()))
m[l-1:r]=reversed(m[l-1:r])
print(*m)