#Syntax Error-you get it before compile timr
# print("hello"
a=10
b=5
if a>5:
    print("hi")
#Logical Error-here you wont get the expected output
#Consider addition of two nums but here we are using product so it give logical error
a=10
b=20
print(a*b)
#Exception handling
a=10
b=0
print("Execution start")
print(a+b)
print(a-b)
print(a*b)
try:
    print(a/b)
except ZeroDivisionError as e:
    print("Dont divide by zero")
print("Execution stop")
#ValueError Exception
try:
    a=int("abc")
    print("hi")
except ValueError as e:
    print("Invalid input,enter valid integer")
print("Execution end")
#Using single try,multiple except blocks
try:
    a=int(input("Enter a:")) #10
    b=int(input("Enter b:")) #0
    result=a/b
    print("result:",result)
except ZeroDivisionError:
    print("dont divide by zero")
except ValueError:
    print("invalid input")
print("execution stop")
#try-except with else
try:
    a=int(input("Enter a:")) 
    b=int(input("Enter b:"))
    result=a/b
except ZeroDivisionError as e:
    print("dont divide by zero")
    print("exception message is:",e)
else:
    print("no exception in try block,due to that i am geting executed")
    print("result is",result)
#nestes try-except
try:
    a=int(input("Enter a:")) 
    try:
        result=a/2
        print("result :",result)
    except ZeroDivisionError:
        print("dont divide by zero")
except ValueError:
    print("invalid input")
#default except block
try:
    a=int(input("Enter a:")) 
    print("a is:",a)
except ZeroDivisionError:
    print("dont divide by zero")
except:
    print("no except block is matched.")
#finally block
try:
    a=int(input("Enter a:")) 
    print("a is:",a)
except ZeroDivisionError:
    print("dont divide by zero")
finally:
    print("Always executed")