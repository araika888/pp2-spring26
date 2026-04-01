def num(q):
    if q<=0:
        return False

    for p in [2,3,5]:
        while q%p==0:
            q//=p

    return q==1

q=int(input())

if num(q):
    print("Yes")
else:
    print("No")