# Input a Square Matrix and fin sum of upper and lower triangular matrix
n = int(input("Enter the No. of Rows : "))
m = int(input("Enter the No. of Columns : "))
A = []
if (n != m):
    raise Exception("Out of Bound : Given Matrix is not a Square Matrix !!")
else:
    for i in range(n):
        r=[]
        for j in  range(m):
            print("A[",i,"][",j,"] : ",end = "")
            r.append(int(input()))
        A.append(r)
    print("The Given Square Matrix is : ")
    for i in range(n):
        for j in range(m):
            print(A[i][j],end = " ")
        print()
    # Calculate Lower triangular Matrix
    lower,upper =0,0
    for i in range(n):
        for j in range(m):
            if (i==j or j < i):
                lower += A[i][j]
            if (i == j or j > i):
                upper += A[i][j]
    print("Sum of Lower Triangular Matrix Elements :  ",lower)
    print("Sum of Upper Triangular Matrix Elements : ",upper)
                
                
            
            
