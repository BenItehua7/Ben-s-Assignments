name = input ("Please Enter Your Name: ") 
age = int(input("How old are you?: "))

if 0 <= age <= 100:
    print (name + " will be " , age + 5 , "in Five years")
elif age <=0:
    print("People cannot have a negative age")
elif age >= 100:
    print("100 is the maximum age")
    