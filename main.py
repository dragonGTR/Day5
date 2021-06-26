import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",passwd="123SunilRaj@",database="mysql1")

mycursor = db.cursor()

try:
    mycursor.execute(
        "CREATE TABLE Per (name VARCHAR(50), age smallint UNSIGNED, id int PRIMARY KEY AUTO_INCREMENT)")
except:
    print("Already Exists ")


def insert(name,age):
    mycursor.execute("INSERT INTO Person (name,age) VALUES (%s,%s)",(name,age))
    db.commit()

mycursor.execute("SELECT  * FROM Person")

for x in mycursor:
    print(x)
#
# insert("SUnil",21)

