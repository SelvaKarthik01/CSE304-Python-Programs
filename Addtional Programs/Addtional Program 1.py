# Q1 Animal Program using Classes and Objects
import csv
class Animal :
    def __init__(self):
        self.name = ""
        self.lifetime = 0
        self.food = ""
        self.grade = ""
    def getDetails(self):
        self.name = input("Enter the Name of Animal  : ")
        self.lifetime = int(input("Enter the Lifetime of the Animal : "))
        self.food = input("Enter the Food of the Animal to be given : ")
    def putDetails(self):
        print("Name : ",self.name)
        print("Lifetime : ",self.lifetime)
        print("Food : ",self.food)
        print("Grade :  ",self.grade)

class Dog(Animal):
    def __init__(self):
        super().__init__()
        super().getDetails()
        self.usedin = "police departtment"
        self.noofcrimesdetected = int(input("Enter the No. of Crimes Detected : "))
        self.commandunderstanding = input("Enter the Ratio  : ")
    def ComputeFitness(self):
        if self.noofcrimesdetected >= 25:
            self.grade = "fit"
        elif self.noofcrimesdetected in range(15,25):
            self.grade = "moderate"
        elif self.noofcrimesdetected <= 15:
            raise Exception ("The Dog is Unfit !!")
        
class Horse(Animal):
    def __init__(self):
        super().__init__()
        super().getDetails()
        self.runningspeed = int(input("Enter the Running Speed of the Horse : "))
        self.breed = input("Enter the Breed of the Horse : ")
    def computeFitness(self):
        if self.runningspeed == 80:
            self.grade = "fit"
        elif self.runningspeed == 90:
            self.grade = "unfit"
        else:
            raise Exception ("INVALID SPEED !!!")
class Elephant(Animal):
    def __init__(self):
        super().__init__()
        super().getDetails()
        self.age = int(input("Enter the Age of the Elephant : "))
    def computeFitness(self):
        if self.age > 25:
            self.grade = "fit"
        else:
            raise Exception ("Elephant is Unfit")
def main():
    with open("Animal.csv",'w+',newline = '') as f:
        writer = csv.writer(f)
        writer.writerow(["Animal Type","Life Time","Food ","Grade","Private Attributes"])
        ch = 0
        while(ch != 5):
            print("1. Dog ")
            print("2. Horse ")
            print("3. Elephant")
            print("4. Display Details of  Animals ")
            print("5. To Exit ")
            
            ch = int(input("Enter Your Choice : "))
            if ch == 1:
                D = Dog()
                D.ComputeFitness()
                writer.writerow([D.name,D.lifetime,D.food,D.grade,D.usedin,D.noofcrimesdetected,D.commandunderstanding])
            elif ch == 2:
                H = Horse()
                H.computeFitness()
                writer.writerow([H.name,H.lifetime,H.food,H.grade,H.runningspeed,H.breed])
            elif ch == 3:
                E = Elephant()
                E.computeFitness()
                writer.writerow([E.name,E.lifetime,E.food,E.grade,E.age])
            elif ch == 4:
                f.seek(0)
                reader = csv.reader(f)
                for line in reader:
                    print(line)
            elif ch == 5:
                print("Thank You ...")
            else:
                print("Invalid Input Please Try again later....")
if __name__ == "__main__":
    main()
                
                
                
            
                
    
            
        
    
        
