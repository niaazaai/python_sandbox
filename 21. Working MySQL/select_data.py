import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     port=3306,
#     user="root", 
#     password="c6SUwPIkNV]joQtN", 
#     database="python_practice"
# )

# mycursor = mydb.cursor()
# mycursor.execute("SELECT name, address FROM customers")
# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)



connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root", 
    password="c6SUwPIkNV]joQtN", 
    database="python_practice"
)


database = connection.cursor()

database.execute('SELECT * FROM customers')

select = database.fetchall()

print(select)

for value in select: 
    print(":::> ", value )


# OR WE CAN GET ONLY FIRST RECORD IN THE DATABSE 

database.execute('SELECT * FROM customers')

select = database.fetchone()

print(select)

for value in select: 
    print(":::> ", value )


