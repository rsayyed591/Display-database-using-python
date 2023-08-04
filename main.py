import tkinter as tk
from tkinter import ttk
import mysql.connector

def showData():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="student"
    )
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Info")
    rows = cursor.fetchall()

    conn.close()

    result_window = tk.Toplevel(root)
    result_window.title("Data")

    # Creating a Treeview widget
    tree = ttk.Treeview(result_window)

    # Define columns
    tree["columns"] = ("ID", "Name", "Phone No.", "Gender", "Email")

    # Format columns
    tree.column("#0", width=0, stretch=tk.NO)  # Hide the default first column
    tree.column("ID", anchor=tk.CENTER, width=50)
    tree.column("Name", anchor=tk.CENTER, width=100)
    tree.column("Phone No.", anchor=tk.CENTER, width=100)
    tree.column("Gender", anchor=tk.CENTER, width=50)
    tree.column("Email", anchor=tk.CENTER, width=150)

    # Create headings
    tree.heading("#0", text="", anchor=tk.CENTER)
    tree.heading("ID", text="ID", anchor=tk.CENTER)
    tree.heading("Name", text="Name", anchor=tk.CENTER)
    tree.heading("Phone No.", text="Phone No.", anchor=tk.CENTER)
    tree.heading("Gender", text="Gender", anchor=tk.CENTER)
    tree.heading("Email", text="Email", anchor=tk.CENTER)

    tree.pack(fill="both", expand=True)

    # Insert data into the table
    for row in rows:
        tree.insert("", tk.END, values=row)

root = tk.Tk()
root.title("Show Data of the table")
root.geometry("420x420")

showButton = tk.Button(root, text="Show Data", command=showData)
showButton.pack()

root.mainloop()
