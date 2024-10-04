# To Insert a element in List
L = eval(input("Enter the List : "))
L.sort()
el = eval(input("Enter the Element to be Added : "))
pos = int(input("Enter the Position to be Added : "))
if pos > len(L):
    print("Invalid Position Out of Range !")
else:
    L.insert(pos,el)
print(L)
