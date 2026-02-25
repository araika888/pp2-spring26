#1
import math
degree=float(input("input your degree:"))
radian=math.radians(degree)
print("radian equal is:",round(radian,6))

#2
height=float(input("input height:"))
base1=float(input("input base1:"))
base2=float(input("input base2:"))
S1=((base1+base2)/2)*height
print("Area of trapezoid:",S1)

#3
import math
n=float(input("input n:"))
s=float(input("input s:"))
S2=(n*s**2)/(4*math.tan(math.pi/n))
print("Area of regular polygon:" , S2)
#4
base=float(input("input base:"))
height=float(input("input height:"))
S3=base*height
print("Parallelogram area:" , S3)