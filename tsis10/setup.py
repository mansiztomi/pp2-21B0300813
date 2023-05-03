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
def search_contact(name):
    c.execute("SELECT * FROM phonebook WHERE first_name = ?", (name,))
    rows = c.fetchall()
    if rows:
        return rows
    else:
        return "Contact not found"

# Function to print phonebook
def print_phonebook():
    c.execute("SELECT * FROM phonebook")
    rows = c.fetchall()
    print("Phonebook:")
    for row in rows:
        print(row)

# Function to update contact
def update_contact(user_id, field, new_value):
    c.execute(f"UPDATE phonebook SET {field} = ? WHERE id = ?", (new_value, user_id))
    conn.commit()

# Function to delete contact
def delete_contact(user_id):
    c.execute("DELETE FROM phonebook WHERE id = ?", (user_id,))
    conn.commit()

# Upload data from CSV file
with open('phonebook_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        add_contact(row['first_name'], row['last_name'], row['phone_number'], row['email'], row['address'])

# Prompt user to enter data
while True:
    print("Menu:")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Print phonebook")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        add_contact(first_name, last_name, phone_number, email, address)
    elif choice == 2:
        name = input("Enter name to search: ")
        result = search_contact(name)
        if result == "Contact not found":
            print(result)
        else:
            for row in result:
                print(row)
    elif choice == 3:
        print_phonebook()
    elif choice == 4:
        user_id = input("Enter user ID to update: ")
        field = input("Enter field to update (first_name or phone_number): ")
        new_value = input("Enter new value: ")
        update_contact(user_id, field, new_value)
    elif choice == 5:
        user_id = input("Enter user ID to delete: ")
        delete_contact(user_id)
    elif choice == 6:
        break
    else:
        print("Invalid choice")

# Close connection
conn.close()