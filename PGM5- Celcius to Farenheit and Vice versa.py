#  To Create a Program to Convert Fareheit to Celsius and vice versa
n = input("Do you want to Find Farenheit or Celcius(C or F) : ")
if n == "F" or n == 'f':
    celcius = float(input("Enter the Celcius to find Fareheit : "))
    fareheit = (celcius * (9/5)) + 32
    print("The Fareheit is : ",farenheit," oF")
elif n == "C" or n == "c":
    farenheit = float(input("Enter the Farenheit to find the Celcius : "))
    celcius = (farenheit - 32)*(5/9)
    print("The Celcius is : ",celcius," oC")
else:
    print("Invalid Input Please Try again !!")
