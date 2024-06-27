# Connecting Database and Inserting Tables with their fields
import mysql.connector

con = mysql.connector.connect(
    host="localhost", user="root", password="", database="Employee") # Using Database name which we created
mycursor = con.cursor()

# Creating Tables with their fields and type
# Employee_Data is the table name
# ID, Name, Email_ID, Phone_No, Address, Post, Salary are the Field Names
# After Name their types are defined
mycursor.execute("CREATE Table Employee_Data (ID INT(11) PRIMARY KEY, Name VARCHAR(1000), Email_ID TEXT(1000), Phone_No INT(11), Address Text(1000), Post Text(100),Salary BIGINT(20))")