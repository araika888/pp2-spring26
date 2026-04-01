n=int(input())
k=list(map(int,input().split()))
max_num=k[0]
max_in=0
for i in range(1,n):
    if max_num<k[i]:
        max_num=k[i]
        max_in=i
print(max_in + 1)

