import json  # Import the JSON module to work with JSON files
import os   # Import the OS module to check if a file exists

data_file = "library.txt"

def load_library():
    """Loads the library from a JSON file if it exists, otherwise returns an empty list."""
    if os.path.exists(data_file):
        try:
            with open(data_file, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError): # JSONDecodeError is raised when the JSON data is invalid 
            return []
    return []


def save_library(library):
    """Saves the library list to a JSON file."""
    with open(data_file, "w") as file:
        json.dump(library, file, indent=4) # indent=4 for pretty printing , library is the list to be saved


def get_valid_input(prompt):
    """Keeps asking the user for input until a non-empty value is provided."""
    while True:
        value = input(prompt).strip() # strip() removes leading and trailing whitespaces
        if value:
            return value
        print("Input cannot be empty. Please enter a valid value.")


def add_book(library):
    """Adds a new book to the library and saves the updated list."""
    title = get_valid_input("Enter book title: ")
    author = get_valid_input("Enter book author: ")
    year = get_valid_input("Enter book year: ")
    genre = get_valid_input("Enter book genre: ")
    
    read = input("Have you read the book? (yes / no):  ").strip().lower()
    while read not in ["yes", "no"]:
        print("Invalid input. Please enter 'yes' or 'no'.")
        read = input("Have you read the book? (yes / no):  ").strip().lower()
    
    read = read == "yes"

    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    library.append(new_book)
    save_library(library)
    
    print(f"Book '{title}' added successfully.")


def remove_book(library):
    """Removes a book from the library and saves the updated list."""
    title = get_valid_input("Enter book title to remove: ").lower()
    initial_length = len(library)
    
    library[:] = [book for book in library if book["title"].strip().lower() != title]

    if len(library) < initial_length:
        save_library(library)
        print(f"Book '{title}' removed successfully.")
    else:
        print(f"Book '{title}' not found in the library.")


def search_library(library):
    """Searches for a book by title or author."""
    search_by = get_valid_input("Search by title or author?: ").lower()
    
    if search_by not in ["title", "author"]:
        print("Invalid search criteria. Please enter 'title' or 'author'.")
        return
    
    search_term = get_valid_input(f"Enter the {search_by}: ").lower()

    results = [book for book in library if search_term in book[search_by].strip().lower()]


    if results:
        for book in results:
            status = "Read" if book["read"] else "Unread"
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No results found.")


def display_all_books(library):
    """Displays all books in the library."""
    if library:
        for book in library:
            status = "Read" if book["read"] else "Unread"
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("Library is empty.")


def display_statistics(library):
    """Displays the statistics of read/unread books."""
    total_books = len(library)

    if total_books == 0:
        print("No books in the library to display statistics.")
        return


    total_read_books = sum(1 for book in library if book["read"])
    total_unread_books = total_books - total_read_books

    percentage_read = (total_read_books / total_books) * 100 if total_books else 0
    percentage_unread = (total_unread_books / total_books) * 100 if total_books else 0

    print(f"Total books: {total_books}")
    print(f"Total read books: {total_read_books} ({percentage_read:.2f}%)")
    print(f"Total unread books: {total_unread_books} ({percentage_unread:.2f}%)")


def main():
    library = load_library()

    while True:
        print("\nMenu")
        print("1. Add book")
        print("2. Remove book")
        print("3. Search library")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter choice: ").strip()
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_library(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__": # This block of code will only run if the script is executed directly
    main()

