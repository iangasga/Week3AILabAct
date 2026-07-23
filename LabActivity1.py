def check_borrowing(overdue_books, status):
    if overdue_books == "yes":
        return "Not allowed: overdue books"
    elif status == "suspended":
        return "Not allowed: suspended account"
    else:
        return "Borrowing allowed"


allowed_students = 0

while True:
    name = input("Enter student name (type 'exit' to stop): ")

    if name.lower() == "exit":
        break

    overdue = input("Do you have overdue books? (yes/no): ").lower()
    status = input("Enter status (active/suspended): ").lower()
    books = int(input("How many books do you want to borrow? "))

    result = check_borrowing(overdue, status)
    print(result)

    if result == "Borrowing allowed":
        if books <= 0:
            print("Error: Please enter at least 1 book.")
        elif books > 3:
            print("Warning: You can only borrow up to 3 books.")
            print("Borrowing approved: 3 books")
            allowed_students += 1
        else:
            print("Borrowing approved:", books, "book(s)")
            allowed_students += 1

    print()

print("Library session ended.")
print("Total students allowed to borrow:", allowed_students)
