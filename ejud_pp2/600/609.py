n=int(input())
Key=input().split()
Values=input().split()
i=input()
result=dict(zip(Key,Values))
if i in result:
    print(result[i])
else:
    print("Not found")
