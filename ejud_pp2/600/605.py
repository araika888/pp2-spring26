S=input().lower()
vowels="aeiou"
if any(x in vowels for x in S):
    print("Yes")
else:
    print("No")