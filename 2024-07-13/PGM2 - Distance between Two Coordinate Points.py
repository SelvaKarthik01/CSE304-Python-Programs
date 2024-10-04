# To Find the Distance between Two coordinates in a Graph
import math
x1 = int(input("Enter the x1 Coordinate : "))
x2 = int(input("Enter the x2 Coordinate : "))
y1 = int(input("Enter the y1 Coordinate : "))
y2 = int(input("Enter the y2 Coordinate : "))
distance = math.sqrt((x2-x1)**2 - (y2-y1)**2)
print("The Distance between the Two Coordinate Points are : ",distance)
