from Classes.person_class import Person
from Classes.drink_class import Drink
from Databases.db_functions import people, drink
Max_len_list = 16



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
        people.append(Person(add_person))
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
    if len(drink) <= Max_len_list:
        add_drink = new_drink("Please enter the drink you would like to add")
        choose_temp = new_drink("Do you have a temperature preference? If left blank, your drink will be served at a regular temperature")
        add_blend = new_drink("Please enter a blend if required")
        drink.append(Drink(add_drink, choose_temp, add_blend))
    elif len(drink) >= Max_len_list:
        print("This app may only hold 16 drinks, please remove 1")