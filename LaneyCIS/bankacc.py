User_Name_Input = (input("Enter your name "))
print ("Hello", User_Name_Input,("Welcome to your Bank Account"))

balance = float(input("Enter starting balance: "))
print ("Starting balance: ", balance)
menu_control = int(input("Do you want to Deposit (1) or withdrawal (2): "))

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
    print(User_Name_Input + "New Balance = ", balance)
else:
    print("Invalid choice")
