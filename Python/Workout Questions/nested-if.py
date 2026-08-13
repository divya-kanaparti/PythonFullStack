#1)Write a Python program to check whether a given number is a multiple of 5.If the number is a 
#multiple of 5, then check whether it is also even or odd and print the appropriate message using 
#nested if.
a=int(input("Enter num:"))
if a%5==0:
    if a%2==0:
        print(a,"is multiple of 5 and even")
    else:
        print(a,"is multiple of 5 and Odd")
else:
    print(a,"is not multiple of 5")
    
#2)Write a Python program to check whether a number is a multiple of 5 or not. If it is not a
# multiple of 5, check whether the number is positive or negative and print the result using nested 
#if-else.
b=int(input("Enter num:"))
if b%5!=0:
    if b>0:
        print(b,"is not a multiple of 5 and it is positive.")
    else:
        print(b,"is not a  multiple of 5 and it is negative.")
else:
    print(b,"is a multiple of 5")
    