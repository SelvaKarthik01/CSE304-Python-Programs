#To Calculate the Salary of the Employee
basic_pay = float(input("Enter the Basic Pay if the Employee : "))
hra = 0.10 * basic_pay
ta = 0.05 *basic_pay
gross_salary = basic_pay + hra + ta
net_salary = gross_salary - 0.02*basic_pay
print("The Total Gross Salary of the Employee is : ",gross_salary)
print("The Total Net Salary of the Employee is : ",net_salary)
