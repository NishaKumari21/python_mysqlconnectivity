import mysql.connector as mc
mydb=mc.connect(host="localhost",user="root",passwd="nisha@21",database="python_mysql")
if mydb.is_connected():
    print("Connected to MySQL database")
    mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
values = [
    ("Nisha Kumari",  "Amer"),
    ("Amit Singh",  "Bikaner"),
    ("Rahul Verma", "kashmir"),
]

mycursor.executemany(sql, values)
mydb.commit()

print(f"✅ {mycursor.rowcount} rows inserted successfully!")
