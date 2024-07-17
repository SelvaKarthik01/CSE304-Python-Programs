# To Calculate Area of Triangle using all three sides
import math 
s1 = float(input("Enter the Length of Side 1 : "))
s2 = float(input("Enter the Length of Side 2 : "))
s3 = float(input("Enter the Length of Side 3 : "))
semi = (s1+s2+s3)/3
area = math.sqrt(semi*(semi-s1)*(semi -s2)*(semi-s3))
print("The Area of the Triangle is : ",area,"sq.cm")
