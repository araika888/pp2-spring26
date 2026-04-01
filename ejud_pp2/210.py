n=int(input())
m=list(map(int,input().split()))
s=m.sort(reverse=True)
print(*m)