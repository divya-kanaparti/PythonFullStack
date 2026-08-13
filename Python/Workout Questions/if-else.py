#1)Check whether the number is positive or not
num=int(input("Enter number:"))
if num>0:
    print("Positive number")
else:
    print("Negative number")

#2)Check whether the number is even or odd
n=int(input("Enter number:"))
if n%2==0:
    print("Even")
else:
    print("Odd")

#3)Elgible to Vote or not
age=int(input("Enter age:"))
if age>=18:
    print("You are elgible to vote.")
else:
    print("Not elgible")

#4)Based on marks is it fail or pass
marks=int(input("Enter marks:"))
if marks>=35:
    print("Pass")
else:
    print("Fail")

#5)Greatest of two numbers
a=int(input("Enter a:"))
b=int(input("Enter b:"))
if(a>b):
    print("A is largest")
else:
    print("B is largest")

#6)Given number is multiple of 5 or not
c=int(input("Enter value:"))
if c%5==0:
    print(c ,"is multiple of 5")
else:
    print("Not multiple")

#7)Given number is divisible by 3 and 5.
d=int(input("Enter value:"))
if d%3==0 and d%5==0:
    print(d,"is divisible")
else:
    print("not divisible")

#8)Check is it vowel or consonant
ch=input()
if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")

#9)printing statement
name=input("Enter name:")
print("Welcome,",name,"!")

#10)print zero or not
e=int(input("Enter number:"))
if e>0:
    print("Non-Zero")
else:
    print("Zero")
#-------------------------------------------------------------------------------------------#
#1)given year is a leap year.
year=int(input("Enter year:"))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
#2)Check given number is prime or not
a=int(input("Enter num:"))
if a%1==0 or a%a==0:
    print("Prime number")
else:
    print("Not Prime")
#3)Smallest of three numbers:
n1=int(input("Enter n1:"))
n2=int(input("Enter n2:"))
n3=int(input("Enter n3:"))
if n1<n2 and n1<n3:
    print("n1 is smallest")
elif n2<n3:
    print("n2 is smallest")
else:
    print("n3 is smallest")
#4)check if string is palindrome
str=input()
rev=''
for i in range(len(str)-1,-1,-1):
    rev+=str[i]
if(str==rev):
    print("Palindrome")
else:
    print("not palindrome")
#5)print the absolute value of a number
n=int(input())
print(abs(n))

#6)Sign of the Difference of Two Numbers
num1=int(input("Enter num:"))
num2=int(input("Enter num:"))
if num1-num2>0:
    print("Positive")
else:
    print("Negative")
