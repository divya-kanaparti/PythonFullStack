score=int(input())
income=int(input())
liability=int(input())
# if score>=750:
#     print("Elgible")
# elif 650<=score<=749:
#     print("Conditional Elgibilty")
# else:
#     print("Rejected")
# if income>=50000:
#     print("Elgible")
# if liability<=20000:
#     print("Elgible")
# if score and income and liability:
#     print("Approved")
# if score or income and liability:
#     print("Approved with conditions")
# else:
#     print("Rejected")
if score >= 750 and income >= 50000 and liability <= 20000:
    print("Approved")

elif 650 <= score <= 749 and income >= 50000 and liability <= 20000:
    print("Approved with Conditions")

else:
    print("Rejected")
