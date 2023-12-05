import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",      # or your database host
  user="root",   # your database username
  password="krithicka", # your database password
  database="sdp"  # the database name you want to connect to
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")
for table in mycursor:
    print(table)

mydb.commit()  # Make sure to commit to save changes

# For retrieving data
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()  # fetchall() retrieves all rows

for row in myresult:
  print(row)

mycursor.close()
mydb.close()
