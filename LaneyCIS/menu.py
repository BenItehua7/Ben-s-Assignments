
def menu_control():
    menu_control = int(input("Please input choice: "))
    if menu_control <= 5:
        print("Choice ", (menu_control),"selected")
    elif menu_control > 5:
        print("Invalid Choice")

menu_control()