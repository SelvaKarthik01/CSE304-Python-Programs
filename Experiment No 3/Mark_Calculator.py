def Input():
    n = int(input("Enter the Total No. of Subjects for the Student : "))
    global L
    L = []
    for i in range(n):
        print("Enter the Marks for Subject ",i+1," : ",end="")
        mark = float(input())
        L.append(mark)
    global total_marks
    total_marks = sum(L)
    print(L)

def mark_calc():
    avg_mark = total_marks/len(L)
    global grade
    grade = []
    global d
    d = {10:"S",9:"S",8:"A+",7:"A",6:"B",5:"C",4:"D",3:"E",2:"F",1:"F",0:"F"}
    for i in range(len(L)):
        grade.append(d[L[i]//10])
    print(grade)

def avg_calc():
    average_marks = total_marks /len(L)
    average_grade = d[average_marks//10]
    return average_marks,average_grade
        
