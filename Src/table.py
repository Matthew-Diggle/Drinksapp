def print_table(title, data):
    width = get_table_width(title, data)
    print_header(title, width)
    for item in data:
        print(f'| {item}')
    print_separator(width)
    wait()

def print_header(title, width):
    print_separator(width)
    print(f'| {title}' + "  |")
    print_separator(width)

def print_separator(width):
    print(f"+{'=' * width}+")

# Remember to define item "for item in data" or else "item" won't be defined
def get_table_width(title, data):
    longest = len(title)
    extra_spaces = 3
    for item in data:
        if longest < len(item):

            longest = len(item)
    return longest + extra_spaces

def wait():
    input("Press any key to return to menu")