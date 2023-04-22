import mysql.connector


# python need the driver called mysql-connector
# python -m pip install mysql-connector-python


# to connect to mysql database 
connection = mysql.connector.connect(  
  host="localhost", 
  user="root",  
  password="c6SUwPIkNV]joQtN", 
)

database = connection.cursor()
# database.execute("CREATE DATABASE python")


database.execute("SHOW DATABASES")
for x in database:
  print(x)
