# To FInd the Sum of Lower and Upper Triangular Matrix elements
n = int(input("Enter the No. fo Rows : "))
m = int(input("Enter the No. fo Columns : "))
L = []
for i in range(n):
    L1 = []
    for j in range(m):
        print("A[",i,"]","[",j,"] : ")
        a =  int(input())
        L1.append(a)
    L.append(L1)
for i in range(n):
    for j in range(m):
        print(L[i][j],end = " ")
    print()
    
sum_upper ,sum_lower = 0,0
for i in range(n):
    for j in range(m):
        if j <= i:
            sum_lower += L[i][j]
            print(L[i][j])

for i in range(n):
    for j in range(m):
        if j >= i:
            sum_upper += L[i][j]

print("Sum of Lower Triangular Matrix is : ",sum_lower)
print("Sum of Upper Triangular Matrix is : ",sum_upper)
