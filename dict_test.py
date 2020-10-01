from csv import DictReader
preferences = {}

CSV_FILE = "Favourites.csv"
def load_favourites():
    try:
        with open("CSV_FILE", "r") as file:
            reader = DictReader(file)
            for data in reader:
                preferences[data['Name']] = data['Drink']
            print(preferences)
    except TypeError:
        print("There was a TypeError")

load_favourites()
print(preferences)