n = int(input())
s = list(map(int, input().split()))
count = {}

for i in s:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

maxc = 0
ans = None

for k in count:
    if count[k] > maxc or (count[k] == maxc and k < ans):
        maxc = count[k]
        ans = k
print(ans)


