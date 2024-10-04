# To Calculate the Area of Triangle Circle and Rectangle
import math 
n = 0
while(n != 4):
    print("1. Area of Circle ")
    print("2. Area of Rectangle ")
    print("3. Are of Triangle ")
    print("4. To Exit")
    n = int(input("Enter Your Choice : "))
    if n== 1:
        radius = float(input("Enter the Radius of the Circle : "))
        area = math.pi*(radius**2)
        print("The Area of the Circle : ",area," sq cm.")
    elif n == 2:
        length = float(input("Enter the Length of the Rectangle : "))
        breadth = float(input("Enter the Breadth of the Rectamngle : "))
        area = length*breadth
        print("The Area of the Rectangle is : ",area," sq cm.")
    elif n == 3:
        ch = 0
        print("1. Know Height and Breadth of Traingle ")
        print("2. Know All Three sides of the Triangle ")
        ch = int(input("Enter Your Choice : "))
        if ch == 1:
            breadth = float(input("Enter the Breadth of the Triangle : "))
            height = float(input("Enter the Height of the Triangle : "))
            area = 0.5 * breadth* height
            print("The Area of the Triangle is : ",area," sq cm.")
        elif ch ==2 :
            s1 = float(input("Enter Length of Side 1 : "))
            s2 = float(input("Enter Length fo Side 2 : "))
            s3 = float(input("Enter Length of Side 3 : "))
            s = (s1+s2+s3)/ 3
            area = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
            print("The Area of the Triangle is : ",area," sq cm.")
    elif n == 4:
        print("Thank You !!")
    else:
        print("Invalid Input Please Try Again !!")
