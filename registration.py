import tkinter
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

from main import main_window

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kimutai",
    port="3306",
    database='python'
)
mycursor = mydb.cursor()

window = tkinter.Tk()
window.title("University Clinic Login and Registration")
window.geometry("400x300")
frame = tkinter.Frame(window)
frame.pack()


def register():
    username = entry_username.get()
    password = entry_password.get()

    # Check if the username or password fields are empty
    if not username or not password:
        messagebox.showerror("Error", "Username and password are required.")
        return

    # Check if the username already exists in the database

    mycursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    if mycursor.fetchone():
        messagebox.showerror("Error", "Username already exists. Please choose a different username.")
        return

    # Insert the new user data into the database
    insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    mycursor.execute(insert_query, (username, password))
    mydb.commit()

    messagebox.showinfo("Success", "Registration successful. You can now log in.")


def login():
    username = entry_username.get()
    password = entry_password.get()

    # Check if the username or password fields are empty
    if not username or not password:
        messagebox.showerror("Error", "Username and password are required.")
        return

    # Check if the provided login credentials exist in the database
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("Success", "Login successful. Welcome, {}!".format(username))
        window.destroy()  # Close the login window
        main_window(username)  # Open the main window with the logged-in username
    else:
        messagebox.showerror("Error", "Invalid login credentials. Please try again.")

# Create labels, entry fields, and buttons here
label_username = tkinter.Label(window, text="Username:")
label_username.pack()
entry_username = tkinter.Entry(window)
entry_username.pack()

label_password = tkinter.Label(window, text="Password:")
label_password.pack()
entry_password = tkinter.Entry(window, show="*")  # Masking password with '*'
entry_password.pack()

btn_register = tkinter.Button(window, text="Register", command=register)
btn_register.pack()

btn_login = tkinter.Button(window, text="Login", command=login)
btn_login.pack()

window.mainloop()
