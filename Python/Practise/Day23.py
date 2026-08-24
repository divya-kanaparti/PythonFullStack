class Student:
    collegename="Codegnan"
    def __init__(self):
        self.name='raju'
        self.age=24
        self.marks=75
    #INSTANCE METHOD
    def Talk(self):
        print("my name is:",self.name)
        print("my age is:",self.age)
        print("my marks are:",self.marks)
    #CLASS METHOD
    @classmethod
    def Show(cls):
        print("my college name is:",cls.collegename)
        print("my college name is:",Student.collegename)
    @staticmethod
    def Display():
        print("I am static method,also helper function")
s=Student()
s.Talk() #we call instance by reference variable
Student.Show()
Student.Display() #prefered by class method to call 
s.Display()

#Can you modify class variable inside the constructor
class Student:
    collegename="Codegnan"
    def __init__(self):
        self.name='raju'
        self.age=24
        self.marks=75
        print("college name is:",Student.collegename)
        Student.collegename="KMIT"
        self.collegename="KMIT" #it refers object so dont chnage the variable
        print("college name is:",Student.collegename)
s=Student()

#Can you access class variable inside instance method
class Student:
    collegename="Codegnan"
    def __init__(self):
        self.name='raju'
        self.age=24
        self.marks=75
    #INSTANCE METHOD
    def Talk(self):
        print("my name is:",self.name)
        print("my age is:",self.age)
        print("my marks are:",self.marks)
        print("college name is:",self.collegename)
        self.collegename="KMIT"
        print("after chnage college name:",self.collegename)
    #CLASS METHOD
    @classmethod
    def Show(cls):
        print("my college name is:",cls.collegename)
        print("my college name is:",Student.collegename)
        cls.collegename="XYZ" #can change the variable
    @staticmethod
    def Display():
        print("I am static method,also helper function")
s=Student()
s.Talk() 
class Test:
    def __init__(self):
        print("Hello")
t=Test()
t.__init__()
#NO PARAMETERIZED CONSTRUCTOR
class Employee:
    def __init__(self):
        self.name='ria'
        self.id='123'
        self.salary=50000
        print("my name is",self.name)
e=Employee()
#PARAMETERIZED CONSTRUCTOR
class Emp:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def display(self):
        print("my name is:",self.name)
        print("my id is:",self.id)
        print("my salary is",self.salary)
e1=Emp('raj','233',45000)
e1.display()
e2=Emp('hari','539',34000)
e2.display()
