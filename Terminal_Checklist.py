'''
This file makes a terminal checklist.
You can add, remove, update, and read entries from the list.
An empty checkbox is prepended to every new entry.
You can then check or uncheck the entry's checkbox.
'''

checklist = []

print(checklist)

# Define Functions
def create(item):
    checklist.append(item)

def read(index):
    print(checklist[index])

def update(index, item):
    checklist[index]=item

def destroy(index):
    checklist.pop(index)

def mark_completed(index):
    checklist[index]="*"+checklist[index]

def list_all_items():
    for item in checklist:
        print(item) 

def select(function_code):
  
    if function_code == "C":
        input_item = input("Input item:")
        create(input_item)
        running = True 

        return running

    elif function_code== "R":
        input_item=input("what index element do you want to read:")
        read(int(input_item))

        running=True

        return running

    elif function_code=="U":
        input_index = input("what index do you want to call:")
        input_item = input("what item do you want to update in the index:")
        update (int(input_index),input_item)
        running = True

        return running

    elif function_code == "M":
        input_item = input ("what do you want to mark off:")
        mark_completed(int(input_item))
        running = True 

        return running 
    
    elif function_code =="D":

        input_index = input("what index do you want to remove?:")
        destroy(int(input_index))
        running = True

        return running

    elif function_code == "L":
        list_all_items()
        running =True

        return running 

    elif function_code == "Q":
        print("Thanks for using the checklist! Until next time!")
        running = False
    
        return running

running = True

while running:
    selection =input("Press C to add to the list, R to Read from the list, L to display the list, and Q to quit, M to mark completed,U to update, D to destroy:").upper()

    running = select(selection)
