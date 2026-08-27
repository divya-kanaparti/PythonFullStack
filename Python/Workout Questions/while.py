i=1
while i<=10:
    print(i)
    i+=1
#eg:2=CountDown
n=int(input("Enter no:"))
while n>=1:
    print(n)
    n-=1
#eg:3=sum of even nos
sum = 0
counter = 2 
while counter <= 100:
    sum += counter  
    counter += 2  
print("Sum of even numbers:",sum) 
#eg:4
import random
number = random.randint(1, 100)
guess = 0
print("Guess the number between 1 and 100!")
while guess != number:
    guess = int(input("Enter your guess: "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct,You guessed the number!")
#eg:5=factorial
fact=int(input())
i=1
factorial=1
while i<=fact:
    factorial=factorial*i
    i+=1
print(factorial) 
#eg:6
counter = 2 
while counter <= 50:
    print(counter) 
    counter += 2  
#eg:7=sum of digits
n=int(input("Enter num:"))
sum=0
while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10
print(sum)
#eg:8 multiplication table
i=1
n=int(input())
while i<=10:
    print(f"{n} X {i} = {n * i}")
    i+=1
#eg:9 factors
b=int(input("Enter no:"))
i=1
while i<=b:
    if b%i==0:
        print(i)
    i+=1
#eg:10=reverse even number
c=int(input("Enter no:"))
rev=0
while c>0:
    digit=c%10
    rev=(rev*10)+digit
    c=c//10
print(rev)
#eg:11=Password validation
pwd=1234
pass=input()
while pass!=pwd:
    print("Enter password:")
print("Granted")