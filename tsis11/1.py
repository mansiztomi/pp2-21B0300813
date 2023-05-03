import csv
import sqlite3

# Connect to database
conn = sqlite3.connect('phonebook.db')
c = conn.cursor()

# Create phonebook table
c.execute('''CREATE TABLE IF NOT EXISTS phonebook (
                id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT,
                phone_number TEXT NOT NULL,
                email TEXT,
                address TEXT
            )''')

# Function to add contact
def add_contact(first_name, last_name, phone_number, email, address):
    c.execute("INSERT INTO phonebook (first_name, last_name, phone_number, email, address) VALUES (?, ?, ?, ?, ?)",
              (first_name, last_name, phone_number, email, address))
    conn.commit()

# Function to search contact
def search_contact(pattern):
    c.execute("SELECT * FROM phonebook WHERE first_name LIKE ? OR last_name LIKE ? OR phone_number LIKE ?",
              (f"%{pattern}%", f"%{pattern}%", f"%{pattern}%"))
    rows = c.fetchall()
    if rows:
        return rows
    else:
        return "Contact not found"

# Function to print phonebook
def print_phonebook(limit, offset):
    c.execute("SELECT * FROM phonebook LIMIT ? OFFSET ?", (limit, offset))
    rows = c.fetchall()
    print("Phonebook:")
    for row in rows:
        print(row)

# Function to update contact
def update_contact_by_name(first_name, last_name, phone_number):
    c.execute("UPDATE phonebook SET phone_number = ? WHERE first_name = ? AND last_name = ?",
              (phone_number, first_name, last_name))
    conn.commit()

# Procedure to insert new user or update phone if user already exists
def insert_or_update_user(first_name, last_name, phone_number):
    c.execute("SELECT id FROM phonebook WHERE first_name = ? AND last_name = ?", (first_name, last_name))
    row = c.fetchone()
    if row:
        c.execute("UPDATE phonebook SET phone_number = ? WHERE id = ?", (phone_number, row[0]))
        print("User already exists, phone number updated.")
    else:
        add_contact(first_name, last_name, phone_number, "", "")

# Procedure to insert many new users by list of name and phone
def insert_many_users(data):
    incorrect_data = []
    for d in data:
        if not isinstance(d, tuple) or len(d) != 2 or not isinstance(d[0], str) or not isinstance(d[1], str):
            incorrect_data.append(d)
            continue
        if not d[1].isdigit():
            incorrect_data.append(d)
            continue
        add_contact(d[0], "", d[1], "", "")
    return incorrect_data

# Function to query data from the tables with pagination
def query_with_pagination(limit, offset):
    c.execute("SELECT COUNT(*) FROM phonebook")
    total_rows = c.fetchone()[0]
    c.execute("SELECT * FROM phonebook LIMIT ? OFFSET ?", (limit, offset))
    rows = c.fetchall()
    return rows, total_rows

# Procedure to delete contact by username or phone
def delete_contact(name_or_phone):
    c.execute("DELETE FROM phonebook WHERE first_name = ? OR phone_number = ?", (name_or_phone, name_or_phone))
    conn.commit()

# Upload data from CSV file
with open('phonebook_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        add_contact(row['first_name'], row['last_name'], row['phone_number'], row['']