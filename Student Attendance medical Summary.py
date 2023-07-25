import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kimutai",
    port="3306",
    database='python'
)
mycursor = mydb.cursor()

style = ttk.Style()
style.theme_use("clam")  # You can use different themes like "clam", "default", etc.

# Change the background color of the header (column names) and even rows
style.configure("Treeview.Heading", background="#1f3a93", foreground="white", font=("Arial", 10, "bold"))
style.configure("Treeview", background="white", foreground="#1f3a93", font=("Arial", 10))

# Adjust the row height
style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])  # Adjust row height automatically

def populate_table():
    mycursor.execute("SELECT student_number, full_name, Gender, Age, Nationality, Insurance, Treatment, no_of_Visits FROM student_information")
    data = mycursor.fetchall()

    # Clear the existing table data
    for row in table.get_children():
        table.delete(row)

    # Insert new data into the table
    for entry in data:
        table.insert("", "end", values=entry)

# Create the main Tkinter window
window = tk.Tk()
window.title("Student Information Table")

# Create a Treeview widget to display the table
table = ttk.Treeview(window, columns=("Student Number", "Full Name", "Gender", "Age", "Nationality", "Insurance", "Treatment", "Number of Visits"), show="headings")
table.heading("Student Number", text="Student Number")
table.heading("Full Name", text="Full Name")
table.heading("Gender", text="Gender")
table.heading("Age", text="Age")
table.heading("Nationality", text="Nationality")
table.heading("Insurance", text="Insurance")
table.heading("Treatment", text="Treatment")  # Add Treatment column heading
table.heading("Number of Visits", text="Number of Visits")  # Add Number of Visits column heading
table.pack()

# Populate the table with data from the database
populate_table()

# Add a button to refresh the table (in case new data is added)
btn_refresh = tk.Button(window, text="Refresh", command=populate_table)
btn_refresh.pack()

window.mainloop()
