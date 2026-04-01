n=int(input())
words=input().split()
result=max(words,key=len)
print(result)