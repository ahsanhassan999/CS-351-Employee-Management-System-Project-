

# Employee Management System Using Python


# importing mysql connector
import mysql.connector

# making Connection
con = mysql.connector.connect(
    host="localhost", user="root", password="", database="Employee")


import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


from pathlib import Path


# Function to switch between frames
def show_frame(frame):
    frame.tkraise()


# Define the relative_to_assets function
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/hassanrizvi/Documents/GitHub/CS-351-Employee-Management-System-Project-/buildMain /assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Main window setup
root = tk.Tk()
root.geometry("862x519")
root.configure(bg="#FFFFFF")

# Create a container for all frames
container = tk.Frame(root)
container.pack(fill="both", expand=True)

# Configure rows and columns of the container
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

# Creating Frames

# Frame 1 (Login Page)
frame1 = tk.Frame(container, bg="#FFFFFF")
frame1.grid(row=0, column=0, sticky="nsew")

# Frame 2 (Menu Page)
frame2 = tk.Frame(container, bg="#FFFFFF")
frame2.grid(row=0, column=0, sticky="nsew")

# Frame 3 (Add Records)
frame3 = tk.Frame(container, bg="#FFFFFF")
frame3.grid(row=0, column=0, sticky="nsew")

# Frame 4 (Edit Records)
frame4 = tk.Frame(container, bg="#FFFFFF")
frame4.grid(row=0, column=0, sticky="nsew")

# Frame 5 (Remove Record)
frame5 = tk.Frame(container, bg="#FFFFFF")
frame5.grid(row=0, column=0, sticky="nsew")


# Frame 7 (Search Record)
frame7 = tk.Frame(container, bg="#FFFFFF")
frame7.grid(row=0, column=0, sticky="nsew")

# Populate Frame 1
canvas1 = tk.Canvas(
    frame1,
    bg="#8D0000",
    height=519,
    width=862,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas1.place(x=0, y=0)
canvas1.create_rectangle(431.0,0.0,862.0,519.0,fill="#FFD6D6",outline="")

canvas1.create_text(
    14.0,
    336.0,
    anchor="nw",
    text="CS-351 Programming Fundamentals (Project)\nGroup Members:\n47.Syed Ahsan Hassan Rizvi (S.No: 676514)\n43. Shahrukh Khan (S.No: 679023)\n57.Syed Wasif Ali Rizvi (S.No: 675454)\n68. Syed Farzam Ahmed Warsi (S.No: 677419)\n\n",
    fill="#FFFFFF",
    font=("CatamaranRoman Bold", 16 * -1)
)


def enter_data():
    username = entry_username.get()
    password = entry_password.get()
    if username == "Admin" and password == "admin":
        messagebox.showinfo(title="Login", message="Login Successful")
        show_frame(frame2)
    else:
        messagebox.showerror(title="Error", message="Invalid Username and/or Password")
        


Login_button_image = tk.PhotoImage(file=relative_to_assets("Login button.png"))
button_1 = tk.Button(
    frame1,
    image=Login_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=enter_data,
    relief="flat"
)
button_1.place(x=565, y=393, width=180, height=55)

canvas1.create_text(14, 57, anchor="nw", text="Employee Management System", fill="#FCFCFC",
                    font=("Aclonica Regular", 24 * -1))
canvas1.create_rectangle(14, 87, 420, 92, fill="#FCFCFC", outline="")

entry_image_password = tk.PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_password = canvas1.create_image(655, 314, image=entry_image_password)
entry_password = tk.Entry(frame1, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_password.place(x=494, y=285, width=321, height=55)

entry_image_username = tk.PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_username = canvas1.create_image(655, 203, image=entry_image_username)
entry_username = tk.Entry(frame1, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_username.place(x=494, y=174, width=321, height=55)

canvas1.create_text(489, 260, anchor="nw", text="Password", fill="#7C0000", font=("Roboto Bold", 20 * -1))
canvas1.create_text(489, 149, anchor="nw", text="Username", fill="#7C0000", font=("Roboto Bold", 20 * -1))

canvas1.create_text(
    14, 115, anchor="nw",
    text="The Employee Management System (EMS) automates \nthe management of employee data to enhance \nproductivity and accuracy in HR processes.",
    fill="#FFFFFF", font=("CatamaranRoman Black", 16 * -1)
)

canvas1.create_text(
    519, 61, anchor="nw",
    text="Enter details to Login",
    fill="#7C0000", font=("RobotoRoman Black", 26 * -1)
)

# Populate Frame 2 (Menu Page)


canvas2 = tk.Canvas(
    frame2,
    bg="#8D0000",
    height=519,
    width=862,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas2.place(x=0, y=0)
canvas2.create_rectangle(
    431.0,
    0.0,
    862.0,
    519.0,
    fill="#FFD6D6",
    outline=""
)

canvas2.create_text(
    14.0,
    57.0,
    anchor="nw",
    text="Employee Management System",
    fill="#FCFCFC",
    font=("Aclonica Regular", 24 * -1)
)

canvas2.create_text(
    14, 115, anchor="nw",
    text="The Employee Management System (EMS) automates \nthe management of employee data to enhance \nproductivity and accuracy in HR processes.",
    fill="#FFFFFF", font=("CatamaranRoman Black", 16 * -1)
)

canvas2.create_text(
    14.0,
    336.0,
    anchor="nw",
    text="CS-351 Programming Fundamentals (Project)\nGroup Members:\n47.Syed Ahsan Hassan Rizvi (S.No: 676514)\n43. Shahrukh Khan (S.No: 679023)\n57.Syed Wasif Ali Rizvi (S.No: 675454)\n68. Syed Farzam Ahmed Warsi (S.No: 677419)\n\n",
    fill="#FFFFFF",
    font=("CatamaranRoman Bold", 16 * -1)
)

canvas2.create_rectangle(
    14.0,
    87.0,
    420.0,
    92.0,
    fill="#FCFCFC",
    outline=""
)

canvas2.create_text(
    556.0,
    47.0,
    anchor="nw",
    text="Menu Options",
    fill="#7C0000",
    font=("RobotoRoman Black", 26 * -1)
)

# Add more widgets to frame2 as needed
# Example buttons
Add_button_image = tk.PhotoImage(file=relative_to_assets("Add Record Button.png"))
button_2 = tk.Button(
    frame2,
    image=Add_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(frame3),
    relief="flat"
)
button_2.place(x=446.0, y=129.0, width=180.0, height=55.0)

Remove_button_image = tk.PhotoImage(file=relative_to_assets("Remove Record Button.png"))
button_3 = tk.Button(
    frame2,
    image=Remove_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(frame5),
    relief="flat"
)
button_3.place(x=647.0, y=129.0, width=180.0, height=55.0)

Edit_button_image = tk.PhotoImage(file=relative_to_assets("Edit Button.png"))
button_4 = tk.Button(
    frame2,
    image=Edit_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(frame4),
    relief="flat"
)
button_4.place(x=446.0, y=240.0, width=180.0, height=55.0)

Display_button_image = tk.PhotoImage(file=relative_to_assets("Display Records Button.png"))
button_5 = tk.Button(
    frame2,
    image=Display_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Display_Records(),
    relief="flat"
)
button_5.place(x=649.0, y=240.0, width=180.0, height=55.0)

Search_button_image = tk.PhotoImage(file=relative_to_assets("Search Button.png"))
button_6 = tk.Button(
    frame2,
    image=Search_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(frame7),
    relief="flat"
)
button_6.place(x=446.0, y=353.0, width=180.0, height=55.0)

Back_button_image = tk.PhotoImage(file=relative_to_assets("Back button.png"))
button_7 = tk.Button(
    frame2,
    image=Back_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(frame1),
    relief="flat"
)
button_7.place(x=652.0, y=353.0, width=180.0, height=55.0)

# Frame3 (Adding New Record) Page
canvas3 = tk.Canvas(
    frame3,
    bg="#8D0000",
    height=519,
    width=862,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas3.place(x=0, y=0)
canvas3.create_rectangle(
    45.0,
    0.0,
    807.0,
    519.0,
    fill="#FFD6D6",
    outline="")

Heading_Img_newrecords = tk.PhotoImage(file=relative_to_assets("Adding New Records Button.png"))
heading_newrecords = canvas3.create_image(195.0, 30.0, image=Heading_Img_newrecords)

button_image_1 = tk.PhotoImage(
    file=relative_to_assets("Add Record Button.png"))
button_1 = tk.Button(
    frame3,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Add_Employ(),
    relief="flat"
)
button_1.place(
    x=444.0,
    y=443.0,
    width=180.0,
    height=55.0
)

entry_image_address = tk.PhotoImage(
    file=relative_to_assets("Address Bar.png"))
canvas3.create_image(
    584.0,
    353.5,
    image=entry_image_address
)
entry_address = tk.Entry(
    frame3,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_address.place(
    x=456.0,
    y=295.0,
    width=256.0,
    height=118.0
)

canvas3.create_text(
    454.0,
    256.0,
    anchor="nw",
    text="Address",
    fill="#7C0000",
    font=("Roboto Bold", 20 * -1)
)

entry_image_salary = tk.PhotoImage(
    file=relative_to_assets("Entry Bar Add Records.png"))
entry_salary = canvas3.create_image(
    584.0,
    228.5,
    image=entry_image_salary
)
entry_salary = tk.Entry(
    frame3,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_salary.place(
    x=456.0,
    y=215.0,
    width=256.0,
    height=30.0
)

canvas3.create_text(
    454.0,
    178.0,
    anchor="nw",
    text="Salary",
    fill="#7C0000",
    font=("Roboto Bold", 20 * -1)
)

entry_image_post = tk.PhotoImage(
    file=relative_to_assets("Entry Bar Add Records.png"))
entry_bg_post = canvas3.create_image(
    584.0,
    142.5,
    image=entry_image_post
)
entry_post = tk.Entry(
    frame3,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_post.place(
    x=456.0,
    y=128.0,
    width=256.0,
    height=30.0
)

canvas3.create_text(
    454.0,
    92.0,
    anchor="nw",
    text="Post",
    fill="#7C0000",
    font=("Roboto Bold", 20 * -1)
)

entry_image_phoneno = tk.PhotoImage(
    file=relative_to_assets("Entry Bar Add Records.png"))
entry_bg_phoneno = canvas3.create_image(
    211.5,
    396.5,
    image=entry_image_phoneno
)
entry_phoneno = tk.Entry(
    frame3,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_phoneno.place(
    x=83.5,
    y=380.0,
    width=256.0,
    height=30.0
)

entry_image_email = tk.PhotoImage(
    file=relative_to_assets("Entry Bar Add Records.png"))
entry_bg_email = canvas3.create_image(
    211.5,
    310.5,
    image=entry_image_email
)
entry_email = tk.Entry(
    frame3,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_email.place(
    x=83.5,
    y=295.0,
    width=256.0,
    height=30.0
)

canvas3.create_text(
    82.0,
    260.0,
    anchor="nw",
    text="Email ID ",
    fill="#7C0000",
    font=("Roboto Bold", 20 * -1)
)

canvas3.create_text(
    82.0,
    346.0,
    anchor="nw",
    text="Phone No",
    fill="#7C0000",
    font=("Roboto Bold", 20 * -1)
)

entry_image_Name = tk.PhotoImage(
    file=relative_to_assets("Entry Bar Add Records.png"))
entry_bg_Name = canvas3.create_image(
    211.5,
    228.5,
    image=entry_image_Name
)
entry_Name = tk.Entry(
    frame3,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_Name.place(
    x=83.5,
    y=215.0,
    width=256.0,
    height=30.0
)

canvas3.create_text(
    82.0,
    178.0,
    anchor="nw",
    text="Employee Name ",
    fill="#7C0000",
    font=("Roboto Bold", 20 * -1)
)

button_image_2 = tk.PhotoImage(
    file=relative_to_assets("Back Button.png"))
button_2 = tk.Button(
    frame3,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(frame2),
    relief="flat"
)
button_2.place(
    x=71.5,
    y=443.0,
    width=180.0,
    height=55.0
)

entry_image_id = tk.PhotoImage(
    file=relative_to_assets("Entry Bar Add Records.png"))
entry_bg_id = canvas3.create_image(
    211.5,
    142.5,
    image=entry_image_id
)
entry_id = tk.Entry(
    frame3,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_id.place(
    x=83.5,
    y=130.0,
    width=256.0,
    height=30.0
)

canvas3.create_text(
    82.0,
    92.0,
    anchor="nw",
    text="Employee Id",
    fill="#7C0000",
    font=("Roboto Bold", 20 * -1)
)



canvas3.create_rectangle(
    408.0,
    108.02481079101562,
    409.0,
    443.0248107910156,
    fill="#7C0000",
    outline="")

# Frame 4 (Edit Buttons)
canvas4 = tk.Canvas(
    frame4,
    bg = "#8D0000",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas4.place(x=0, y=0)
canvas4.create_rectangle(
    45.0,
    0.0,
    807.0,
    519.0,
    fill="#FFD6D6",
    outline="")

Heading_Img = tk.PhotoImage(file=relative_to_assets("Edit Records Button.png"))
heading = canvas4.create_image(130, 33.4, image=Heading_Img)



button_image_editf4 = tk.PhotoImage(
    file=relative_to_assets("Edit Button.png"))
button_editf4 = tk.Button(
    frame4,
    image=button_image_editf4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Update_Employ(),
    relief="flat"
)
button_editf4.place(
    x=444.0,
    y=443.0,
    width=180.0,
    height=55.0
)

entry_image_editaddress = tk.PhotoImage(
    file=relative_to_assets("Address Bar.png"))
entry_bg_editaddress = canvas4.create_image(
    584.0,
    271.5,
    image=entry_image_editaddress
)
entry_editaddress = tk.Entry(
    frame4,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_editaddress.place(
    x=456.0,
    y=212,
    width=256.0,
    height=120.0
)

canvas4.create_text(
    454.0,
    178.0,
    anchor="nw",
    text="New Address",
    fill="#7C0000",
    font=("Roboto Bold", 20 * -1)
)

entry_image_newsalary = tk.PhotoImage(
    file=relative_to_assets("Entry Bar Add Records.png"))
entry_bg_newsalary = canvas4.create_image(
    584.0,
    142.5,
    image=entry_image_newsalary
)
entry_newsalary = tk.Entry(
    frame4,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_newsalary.place(
    x=456.0,
    y=126.5,
    width=256.0,
    height=33.0
)

canvas4.create_text(
    454.0,
    92.0,
    anchor="nw",
    text="New Salary",
    fill="#7C0000",
    font=("Roboto Bold", 20 * -1)
)

entry_image_newpost = tk.PhotoImage(
    file=relative_to_assets("Entry Bar Add Records.png"))
entry_bg_newpost = canvas4.create_image(
    211.0,
    386.5,
    image=entry_image_newpost
)
entry_newpost = tk.Entry(
    frame4,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_newpost.place(
    x=83.0,
    y=370.0,
    width=256.0,
    height=33.0
)

canvas4.create_text(
    82.0,
    338.0,
    anchor="nw",
    text="New Post",
    fill="#7C0000",
    font=("Roboto Bold", 20 * -1)
)

entry_image_newphoneno = tk.PhotoImage(
    file=relative_to_assets("Entry Bar Add Records.png"))
entry_bg_newphoneno = canvas4.create_image(
    211.0,
    306.5,
    image=entry_image_newphoneno
)
entry_newphoneno = tk.Entry(
    frame4,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_newphoneno.place(
    x=83.0,
    y=290.0,
    width=256.0,
    height=35.0
)

entry_image_newemailid = tk.PhotoImage(
    file=relative_to_assets("Entry Bar Add Records.png"))
entry_bg_newemailid = canvas4.create_image(
    211.5,
    228.5,
    image=entry_image_newemailid
)
entry_newemailid = tk.Entry(
    frame4,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_newemailid.place(
    x=83.5,
    y=212.0,
    width=256.0,
    height=35.0
)

canvas4.create_text(
    82.0,
    178.0,
    anchor="nw",
    text="New Email ID ",
    fill="#7C0000",
    font=("Roboto Bold", 20 * -1)
)

canvas4.create_text(
    82.0,
    256.0,
    anchor="nw",
    text="New Phone No",
    fill="#7C0000",
    font=("Roboto Bold", 20 * -1)
)

button_image_backf4 = tk.PhotoImage(
    file=relative_to_assets("Back Button.png"))
button_backf4 = tk.Button(
    frame4,
    image=button_image_backf4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(frame2),
    relief="flat"
)
button_backf4.place(
    x=71.5,
    y=443.0,
    width=180.0,
    height=55.0
)

entry_image_employeeid = tk.PhotoImage(
    file=relative_to_assets("Entry Bar Add Records.png"))
entry_bg_employeeid = canvas4.create_image(
    211.5,
    142.5,
    image=entry_image_employeeid
)
entry_employeeid = tk.Entry(
    frame4,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_employeeid.place(
    x=83.5,
    y=126.0,
    width=256.0,
    height=35.0
)

canvas4.create_text(
    82.0,
    92.0,
    anchor="nw",
    text="Employee Id",
    fill="#7C0000",
    font=("Roboto Bold", 20 * -1)
)

canvas4.create_rectangle(
    408.0,
    108.02481079101562,
    409.0,
    443.0248107910156,
    fill="#000000",
    outline="")

# Frame 5 (Remove Records)

canvas5 = tk.Canvas(
    frame5,
    bg = "#7C0000",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas5.place(x = 0, y = 0)
canvas5.create_rectangle(
    430.9999999999999,
    7.105427357601002e-15,
    861.9999999999999,
    519.0,
    fill="#FFD6D6",
    outline="")

canvas5.create_text(
    13.999999999999886,
    336.0,
    anchor="nw",
    text="CS-351 Programming Fundamentals (Project)\nGroup Members:\n47.Syed Ahsan Hassan Rizvi (S.No: 676514)\n43. Shahrukh Khan (S.No: 679023)\n57.Syed Wasif Ali Rizvi (S.No: 675454)\n68. Syed Farzam Ahmed Warsi (S.No: 677419)\n\n",
    fill="#FFFFFF",
    font=("CatamaranRoman Bold", 16 * -1)
)

button_image_backf5 = tk.PhotoImage(
    file=relative_to_assets("Back Button.png"))
button_backf5 = tk.Button(
    frame5,
    image=button_image_backf5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(frame2),
    relief="flat"
)
button_backf5.place(
    x=470.5,
    y=353.0,
    width=180.0,
    height=55.0
)



button_image_removeepmloyeef5 = tk.PhotoImage(
    file=relative_to_assets("Remove Record Button.png"))
button_removeemployeef5 = tk.Button(
    frame5,
    image=button_image_removeepmloyeef5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Remove_Employ(),
    relief="flat"
)
button_removeemployeef5.place(
    x=654.5,
    y=353.0,
    width=180.0,
    height=55.0
)

canvas5.create_text(
    13.999999999999886,
    57.00000000000001,
    anchor="nw",
    text="Employee Management System",
    fill="#FCFCFC",
    font=("Aclonica Regular", 24 * -1)
)

canvas5.create_rectangle(
    13.999999999999886,
    87.0,
    419.9999999999999,
    92.00000000000003,
    fill="#FCFCFC",
    outline="")

entry_image_removeid = tk.PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_removeid = canvas5.create_image(
    654.4999999999999,
    252.5,
    image=entry_image_removeid
)
entry_removeid = tk.Entry(
    frame5,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_removeid.place(
    x=493.9999999999999,
    y=225.0,
    width=321.0,
    height=55.0
)

canvas5.create_text(
    490.9999999999999,
    184.0,
    anchor="nw",
    text="Employee ID",
    fill="#7C0000",
    font=("Roboto Bold", 24 * -1)
)

canvas5.create_text(
    13.999999999999886,
    115.0,
    anchor="nw",
    text="The Employee Management System (EMS) automates \nthe management of employee data to enhance \nproductivity and accuracy in HR processes.",
    fill="#FFFFFF",
    font=("CatamaranRoman Black", 16 * -1)
)

canvas5.create_text(
    490.9999999999999,
    61.00000000000001,
    anchor="nw",
    text="Remove Employee Record",
    fill="#7C0000",
    font=("RobotoRoman Black", 26 * -1)
)



# Frame 7 (Search Record)

canvas7 = tk.Canvas(
    frame7,
    bg = "#7C0000",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas7.place(x = 0, y = 0)
canvas7.create_rectangle(
    430.9999999999999,
    7.105427357601002e-15,
    861.9999999999999,
    519.0,
    fill="#FFD6D6",
    outline="")

canvas7.create_text(
    13.999999999999886,
    336.0,
    anchor="nw",
    text="CS-351 Programming Fundamentals (Project)\nGroup Members:\n47.Syed Ahsan Hassan Rizvi (S.No: 676514)\n43. Shahrukh Khan (S.No: 679023)\n57.Syed Wasif Ali Rizvi (S.No: 675454)\n68. Syed Farzam Ahmed Warsi (S.No: 677419)\n\n",
    fill="#FFFFFF",
    font=("CatamaranRoman Bold", 16 * -1)
)

button_image_searchf7 = tk.PhotoImage(
    file=relative_to_assets("Search Button.png"))
button_searchf7 = tk.Button(
    frame7,
    image=button_image_searchf7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Search_Employ(),
    relief="flat"
)
button_searchf7.place(
    x=655.9999999999999,
    y=353.0,
    width=180.0,
    height=55.0
)


button_image_backf7 = tk.PhotoImage(
    file=relative_to_assets("Back Button.png"))
button_backf7 = tk.Button(
    frame7,
    image=button_image_backf7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(frame2),
    relief="flat"
)
button_backf7.place(
    x=470.5,
    y=353.0,
    width=180.0,
    height=55.0
)




canvas7.create_text(
    13.999999999999886,
    57.00000000000001,
    anchor="nw",
    text="Employee Management System",
    fill="#FCFCFC",
    font=("Aclonica Regular", 24 * -1)
)

canvas7.create_rectangle(
    13.999999999999886,
    87.0,
    419.9999999999999,
    92.00000000000003,
    fill="#FCFCFC",
    outline="")

entry_image_employeeidsearch = tk.PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_employeeidsearch = canvas7.create_image(
    654.4999999999999,
    252.5,
    image=entry_image_employeeidsearch
)
entry_employeeidsearch = tk.Entry(
    frame7,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_employeeidsearch.place(
    x=494.9999999999999,
    y=226.0,
    width=321.0,
    height=55.0
)

canvas7.create_text(
    490.9999999999999,
    184.0,
    anchor="nw",
    text="Employee ID",
    fill="#7C0000",
    font=("Roboto Bold", 24 * -1)
)

canvas7.create_text(
    13.999999999999886,
    115.0,
    anchor="nw",
    text="The Employee Management System (EMS) automates \nthe management of employee data to enhance \nproductivity and accuracy in HR processes.",
    fill="#FFFFFF",
    font=("CatamaranRoman Black", 16 * -1)
)

canvas7.create_text(
    490.9999999999999,
    61.00000000000001,
    anchor="nw",
    text="Search Employee Record",
    fill="#7C0000",
    font=("RobotoRoman Black", 26 * -1))


#Displaying Records
def Display_Records():
    window_1 = tk.Tk()
    window_1.title("Display Records")
    window_1.geometry("1325x300")

    frame8 = tk.Frame(window_1, background="grey")
    trv = ttk.Treeview(frame8, columns=(1, 2, 3, 4, 5, 6, 7), height=15, show="headings")
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

    sql = "SELECT * FROM Employee_Data"

    c = con.cursor()
    # Executing the sql query
    c.execute(sql)

    # Fetching all details of all the Employees
    r = c.fetchall()
    for i in r:
        trv.insert("",'end', value=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

    trv.grid(row=0, column=0)
    frame8.grid(row=0, column=0)
    window_1.mainloop()

# Searching Records
def Search_Employ():
    Id = entry_employeeidsearch.get()
    # checking If Employee Id is Exit Or Not
    if (check_employee(Id) == False):
        messagebox.showerror(title="Error", message="This Employee ID do not Exists!")

    else:
        window_1 = tk.Tk()
        window_1.title("Display Records")
        window_1.geometry("1325x300")

        frame8 = tk.Frame(window_1, background="grey")
        trv = ttk.Treeview(frame8, columns=(1, 2, 3, 4, 5, 6, 7), height=15, show="headings")
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
        # query to search Employee from empdata table
        sql = 'select * from Employee_Data where Id = %s'
        data = (Id,)
        c = con.cursor()

        # executing the sql query
        c.execute(sql, data)

        # fetching all details of all the employee
        r = c.fetchall()
        for i in r:
            trv.insert("", 'end', value=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

            trv.grid(row=0, column=0)
            frame8.grid(row=0, column=0)
            window_1.mainloop()


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
# Function to Add_Employ
def Add_Employ():

    Id = entry_id.get()
    # checking If Employee Id is Exit Or Not
    if (check_employee(Id) == True):
        messagebox.showerror(title="Error", message="Employee Id Already Exists!")
    else:
        Name = entry_Name.get()
        # checking If Employee Name is Exit Or Not
        if (check_employee_name(Name) == True):
            messagebox.showerror(title="Error", message="Employee Name Already Exists!")

        else:
            Email_Id = entry_email.get()
            Phone_no = entry_phoneno.get()
            Address = entry_address.get()
            Post = entry_post.get()
            Salary = entry_salary.get()
            data = (Id, Name, Email_Id, Phone_no, Address, Post, Salary)
            # Instering Employee Details in
            # the Employee (empdata) Table
            sql = 'insert into Employee_Data values(%s,%s,%s,%s,%s,%s,%s)'
            c = con.cursor()

            # Executing the sql Query
            c.execute(sql, data)

            # Commit() method to make changes in the table
            con.commit()
            messagebox.showinfo(title="Accepted", message="New Record Added Successfully")

# Function to Edit_Employ
def Update_Employ():

    Id = entry_employeeid.get()
    # checking If Employee Id is Exit Or Not
    if (check_employee(Id) == False):
        messagebox.showerror(title="Error", message="This Employee ID doesnot exists!")

    else:

        Email_Id = entry_newemailid.get()
        Phone_no = entry_newphoneno.get()
        Address = entry_editaddress.get()
        Post = entry_newpost.get()
        Salary  = entry_newsalary.get()

        if Email_Id != "":
            sql = 'UPDATE Employee_Data set Email_Id = %s Where Id = %s'
            data = (Email_Id, Id)
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            messagebox.showinfo(title="Accepted", message="Email ID Updated")
        if Phone_no != "":
            sql = 'UPDATE Employee_Data set Phone_no = %s Where Id = %s'
            data = (Phone_no, Id)
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            messagebox.showinfo(title="Accepted", message="Phone No Updated")
        if Address != "":
            sql = 'UPDATE Employee_Data set Address = %s Where Id = %s'
            data = (Address, Id)
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            messagebox.showinfo(title="Accepted", message="Address Updated")
        if Post != "":
            sql = 'UPDATE Employee_Data set Post = %s Where Id = %s'
            data = (Post, Id)
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            messagebox.showinfo(title="Accepted", message="Post Updated")
        if Salary != None:
            sql = 'UPDATE Employee_Data set Salary = %s Where Id = %s'
            data = (Salary, Id)
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            messagebox.showinfo(title="Accepted", message="Salary Updated")

# Function to Remove Records
def Remove_Employ():

    Id = entry_removeid.get()
    # checking If Employee Id is Exit Or Not
    if (check_employee(Id) == False):
        messagebox.showerror(title="Error", message="This ID does not Exists!")

    else:
        # query to delete Employee from empdata table
        sql = 'delete from Employee_Data where Id = %s'
        data = (Id,)
        c = con.cursor()

        # executing the sql query
        c.execute(sql, data)

        # commit() method to make changes in the empdata table
        con.commit()
        messagebox.showinfo(title="Accepted", message="Record Deleted Successfully")




# Show the first frame initially
show_frame(frame1)

# Start the Tkinter event loop
root.resizable(False, False)
root.mainloop()
