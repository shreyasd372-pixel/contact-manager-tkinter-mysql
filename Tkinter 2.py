""" GUI Programming in Python using Tkinter with MySQL Database """
import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

# --- Database Connection Setup ---
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="Password",  # Replace with your MySQL password
        database="contact_db",  # Replace with your database name
    )
    cursor = conn.cursor()
except mysql.connector.Error as err:
    messagebox.showerror(
        "Database Error", f"Failed to connect to MySQL server: \n{err}"
    )
    exit()

# Ensure table exists in the database
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS contacts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        phone VARCHAR(50) NOT NULL
    )
"""
)
conn.commit()


# --- Functions ---
def load_contacts():
    """Loads all contacts from the database into the Treeview."""
    for item in contact_table.get_children():
        contact_table.delete(item)

    cursor.execute("SELECT id, name, phone FROM contacts")
    for row in cursor.fetchall():
        # row[0] is the database ID, stored as the item's iid in the Treeview
        contact_table.insert("", tk.END, iid=row[0], values=(row[1], row[2]))


def clear_fields():
    en_name.delete(0, tk.END)
    en_phone.delete(0, tk.END)


def add_contact():
    name = en_name.get().strip()
    phone = en_phone.get().strip()

    if name == "" or phone == "":
        messagebox.showerror("ERROR", "Name and Mobile required")
        return

    # Insert into MySQL Database
    cursor.execute(
        "INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone)
    )
    conn.commit()

    clear_fields()
    load_contacts()
    messagebox.showinfo("Success", "Contact added successfully!")


def delete_contact():
    selected = contact_table.focus()
    if not selected:
        messagebox.showerror("ERROR", "Select a contact")
        return

    cursor.execute("DELETE FROM contacts WHERE id = %s", (selected,))
    conn.commit()

    clear_fields()
    load_contacts()
    messagebox.showinfo("Success", "Contact deleted successfully!")


def edit_contact():
    selected = contact_table.focus()
    if not selected:
        messagebox.showerror("ERROR", "Select a contact")
        return

    name = en_name.get().strip()
    phone = en_phone.get().strip()

    if name == "" or phone == "":
        messagebox.showerror("ERROR", "Name and Mobile required")
        return

    # Update MySQL record
    cursor.execute(
        "UPDATE contacts SET name = %s, phone = %s WHERE id = %s",
        (name, phone, selected),
    )
    conn.commit()

    clear_fields()
    load_contacts()
    messagebox.showinfo("Success", "Contact updated successfully!")


def fill_fields(event):
    selected = contact_table.focus()
    if selected:
        data = contact_table.item(selected, "values")
        clear_fields()
        en_name.insert(0, data[0])
        en_phone.insert(0, data[1])


# --- GUI Setup ---
win = tk.Tk()
win.title("Contact Manager (MySQL)")
win.geometry("700x400")

# Frames
left_frame = tk.Frame(win, bd=3, relief="ridge", padx=20, pady=20)
left_frame.pack(side="left", fill="both", expand=True)

right_frame = tk.Frame(win, bd=3, relief="ridge", padx=20, pady=20)
right_frame.pack(side="right", fill="both", expand=True)

# Left Side Components
tk.Label(
    left_frame, text="Add / Edit Contact", font=("Arial", 14, "bold")
).pack(pady=10)

tk.Label(left_frame, text="Name :").pack(anchor="w")
en_name = tk.Entry(left_frame)
en_name.pack(fill="x", pady=5)

tk.Label(left_frame, text="Mobile Number :").pack(anchor="w")
en_phone = tk.Entry(left_frame)
en_phone.pack(fill="x", pady=5)

# Buttons
tk.Button(left_frame, text="ADD", command=add_contact).pack(fill="x", pady=3)
tk.Button(left_frame, text="EDIT", command=edit_contact).pack(fill="x", pady=3)
tk.Button(left_frame, text="DELETE", command=delete_contact).pack(
    fill="x", pady=3
)
tk.Button(left_frame, text="CLEAR", command=clear_fields).pack(fill="x", pady=3)

# Right Side Components
tk.Label(
    right_frame, text="Saved Contacts", font=("Arial", 14, "bold")
).pack(pady=10)
columns = ("name", "phone")
contact_table = ttk.Treeview(right_frame, columns=columns, show="headings")
contact_table.heading("name", text="Name")
contact_table.heading("phone", text="Mobile Number")
contact_table.column("name", width=150)
contact_table.column("phone", width=150)
contact_table.pack(fill="both", expand=True)

contact_table.bind("<ButtonRelease-1>", fill_fields)

# Load existing data on startup
load_contacts()

win.mainloop()

# Clean up connection on exit
if "conn" in locals() and conn.is_connected():
    cursor.close()
    conn.close()

print("Thank you.")