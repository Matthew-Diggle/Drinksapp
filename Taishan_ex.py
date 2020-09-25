#import os 
import os
os.system("clear")
# Define lists
def load_people(filepath):     # returns a list of names from a text file
    people = []
    with open(filepath, "r") as persons:
        [people.append(line.strip()) for line in persons.readlines() if not line.isspace()]  # removes new line indicator and spaces
    return people
def load_drinks(filepath):     # return a list of drinks from a text file
    drinks = []
    with open(filepath, "r") as all_drinks:
        [drinks.append(line.strip()) for line in all_drinks.readlines() if not line.isspace()]  # removes new line indicator and spaces
    return drinks
# Create borders for lists
def table_width(header, data):
    biggest = len(header)
    for item in data:
        if len(item) > biggest:
            biggest = len(item)
    return biggest + 2
def table(header, data):
    separator = '+' + '='*table_width(header, data) + '+'
    print('\n' + separator)
    print(f'| {header}' + ' '*(table_width(header, data)-len(header)-1) + '|')
    print(separator)
    for item in data:            
        print('|' + ' ' + item + ' '*(table_width(header, data)-len(item)-1) + '|')
    print(separator)
# Add to the lists
def add_to_table(header, data):
    add_more = True
    add_table = True
    while add_table:
        # checks for people or drinks
        if data == drinks:
            item = 'drink'
        else:
            item = 'person'
        # ask user for data input 
        new_data = input(f"\nPlease add a new {item} to the list: ").title()
        # append input to the data list
        data.append(new_data)
        # ask user again whether they want to input more
        while add_more:
            choice = input(f"Do you want to add more {header.lower()}, Y or N?: ")
            if choice[0] == 'N' or choice[0] == 'n':
                print("\nThank you!")
                add_more = False
                add_table = False
            elif choice[0] == 'Y' or choice[0] == 'y':
                add_more = False
                add_table = True
            else:
                print("\nSorry, I dont understand!")
        add_more = True
# Save the new additions to the lists
def save_data(filepath, data):
    try:
        with open(filepath, 'w') as data_file:
            [data_file.write(item + '\n') for item in data]
    except:
        print('Failure opening file!') 
# Assign preferences to people       
def assign_fave_drink(people, drinks): 
    chosen_name = True
    chosen_drink = True
    selected_name = []   # list to check no multiple assignments occur 
    drinks_dictionary = {}
    a = 1
    # input to choose name from list
    while a <= len(people):
        while chosen_name:
            table('PEOPLE', people)
            name = input("\nChoose a person from the list: ").title()
            if name not in people:
                print(f"\n{name} isn't on the list, try again.")
            elif name in selected_name:
                print("\nThat person has already been selected, try again.")
            else:
                chosen_name = False
        # select that names favourite drink
        while chosen_drink:
            table('DRINKS', drinks)
            drink = input(f"\nWhat is {name}'s favourite drink?: ").title()
            if drink not in drinks:
                print(f"\n{drink} isn't on the menu, try again.")
            else:
                chosen_drink = False
        a+=1
        chosen_name = True
        chosen_drink = True
        drinks_dictionary[f'{name}'] = f'{drink}'
        selected_name.append(name)
    return drinks_dictionary
# Generate a list of preferences 
def person_and_drink(header, data):    # Generating a list of preferences                       
    print(f"\n{header}\n")
    [print(f"{name}'s favourite drink: {data[name]}") for name in data.keys()]
# Create the menu with user input
def menu():
    print("""
    Welcome to my wonderful factory of assorted beverages.
    Please ensure that you abide by social distancing measures
    when in the venue!
    Please select an option: 
    1. View all people
    2. View all drinks
    3. Add people
    4. Add drinks
    5. Favourite drinks selection
    6. Preferences 
""")
def view_another_page():    # The user decides if they wish to view the menu, FIX ERROR!
    while True:
        choice = input("\nWould you like to view the menu again, Y or N?: ")
        if choice[0] == 'y':
            return choice  # returns True for the app logic
        if choice[0] == 'n':
            return False   # for the app logic
        else:
            print("\nI dont understand.") 
# APP LOGIC 
while True:
    view_menu = True
    menu()            # show the menu
    people = load_people('names.txt')
    drinks = load_drinks('drinks.txt')
    while view_menu:          # Loop for decision making, accounting for mistakes
        try:    
            option = int(input("\nChoose your selection here (1-6): "))  # user picks their desired page
            if option == 1:
                table('PEOPLE', people)  
                view_menu = False
            elif option == 2:
                table('DRINKS', drinks) 
                view_menu = False
            elif option == 3:
                add_to_table('PEOPLE',people)
                table('PEOPLE',people)
                save_data('names.txt',people)
                view_menu = False
            elif option == 4:
                add_to_table('DRINKS',drinks)
                table('DRINKS', drinks)
                save_data('drinks.txt', drinks)
                view_menu = False
            elif option == 5:
                preferences = assign_fave_drink(people, drinks)
                view_menu = False
            elif option == 6: 
                person_and_drink("PREFERENCES", preferences)   
                view_menu = False
            else: 
                print("\nSorry I dont understand.\nPlease choose between 1 and 6.")
        except ValueError as v:        # Raised if anything other than an integer is input.
            print('\n')
            print(v)
            print("That is not an integer between 1 and 6, try again!")
        except NameError as n:         # Raised if the preferences list is opened without 
            print('\n')                # assigning people to drinks
            print(n)
            print("No drinks have been assigned to people yet")   
    if not view_another_page():       # Ending the app
        print("\nThanks for stopping by, see you soon!\n")
        break