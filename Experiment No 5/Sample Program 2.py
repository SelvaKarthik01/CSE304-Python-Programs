# To Write fruit names in a File
with open("fruits.txt",'a+') as f:
    L = eval(input("Enter the List fo Fruits Name to be Added : "))
    for i in L:
        f.write(i+"\n")
    print("Fruits Written into File Successfully !!")
    
