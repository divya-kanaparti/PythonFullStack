base=5000
amt=base
seat=input("Enter type of seat: ")
day=int(input("Enter no of days: "))
festival=input().lower()=='true'
age=int(input("Enter age: "))
if festival:
    amt+=amt*0.2
if seat=="Business":
    amt+=amt*0.4
    # amt*=1.4
elif seat=="Premium Economy":
    amt+=amt*0.2
    # amt*=1.2
else:
    pass
if day>30:
    amt-=amt*0.1
    # amt*=0.9
elif day<7:
    amt+=amt*0.25
    # amt*=1.25
if age>60:
    amt-=amt*0.15
print(amt)


