#  To Calculate the BMI for a Person
weight = float(input("Enter the Weight of the Person (in Kgs) : "))
height = float(input("Enter the Height of the Person :(in cms) "))
bmi = weight/((height/100)**2)
print("Your BMI is : ",bmi)
if (bmi <=18.5):
    print("Hey You are UnderWeight ! Eat Some Food ;)")
elif (bmi >=18.5 and bmi < 25):
    print("Hey You are Fit Stay the Same ;)")
elif (bmi  >= 25 and bmi < 30 ):
    print("Hey You are Overweight ! Try Eating Healthy ;)")
else:
    print("Obese ! Bro You are a Loser ;(")
