import Src.table
from Classes.person_class import Person
class Round:
    def __init__(self, owner_name):
        self.owner = owner_name
        self.orders = {} 
    
    def add_order(self, name, drink, blend, temp):
        self.orders[name] = drink

    def print_order(self):
        items = []
        for name, drink, blend, temp in self.orders.items():
            items.append(f'{name} ordered a {temp} {blend} {drink}' )
        Src.table.print_table(f"{self.owner}'s round", items)

round = Round("Carlos")
round.print_order()