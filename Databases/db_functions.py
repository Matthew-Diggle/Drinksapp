import pymysql
from Classes.person_class import Person
from Classes.drink_class import Drink
# from Src.Add_data_to_menu import Preferences


def connect_db():
	connection = pymysql.connect(
		host="localhost",
    	port=33066,
		user="root",
		passwd="password",
		database="Drink_app"
	)
	return connection

def data_load_persons():
    data_list = []
    cursor = connect_db().cursor()
    cursor.execute("SELECT * FROM Person")
    while True:
        data_info = cursor.fetchone()
        if data_info == None:
            break
        data_list.append(Person(data_info[1]))
        connect_db().commit
    cursor.close()
    connect_db().close()
    return data_list

def data_load_drinks():
    data_list = []
    cursor = connect_db().cursor()
    cursor.execute("SELECT * FROM Drinks")
    while True:
        data_info = cursor.fetchone()
        if data_info == None:
            break
        data_list.append(Drink(data_info[0], data_info[1], data_info[2]))
        connect_db().commit
    cursor.close()
    connect_db().close()
    return data_list

def add_new_person_to_db():
    connection = pymysql.connect(
    host="localhost",
    port=33066,
    user="root",
    passwd="password",
    database="Drink_app"
)
    cursor = connection.cursor()
    for i in people: 
        if i == people[-1]:
            cursor.execute(f"INSERT INTO Person (Name) VALUES ('{i.name}')")
            connection.commit()
    cursor.close()
    connection.close()

def add_new_drink_to_db():
    connection = pymysql.connect(
		host="localhost",
    	port=33066,
		user="root",
		passwd="password",
		database="Drink_app"
	)
    cursor = connection.cursor()
    for i in drink: 
        if i == drink[-1]:
            cursor.execute(f"INSERT INTO Drinks (Drink, Temp, Blend) VALUES ('{i.drink_name}', '{i.temp}', '{i.blend}')")
            connection.commit()
    cursor.close()
    connection.close()

# def add_preferences_to_db():
#     connection = pymysql.connect(
# 		host="localhost",
#     	port=33066,
# 		user="root",
# 		passwd="password",
# 		database="Drink_app"
# 	)
#     cursor = connection.cursor()
#     for key, value in Preferences.items():
#         if key == Preferences.keys()[-1]:
#             cursor.execute(f'INSERT INTO Preferences (Name, Drink) VALUES ({key}, {value}')
#             connection.commit()
#     cursor.close()
#     connection.close()




people = data_load_persons()
drink = data_load_drinks()
# data_load()