n=int(input())
m=list(map(int,input().split()))
unique_incr=sorted(set(m))
print(*unique_incr)