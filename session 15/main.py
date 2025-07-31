from library_mgt_sys import Library, LibraryInterface

# Run the program
if __name__ == "__main__":
    library = Library("City Public Library")
    interface = LibraryInterface(library)
    
 # Initialize with sample data
    print("🏛️  Welcome to the Library Management System!")
    print("Loading sample data...")
    interface.initialize_sample_data()
    
  # Main program loop
    while True:
        interface.display_menu()
        choice = interface.get_user_choice()
        
        if choice == 1:
            interface.add_book_menu()
        
        elif choice == 2:
            interface.add_member_menu()
        
        elif choice == 3:
            interface.borrow_book_menu()
        
        elif choice == 4:
            interface.return_book_menu()
        
        elif choice == 5:
            print("\n--- All Books ---")
            interface.library.display_all_books()
        
        elif choice == 6:
            print("\n--- Available Books ---")
            interface.library.display_available_books()
        
        elif choice == 7:
            interface.display_member_books_menu()
        
        elif choice == 8:
            print("\n--- All Members ---")
            interface.library.display_all_members()
        
        elif choice == 9:
            interface.search_book_menu()
        
        elif choice == 10:
            print("\n👋 Thank you for using the Library Management System!")
            print("Goodbye!")
            break
        
        # Pause before showing menu again
        input("\nPress Enter to continue...")
