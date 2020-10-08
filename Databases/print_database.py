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
    cursor.execute("SELECT * FROM Drink_app.Preferences")
    while True:
        row = cursor.fetchone()
    
        if row == None:
            break
        print("ID - " + str(row[0]) + " " + "Name - " + str(row[1]) + " " + "Drink - " + str(row[2]))
    connection.commit()
    cursor.close()
    connection.close()

main()