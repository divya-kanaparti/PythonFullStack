#DATA ABSTRACTION
from abc import abstractmethod,ABC
class Fruits:
    #valid abstract method
    @abstractmethod
    def Taste(self):
        pass
t=Fruits()
t.Taste()
#eg:2
#canot create object for abstract class as it is unimplemented
class fruit(ABC):
    @abstractmethod
    def taste(self):
        pass
    def M1(self):
        print("i am m1()")
# f=fruit()
# f.m1()
#eg:3
class fruit(ABC):
    @abstractmethod
    def taste(self):
        pass
    def M1(self):
        print("i am m1()")
class child(fruit):
    def taste(self):
        print("super")
c=child()
c.taste()
c.M1()

#eg:4
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
class Bike(Vehicle):
    def start_engine(self):
        print("starts with kick")
    def stop_engine(self):
        print("off the key")
b=Bike()
b.start_engine()
b.stop_engine()
#eg:5 BANK
class BANK(ABC):
    @abstractmethod
    def loan(self):
        pass
    def message(self):
        print("hello")
class SBI(BANK):
    def loan(self):
        print("SBI loan is 5%")
class HDFC(BANK):
    def loan(self):
        print("HDFC loan is 15%")
h=HDFC()
h.loan()
s=SBI()
s.loan()