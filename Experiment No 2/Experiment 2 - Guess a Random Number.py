# To Guess a Random Number bewteen 1 and 9
import random
target = random.randint(1,10)
while(True):
    n = int(input("Guess a Number between 1 and 9 : "))
    if n >= 1 and n <= 9:
        if n > target :
            print("Oh Too High !! Try again with a Lower Number !")
        elif n < target :
            print("Oh Too Low !! Try again with a Higher Number !")
        elif n == target:
            print("Oh You Guessed It ! Its ",target)
            break
        else:
            print("Unexpected Error Occured Please Try Again !!")
    else:
        print("Invalid Input Please Enter a Number Between 1 and 9 ONLY !")
    
