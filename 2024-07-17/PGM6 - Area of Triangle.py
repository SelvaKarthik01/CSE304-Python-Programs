# To Find the Area of Triangle using Three Sides of it
import math 
L = eval(input("Enter the Three sides of the Triangle : "))
if len(L) != 3:
    print("Invalid Input")
a = L[0]
b = L[1]
c = L[2]
s = a+b+c/2
area = math.sqrt((s*(s-a)*(s-b)*(s-c)))
print("The Area of the Triangle is : ",area," sq.cm")

    
