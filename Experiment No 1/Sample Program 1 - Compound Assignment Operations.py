# To Exihibit the Functional Behaviour of all the Arithmatic Operators using Compound Assignment Operators
a = int(input("Enter the Value for a : "))
b = int(input("Enter the value for b : "))
a1 = a
b1 = b
a += b
print(a1," += ",b1," : ","a = ",a)
a = a1
b = b1 
a -= b
print(a1," -= ",b1," : ","a = ",a)
a = a1
b = b1 
a *= b
print(a1," *= ",b1," : ","a = ",a)
a = a1
b = b1 
a /= b
print(a1," /= ",b1," : ","a = ",a)
a = a1
b = b1 
a //= b
print(a1," //= ",b1," : ","a = ",a)
a = a1
b = b1 
a**= b
print(a1," **= ",b1," : ","a = ",a)
