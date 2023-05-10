import mysql.connector


connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='python'
)

database = connection.cursor()

# LIST PREVIOUSE TABLSE 
database.execute("SHOW TABLES")
for x in database:
  print(x)
  

# CREATE TABLE 
# database.execute('CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))')


# TO ALTER TABLE 
# database.execute('ALTER TABLE customers ADD COLUMN comment VARCHAR(255)')
