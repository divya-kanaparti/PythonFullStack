class Student:
    def __init__(self):
        print("I am constuctor")
        print("adress of self: ",id(self))
#obj creation
s1=Student()
print("adress of s1:",id(s1))
s2=Student()
print("adress of s2:",id(s2))

#eg:2
class Student:
    def __init__(self):
        self.name='raj'
        self.age=23
        print("my name is ",self.name)
        print("my age is ",self.age)
#obj creation
s1=Student()
print("my name outside class is:",s1.name)
print("my age is: ",s1.age)
#eg:3
class Student:
    colegename="Codegnan"
    def __init__(self):
        self.name='raj'
        self.age=23
        print("my name is ",self.name)
        print("my age is ",self.age)
        print("my college name is ",Student.colegename)
#obj creation
s1=Student()
print("my name outside class is:",s1.name)
print("my age is: ",s1.age)
print(s1.colegename)
#eg:4
#local variable
class Test:
    #instance method
    def Show(self):
        x=100 #local variable
        print("Value is: ",x)
t=Test()
t.Show()