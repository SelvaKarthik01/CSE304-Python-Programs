from datetime import date
today = date.today()
date1 = input("Enter your DOB : (DD-MM-YYYY)")
L = date1.split("-")
my_date = date(2024,int(L[1]),int(L[0]))
print(my_date)
print(today)
rem = my_date - today
print(rem)
print("Total No. of Days Remaining for Your Birthday is : ",rem)
year = int(input("Enter a Year to find if its Leap Year or not : "))
if (year % 100 != 0 and year % 4 == 0 or year  % 400 == 0):
    print("Its a Leap year !!")
else:
    print("Its not a Leap Year")
