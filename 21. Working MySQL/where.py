import mysql.connector 


connection = mysql.connector.connect(
    host = "localhost" , 
    user = "root" , 
    password = "" , 
    database = "python"
)
database = connection.cursor()

database.execute('SELECT * FROM customers WHERE id = 1')
myresult = database.fetchall()

for x in myresult:
  print(x)
