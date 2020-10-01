import csv
from csv import reader, DictReader
import pymysql

connection = pymysql.connect(host="localhost", port=33066, user="root", passwd="password", database="Drink_app")
filepath = "csv_database.csv"

#database connector function
# def connector():
#     connection
#     cursor = connection.cursor()
#     return (connection, cursor)

#Upload csv data to database
def upload():
    connection
    cursor = connection.cursor()
    with open(filepath, "r") as file_:
        csv_data = csv.reader(file_, quoting=csv.QUOTE_ALL)
        # print(csv_data)
        next(csv_data) #Skips first line of csv
        for row in csv_data:
            cursor.execute("INSERT INTO Practice_csv(`User Name`, Name, `Display Name`, `Job Title`, Department, `Office Number`, `Office Phone`, `Mobile Phone`, Fax, Address, City, `State OR Province`, `ZIP OR Post code`, `Country OR Region`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", row)
            connection.commit()
    cursor.close()
    connection.close()
    print("Done")

# upload()

#Split csv name to First and Last name capitalised.
def load_csv():
    data_list = []
    with open(filepath,'r') as csv_file:
        csv_reader = DictReader(csv_file)
        for row in csv_reader:
            data_list.append(row['Display Name'])
            string =' '.join((map(str,data_list)))
            x_names = string.split(' ')
            global first_names
            first_names = []
            global surnames
            surnames = []
            for i,x in enumerate(x_names):
                if i % 2 == 0:
                    first_names.append(x.title())
                else:
                    surnames.append(x.title())
        # print(first_names) 
        # print(surnames)
        return first_names, surnames

load_csv()

#Insert new names into database
# def upload_fixed_names():
#     connection = pymysql.connect(
#         host="localhost",
#         port=33066,
#         user="root",
#         passwd="password",
#         database="Drink_app"
#     )
#     cursor = connection.cursor()
#     args = (first_names, surnames)
# 	cursor.execute("INSERT INTO Practice_csv (`First Name`, Surname) VALUES (%s, %s)", args)
#     connection.commit()
#     cursor.close()
#     connection.close()
# upload_fixed_names()

def wap():
    # connection = pymysql.connect(host="localhost", port=33066, user="root", passwd="password", database="Drink_app")
    # cursor = connection.cursor()
    # connector()[0]
    # connector()[1]
    connection
    cursor = connection.cursor()
    for i,s in zip(first_names, surnames):
        args = (i,s)
        cursor.execute("UPDATE Practice_csv SET `First Name` = 'i', Surname = 's' WHERE `First Name` IS NOT Annissa", args)
    connection.commit()
    cursor.close()
    connection.close()
    print("done")
wap()