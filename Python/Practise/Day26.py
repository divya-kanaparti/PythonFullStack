class Employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print("name is:",self.name)
class Manager(Employee):
    def __init__(self,name,dept):
        super().__init__(name)
        self.dept=dept
    def show(self):
        super().show()
        print("Dept name is:",self.dept)
m=Manager("raj","cse")
m.show()
#eg:2
#public modifier=>can be accessed anywhere in class.
class Student:
    def __init__(self):
        self.name="allen"
        self.age=23
        self.marks=87
    def display(self):
        print("my name is:",self.name)
s=Student()
s.display()
print(s.name)
#protected modifier=>accessed in class and sub class(_)
class Student:
    def __init__(self):
        self.name="allen"
        self.age=23
        self._marks=87
    def display(self):
        print("my name is:",self.name)
class Child(Student):
    def show(self):
        print("marks are:",self._marks)
c=Child()
c.display()
c.show()
#private acess modifier=>canot acess in child class and outside class
class Student:
    def __init__(self):
        self.name="kevin"
        self.age=23
        self._marks=87
        self.__color="white"
    def display(self):
        print("my name is:",self.name)
        print("color is:",self.__color)
class Child(Student):
    def show(self):
        print("marks are:",self._marks)
s=Student()
s.display()
c=Child()
c.display()
c.show()
# print(s.__color) # canot acess it return attribute error using mangling we solve
print(s._Student__color)
#eg:Bank example
#using getter and setter we acess encapsulated data
class Bank:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance #encapsulated
    def showBalance(self):
        print("your balance is:",self.__balance)
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            return f"amount {amount} is deposited"
        else:
            return f"Invalid amount {amount}"
    def withdraw(self,amount):
        if amount>0 and amount<=self.__balance:
            self.__balance-=amount
            return f"withdrawn amount is {amount}"
        else:
            return f"Insufficient balance"
b=Bank("smith",30000)
b.showBalance()
print(b.deposit(1000))
b.showBalance()
print(b.withdraw(1500))
b.showBalance()