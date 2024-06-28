# Employee Management System Using Python - Sagar Developer


# importing mysql connector
import mysql.connector

# making Connection
con = mysql.connector.connect(
    host="localhost", user="root", password="", database="Employee")




# Function to Add_Employ
def Add_Employ():
    print("{:>60}".format("-->>Add Employee Record<<--"))
    Id = input("Enter Employee Id: ")
    # checking If Employee Id is Exit Or Not
    if (check_employee(Id) == True):
        print("Employee ID Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        Add_Employ()
    Name = input("Enter Employee Name: ")
    # checking If Employee Name is Exit Or Not
    if (check_employee_name(Name) == True):
        print("Employee Name Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        Add_Employ()
    Email_Id = input("Enter Employee Email ID: ")
    Phone_no = input("Enter Employee Phone No.: ")
    Address = input("Enter Employee Address: ")
    Post = input("Enter Employee Post: ")
    Salary = input("Enter Employee Salary: ")
    data = (Id, Name, Email_Id, Phone_no, Address, Post, Salary)
    # Instering Employee Details in
    # the Employee (empdata) Table
    sql = 'insert into Employee_Data values(%s,%s,%s,%s,%s,%s,%s)'
    c = con.cursor()

    # Executing the sql Query
    c.execute(sql, data)

    # Commit() method to make changes in the table
    con.commit()
    print("Successfully Added Employee Record")
    press = input("Press Any Key To Continue..")
    menu()


# Function To Check if Employee With
# given Name Exist or not
def check_employee_name(employee_name):
    # query to select all Rows from
    # employee(empdata) table
    sql = 'select * from Employee_Data where Name=%s'

    # making cursor buffered to make
    # rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_name,)

    # Execute the sql query
    c.execute(sql, data)

    # rowcount method to find number
    # of rowa with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False


# Function To Check if Employee With
# given Id Exist or not
def check_employee(employee_id):
    # query to select all Rows from
    # employee(empdata) table
    sql = 'select * from Employee_Data where Id=%s'

    # making cursor buffered to make
    # rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_id,)

    # Execute the sql query
    c.execute(sql, data)

    # rowcount method to find number
    # of rowa with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False


# Function to Display_Employ
def Display_Employ():
    print("{:>60}".format("-->> Display Employee Record <<--"))
    # query to select all rows from Employee (empdata) Table
    sql = 'select * from Employee_Data'
    c = con.cursor()

    # Executing the sql query
    c.execute(sql)

    # Fetching all details of all the Employees
    r = c.fetchall()
    for i in r:
        print("Employee Id: ", i[0])
        print("Employee Name: ", i[1])
        print("Employee Email Id: ", i[2])
        print("Employee Phone No.: ", i[3])
        print("Employee Address: ", i[4])
        print("Employee Post: ", i[5])
        print("Employee Salary: ", i[6])
        print("\n")
    press = input("Press Any key To Continue..")
    menu()


# Function to Update_Employ
def Update_Employ():
    print("{:>60}".format("-->> Update Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    # checking If Employee Id is Exit Or Not
    if (check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        Email_Id = input("Enter Employee Email ID: ")
        Phone_no = input("Enter Employee Phone No.: ")
        Address = input("Enter Employee Address: ")
        # Updating Employee details in empdata Table
        sql = 'UPDATE Employee_Data set Email_Id = %s, Phone_no = %s, Address = %s where Id = %s'
        data = (Email_Id, Phone_no, Address, Id)
        c = con.cursor()

        # Executing the sql query
        c.execute(sql, data)

        # commit() method to make changes in the table
        con.commit()
        print("Updated Employee Record")
        press = input("Press Any Key To Continue..")
        menu()


# Function to Promote_Employ
def Promote_Employ():
    print("{:>60}".format("-->> Promote/Demote Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    # checking If Employee Id is Exit Or Not
    if (check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        sql = 'select * from Employee_Data'
        c = con.cursor()

        # Executing the sql query
        c.execute(sql)

        # Fetching all details of all the Employees
        r = c.fetchone()

        print("1.Employee Id: ", r[0])
        print("2.Employee Name: ", r[1])
        print("3.Employee Email Id: ", r[2])
        print("4.Employee Phone No.: ", r[3])
        print("5.Employee Address: ", r[4])
        print("6.Employee Post: ", r[5])
        print("7.Employee Salary: ", r[6])
        print("\n")
        Choice = input("Which Field you want to edit: ")
        



        Post = input("Enter New Post: ")
        Amount = int(input("Enter New Salary: "))

        # query to fetch salary of Employee with given data
        sql = 'UPDATE Employee_Data set Post = %s, Salary = %s where Id = %s'
        data = (Post, Amount, Id)
        c = con.cursor()

        # executing the sql query
        c.execute(sql, data)

        con.commit()
        print("Employee Promoted/Demoted")
        press = input("Press Any key To Continue..")
        menu()


# Function to Remove_Employ
def Remove_Employ():
    print("{:>60}".format("-->> Remove Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    # checking If Employee Id is Exit Or Not
    if (check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        # query to delete Employee from empdata table
        sql = 'delete from Employee_Data where Id = %s'
        data = (Id,)
        c = con.cursor()

        # executing the sql query
        c.execute(sql, data)

        # commit() method to make changes in the empdata table
        con.commit()
        print("Employee Removed")
        press = input("Press Any key To Continue..")
        menu()


# Function to Search_Employ
def Search_Employ():
    print("{:>60}".format("-->> Search Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    # checking If Employee Id is Exit Or Not
    if (check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        # query to search Employee from empdata table
        sql = 'select * from Employee_Data where Id = %s'
        data = (Id,)
        c = con.cursor()

        # executing the sql query
        c.execute(sql, data)

        # fetching all details of all the employee
        r = c.fetchall()
        for i in r:
            print("Employee Id: ", i[0])
            print("Employee Name: ", i[1])
            print("Employee Email Id: ", i[2])
            print("Employee Phone No.: ", i[3])
            print("Employee Address: ", i[4])
            print("Employee Post: ", i[5])
            print("Employee Salary: ", i[6])
            print("\n")
        press = input("Press Any key To Continue..")
        menu()


# Menu function to display menu
def menu():
    print("{:>60}".format("************************************"))
    print("{:>60}".format("-->> Employee Management System <<--"))
    print("{:>60}".format("************************************"))
    print("1. Add Employee")
    print("2. Display Employee Record")
    print("3. Update Employee Details")
    print("4. Promote/Demote Employee Record")
    print("5. Remove Employee Record")
    print("6. Search Employee Record")
    print("7. Exit\n")
    print("{:>60}".format("-->> Choice Options: [1/2/3/4/5/6/7] <<--"))

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        Add_Employ()
    elif ch == 2:
        Display_Employ()
    elif ch == 3:
        Update_Employ()
    elif ch == 4:
        Promote_Employ()
    elif ch == 5:
        Remove_Employ()
    elif ch == 6:
        Search_Employ()
    elif ch == 7:
        print("{:>60}".format("Have A NIce Day :)"))
        exit(0)
    else:
        print("Invalid Choice!")
        press = input("Press Any key To Continue..")
        menu()


# Calling menu function
menu()