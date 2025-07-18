# Library User Management System

# Constants
MEMBERSHIP_TYPES = ["basic", "premium", "student"]
STATUS_OPTIONS = ["active", "inactive", "suspended"]

# Global variables
users =[
    {
        'id': 1001,
        'name': "Aamir",
        'email': "amir@gmail.com",
        'phone': "093833",
        'membership_type': "premium",
        'status': 'active'
    },
    {
        'id': 1002,
        'name': 'Hassan',
        'email': 'hasan@gmail.com',
        'phone': '987654',
        'membership_type': 'basic',
        'status': 'inactive'
    },
    {
        'id': 1003,
        'name': 'Maira',
        'email': 'maira@gmail.com',
        'phone': '123456',
        'membership_type': 'student',
        'status': 'active'  
    }
]

next_user_id = 1004 # next: 1005
 



# Functions
# 1
def register_user():
    global next_user_id
    print("== User Registration ==")
    name = input("Enter name: ")
    email = input("Enter email: ") #bilalsaeed@gmail.com
    if "@" not in email:
        print("Invalid email format.")
        return
    phone = input("Enter phone: ")
    if not phone:
        print("Phone number cannot be empty.")
        return
    membership_type = input("Enter membership type (basic/premium/student): ").lower() #Basic --> basic
    if membership_type not in MEMBERSHIP_TYPES:
        print("Invalid membership type.")
        return

# dictionary:: it stores all the detail that were enter by user: n,e,p etcc

    user = { # single item for dictionary
        'id': next_user_id,
        'name': name,
        'email': email,
        'phone': phone,
        'membership_type': membership_type,
        'status': 'active'
    }

    users.append(user)
    print("✓ User registered successfully!")
    print("User ID:", next_user_id)
    next_user_id += 1 # same as: next_user_id = next_user_id + 1



            
#2
def display_all_users():
    print("=== All Registered Users ===")
    if not users:
        print("No users found.")
        return # retunn is used to exit the function if not true 
    for user in users: # f is modifier u can add anything like id=1001, email= aamir@gmail.com so f take the value from user and insert it 
        print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}, Membership: {user['membership_type']}, Status: {user['status']}")

    print("Total users:", len(users)) # len(users) gives the total number of users in the list

#3
def search_user(user_id):
    print("=== Search User ===")
    for user in users:
        if user['id'] == user_id: # input by users If this user's ID is equal to the ID the person typed in
            print(f"ID: {user['id']}\nName: {user['name']}\nEmail: {user['email']}\nPhone: {user['phone']}\nMembership: {user['membership_type']}\nStatus: {user['status']}")
            return
    print("User not found.")

#4 
def update_user_status(user_id, new_status):
    print("=== Update User Status ===")
    if new_status not in STATUS_OPTIONS:
        print("Invalid status option.")
        return
    for user in users:
        if user['id'] == user_id:
            user['status'] = new_status
            print("Status updated successfully.")
            return
    print("User not found.")

# 5


# Main Menu 
while True:
    print("=== Library User Management System ===")
    print("1. Register new user")
    print("2. View all users")
    print("3. Search user by ID")
    print("4. Update user status")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        register_user()

    elif choice == "2":
        display_all_users()

    elif choice == "3":
        user_id = input("Enter user ID to search: ")
        if user_id.isdigit():
            search_user(int(user_id))
        else:
            print("Invalid ID format.")

    elif choice == "4":
        user_id = input("Enter user ID to update: ")
        new_status = input("Enter new status (active/inactive/suspended): ").lower()
        if user_id.isdigit():
            update_user_status(int(user_id), new_status)
        else:
            print("Invalid ID format.")

    elif choice == "5":
        print("Goodbye MF!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
