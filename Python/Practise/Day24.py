#METHOD OVERLOADING
class Test:
    def Add(self,a,b):
        print(f"the sum of {a} and {b} is: {a+b}")
    def Add(self,a,b,c):
        print(f"the sum of {a} ,{b} and {c} is: {a+b+c}")
t=Test()
# t.Add(10,20) #Type error as overrided by the next method
t.Add(10,20,30)
#eg:2
class Greet:
    def Hello(self,name=None):
        if name:
            print("hello",name)
        else:
            print("hello")
g=Greet()
g.Hello()
g.Hello("Allen")
#Using arbitary we acheive method overloading
class Demo:
    def Add(self,*l): #stores data in tuple
        sum=0
        for i in l:
            sum=sum+i
        print("sum is",sum)
d=Demo()
d.Add(10,20)
#CONSTRUCTOR OVERLOADING
class Sample:
    def __init__(self):
        print("No argument")
    def __init__(self,a):
        print("one arg constructor")
# t=Test() #Type error
t=Sample(10)
#METHOD OVERRIDING
class A:
    def M1(self):
        print("m1 method")
class B(A):
    def M1(self):
        print("second method")
b=B()
b.M1()
#eg:2
#same method in diff class i.e method overriding
class Shop:
    def Calculatebill(self,a,b=0):
        total=a+b
        print(f"total bill :{total}")
class Customer(Shop):
    def Calculatebill(self,a,b=0):
        total=a+b
        discount=total*0.1
        totalamt=total-discount
        print("total amount",totalamt)

s=Customer
s.Calculatebill(100,300)
#OPERATOR OVERLOADING
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __str__(self):
        return str(self.pages)
    def __add__(self,other):
        return Book(self.pages+other.pages)
b1=Book(100)
b2=Book(200)
print(b1+b2) #type error thats y we use magic methods like add
print(b1) #obj adress