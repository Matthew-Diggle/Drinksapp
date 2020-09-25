people = []
drinks = []
Max_len_list = 16

def new_name(message):
    return input(f'{message} \n')

def new_drink(message):
    return input(f'{message} \n')

def add_people():
    addition = True 
    add_person = new_name("Please enter your name.")
    if len(people) <=  Max_len_list:
        people.append(add_person)
        addition = True
    while addition:
        add_more = input('Would you like to add a new person? Please type "Yes" or "No" \n')
        if add_more == "Yes":
            addition = True
        elif add_more == "No":
            addition = False
            break
        if len(people) >= Max_len_list:
            print("This app may only hold 16 names, please remove 1")
            addition = False

def add_drink():
    if len(drinks) <= Max_len_list:
        add_drink = new_drink("Please enter the drink you would like to add")
        drinks.append(add_drink)
    elif len(drinks) >= Max_len_list:
        print("This app may only hold 16 drinks, please remove 1")