# f = open("notes.txt","w")
# f.close()

# while True:
#     # show menu
#     choice = input("Choose an option: ")

#     if choice == "1":
#         # ask for a note, then append it to notes.txt
#         ...
#     elif choice == "2":
#         # open notes.txt in read mode and display its contents
#         # handle FileNotFoundError if it doesn't exist
#         ...
#     elif choice == "3":
#         break
#     else:
#         print("Invalid choice. Try again.")



f = open("notes.txt", "w")
f.close()

while True:
    print("\n--- Notes App ---")
    print("1. Add a Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        note = input("Enter your note: ")

        f = open("notes.txt", "a")
        f.write(note + "\n")
        f.close()

        print("Note saved successfully!")

    elif choice == "2":
        try:
            f = open("notes.txt", "r")
            content = f.read()
            f.close()

            print("\nYour Notes:")
            print(content)

        except FileNotFoundError:
            print("Notes file not found!")

    elif choice == "3":
        print("Exiting Notes App. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
