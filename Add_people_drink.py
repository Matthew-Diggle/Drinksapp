people = []
drinks = []
Max_len_list = 16
WELCOME = """Welcome to BrewApp v0.1!
Please select an option from the list: 

[1] Get all people 
[2] Get all drinks 
[3] Add people
[4] Add drinks
[5] Show all drinks
[6] Select your favourite gitdrink
[7] See Preferences
[8] Predefined drinks list descriptions
[0] Exit 
"""

def welcome_screen():
    print(WELCOME)

def new_name(message):
    return input(f'{message} \n')

def new_drink(message):
    return input(f'{message} \n')

def add_people():
    # addition = True 
    add_person = new_name("Please enter your name.")
    confirmation_input = input("Would you like to add a new person? Please type 'Yes' or 'No' \n")
    output(confirmation_input)
    if len(people) <=  Max_len_list:
        people.append(add_person)
    #     addition = True
    # while addition:
    #     add_more = input('Would you like to add a new person? Please type "Yes" or "No" \n')
    #     if add_more == "Yes":
    #         addition = True
    #     elif add_more == "No":
    #         addition = False
    #         break
    #     if len(people) >= Max_len_list:
    #         print("This app may only hold 16 names, please remove 1")
    #         addition = False

def output(confirmation_input):
    if confirmation_input == "Yes":
        add_people()
    else:
        confirmation_input 

def add_drink():
    if len(drinks) <= Max_len_list:
        add_drink = new_drink("Please enter the drink you would like to add")
        drinks.append(add_drink)
    elif len(drinks) >= Max_len_list:
        print("This app may only hold 16 drinks, please remove 1")