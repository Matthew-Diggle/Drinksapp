import sys
args = sys.argv
print(args)

name_ = ['John', 'Sarah', 'Maurice', 'Paul']
favourite_drink = ['coffee', 'juice', 'water', 'coke']

def get_people():   
    print(name)
def get_drink():
    print(favourite_drink)
for drink in favourite_drink:
    print(drink)

for x, name in enumerate(name_):
    print(x, name)
for y, drink in enumerate(favourite_drink):
    print(y, favourite_drink)
print("My name is " , name_ , " and my favourite drink is " , favourite_drink)