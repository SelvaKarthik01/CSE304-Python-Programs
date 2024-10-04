# To Remove Duplicates Elements from the List
def rem_dup(L):
    L1 = []
    for i in L:
        if i not in L1:
            L1.append(i)
    L = L1
L = eval(input("Enter the List : "))
rem_dup(L)
print("The List after removal of Duplication : ",L)
