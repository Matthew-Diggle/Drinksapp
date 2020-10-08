import csv

class Order:
    def __init__(self, name, drink):
        self.name = name
        self.drink = drink

def round_writer(): 
    writer = csv.writer(file_ref, quoting=csv.QUOTE_ALL)

def round_reader():
    reader = csv.reader(file_ref)
    
round = [Order("john", "Coffee"), Order("Sally", "Tea"), Order ("Mark", "Coke"), Order("Lisa", "Beer")]

try:
    with open('drinks.csv', 'w') as csvfile:
        writer()
        for order in round:
            writer.writerow([order.name, order.drink])
except:
    print("Unable to write round")

orders = []

try:
    with open('Drinks.csv')