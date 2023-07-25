import tkinter
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

def main_window(username):
    def submit_data():
        studentnumber = student_number_entry.get()
        fullname = full_name_entry.get()
        gender = gender_combobox.get()
        age = age_spinbox.get()
        nationality = nationality_combobox.get()
        insurance = Insurance_combobox.get()
        treatment = treatment_entry.get()  # Get the treatment value from the Entry widget

        print("Student Number:", studentnumber)
        print("Full Name:", fullname)
        print("Gender:", gender)
        print("Age:", age)
        print("Nationality:", nationality)
        print("Medical Insurance:", insurance)
        print("Treatment:", treatment)

        insertData(studentnumber, fullname, gender, age, nationality, insurance, treatment)

    def insertData(student_number, full_name, gender, age, nationality, insurance, treatment):
        # Prepare the SQL query to insert data into the database
        sql = "INSERT INTO student_information (student_number, full_name, Gender, Age, Nationality, Insurance, Treatment) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (student_number, full_name, gender, age, nationality, insurance, treatment)

        try:
            # Execute the SQL query
            mycursor.execute(sql, values)
            mydb.commit()
            messagebox.showinfo("Success", "Data inserted successfully!")
        except mysql.connector.Error as err:
            print("Error:", err)
            messagebox.showerror("Error", "Error occurred while inserting data.")
            mydb.rollback()

    window = tkinter.Tk()
    window.title("Student clinic Attendance FORM")
    frame = tkinter.Frame(window)
    frame.pack()

    # saving student information

    student_information_frame = tkinter.LabelFrame(frame, text="student information")
    student_information_frame.grid(row=0, column=0, padx=20, pady=10)

    first_name_label = tkinter.Label(student_information_frame, text="Student Number")
    first_name_label.grid(row=0, column=0)

    last_name_label = tkinter.Label(student_information_frame, text="Full Name")
    last_name_label.grid(row=0, column=1)

    student_number_entry = tkinter.Entry(student_information_frame)
    full_name_entry = tkinter.Entry(student_information_frame)
    student_number_entry.grid(row=1, column=0)
    full_name_entry.grid(row=1, column=1)

    gender_label = tkinter.Label(student_information_frame, text="gender")
    gender_combobox = ttk.Combobox(student_information_frame, values=["Male", "Female", ])
    gender_label.grid(row=0, column=2)
    gender_combobox.grid(row=1, column=2)

    age_label = tkinter.Label(student_information_frame, text="age")
    age_spinbox = tkinter.Spinbox(student_information_frame)
    age_label.grid(row=3, column=0)
    age_spinbox.grid(row=4, column=0)

    nationality_label = tkinter.Label(student_information_frame, text="Nationality")
    nationality_combobox = ttk.Combobox(student_information_frame,
                                        values=["Kenyan", "Ugandan", "Asian", "Tanzanian", "Australian", "Congolese"])
    nationality_label.grid(row=3, column=1)
    nationality_combobox.grid(row=4, column=1)

    Insurance = tkinter.Label(student_information_frame, text="Medical Insurance")
    Insurance_combobox = ttk.Combobox(student_information_frame, values=["YES", "NO"])
    Insurance.grid(row=3, column=2)
    Insurance_combobox.grid(row=4, column=2)

    for widget in student_information_frame.winfo_children():
        widget.grid(padx=10, pady=5)

    # courses registration information
    course_frame = tkinter.LabelFrame(frame)
    course_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

    registered_label = tkinter.Label(course_frame, text="Registration Status")
    registered_check = tkinter.Checkbutton(course_frame, text="Currently Registered")
    registered_label.grid(row=0, column=0)
    registered_check.grid(row=1, column=0)

    semesters_label = tkinter.Label(course_frame, text="Semester")
    semesters_spinbox = tkinter.Spinbox(course_frame, from_=1, to=8)
    semesters_label.grid(row=0, column=1)
    semesters_spinbox.grid(row=1, column=1)

    treatment_label = tkinter.Label(course_frame, text="Treatment")
    treatment_entry = tkinter.Spinbox(course_frame, from_=1, to=8)
    treatment_label.grid(row=0, column=2)
    treatment_entry.grid(row=1, column=2)

    for widget in course_frame.winfo_children():
        widget.grid(padx=10, pady=5)

    # Accept terms
    terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
    terms_frame.grid(row=2, column=0, sticky="new", padx=20, pady=20)

    accept_terms = tkinter.Checkbutton(terms_frame, text="Accept terms & Conditions")
    accept_terms.grid(row=0, column=0)

    # Enter data
    button = tkinter.Button(frame, text="submit data", command=submit_data)
    button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

    window.mainloop()

    if __name__ == "__main__":
        main_window("Test User")
