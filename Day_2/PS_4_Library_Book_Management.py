# Library Book Management (Using Dictionaries)

dict = {}
while True:
    print("----- Welcome to our library ------")
    choice = int(input("\nWhat you want to do?\n1. Add new book\n2. Display all books\n3. Retrieve book data\n4. Remove a book\n5. Exit\nEnter your choice: "))

    if choice == 1:
        Book_no = int(input("Enter the number of books you want to add : "))
        for i in range(1, Book_no+1):
            book_id = input("Enter the book id : ")
            book_title = input("Enter the title of the book : ")
            dict[i] = {"Book ID":book_id, "Book Title":book_title}
        print("Books added successfully!")

    elif choice == 2:
        print("\nThe list of all the available books is :")
        for i,j in dict.items():
            print(i,j)

    elif choice == 3:
        retrieve = int(input("\nEnter the book number to retrieve the data : "))
        print(dict[retrieve])

    elif choice == 4:
        remove = int(input("\nEnter the book number to remove the data : "))
        dict.pop(remove)
        print("Book removed successfully!") 

    elif choice == 5:
        print("Exiting...")
        break
