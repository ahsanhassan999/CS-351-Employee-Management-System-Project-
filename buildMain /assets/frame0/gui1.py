import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector


con = mysql.connector.connect(
    host="localhost", user="root", password="", database="Employee")


window_1 =Tk()
window_1.title("Display Records")
window_1.geometry("1325x300")

frame = tk.Frame(window_1, background="grey")
trv = ttk.Treeview(frame, columns=(1,2,3,4,5,6,7), height=15, show="headings")
trv.column(1, anchor=CENTER, stretch=NO, width=50)
trv.column(2, anchor=CENTER, stretch=NO, width=200)
trv.column(3, anchor=CENTER, stretch=NO, width=250)
trv.column(4, anchor=CENTER, stretch=NO, width=120)
trv.column(5, anchor=CENTER, stretch=NO, width=500)
trv.column(6, anchor=CENTER, stretch=NO, width=100)
trv.column(7, anchor=CENTER, stretch=NO, width=100)

trv.heading(1, text="ID")
trv.heading(2, text="Name")
trv.heading(3, text="Email ID")
trv.heading(4, text="Phone No")
trv.heading(5, text="Address")
trv.heading(6, text="Post")
trv.heading(7, text="Salary (Rs/-)")


def Display_Records():


    sql = "SELECT * FROM Employee_Data"

    c = con.cursor()
    # Executing the sql query
    c.execute(sql)

    # Fetching all details of all the Employees
    r = c.fetchall()
    for i in r:
        trv.insert("",'end', value=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

    trv.grid(row=0, column=0)
    frame.grid(row=0, column=0)
    window_1.mainloop()


Display_Records()