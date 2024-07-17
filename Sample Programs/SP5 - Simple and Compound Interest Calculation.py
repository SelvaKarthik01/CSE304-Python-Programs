# To Calculate the Simple and Compound Interest
p = float(input("Enter the Principle amount : "))
r =  float(input("Enter the Rate of Interest : "))
t = int(input("Enter the Total No. of Years : "))
simple_interest = p*r*t/100
compound_interest = p*((1+r/100)**t) - p
print("The Simple Interest is : ",simple_interest)
print("The Compound Interest is : ",compound_interest)
