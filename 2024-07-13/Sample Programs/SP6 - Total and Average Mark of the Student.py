#To Find the Total and Average of the Student
n = int(input("Enter the No. of Subjects : "))
sum = 0 
for i in range(1,n+1):
    print("Enter the Mark in Subject",i," : ",end = "")
    sum += int(input())
print("The Total Marks Obtained by the Student is : ",sum)
avg  = sum /n
print("The Average Mark Obtained by the Student is : ",avg)

               
