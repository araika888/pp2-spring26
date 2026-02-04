for c in "banana":
    print(c,end=",")
print()

number=[2,4,6,8,3,10,12]
for x in number:
    print(x,end="|")
    if x==3:
        break
print()

alphabet=['a','r','a','i','q']
for e in alphabet:
    if e!='q':
        print(e,end="")
    else:
        break
print()