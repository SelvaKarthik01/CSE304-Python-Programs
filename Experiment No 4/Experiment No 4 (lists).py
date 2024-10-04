# String Encryption and Decryption
ch = 0
while(ch != 3):
    print("1. Encryption")
    print("2. Decryption")
    print("3. To Exit ")
    ch = int(input("Enter Your Choice :  "))
    if ch == 1:
        s = input("Enter the String for Encryption : ")
        s = list(s)
        for i in range(len(s)):
            s[i] = chr(ord(s[i])+2)
        s = "".join(s)
        print("The Encrypted String : ",s)
    elif ch == 2:
        s = input("Enter String for Decryption : ")
        s = list(s)
        for i in range(len(s)):
            s[i] = chr(ord(s[i])-2)
        s = "".join(s)
        print("The Decrypted String : ",s)
    elif ch == 3:
        print("Thank You ")
    else:
        print("Enter Valid Choice !!")
