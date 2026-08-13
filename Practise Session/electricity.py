unit=int(input("Enter units:"))
age=input("Enter age:").lower()=="true"
if 0<unit<=100:
    bill=unit*1.5
elif 100<unit<=200:
    bill=unit*2.5
elif 200<unit<=500:
    bill=unit*4
elif 500<unit<=800:
    bill=unit*6
else:
    bill=unit*6*1.05
# bill=unit*rate
if age:
    bill=bill*0.9

print(bill)