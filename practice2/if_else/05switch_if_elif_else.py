
username="Email"
password="python123"
is_active=True

if username:
    if password:
        if is_active:
            print("Log successful")
        else:
            print("Log not successful")
    else:
        print("Password required")
else:
    print("Username required")

a=100
b=300 
if b<a:
    print("YES")
else:
    pass

m=8
d=26
match d:
    case 1 | 2 | 3 | 26 | 28 if m==8:
        print("my birthday")
    case _:
        print("No match")
