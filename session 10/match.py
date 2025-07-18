print("=== Library User Management System ===")
print("1. Register new user")
print("2. View all users")
print("3. Search user by ID")
print("4. Update user status")
print("5. Exit")


choice = input("Enter your choice (1-5): ")

# if choice == "1":
#     print("You chose Option 1")

# elif choice == "2":
#     print("You chose Option 2")

# elif choice == "3":
#     print("You chose Option 3")

# elif choice == "4":
#     print("You chose Option 4")

# elif choice == "5":
#     print("You chose Option 5")

# Programming concept: switch ===> match (in python)

match choice:
    case "1":
        print("You chose Option 1")
    case "2":
        print("You chose Option 2")
    case "3":
        print("You chose Option 3")
    case "4":
        print("You chose Option 4")
    case "5":
        print("You chose Option 5")


