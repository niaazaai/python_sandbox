import mysql.connector 


connection = mysql.connector.connect(
    host = "localhost" , 
    user = "root" , 
    password = "" , 
    database = "python"
)
database = connection.cursor()