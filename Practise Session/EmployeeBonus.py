salary=int(input())
rating=int(input())
experince=int(input())
attendance=int(input())
bonus=0
if rating==5:
    bonus+=salary*0.25 
elif rating==4:
    bonus+=salary*0.15
elif rating==3:
    bonus+=salary*0.10
if experince>10:
    bonus+=salary*0.10
elif experince >= 5:
    bonus+=salary*0.05
if attendance>=95:
    bonus+=5000
elif 85<=salary:
    bonus+=2000
print(bonus)
