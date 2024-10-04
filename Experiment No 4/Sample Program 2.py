# Tuple Packing and Unpacking Applications
t = ()
ch = 0
while(ch != 3):
    print("1. Add Person")
    print("2. Display Details ")
    print("3. To Exit ")
    ch = int(input("Enter Your Choice : "))
    if ch == 1:
        name = input("Enter the Name of the Person : ")
        age = int(input("Enter the Age of the Person : "))
        address = input("Enter the Address of the Person : ")
        t += ((name,age,address),)
    elif ch == 2:
        search = input("Enter the Name to be Searched : ")
        for i in t:
            if i[0] == search:
                name,age,address = i
                break
            
        print("Name : ",name)
        print("Age : ",age)
        print("Address : ",address)
    elif ch == 3:
        print("Thank You")
    else:
        print("Invalid Input Please Try Again !!")
    
