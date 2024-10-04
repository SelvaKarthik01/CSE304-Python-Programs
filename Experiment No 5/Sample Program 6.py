# Copy from One CSV File to Another
import csv
with open("input.csv",'r') as f:
    reader = csv.reader(f)
    with open("input1.csv",'w',newline='') as f1:
        writer = csv.writer(f1)
        for row in reader :
            writer.writerow(row)
            print("Rows Written Successfully !!")

    
    
