n=int(input())
count={}
for i in range(n):
    l,x=input().split()
    x=int(x)

    if l in count:
        count[l]+=x
    else:
        count[l]=x

for k in sorted(count):
    print(k,count[k])