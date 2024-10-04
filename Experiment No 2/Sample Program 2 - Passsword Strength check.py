# To Check the Strength of the Password
email = input("Enter Your Email ID : ")

upper,lower,digit = 0,0,0
if email.endswith("@sastra.ac.in") or email.endswith("@sastra.edu"):
    pwd = input("Enter Your Password : ")
    if len(pwd) > 8:
        for i in range(len(pwd)):
            if pwd[i].isupper():
                upper = 1
            elif pwd[i].islower():
                lower = 1
            elif pwd[i].isdigit():
                digit = 1
            elif s[i] in "!@#$%^&*(),.?:{}|<>":
                    special = 1
        if upper == lower == digit == 1 or upper ==digit ==1 or lower == digit == 1 and special ==1:
            print("Hey its a Strong Password !!")
        elif upper == lower == digit == 1 or upper ==digit ==1 or lower == digit == 1 and special ==0 :
                print("Its Moderate Password  !")
        else:
            print("Its Weak Password  !")
    else:
        print("Its a Weak Password !!")
else:
    print("Domain Email ID is wrong cannot perform Password Check !!")
    
                
