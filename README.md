# 📔 Personal Journal Manager

A simple Python-based **Personal Journal Manager** that allows users to create, view, search, and delete journal entries through a menu-driven interface.

The project demonstrates **Object-Oriented Programming (OOP), file handling, exception handling, and Python modules**.

## 📌 Features

* 📝 **Add a New Entry** – Add a journal entry with an automatic date and time.
* 📖 **View All Entries** – Display all saved journal entries.
* 🔍 **Search for an Entry** – Search entries using a keyword or date.
* 🗑️ **Delete All Entries** – Delete the complete journal after confirmation.
* 📄 **Create Journal File** – Create a new journal file without overwriting an existing one.
* 🚪 **Exit** – Safely exit the application.

## 🛠️ Concepts Used

### Object-Oriented Programming

* Class and Object
* Constructor `__init__`
* Instance methods
* Object-based file management

### File Handling

* Reading files
* Writing to files
* Appending data
* Creating new files
* Deleting files

### Exception Handling

* `try-except`
* `FileNotFoundError`
* `FileExistsError`
* `PermissionError`
* `OSError`
* `ValueError`
* `KeyboardInterrupt`

### Python Modules

* `os`
* `datetime`

### Other Python Concepts

* `while` loop
* `for` loop
* `if-elif-else`
* User input
* String methods
* f-strings
* Boolean variables

## 📂 Project Structure

```text
Personal-Journal-Manager/
│
├── journal_manager.py
├── journal.txt
└── README.md
```

## ▶️ How to Run

### 1. Check Python Installation

Make sure Python is installed on your system.

```bash
python --version
```

### 2. Run the Program

Open the terminal in the project folder and run:

```bash
python journal_manager.py
```

The program will display a menu with six options.

## 📋 Menu Options

```text
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Create Journal File
6. Exit
```

## 📷 Sample Output

### Add Entry

```text
========== PERSONAL JOURNAL ==========
Welcome to Personal Journal Manager!
Please select an option:

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Create Journal File
6. Exit
======================================

Enter your choice: 1
Enter your journal entry:
Today I learned Python file handling.

Entry added successfully.
```

### View Entries

```text
========== JOURNAL ENTRIES ==========
[2026-10-08 20:15:30] Today I learned Python file handling.
=====================================
```

### Search Entry

```text
========== SEARCH RESULTS ==========
[2026-10-08 20:15:30] Today I learned Python file handling.
==========================================
```

### Delete Entries

```text
Are you sure you want to delete all entries? (yes/no): yes

All journal entries have been deleted.
```

## 📚 What I Learned

Through this project, I learned:

* How to create a **class and object** in Python
* How to work with text files
* How to read, write, append, and create files
* How to search data inside a file
* How to delete files using the `os` module
* How to add timestamps using `datetime`
* How to handle different types of errors
* How to create a menu-driven application
* How to handle invalid user input
* How to use exception handling effectively

## 🎯 Project Objective

The objective of this project is to build a simple command-line journal application while practicing important Python concepts such as **OOP, file handling, exception handling, loops, conditions, and modules**.

## 👨‍💻 Author

**Laksh Prajapat**

BCA Student | Python & AI/ML Learner

---

⭐ **If you found this project useful, consider giving it a star!**

