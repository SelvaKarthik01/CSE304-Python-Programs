# To Build a Shopping Cart management using Dicrtionaries
d = {}
print("\t ************************ Shopping Cart Management ***************************** \t")
ch = 0
while(ch != 5):
    print("1. Add Item to Cart")
    print("2. View Cart ")
    print("3. Remove Item from Cart ")
    print("4. Calculate Total Cost ")
    print("5. To Exit ")
    ch = int(input("Enter Your Choice : "))
    if ch == 1:
        item_code = input("Enter the Item Code to be Added in Cart : ")
        item_name = input("Enter the Item Name to be Added in Cart : ")
        price = float(input("Enter the Price of the Item : "))
        qty = int(input("Enter Quantity of the Item : "))
        if item_code not in d:
            d[item_code] = [item_name,price,qty]
            print("Item Added to Cart Successfully !!")
        else:
            print("Item Already Exists !!")
    elif ch == 2:
        print("Shopping Cart Contents : ")
        print()
        for i,j in d.items():
            print("Item Code : ",i," | Item Name : ",j[0]," | Price : ",j[1]," | Quantity : ",j[2])
    elif ch == 3:
        delete = input("Enter the Item Code to be Removed :  ")
        if delete in d:
            del d[delete]
            print("Item Successfully removed from the Cart !!")
            break
        else:
            print("Item Not Found in Cart !!")
    elif ch == 4 :
        cost = 0
        for i in d.values():
            cost += i[1]*i[2]
        print("Total Cost of All  Items in the Cart : $",cost)
    elif ch == 5:
        print("Thank You and Visit Again !!")
    else:
        print("Invalid Input Please Try Again !!")
    
