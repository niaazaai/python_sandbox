import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user="root", 
    # password='c6SUwPIkNV]joQtN', 
    password='', 
    # database="python_practice"
    database="python"
)


database = connection.cursor()

# query  = 'INSERT INTO customers ( name , address , comment ) VALUES (%s, %s, %s)'
# query_value = ("ahmad" , "9th District" , "comment 01")
# database.execute(query , query_value)

# connection.commit()

# print(f"query executed : {database.lastrowid}")
# print(database.rowcount, "record inserted.")



# if we insert many record at once 
query  = 'INSERT INTO customers ( name , address ) VALUES (%s, %s)'
query_value = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

database.executemany(query , query_value)
connection.commit()

print(f"query executed : {database.lastrowid}")
print(database.rowcount, "record inserted.")

