User_Name_Input = (input("Enter your name "))
print ("Hello", User_Name_Input,("Welcome to your Bank Account"))

def balance():
    balance = float(input("Enter starting balance "))
    print ("Starting balance: ", balance)


def menu_control():
    menu_control == float(input("Do you want to deposit (1) or withdrawal (2)?: "))
    if menu_control == 1:
        print("Deposit selected")
        deposit()   
    elif menu_control == 2:
        print("Withdrawl selected")
        withdrawal()

def deposit():
        menu_control == 1
        float(input("How much do you want to deposit? "))
        print (balance = balance + deposit)

def withdrawal():
     menu_control == 2
     float(input("How much do you want to withdrawal? "))
     print (balance = balance - withdrawal)

def main():
    User_Name_Input()
    balance()
    menu_control()

main()