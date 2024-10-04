# Write Hobbies into a FIle without using Write() Function
with open("hobbies.txt",'w+') as f:
    L = []
    for i in range(5):
        print("Enter Hobby ",i+1," : ",end = "")
        hobby = input()
        L.append(hobby+"\n")
    for i in L:
        f.writelines(i)
    f.seek(0)
    print(f.read())
