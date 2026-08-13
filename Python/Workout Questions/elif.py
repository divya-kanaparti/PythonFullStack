#1)Greatest of three numbers
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
if a>b and a>c:
    print("A is largest")
elif b>c:
    print("B is largest")
else:
    print("C is largest")

#2)check whether it is a three digit number or not
n=int(input("Enter n:"))
if 100<=n<=999:
    print("Three digit number")
else:
    print("Not a three digit number")

#3)temeprature
temp=int(input("Enter temp:"))
if temp>30:
    print("Hot")
elif 15<temp<30:
    print("Pleasant")
else:
    print("Cold")

#4)Check number is positive,negative,zero
num=int(input("Enter num:"))
if num>0:
    print("Positive")
elif num==0:
    print("Zero")
else:
    print("Negative")

#5)User marks
marks=int(input("Enter marks:"))
if marks>=90:
    print("A")
elif 80<=marks<90:
    print("B")
elif 70<=marks<79:
    print("C")
elif 60<=marks<69:
    print("D")
else:
    print("F")

#6)Type of polygon
n=int(input("Enter value:"))
if n==3:
    print("Triangle")
elif n==4:
    print("Quadrilatertal")
elif n==5:
    print("Pentagon")
else:
    print("Unknown shape")

#7)Bus Fare
age=int(input("Enter age:"))
if age <5:
    print("Free")
elif 5<age<18:
    print("Half Ticket")
else:
    print("Full Ticket")

#8)Student Grade Calci
mark1=int(input("Enter value:"))
mark2=int(input("Enter value:"))
mark3=int(input("Enter value:"))
avg=(mark1+mark2+mark3)/3
if avg>90:
    print("Excellent")
elif 70<avg<90:
    print("Good")
else:
    print("Need improvement")