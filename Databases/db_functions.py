import pymysql
from Classes.person_class import Person
from Classes.drink_class import Drink


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



people = data_load_persons()
drink = data_load_drinks()
# data_load()