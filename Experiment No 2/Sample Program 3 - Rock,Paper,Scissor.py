# To Create a Simple Rock Paper Scissor Console Game
import random 
print("Welcome to the Rock Paper Scissor")
n = 0
while(n != 4):
    print("1. Rock ")
    print("2. Paper ")
    print("3. Scissor ")
    print("4. Exit ")
    n = int(input("Enter Your Choice"))
    ch = random.randint(0,2)
    choice = ["Rock","Paper","Scissor"]
    if n == 1 and choice[ch] == "Rock":
        print("You Choose Rock !")
        print("Computer Choose Rock !")
        print("Both are Equal !")
    elif n == 1 and choice[ch] == "Paper":
        print("You Choose Rock !")
        print("Computer Choose Paper !")
        print("You Win !")
    elif n == 1 and choice[ch] == "Scissor":
        print("You Choose Rock !")
        print("Computer Choose Scissor !")
        print("Computer Wins !")
    elif n == 2 and choice[ch] == "Rock":
        print("You Choose Paper !")
        print("Computer Choose Rock !")
        print("You Win !")
    elif n == 2 and choice[ch] == "Paper":
        print("You Choose Paper !")
        print("Computer Choose Paper !")
        print("Both are Equal !")
    elif n == 2 and choice[ch] == "Scissor":
        print("You Choose Paper !")
        print("Computer Choose Scissor !")
        print("ComputerWins !")

    elif n == 3 and choice[ch] == "Rock":
        print("You Choose Scissor !")
        print("Computer Choose Rock !")
        print("Computer Wins !")

    elif n == 3 and choice[ch] == "Paper":
        print("You Choose Scissor !")
        print("Computer Choose Paper !")
        print("You Win !")

    elif n == 3 and choice[ch] == "Scissor":
        print("You Choose Scissor !")
        print("Computer Choose Scissor !")
        print("Both are Equal !")
    elif n == 4:
        print("Thank You for Playing with Us :)")
    a = input("Do You Wan to Play Again (Y/N) : ")
    if a == "Y":
        continue
    else:
        break

    
    
        
