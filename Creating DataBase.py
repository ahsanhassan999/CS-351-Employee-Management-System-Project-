# Creating DataBase On which we will save all Data
import mysql.connector

con = mysql.connector.connect(
    host="localhost", user="root", password="",)
mycursor = con.cursor()

mycursor.execute("CREATE DATABASE Employee5") # Employee is the DataBase name which will be Created
