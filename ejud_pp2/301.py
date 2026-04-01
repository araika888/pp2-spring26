m=list(map(int,input()))
a=len(m)
p=0
p1=0
for i in range(a):
    if m[i]%2==0:
        p+=1
    else:
        p1+=1
if p==a:
    print("Valid")
else:
    print("Not valid")

        
    

