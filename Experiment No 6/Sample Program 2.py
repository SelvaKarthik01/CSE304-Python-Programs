# To Create a Dictionary called Product to store information and Create  user Defined Exception
product = {}
d = {}
def getData(product):
    product_code = int(input("Enter the product Code : "))
    if product_code in product:
        raise Exception("DUPLICATE : Product Details Already Present ")
    else:
        product_name = input("Enter the Product Name : ")
        product_qty = int(input("Enter the Quantity : "))
        product_price = float(input("Emter the Price: "))
        d["Name"] = product_name
        d["Qty"] = product_qty
        d["Price"] = product_price
        product[product_code] = d
def Search(product):
    searchid = int(input("Enter the Product ID ot be Searched : "))
    try:
        if searchid in product:
            for i,j in product.items():
                if i == searchid:
                    total = j["Qty"]*j["Price"]
                    print("Total Cost : ",total)
                    break
        else:
            raise Exception("Not Found : The Product ID is not Present")
    except Exception as e:
        print(f"Exception : {e}")
n = int(input("Enter the Total No. of Products to be Added : "))
for i in range(n):
    getData(product)
Search(product)
