# To Find the Reverse of a String
s = input("Enter the String : ")
print("Using Slicing : ",s[::-1])
print("Using Iteration : ",end = "")
s1 = ""
for i in range(len(s)-1,-1,-1):
    s1 += s[i]
print(s1)
