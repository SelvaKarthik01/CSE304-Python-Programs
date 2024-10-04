# To Show words less than 3 in a file
with open("newfile.txt",'r') as f:
    words = f.read()
    words = words.split()
    print("All words less than 3 in the file :  ")
    for i in words:
        if len(i) <= 3:
            print(i)
