import csv

def InsertCSV(d):
    try:
        L1 = []  # List to store records with accno < 100
        with open('student.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            # Write header
            writer.writerow(['Customer ID', 'Account Number', 'Name', 'Balance'])

            for cid, details in d.items():
                if details["accno"] >= 100:
                    writer.writerow([cid, details["accno"], details["name"], details["balance"]])
                else:
                    L1.append([cid, details["accno"], details["name"], details["balance"]])
                    raise Exception("Name Error: Customer ID < 100")

    except Exception as e:
        print(f"Exception: {e}")
    finally:
        print("\nCSV File Content:")
        with open('student.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
        print("\nList of Accounts with ID < 100:")
        for item in L1:
            print(item)

n = int(input("Enter the No. of Bank Customer Details You want to Know: "))
d = {}
for i in range(n):
    print(f"Customer No. {i + 1} Details:\n")
    cid = int(input("Customer ID: "))
    accno = int(input("Account Number: "))
    name = input("Customer Name: ")
    balance = float(input("Balance: "))

    d[cid] = {
        "accno": accno,
        "name": name,
        "balance": balance
    }

InsertCSV(d)
