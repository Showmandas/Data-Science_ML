import math

# square root
x= math.sqrt(2*3)
# print(x)

base=10
height=20
hypotenus=math.sqrt(base ** 2 + height ** 2)
# print(hypotenus)

angle_radians= math.atan(height/base)
# print("area of radian : ",angle_radians)

angle_degree = math.degrees(angle_radians)
print("angle of degree : ",round(angle_degree,2)) #round the degree

ceil = math.ceil(angle_degree)
# print(ceil)

floor=math.floor(angle_degree)
print(floor)