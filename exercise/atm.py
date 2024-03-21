print("==========Welcome to ATM==========")
pin_code=1234
amount=10000
pin=int(input("Enter your pin code: "))
if pin==pin_code:
    print("1. Check Balance")
    print("2. Withdraw Money")
    option=int(input("Enter your option: "))
    if option==1:
        print("Your balance is: ",amount)
    elif option==2:
        new_amount=int(input("Enter the amount: "))
        if new_amount<=amount:
            n=amount-new_amount
            print("Please collect your cash")
            print("withdrawn amount: ",new_amount)
            print("Your new balance is: ",n)
        else:
            print("Insufficient balance")
    else:
        print("Invalid option")
else:
    print("Invalid pin code")
 