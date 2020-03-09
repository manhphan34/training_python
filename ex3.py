from math import sqrt, pow
c1 = input("Enter lenght of c1: ")
while c1.isdigit() == False or int(c1) <= 0: 
    c1 = input("Enter lenght of c1: ")
c2 = input("Enter lenght of c2: ")
while c2.isdigit() == False or int(c2) <= 0: 
    c2 = input("Enter lenght of c2: ")
print("hypotenuse = ", sqrt(pow(int(c1),2) + pow(int(c2), 2)))
print("acreage = ", int(c1)*int(c2)/2)

