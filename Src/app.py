import sys
import os.path
# can also use from 'filename' import 'function'
from .table import print_table, print_header, print_separator, get_table_width
from Classes.drink_class import Drink
from Classes.person_class import Person
from Classes.descriptions import all_properties
from .Add_data_to_menu import add_people, add_drink, new_drink, new_name, output
from Databases.Database_connection import connect_db
from Databases.db_functions import people, drink
# args = sys.argv
# from csv import writer, reader
# Define dataz
# Expected commands - In capitals so others know not to change these variables

GET_PEOPLE_ARGS = "1"
GET_DRINKS_ARGS = "2"
ADD_PEOPLE = "3"
ADD_DRINKS = "4"
PLACE_ORDER = "5"
CHOOSE_FAVOURITE = "6"
SEE_FAVOURITES = "7"
DESCRIPTION = "8"
EXIT_ARG = "0"

# people = []
# drinks = []
Preferences = {}
# Max_len_list = 16
# """ """ used for multi-line strings instead of multiple print lines
WELCOME = """Welcome to BrewApp v0.1!
Please select an option from the list: 

[1] Get all people 
[2] Get all drinks 
[3] Add people
[4] Add drinks
[5] Show all drinks
[6] Select your favourite drink
[7] See Preferences
[8] Predefined drinks list descriptions
[0] Exit 
"""

# File paths

def welcome_screen():
    print(WELCOME)

def wait():
    input("Press any key to return to menu")

def show_drinks():
    for i, drink in enumerate(drinks, start=1):
        drinks.append(f'{i} {drink}')
    print_table('Drinks', drinks)

def print_train():
    print('''                                             (@@@)     (@@@@@)
                                       (@@)     (@@@@@@@)        (@@@@@@@)
                                 (@@@@@@@)   (@@@@@)       (@@@@@@@@@@@)
                            (@@@)     (@@@@@@@)   (@@@@@@)             (@@@)
                       (@@@@@@)    (@@@@@@)                (@)
                   (@@@)  (@@@@)           (@@)
                (@@)              (@@@)
               .-.               
               ] [    .-.      _    .-----.
        ."   """"   """""" """"| .--`
         (:--:--:--:--:--:--:--:-| [___    .------------------------.
    |C&O  :  :  :  :  :  : [_9_] |'='|.----------------------.|
        /|.___________________________|___|'--.___.--.___.--.___.-'| 
       / ||_.--.______.--.______.--._ |---\'--\-.-/==\-.-/==\-.-/-'/--
      /__;^=(==)======(==)======(==)=^~^^^ ^^^^(-)^^^^(-)^^^^(-)^^^ jgs
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')

def make_selection(message):
    return input(f'{message} \n')

def make_preference(message):
    return input(f'{message} \n')

def print_favourites():
    for name, pref_drink in Preferences.items():
        print(name+ "'s drink of choice is " + str(pref_drink) +".")

def unpack_Person():
    Person_list = [person.name for person in people]
    return Person_list

def unpack_Drink():
    Drink_list = [drinks.drink_name for drinks in drink]
    return Drink_list


# def add_people():
#     addition = True 
#     add_person = new_name("Please enter your name.")
#     if len(people) <=  Max_len_list:
#         people.append(add_person)
#         addition = True
#     while addition:
#         add_more = input('Would you like to add a new person? Please type "Yes" or "No" \n')
#         if add_more == "Yes":
#             addition = True
#         elif add_more == "No":
#             addition = False
#             break
#         if len(people) >= Max_len_list:
#             print("This app may only hold 16 names, please remove 1")
#             addition = False

# def add_drink():
#     if len(drinks) <= Max_len_list:
#         add_drink = new_drink("Please enter the drink you would like to add")
#         drinks.append(add_drink)
#     elif len(drinks) >= Max_len_list:
#         print("This app may only hold 16 drinks, please remove 1")

def choose_fave():
    # for index, item in enumerate(data, start=1):
    #     print(f'[{index}], {item}')
    name = make_preference("Please enter your name, followed by your preferred drink! \n")
    pref_drink = input()
    Preferences[name] = pref_drink

#load/save data
#Look at load_favourites


# def load_favourites():
#     csv_columns = ["Name", "Drink"]
#     Preferences
#     try:
#         with open("CSV_FILE", "w") as file:
#             csv_writer = csv.writerow(file, fieldnames=csv_columns)
#             csv_writer.writeheader()
#             for data in Preferences:
#                 csv_writer.writerow(data)
#     except TypeError:
#         print("There was a TypeError")


# def load_favourites():
#     csv_columns = ["Name", "Drink"]
#     try:
#     with open("CSV_FILE", "a+", newline = "") as f:
#         csv_writer = writer(f, fieldnames=csv_columns)
#         csv_writer.writeheader()
#         for data in pref:
#             csv_writer.writerow(data)
#   except TypeError:
#        print("There was a TypeError")


    # for item in Preferences(CSV_FILE):
    #     # Unpacking the items in the list to separate variables
    #     # https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/
    #     # I know items.split will return a list with two items, because of the second argument
    #     # it will only split once even if there are more instances of ':' in the string
    #     names, drinks = item.split(":", 1)
    #     if name in people and drink in drinks:
    #         Preferences[name] = drink
    #     else:
    #         print('Unexpected data returned when loading favourites.')
    #         print(f'Drink is known: {drink in drinks}')
    #         print(f'Name is known: {name in people}')

# def load_favourites():
#     try:
#         with open(CSV_FILE, "r") as f:
#             contents = f.read()
#             dictionary = ast.literal_eval(contents)
#         f.close()
#         print(Preferences)

    # try:
    #     with open(NAME_FILE, "r") as f:
    #         for name in f.readlines():
    #             people.append(name.strip())
    #     with open(DRINKS_FILE, "r") as f:
    #         for name in f.readlines():
    #             drinks.append(name.strip())
    #     load_favourites()
    # except FileNotFoundError:
    #     print("An error occured whilst finding this file. Please check that this file exists.")
    #     exit()
    # except Exception as e:
    #     print(f'Unable to load data from "{NAME_FILE}" with error: {str(e)}')


def data_save():
    with open(NAME_FILE, "w") as file:
        file.writelines([f'{name}\n' for name in people])
    with open(DRINKS_FILE, "w") as file:
        file.writelines([f'{drink}\n' for drink in drinks])
    # with open("CSV_FILE", "w") as f:
    #     w = f.writelines([f]))
    #     w.writeheader()
    #     w.writerow(CSV_FILE)

# def save_favourites():
#     favourites = []
#     for item


def start():
    data_load()

def exit1():
    data_save()
    print("Thankyou for using BrewApp")
    exit()

# Start of app
# start()
if __name__ == "__main__":
    while True:
        welcome_screen()
        selection = make_selection("Choose your selection:")
        
# Handle arguments
        if selection == GET_PEOPLE_ARGS:
            print_table('People', unpack_Person())
        elif selection == GET_DRINKS_ARGS:
            print_table('Drink', unpack_Drink())
        elif selection == ADD_PEOPLE:
            add_people()
            wait()
        elif selection == ADD_DRINKS:
            add_drink()
            wait()
        # elif selection == PLACE_ORDER:
        #     #Round function
        elif selection == CHOOSE_FAVOURITE:
            choose_fave()
            wait()
        elif selection == SEE_FAVOURITES:
            print_favourites()
            wait()
        elif selection == DESCRIPTION:
            all_properties()
            wait()
        elif selection == EXIT_ARG:
            data_save()
            exit1()

#testing merge