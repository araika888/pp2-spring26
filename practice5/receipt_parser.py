#1
import re
pattern="ab*"
tests=["a","abbb","abc","ac","abbc","cab"]
for s in tests:
    if re.fullmatch(pattern,s):
        print(s,"fits")
    else:
        print(s,"not fits")
#2
import re
pattern="abb"
pattern2="abbb"
tests=["abb","abbb","a","abcb","abbbb","aabb","aaaa","abb"]
for k in tests:
    if re.fullmatch(pattern,k) or re.fullmatch(pattern2,k):
        print(k,"it's match")
    else:
        print(k,"it's not match")
#3
import re
pattern="^[a-z]+_[a-z]+$"
tests=["abc_def","a_b","hello_world","A_Bcd","abc__def","_a_v","abc_"]
for i in tests:
    if re.fullmatch(pattern,i):
        print(i,"it's match")
    else:
        print(i,"it's not match")
#4
import re
pattern="ab{0,1}"
tests=["abb","a","ab","abb","abc","aabbb","aabb"]
for w in tests:
    if re.fullmatch(pattern,w):
        print(w,"it's match")
    else:
        print(w,"it's not match")
#5
import re
patter="ab+"
tests=["aaabbbb","abb","abbbb","aabbbb","a","abbbb"]
for t in tests:
    if re.fullmatch(patter,t):
        print(t,"it's match")
    else:
        print(t,"it's not match")
#6
import re
pattern="ab{0,1}c"
tests=["abc","ac","abbc","acc"]
for q in tests:
    if re.fullmatch(pattern,q):
        print(q,"it's math")
    else:
        print(q,"it's not match")
#7
import re
pattern="a[bc]"
tests=["ab","ac","abc","acb","bc"]
for p in tests:
    if re.fullmatch(pattern,p):
        print(p,"it's match")
    else:
        print(p,"it's not match")
#8
import re
pattern="a.*b"
tests=["a123b","ab","abdcfdb","abcd","aSDEDEDXDb"]
for a in tests:
    if re.fullmatch(pattern,a):
        print(a,"it's match")
    else:
        print(a,"it's not match")
#9
import re
pattern="[0-9].*"
tests=["12s","c23","22a","1_0arai","1numberkbtu"]
for m in tests:
    if re.fullmatch(pattern,m):
        print(m,"it's match")
    else:
        print(m,"it's not match")
#10
import re
pattern=".*[0-9]"
tests=["araika888","tknvarai008","1task1","7","908raya0","kbtu1","uni45m"]
for g in tests:
    if re.fullmatch(pattern,g):
        print(g,"it's match")
    else:
        print(g,"it's not match")