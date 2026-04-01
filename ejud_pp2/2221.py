n=int(input())
arr=list(map(int,input().split()))
first=arr[0]
count=0

for i in arr:
    if first==arr[i]:
        count+=1
print(count)