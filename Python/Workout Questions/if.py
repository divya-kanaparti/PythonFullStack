#1)program that checks if a number is positive.
a=int(input("Enter a:"))
if a>0:
    print("It is positive")

#2)Checks string is empty or not 
s=input()
if s=="":
    print("Empty")
else:
    print("Not Empty")

#3) if a number is positive, negative, or zero
b=int(input("Enter val:"))
if b>0:
    print("Positive")
if b<0:
    print("Negative")
if b==0:
    print("Zero")

#4)Check if a number is a multiple of both 3 and 5.
n=int(input("Enter n:"))
if n%3==0 and n%5==0:
    print("Is multiple of both 3 and 5.")

#5)given number is a perfect square.
c=int(input("Enter c:"))
if (c **0.5)**2==c:
    print("Perfect Square")
else:
    print("Not perfect square")

#6)number is divisible by both 2 and 3
d=int(input("Enter d:"))
if d%2==0 and d%3==0:
    print("Divisible")

#7)given number is a perfect cube
m=int(input("Enter m:"))
if int (m **(1/3))**3==m:
    print("Perfect Cube")
else:
    print("Not perfect Cube")

#8) number is a multiple of 4.
z=int(input("Enter value:"))
if z%4==0:
    print("Multiple of 4")
