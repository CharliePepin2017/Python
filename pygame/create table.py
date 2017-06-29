import sqlite3
#Creating a database name
connection = sqlite3.connect("company.db")
cursor = connection.cursor ()

#create a table called as students
"""CREATE TABLE Tables (
Int Id,
Name Varchar(20)
);"""
sql_command ="""INSERT INTO Tables (Id, Name, Age, Height, Weight) VALUES(1, "Varchar", 37 ,"5 feet 11 inches" , "185 lbs")"""

cursor.execute(sql_command)

# Save the changes
connection.commit()
connection.close()
