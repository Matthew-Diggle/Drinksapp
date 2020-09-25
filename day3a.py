import sys
args = sys.argv

# Define data
# Expected commands - In capitals so others know not to change these variables
GET_PEOPLE_ARGS = "1"
GET_DRINKS_ARGS = "2"
ADD_PEOPLE = "3"
ADD_DRINKS = "4"
CHOOSE_FAVOURITE = "5"
SEE_FAVOURITES = "6"
NAME_FILE_DATA = "7"
EXIT_ARG = "8"

people = []
drinks = ['Tea', 'Mocha', 'Coffee', 'Americano']
Preferences = {}
New_names = []
Max_len_list = 8
# """ """ used for multi-line strings instead of multiple print lines
Menu = """Welcome to BrewApp v0.1!
Please select an option from the list: 

[1] Get all people 
[2] Get all drinks 
[3] Add people
[4] Add drinks
[5] Select your favourite drink
[6] See Preferences
[7] Upload name file data
[8] Exit 
"""

# define functions

def print_table(title, data):
    width = get_table_width(title, data)
    print_header(title, width)
    for item in data:
        print(f'| {item}')
    print_separator(width)
    wait()

def print_header(title, width):
    print_separator(width)
    print(f'| {title}')
    print_separator(width)

def print_separator(width):
    print(f"+{'=' * width}")

# Remember to define item "for item in data" or else "item" won't be defined
def get_table_width(title, data):
    longest = len(title)
    extra_spaces = 4
    for item in data:
        if longest < len(item):
            longest = len(item)
    return longest + extra_spaces

def print_menu():
    print(Menu)

def make_selection(message):
    return input(f'{message} \n')

def new_name(message):
    return input(f'{message} \n')

def new_drink(message):
    return input(f'{message} \n')

def make_preference(message):
    return input(f'{message} \n')

def print_name_drink():
    for name, pref_drink in Preferences.items():
        print(name+ "'s drink of choice is " + pref_drink +".")

def add_people():
    if len(people) <  Max_len_list:
        add_person = new_name("Please enter your name.")
        people.append(add_person)
    elif len(people) == Max_len_list:
        print("This app may only hold 8 names, please remove 1")

def add_drink():
    if len(drinks) < Max_len_list:
        add_drink = new_drink("Please enter the drink you would like to add")
        drinks.append(add_drink)
    elif len(drinks) == Max_len_list:
        print("This app may only hold 8 drinks, please remove 1")

def choose_fave():
    name = make_preference("Please enter your name, followed by your preferred drink! \n")
    pref_drink = input()
    Preferences[name] = pref_drink

def update_names_with_file():
    with open("Names.txt", "r") as f:
        for name in f.readlines():
            people.append(name.strip())
    print(people)
    

def wait():
    input("Press any key to return to menu")

#if user_input == GET_PEOPLE_ARGS or 1:
#    print_table('People', people)
#elif user_input == GET_DRINKS_ARGS or 2:
#    print_table('Drinks', drinks)
#else:
#    print(f'{user_input} is not a command that I recognise.')
# No longer need these arguments, edited to comments for reference to reflect when building up program in the future.

while True:
    print_menu()
    selection = make_selection("Choose your selection:")

    
    
# Handle arguments
    if selection == GET_PEOPLE_ARGS:
        print_table('People', people)
    elif selection == GET_DRINKS_ARGS:
        print_table('Drinks', drinks)
    elif selection == ADD_PEOPLE:
        add_people()
    elif selection == ADD_DRINKS:
        add_drink()
    elif selection == CHOOSE_FAVOURITE:
        choose_fave()
    elif selection == SEE_FAVOURITES:
        print_name_drink()
    elif selection == NAME_FILE_DATA:
        update_names_with_file()
    elif selection == EXIT_ARG:
        print("Thankyou for using BrewApp")
        exit()