# To Create a Program to Calculate the The Area of Square and Area of Circle
import math
n = int(input("Do You want to find the Area of Square or  Circle : (1/2)"))
if n == 1:
    side = float(input("Enter the Length of the Side of Square : "))
    area_square = side **2
    print("The Area of the Square is : ",area_square,"sq.cm")
elif n == 2:
    radius = float(input("Enter the Radius of the Circle : "))
    area_circle = math.pi *(radius**2)
    print("The Area of the Circle is : ",area_circle,"sq.cm")
else:
    print("Invalid Input Try Again !!")

    
