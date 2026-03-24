"""
when all the length of the sides of s the triangle is known as  -  a b  c 

 first  find semi perimeter  s = (a + b + c) / 2
 """ 

a  = float  (input("Enter the length of the first side of the triangle: "))

b  = float (input("Enter the length of the second side of the triangle: "))

c  = float (input("Enter the length of the third side of the triangle: ")) 

s = (a + b + c) / 2 
# area = (s * (s - a) * (s - b) * (s - c)) 

area = (s * (s - a) * (s - b) * (s - c)) ** 0.5 

print("The area of the triangle is:", area)

