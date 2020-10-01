import pymysql
#import Names.txt

def main():
	connection = pymysql.connect(
		host="localhost",
    	port=33066,
		user="root",
		passwd="password",
		database="Drink_app"
	)
	cursor = connection.cursor()
	args = ("John", "Coke")
	cursor.execute("INSERT INTO Preferences (Name, Drink)" "VALUES (%s, %s)", args)
	connection.commit()
	cursor.close()
	connection.close()
	print("done")
main()