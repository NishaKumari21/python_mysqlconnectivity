import mysql.connector as mc
mydb=mc.connect(host="localhost",user="root",passwd="nisha@21",database="python_mysql")
if mydb.is_connected():
    print("Connected to MySQL database")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
    # mycursor.execute("show tables ")
    for i in mycursor:
        print(i)
    print("table created successfully")