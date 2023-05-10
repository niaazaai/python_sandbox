import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost' , 
    username = 'root' , 
    password = '' ,
    database = 'python'
)

database = connection.cursor()
sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )
database.execute(sql, adr)
connection.commit()
print(database.rowcount, "record(s) deleted")