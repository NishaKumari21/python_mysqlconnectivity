import mysql.connector as mc
mydb=mc.connect(host="localhost",user="root",passwd="nisha@21")
if mydb.is_connected():
    print("Connected to MySQL database")
    mycursor = mydb.cursor()
    mycursor.execute("create database python_mysql")
    print("DB created successfully")