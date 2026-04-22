#1
f=open("demofile.txt")
print(f.read())
#2
file=open("demofile.txt","r")
content=file.read()
print(content)
file.close()
#3
with open("demofile.txt","r") as file:
    content=file.read()
    print(content)
#4
f=open("demofile.txt")
print(f.readline())
f.close()
#5
with open("demofile.txt") as f:
    print(f.read(5))
#6
with open("demofile.txt") as f:
    print(f.readline())
    print(f.readline())
#7 
with open("demofile.txt") as f:
    for x in f:
        print(x)