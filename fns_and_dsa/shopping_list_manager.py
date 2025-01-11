
def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")
    

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        
        # Logic for adding, reving, viewing, and exiting the shopping list
        if choice == "1":
            item = input("Enter name of item: ").strip()
            shopping_list.append(item)
        
        elif choice == "2":
            item = input("Enter name of item: ").strip()
            shopping_list.remove(item)
        
        elif choice == "3":
            print(shopping_list)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()