import mysql.connector as mc 
mydb=mc.connect(host="localhost",user="root",passwd="nisha@21")
if(mydb.is_connected()):
    print('connected')
else:
    print('unable to connect')


mycursor = mydb.cursor()
mycursor.execute("show databases")
for i in mycursor:
  print(i)
