base=10000
age=int(input("Enter age: "))
hscore=int(input("Enter score: "))
vehicle=input()
if age<25:
    base*=1.2
elif age>50:
    base*=1.15
if hscore>=80:
    base*=0.9
elif hscore<60:
    base*=1.2
if vehicle=="Sports":
    base*=1.3
elif vehicle=="suv":
    base*=1.15
print(round(base,2))