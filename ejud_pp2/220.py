n = int(input())
doc = {}
for _ in range(n):
    cmd = input().split()
    if cmd[0] == "set":
        doc[cmd[1]] = cmd[2]
    elif cmd[0] == "get":
        key = cmd[1]
        if key in doc:
            print(doc[key])
        else:
            print("KE: no key", key, "found in the document")
