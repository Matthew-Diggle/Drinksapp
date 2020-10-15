import pymysql

def connect_db():
	connection = pymysql.connect(
		host="localhost",
    	port=33066,
		user="root",
		passwd="password",
		database="Drink_app"
	)
	return connection



# def main():
# 	connection = pymysql.connect(
# 	host="localhost",
# 	port=33066,
# 	user="root",
# 	passwd="password",
# 	database="Drink_app"
# 	)
# 	cursor = connection.cursor()
# 	args = ("")
# 	cursor.execute("INSERT INTO Drinks (Drink) VALUES (%s)", args)
# 	connection.commit()
# 	cursor.close()
# 	connection.close()
# 	print("done")