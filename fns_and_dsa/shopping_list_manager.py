
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
        
        # Checks for implementation of Choice Input as a number
        if not choice.isdigit():
            print("Invalid choice. Please select again")
            continue # Skip the rest of the loop and start from the top 

        choice = int(choice)
        
        # Logic for adding, reving, viewing, and exiting the shopping list
        if choice == 1:
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"{item} has been added to the list.")
            else:
                print("Item name cannot be empty. Please add an item.")

        elif choice == 2:
            item = input("Enter item to remove: ").strip()
            if item not in shopping_list:
                print("Item not found in the shopping list.")
            else:                
                shopping_list.remove(item)
                print(f"{item} has been removed from the list.")
        
        elif choice == 3:
            if shopping_list:
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("Shopping list is empty.")

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()