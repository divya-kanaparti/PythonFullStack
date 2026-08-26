#INHERITANCE
#SIMPLE INHERITANCE
class Animal:
    def Sound(self):
        print("making sound")
class Dog(Animal):
    def Bark(self):
        print("barking")
d=Dog()
d.Sound
d.Bark()
#MULTIPLE INHERITANCE
class Father:
    def Dance(self):
        print("dancing")
class Mother:
    def Cook(self):
        print("cooking")
class Child(Father,Mother):
    def play(self):
        print("playing")
c=Child()
c.Dance()
c.Cook()
c.play()
print(Child.__mro__)
#MULTI-LEVEL INHERITANCE
class Employee:
    def Work(self):
        print("working")
class Devloper(Employee):
    def Devlop(self):
        print("writes the code")
class Intern(Devloper):
    def Learn(self):
        print("learning")
i=Intern()
i.Learn()
i.Devlop()
i.Work()
#HIERARICAL INHERITANCE
class Vehicle:
    def fuel_type(self):
        print("petrol or diesel")
class Car(Vehicle):
    def Drive(self):
        print("driving")
class Bike(Vehicle):
    def Ride(self):
        print("riding")
b=Bike()
b.fuel_type()
b.Ride()
#SUPER() METHOD
class Emp:
    def __init__(self,name):
        self.name=name
    def Show(self):
        print("employee name is:",self.name)
class Manager(Emp):
    def __init__(self,name,dept):
        super().__init__(name)
        self.dept=dept
    def Show(self):
        super().Show()
        print("Dept is:",self.dept)
m=Manager('divya','trainee')
m.Show()