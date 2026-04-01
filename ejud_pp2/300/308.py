import math
rise,radian=map(int,input().split())
radian=math.atan(rise/radian)
gradus=math.degrees(radian)
print(gradus)