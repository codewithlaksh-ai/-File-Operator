import os 
from datetime import datetime

class JournalManager:

    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self):
        try:
            entry = input("Enter your journal entry: \n").strip()
            if entry == "":
                print("Entry cannot be empty. ")
                return

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            journal_entry = f"[{timestamp}] {entry}\n"

            with open(self.filename,"a") as file:
                file.write(journal_entry)

            print("Entry added successfully.")

        except PermissionError:
            print("Error: Permission denied. Cannot write to the file.")

        except OSError as e:
            print("File error:", e)

    def view_entries(self):
        try:
            with open(self.filename,"r") as file:
                content = file.read()

            if content.strip() == "":
                print("Journal is empty. ")
            else:
                print("\n========== JOURNAL ENTRIES ==========")
                print(content)
                print("=====================================")

        except FileNotFoundError:
            print("No journal found. Add an entry first.")
        except PermissionError:
            print("Error: Permission denied. Cannot read the file.")
        except OSError as e:
            print("File error:", e)

    def search_entry(self):
        keyword = input("Enter keyword or date to search: ").strip()

        if keyword == "":
            print("Search keyword cannot be empty.")
            return
        try:
            with open(self.filename,"r") as file:
                entries = file.readlines()
            found = False
            print("\n========== SEARCH RESULTS ==========")
            for entry in entries:
                if keyword.lower() in entry.lower():
                    print(entry.strip())
                    found = True

            if not found:
                print("No matching entry found. ")

            print("==========================================")

        except FileNotFoundError:
            print("No journal found. Add an entry first.")
        except PermissionError:
            print("Error: Permission denied. Cannot read the file.")
        except OSError as e:
            print("File error:", e)

    def delete_entries(self):
        if not os.path.exists(self.filename):
            print("Journal file does not exist. ")
            return

        confirmation = input("Are you sure you want to delete all entries? (yes/no): ").strip().lower()

        if confirmation != "yes":
            print("Delete operation cancelled.")
            return

        try:
            os.remove(self.filename)
            print("All journal entries have been deleted.")

        except PermissionError:
            print("Error: Permission denied. Cannot delete journal entries.")
        except OSError as e:
            print("File error:", e)

    def create_new_file(self):
        try:
            with open(self.filename,"x"):
                pass

            print("New journal file created successfully. ")

        except FileExistsError:
            print("Journal file already exists.")

        except PermissionError:
            print("Error: Permission denied.")

        except OSError as e:
            print("File error:", e)

journal = JournalManager()

while True:


    print("\n========== PERSONAL JOURNAL ==========")
    print("Welcome to Personal Journal Manager! ")
    print("Please select an option: \n")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Create Journal File")
    print("6. Exit")
    print("======================================")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            journal.add_entry()

        elif choice == 2:
            journal.view_entries()

        elif choice == 3:
            journal.search_entry()

        elif choice == 4:
            journal.delete_entries()

        elif choice == 5:
            journal.create_new_file()

        elif choice == 6:
            print("Thank you for using Personal Journal.")
            break

        else:
            print("Invalid choice. Please select 1 to 6.")

    except ValueError:
        print("Invalid input. Please enter a number from 1 to 6.")

    except KeyboardInterrupt:
        print("\nProgram interrupted. Goodbye!")
        break  

    