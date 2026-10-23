# Contact Manager Application (Python Tkinter & MySQL)

A desktop-based Contact Management System built using **Python (Tkinter)** for the graphical user interface and **MySQL** for persistent database storage.

---

## Features
- **Add Contacts:** Save new names and mobile numbers securely to a MySQL database.
- **Edit Contacts:** Update existing contact details easily by selecting them from the list.
- **Delete Contacts:** Remove unwanted contacts with a single click.
- **Persistent Storage:** Data is stored in a local MySQL database so it doesn't disappear when you close the app.
- **Interactive UI:** Clean layout featuring an intuitive table view (Treeview) and form fields.

---

## Prerequisites
Before running the application, make sure you have the following installed:
- Python (3.x recommended)
- MySQL Server running locally
- Python MySQL connector package

You can install the required Python package via terminal:
```bash
pip install mysql-connector-python
Database Setup
Open your MySQL command line client or Workbench and create the database:

SQL
CREATE DATABASE contact_db;
The application will automatically create the required contacts table upon its first successful connection.

How to Run
Clone this repository or download the source code files.

Open Tkinter 2.py and update your MySQL credentials (user and password) to match your local setup:

Python
conn = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="YOUR_PASSWORD", 
    database="contact_db",
)
Run the Python script:

Bash
python "Tkinter 2.py"
Built With
Python (Tkinter, ttk)

MySQL (mysql-connector-python)


---

### Step 2: Push the `README.md` to GitHub

Once you've saved the file in your project folder, open your terminal at `F:\Pycharm main\Tkinter Project` and run these three quick commands to upload it:

```cmd
git add README.md
git commit -m "Add detailed README.md file"
git push
