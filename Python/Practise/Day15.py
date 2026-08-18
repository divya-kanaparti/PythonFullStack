#Functions
#how to create function
def Greet():
    print("Welcome")
Greet()
#2)Addition
def Add(a,b):
    print(a+b)
Add(10,20)
Add(23,40)
#3)Positional argument
#order is maintained
def welcome(name,age):
    print(f'my name is {name} and age is {age}')
welcome('raj',23)
welcome(23,'raj')
#Types:
#i)calling function with args and retutn type
#Additon
def Addition(a,b):
    c=a+b
    return c
    print("end")#unreachable code
r=Addition(10,20)
print(r)
#Addition(10)#type error
#ii)calling function with args,without retutn type
def welcome(name,age):
    print(f'my name is {name} and age is {age}')
welcome('raj',23)
welcome(23,'raj')
#iii)calling function without args,with retutn type
def greet():
    return "welcome"
res=greet()
print(r)
#iv)calling function without args,without retutn type
#we use print function
#keyword arguments here order is not required
#eg:User details collections
def welcome(name,age):
    print(f'my name is {name} and age is {age}')
welcome(name='raj',age=23)
#Default parameter value
def Country(country='India'):
    print("my country is",country)
Country('usa')
Country()
#Arbitary arguments(*)
def BillCal(*l):
    print(l)
    print(sum(l))
#stored in form of tuple
BillCal(10,20,30,40)
#Keyword arbitary arguments(**)
def info(**details):
    print(details)
info(name='Raj',age=23,height=5.7)