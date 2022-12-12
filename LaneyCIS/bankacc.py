def deposit(deposit_amount):
    global balance
    balance = balance + deposit_amount
    
    if deposit_amount > 0:
        balance + deposit_amount
    else:
        print("invalid input")

def withdrawal(withdrawal_amount):
    global balance 
    if balance>withdrawal_amount:
        balance =balance - withdrawal_amount
    else:
        print("invalid input ")

def main():
    global balance
    try:
        User_Name_Input= str(input("Enter Name: "))
    except:
        print("invalid input")
    print ("Hello", User_Name_Input, " Welcome to your Bank account")
    try:
        balance = float(input("Enter starting balance: "))
        print ("Starting balance: ", balance)
    except:
        print("invalid input")
    try:
        menu_control = int(input("Do you want to Deposit (1) or withdrawal (2): "))
    except:
        print("invalid input")
    if menu_control == 1:
        deposit = float(input("Enter amount you want to deposit: "))
        if deposit > 0:
            balance = balance + deposit
            print("New balance = ", balance)
        else:
         print("Invalid choice")
        print("Choice 1 (Deposit) entered")
    elif menu_control == 2:
        print ("Choice 2 (Withdrawal) entered")
        withdrawal = float(input("Enter amount you want to withdrawal: "))
        if balance >= withdrawal:
         balance = balance- withdrawal
         print("You Withdrew: ", balance)
        else:  
          print("Invalid withdrawal")
        print(User_Name_Input + "'s New Balance = ", balance)
    else:
        print("Invalid choice")
main()