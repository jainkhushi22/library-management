# library management system
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return "'{}' by {} - {}".format(self.title, self.author, status)


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books: list[Book] = []

    def add_book(self, title: str, author: str):
        new_book = Book(title, author)
        self.books.append(new_book)
        print("Book '{}' added to {}.".format(title, self.name))

    def remove_book(self, title: str) :
        for b in self.books:
            if b.title.lower() == title.lower():
                self.books.remove(b)
                print("Book '{}' removed from {}.".format(title, self.name))
                return
        print("Book '{}' not found.".format(title))

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("Books in {}:".format(self.name))
        for b in self.books:
            print(" - {}".format(b))

    def issue_book(self, title: str):
        for b in self.books:
            if b.title.lower() == title.lower():
                if b.is_issued:
                    print("Book '{}' is already issued.".format(b.title))
                else:
                    b.is_issued = True
                    print("You have issued '{}'. Please return it on time.".format(b.title))
                return
        print("Book '{}' not found.".format(title))

    def return_book(self, title: str):
        for b in self.books:
            if b.title.lower() == title.lower():
                if b.is_issued:
                    b.is_issued = False
                    print("Thank you for returning '{}'.".format(b.title))
                else:
                    print("Book '{}' was not issued.".format(b.title))
                return
        print("Book '{}' not found.".format(title))


def menu():
    print("\n========== Library Menu ==========")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Display Books")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")


def main():
    lib = Library("City Library")

    while True:
        try:
            menu()
            choice = int(input("Enter choice (1-6): "))

            match choice:
                case 1:
                    title = input("Enter book title: ").strip()
                    author = input("Enter author name: ").strip()
                    lib.add_book(title, author)

                case 2:
                    title = input("Enter title of the book to remove: ").strip()
                    lib.remove_book(title)

                case 3:
                    lib.display_books()

                case 4:
                    title = input("Enter title of the book to issue: ").strip()
                    lib.issue_book(title)

                case 5:
                    title = input("Enter title of the book to return: ").strip()
                    lib.return_book(title)

                case 6:
                    print("Exiting the Library Management System. Goodbye!")
                    break

                case _:
                    print("Invalid choice. Please select between 1 and 6.")

        except ValueError:
            print("Please enter a valid integer choice.")


if __name__ == "__main__":
    main()
