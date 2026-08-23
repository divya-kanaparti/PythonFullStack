#ATM TASK(PROJECT)
pin="1234"
balance=50000
attempts=0
maxattempt=3
trans=[]
while True:
    enterpin=input("Enter atm pin: ")
    if pin==enterpin:
        print("Pin verification successful.")
        break
    else:
        attempts+=1
        print("Invalid pin,remaining attempts are:",(maxattempt-attempts))
        if attempts>=maxattempt:
            print("Card is blocked...")
            exit()
print("Next you will see menu...")
#main functionalty
while True:
    print("----MENU----")
    print("press-1 for checking balance: ")
    print("press-2 for deposit: ")
    print("press-3 for withdrawl")
    print("press-4 for last 4 transactions: ")
    print("press-5 for exit: ")
    choice=input("enter your choice: ")
    if choice=="1":
        print("Your total balance is:",balance)
    elif choice=="2":
        amount=int(input("enter amount to deposit:"))
        if amount>0:
            balance=balance+amount
            trans.append(f"deposit amount is :{amount} ")
            if len(trans)>5:
                trans.pop(0)
            print("amount is deposited,current balance is:",balance)
        else:
            print("enter valid amount.")
    elif choice=="3":
        amount=int(input("Enter amount to withdraw: "))
        if amount>0 and amount<=balance:
            balance=balance-amount
            trans.append(f"withdrawn amount is: {amount}")
            if len(trans)>5:
                trans.pop(0)
            print("amount is withdrawn,current balance is:",balance)
        else:
            print("please enter valid amount or insufficient balance")
    elif choice=="4":
        if len(trans)!=0:
            for t in trans:
                print(t)
        else:
            print("No transactions")
    elif choice=="5":
        break
    else:
        print("invalid option,please give me valid option")
print("end of project...")