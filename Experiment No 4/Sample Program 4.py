# Developing a E-Commerce Platform
products = {}
customer = {}
order = {}
ch = 0
while(ch != ):
    print("1. Search a Product ")
    print("2. Sell a Product ")
    print("3. Buy a Product  ")
    print("4. Track Order")
    print("5. Administrator ")
    print("6. To Exit ")
    ch = int(input("Enter Your Choice : "))
    if ch == 1:
        search = input("Enter a Product Name to find related Searches : ")
        for i,j in products.items() :
            if search in j[0] :
                print("Product ID : ",i)
                print("Product Name : ",j[0])
                print("Product Price : ",j[1])
                print("Product Addtional Info : ",j[2])
                print()
                print("\t*********************X***********************\t")
    elif ch == 2:
        prod_name = input("Enter the Product Name to be Sold : ")
        prod_price = float(input("Enter the Price to be Sold : "))
        prod_info = input("Any Additonal Information That the Buyer needs to Know : ")
        products["Prod"+str(len(products))] = [prod_name,prod_price,prod_info]
        print("Product is now Added to the Cataloge Buyers can View it Thank You ... ")
    elif ch == 3:
        buy = input("Enter Product ID to be Bought : ")
        if buy in products:
            print("\t ****************** Customer Details ********************* \t ")
            cust_name = input("Enter Your Name : ")
            cust_address = input("Enter Your Address for Shipping : ")
            cust_pay = input("Enter Mode of Payment (Cash/Card/Net) : ")
            ship_status = 0
            print("Order Placed Successfully !")
            customer[buy] = [cust_name,cust_address,cust_pay,ship_status]
        else:
            print("Product ID ",buy," is not Found !!")
    elif ch == 4:
        print("\t *********************** Administration *************************** \t")
        id = input("Enter Product Id to Check for Status : ")
        if id in customer :
            status = int(input("Is the Product Shipped Successfully To the Customer ? (1/0) : "))
            if status == 1:
                customer[id][3] = 1
