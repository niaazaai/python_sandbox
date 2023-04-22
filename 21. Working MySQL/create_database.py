import mysql.connector 


connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='c6SUwPIkNV]joQtN'
)

database = connection.cursor()
database.execute('CREATE DATABASE python_practice')

 