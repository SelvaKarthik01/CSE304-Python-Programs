# To find whether the given String is a Palindrome or not
s = input("Enter the String to find whether it is a Palindrome : ")
s1 = ""
for i in s:
    if ord(i) >= 65 and ord(i) <= 91 or ord(i) >= 97 and ord(i) <= 123 or i in "0123456789":
        s1 += i.lower()
if s1 == s1[::-1]:
    print("Yes !! It is a Palindrome !")
else:
    print("No !! It is not a Palindrome !")
        
        
