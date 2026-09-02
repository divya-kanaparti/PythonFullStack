#OOPS PROJECT
#UNIVERSITY MANAGEMENT SYSTEM
from abc import ABC,abstractmethod
class Person(ABC):
    def __init__(self,name,age):
        self._name=name
        self._age=age
    @abstractmethod
    def get_role(self):
        pass
    def get_info(self):
        return f"name: {self._name},age:{self._age}"
    def get_details(self):
        return f"{self.get_info()},role:{self.get_role()}"
#student class
class Student(Person):
    def __init__(self,name,age,sid,course):
        super().__init__(name,age)
        self._sid=sid
        self._course=course
    def get_role(self):
        return "Student"
    def get_student_info(self):
        return f"{self.get_details()},sid :{self._sid} and course:{self._course}"
#professor class
class Professor(Person):
    def __init__(self,name,age,pid,dept):
        super().__init__(name,age)
        self._pid=pid
        self._dept=dept
    def get_role(self):
        return "Professor"
    def get_profesor_info(self):
        return f"{self.get_details()},pid:{self._pid} and dept :{self._dept}"
#adminstaff class
class Adminstaff(Person):
    def __init__(self,name,age,aid,designation):
        super().__init__(name,age)
        self._aid=aid
        self._designation=designation
    def get_role(self):
        return "AdminStaff"
    def get_admin_info(self):
        return f"{self.get_details()},aid:{self._aid} and designation:{self._designation}"
#University class
class University:
    universityname='ABC University'
    def __init__(self):
        self.__people=[]
    #method to add people in university
    def add_people(self,person:Person):
        self.__people.append(person)
    #display people
    def display_people(self):
        if not self.__people:
            print("no one is registered")
        else:
            for p in self.__people:
                print(p.get_details())
    @classmethod
    def get_uniname(cls):
        return cls.universityname
    @staticmethod
    def Welcome():
        return"Welcome to University.."
print(University.Welcome())
print(University.get_uniname())
#create object
u=University()
while True:
    print("Main Menu:")
    print("press 1 for student registration")
    print("press 2 for professor registration")
    print("press 3 for adminstaff registration")
    print("press 4 for to see registered people")
    print("press 5 for exit")

    choice=input("Enter your choice:")
    if choice=='1':
        name=input("Enter student name:")
        age=int(input("Enter student age:"))
        sid=int(input("Enter student id:"))
        course=input("Enter student course:")
        s=Student(name,age,sid,course)
        u.add_people(s)
        print("Student registration succesful.")
    elif choice=='2':
        name=input("Enter professor name:")
        age=int(input("Enter professor age:"))
        pid=int(input("Enter professor id:"))
        dept=input("Enter professor dept:")
        p=Professor(name,age,pid,dept)
        u.add_people(p)
        print("Professor registration succesful.")
    elif choice=='3':
        name=input("Enter admin name:")
        age=int(input("Enter admin age:"))
        aid=int(input("Enter admin id:"))
        desg=input("Enter admin desg:")
        a=Adminstaff(name,age,aid,desg)
        u.add_people(a)
        print("Admin registration succesful.")
    elif choice=='4':
        u.display_people()
    elif choice=='5':
        print("Thank You for visitng..")
        break
    else:
        print("Invalid option,Try again")