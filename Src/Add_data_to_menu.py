import pymysql
import collections

from Classes.person_class import Person
from Classes.drink_class import Drink
from Databases.db_functions import add_new_drink_to_db, add_new_person_to_db, people, drink
Preferences = {}
Max_len_list = 16



def new_name(message):
    return input(f'{message} \n')

def new_drink(message):
    return input(f'{message} \n')

def add_people():
    # addition = True 
    add_person = new_name("Please enter your name.")
    if len(people) <=  Max_len_list:
        people.append(Person(add_person))
    add_new_person_to_db()
    confirmation_input = input("Would you like to add a new person? Please type 'Yes' or 'No' \n")
    output(confirmation_input)

def output(confirmation_input):
    if confirmation_input == "Yes":
        add_people()
    else:
        confirmation_input
        

def add_drink():
    if len(drink) <= Max_len_list:
        add_drink = new_drink("Please enter the drink you would like to add")
        choose_temp = new_drink("Do you have a temperature preference? If left blank, your drink will be served at our default temperature")
        add_blend = new_drink("Please enter a blend if required")
        drink.append(Drink(add_drink, choose_temp, add_blend))
        add_new_drink_to_db()
    elif len(drink) >= Max_len_list:
        print("This app may only hold 16 drinks, please remove 1")

# def make_preference(message):
#     return input(f'{message} \n')

# def choose_fave():
#     boohoo_com("Person", unpack_Person)
#     name = make_preference("Please enter your name, followed by your preferred drink! \n")
#     pref_drink = input()
#     Preferences[name] = pref_drink
#     global od
#     od = collections.OrderedDict(Preferences.items())
#     global key_list, value_list
#     key_list = []
#     value_list = []
#     for key, value in od.items():
#         key_list.append(key)
#         value_list.append(value)
#     add_preferences_to_db()

# def choose_fave():
#     show_people()
#     name = make_preference("Please enter your name, followed by your preferred drink! If your name is not in the list above, please return to the main menu to add your name.\n")
#     pref_drink = input()
#     Preferences[name] = pref_drink
#     global od
#     od = collections.OrderedDict(Preferences.items())
#     global key_list, value_list
#     key_list = []
#     value_list = []
#     for key, value in od.items():
#         key_list.append(key)
#         value_list.append(value)
#     add_preferences_to_db()

# def add_preferences_to_db():
#     connection = pymysql.connect(
# 		host="localhost",
#     	port=33066,
# 		user="root",
# 		passwd="password",
# 		database="Drink_app"
# 	)
#     cursor = connection.cursor()
#     for i in key_list:
#         for x in value_list:
#             if i == key_list[-1] and x == value_list[-1]:
#                 cursor.execute(f'INSERT INTO Preferences (Name, Drink) VALUES ("{i}", "{x}")')
#                 connection.commit()
#                 # cursor.execute(f'INSERT INTO Person (Name) VALUE ("{i}") WHERE "{i}" not in (Name))')
#                 # connection.commit()
#     # for i in value_list:        
#     #     if i == value_list[-1]:
#     #         cursor.execute(f'UPDATE Preferences (Drink) VALUES ("{i}") WHERE (Name) ')
#     #         connection.commit()
#     cursor.close()
#     connection.close()