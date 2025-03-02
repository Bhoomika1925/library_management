# library_management.py

import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(host="localhost", user="root", password="yourpassword", database="library_db")
cursor = conn.cursor()

def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = input("Enter publication year: ")
    
    query = "INSERT INTO books (title, author, year) VALUES (%s, %s, %s)"
    cursor.execute(query, (title, author, year))
    conn.commit()
    print("Book added successfully!")

def view_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    
    if not books:
        print("No books in the library!")
    else:
        print("\nLibrary Books:")
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}")

def delete_book():
    view_books()
    book_id = input("Enter book ID to delete: ")
    
    query = "DELETE FROM books WHERE id = %s"
    cursor.execute(query, (book_id,))
    conn.commit()
    print("Book deleted successfully!")

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Delete Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        delete_book()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")

cursor.close()
conn.close()
