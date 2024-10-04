# Search a Particular record froma  CSV File
import csv
with open("input.csv",'r') as f :
    reader = csv.reader(f)
    search = input("Enter the Register No. to Search : ")
    for row in reader:

        if row[0] == search:
            print("Register No. : ",row[0])
            print("Name : ",row[1])
            print("Year : ",row[2])
            print("Section : ",row[3])
            print("Marks : ",row[4])
            break
    else:
        print("Given Register No. not found in the File !")
    
