#1)Print numbers from 1 to 5 using a for loop
n=int(input("Enter num:"))
for i in range(1,n+1):
    print(i)
#2) Print even numbers between 1 and 10
n1=int(input("Enter num:"))
for i in range(2,n1+1,2):
    print(i,end=" ")
    print()
#3) multiplication table of a number
n2=int(input("Enter num:"))
for i in range(1,n2+1):
    print(n2,"*" ,i ,"=",n2*i)
#4)Print all characters of a string
str=input("Enter string:")
for i in range(0,len(str)):
    print(str[i])
#5)sum of digits of a number
num=int(input("Enter num:"))
sum=0
while num>0:
    r=num%10
    sum=sum+r
    num=num//10
print(sum)

#6)Reverse a number using a while loop
n3=int(input("Enter num:"))
rev=0
while n3>0:
    r=n3%10
    rev=rev*10+r
    n3=n3//10
print(rev)
#7)factorial of num
n=int(input("Enter fact:"))
fact=1
while n>0:
    fact=fact*n
    n=n-1
print(fact)
#8)squares of numbers from 1 to n
n4=int(input("Enter num:"))
for i in range(1,n4+1):
    print(i*i)