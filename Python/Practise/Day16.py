#Scope
def Student():
    name='Raj'#local
    print(name)
Student()#after execution the data is removed from memory
#print(name)#no output as it is local variable it gives name error
#Global
company='Codegnan'
def display():
    print(company)
display()
print(company)
#eg:
num=10
def Update():
    num=100 #local is preferd first
    print("Inside function",num)
Update()
print("Outside function",num)
#To modify global variable in local we use global keyword
num=10
def Update():
    global num
    num=100 #local is preferd first
    print("Inside function",num)
Update()
print("Outside function",num)
#Non local scope used in nested function
def outer():
    def inner():
        print('inner')
    inner()
    print('outer')
outer()
print('end')
#eg:TYPES OF SCOPE
print("GLOBAL SCOPE")
def outer():
    print('ENCLOSING SCOPE')
    def inner():
        print('LOCAL SCOPE')
    inner()
    print('outer')
outer()
print('end')
#eg:
a=10
def Outer():
    a=50
    def Inner():
        nonlocal a #to change enclosing value we use nonlocal
        a=100
        print(a)
    Inner()
Outer()
#CallByValue
def update(number):
    number=200

number=100
print("Befor calling function",number) #100
update(number)
print("After calling function",number) #100
#CallByReference
def Cart(cart):
    cart.append('mango')
cart=['apple','jam','orange']
print("Before calling function",cart)
Cart(cart)
print("after calling function",cart)
#Lambda Function
#1)Square of number
square=lambda x:x*x
print(square(10))
#2)Addition of 2 nos
add=lambda a,b:a+b
print(add(10,20))
#3)Lambda with if-else
maxi=lambda a,b:a if a>b else b
print(maxi(10,20))

#MAP
l=[10,20,30,40]
r=list(map(lambda x:x+5,l))
print(r)
#FILTER
l1=[1,2,3,4]
res=list(filter(lambda x:x%2==0,l))
print(res)
#REDUCE
from functools import reduce
l2=[1,2,3,4]
r1=reduce(lambda x,y:x+y,l2)
print(r1)

#Sorting
l4=[('raj',23),("Blake",45),('Allen',89)]
r2=sorted(l4,key=lambda x:x[1],reverse=True) #Descending order
print(r2)

