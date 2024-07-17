# To Convert input into a Integer and Perform Mathematical Operations using Strings 
a = input("Enter the First Operand : ")
b = input("Enter the Second Operand : ")
a = int(a)
b = int(b)
n = input("Which Operation you wanna Perform (+ / - /  * /  /  / %) : ")
if n == "+":
    result = a + b
    print("The Addition of the Two Operands is : ",result)
elif n == "-":
    result = a-b
    print("The Subraction of the Two Operands is : ",result)
elif n == "*":
    result = a *b
    print("The Multiplication fo two Operands is : ",result)
elif n == "/":
    result = a/b
    print("The Division of the Two Operands is : ",result)
elif n == "%":
    result = a%b
    print("The Modulus of the Two Operands is : ",result)
else:
    print("Invalid OPerand Please Try Again Later !")
