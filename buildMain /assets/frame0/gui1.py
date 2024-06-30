

import tkinter as tk
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

# Frame 1 (Login Page)
frame1 = tk.Frame(container, bg="#FFFFFF")
frame1.grid(row=0, column=0, sticky="nsew")

# Frame 2 (Menu Page)
frame2 = tk.Frame(container, bg="#FFFFFF")
frame2.grid(row=0, column=0, sticky="nsew")

# Frame 3 (Add Records)
frame3 = tk.Frame(container, bg="#FFFFFF")
frame3.grid(row=0, column=0, sticky="nsew")

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
canvas1.create_rectangle(
    431.0,
    0.0,
    862.0,
    519.0,
    fill="#FFD6D6",
    outline=""
)

canvas1.create_text(
    14.0,
    336.0,
    anchor="nw",
    text="CS-351 Programming Fundamentals (Project)\nGroup Members:\nSyed Ahsan Hassan Rizvi (S.No: 676514)\n43. Shahrukh Khan (S.No: 679023)\nSyed Wasif Ali Rizvi (S.No: 675454)\n68. Syed Farzam Ahmed Warsi (S.No: 677419)\n\n",
    fill="#FFFFFF",
    font=("CatamaranRoman Bold", 16 * -1)
)

def enter_data():
    username = entry_2.get()
    password = entry_1.get()
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

canvas1.create_text(14, 57, anchor="nw", text="Employee Management System", fill="#FCFCFC", font=("Aclonica Regular", 24 * -1))
canvas1.create_rectangle(14, 87, 420, 92, fill="#FCFCFC", outline="")

entry_image_1 = tk.PhotoImage(file=relative_to_assets("Address Bar.png"))
entry_bg_1 = canvas1.create_image(655, 314, image=entry_image_1)
entry_1 = tk.Entry(frame1, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_1.place(x=494, y=285, width=321, height=55)

entry_image_2 = tk.PhotoImage(file=relative_to_assets("Entry Bar Add Records.png"))
entry_bg_2 = canvas1.create_image(655, 203, image=entry_image_2)
entry_2 = tk.Entry(frame1, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_2.place(x=494, y=174, width=321, height=55)

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
    text="CS-351 Programming Fundamentals (Project)\nGroup Members:\nSyed Ahsan Hassan Rizvi (S.No: 676514)\n43. Shahrukh Khan (S.No: 679023)\nSyed Wasif Ali Rizvi (S.No: 675454)\n68. Syed Farzam Ahmed Warsi (S.No: 677419)\n\n",
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
    command=lambda: print("Remove button clicked"),
    relief="flat"
)
button_3.place(x=647.0, y=129.0, width=180.0, height=55.0)

Edit_button_image = tk.PhotoImage(file=relative_to_assets("Edit Button.png"))
button_4 = tk.Button(
    frame2,
    image=Edit_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Edit button clicked"),
    relief="flat"
)
button_4.place(x=446.0, y=240.0, width=180.0, height=55.0)

Display_button_image = tk.PhotoImage(file=relative_to_assets("Display Records Button.png"))
button_5 = tk.Button(
    frame2,
    image=Display_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Display button clicked"),
    relief="flat"
)
button_5.place(x=649.0, y=240.0, width=180.0, height=55.0)

Search_button_image = tk.PhotoImage(file=relative_to_assets("Search Button.png"))
button_6 = tk.Button(
    frame2,
    image=Search_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Search button clicked"),
    relief="flat"
)
button_6.place(x=446.0, y=354.0, width=180.0, height=55.0)

Exit_button_image = tk.PhotoImage(file=relative_to_assets("Back Button.png"))
button_7 = tk.Button(
    frame2,
    image=Exit_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=root.quit,
    relief="flat"
)
button_7.place(x=649.0, y=354.0, width=180.0, height=55.0)

# Populate Frame 3 (Add Records)
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
    431.0,
    0.0,
    862.0,
    519.0,
    fill="#FFD6D6",
    outline=""
)

canvas3.create_text(
    14.0,
    57.0,
    anchor="nw",
    text="Employee Management System",
    fill="#FCFCFC",
    font=("Aclonica Regular", 24 * -1)
)

canvas3.create_text(
    14, 115, anchor="nw",
    text="The Employee Management System (EMS) automates \nthe management of employee data to enhance \nproductivity and accuracy in HR processes.",
    fill="#FFFFFF", font=("CatamaranRoman Black", 16 * -1)
)

canvas3.create_text(
    14.0,
    336.0,
    anchor="nw",
    text="CS-351 Programming Fundamentals (Project)\nGroup Members:\nSyed Ahsan Hassan Rizvi (S.No: 676514)\n43. Shahrukh Khan (S.No: 679023)\nSyed Wasif Ali Rizvi (S.No: 675454)\n68. Syed Farzam Ahmed Warsi (S.No: 677419)\n\n",
    fill="#FFFFFF",
    font=("CatamaranRoman Bold", 16 * -1)
)

canvas3.create_rectangle(
    14.0,
    87.0,
    420.0,
    92.0,
    fill="#FCFCFC",
    outline=""
)

canvas3.create_text(
    556.0,
    47.0,
    anchor="nw",
    text="Add Records",
    fill="#7C0000",
    font=("RobotoRoman Black", 26 * -1)
)

canvas3.create_text(
    470.0,
    129.0,
    anchor="nw",
    text="Enter Employee Details",
    fill="#7C0000",
    font=("RobotoRoman Bold", 16 * -1)
)

Name_label = tk.Label(frame3, text="Name", bg="#FFD6D6", fg="#7C0000", font=("RobotoRoman Bold", 14))
Name_label.place(x=460, y=180)
Name_entry = tk.Entry(frame3, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
Name_entry.place(x=460, y=210, width=321, height=25)

ID_label = tk.Label(frame3, text="Employee ID", bg="#FFD6D6", fg="#7C0000", font=("RobotoRoman Bold", 14))
ID_label.place(x=460, y=240)
ID_entry = tk.Entry(frame3, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
ID_entry.place(x=460, y=270, width=321, height=25)

Dept_label = tk.Label(frame3, text="Department", bg="#FFD6D6", fg="#7C0000", font=("RobotoRoman Bold", 14))
Dept_label.place(x=460, y=300)
Dept_entry = tk.Entry(frame3, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
Dept_entry.place(x=460, y=330, width=321, height=25)

Position_label = tk.Label(frame3, text="Position", bg="#FFD6D6", fg="#7C0000", font=("RobotoRoman Bold", 14))
Position_label.place(x=460, y=360)
Position_entry = tk.Entry(frame3, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
Position_entry.place(x=460, y=390, width=321, height=25)

Salary_label = tk.Label(frame3, text="Salary", bg="#FFD6D6", fg="#7C0000", font=("RobotoRoman Bold", 14))
Salary_label.place(x=460, y=420)
Salary_entry = tk.Entry(frame3, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
Salary_entry.place(x=460, y=450, width=321, height=25)

Save_button_image = tk.PhotoImage(file=relative_to_assets("Add Record Button.png"))
button_save = tk.Button(
    frame3,
    image=Save_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Save button clicked"),
    relief="flat"
)
button_save.place(x=560, y=490, width=180, height=55)

# Show the initial frame
show_frame(frame1)

# Run the application
root.mainloop()
