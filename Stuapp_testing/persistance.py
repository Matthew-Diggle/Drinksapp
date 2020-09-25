# Data persistence helper funcs
def exit_with_error(e, msg=None):
    msg = msg if msg else 'Something went wrong'
    print(f'{msg} with error: {str(e)} - exiting')
    exit()
def load_from_file(path):
    data = []
    try:
        with open(path, 'r') as file:
            for line in file.readlines():
                # Check if empty - bail/stop/valdiate as early as possible
                if line == '':
                    continue
                # Trim newline/whitespace
                # Add to data
                data.append(line.strip())
    except FileNotFoundError as e:
        exit_with_error(e, f'File "{path}" cannot be found')
    except Exception as e:
        exit_with_error(e, f'Unable to open file "{path}"')
    return data
def load_favourites(people, drinks):
    for item in load_from_file(FAVOURITES_FILE_PATH):
        # Unpacking the items in the list to separate variables
        # https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/
        # I know items.split will return a list with two items, because of the second argument
        # it will only split once even if there are more instances of ':' in the string
        name, drink = item.split(":", 1)
        if name in people and drink in drinks:
            favourite_drinks[name] = drink
        else:
            print('Unexpected data returned when loading favourites.')
            print(f'Drink is known: {drink in drinks}')
            print(f'Name is known: {name in people}')
def load_data():
    for person in load_from_file(PEOPLE_FILE_PATH):
        people.append(person)
    for drink in load_from_file(DRINKS_FILE_PATH):
        drinks.append(drink)
    load_favourites(people, drinks)
def save_to_file(path, data):
    try:
        with open(path, 'w') as file:
            # List comprehension - make a new list from an list
            # https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
            # There are other ways to this but list comprehension
            # is an idiomatic use of python
            file.writelines([f'{item}\n' for item in data])
    except FileNotFoundError as e:
        exit_with_error(e, f'File "{path}" cannot be found')
    except Exception as e:
        exit_with_error(e, f'Unable to open file "{path}"')
def save_favourites(data):
    items = []
    for item in data.items():
        name, drink = item
        # Defining a consistent structure here so that I can parse/recognise it when loading
        # I realise I could use a CSV format but I wanted to demonstrate "solving" this problem
        # without something being provided to me by the world already
        items.append(f'{name}:{drink}')
    save_to_file(FAVOURITES_FILE_PATH, items)