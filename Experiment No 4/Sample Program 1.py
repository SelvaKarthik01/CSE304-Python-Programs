# Student Mark management System
d = {}
ch = 0
while(ch != 4):
    print("1. Add Student Details ")
    print("2. Calculate Average ")
    print("3. Display All Student Details ")
    print("4. To Exit ")
    ch = int(input("Enter Your Choice : "))
    if ch == 1:
        name = input("Enter Student Name : ")
        n = int(input("How Many Subjects has the Student Appeared : "))
        L = []
        for i in range(n):
            print("Enter Mark for Subject ",i+1," : ",end = "")
            mark = int(input())
            L.append(mark)
        if name not in d:
            d[name] = L
            print("Student Details added Successfully !!")
        else:
            print("Student Details Already Exists !!")
    elif ch == 2:
        search = input("Enter Student Name To Find Average and Otehr Details : ")
        if search in d:
            print("Student Name : ",search)
            print("Marks : ")
            count = 1
            for i in d[search]:
                print("Mark ",count," : ",i)
                count += 1
            print("Average : ",sum(d[search])/len(d[search]))
        else:
            print("Student Name Not Found !!")
    elif ch == 3:
        print("All Student Details in Database : ")
        for i,j in d.items():
            print("Student Name : ",i," | Student Marks : ",j)
    elif ch == 4:
        print("Thank You !!")
    else :
        print("Invalid Input Please Try Again !!")

    
