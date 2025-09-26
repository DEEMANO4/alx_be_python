




def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
                item_name = input("What is your item name?")
                shopping_list.append(item_name)
                pass
            # Prompt for and add an item
        elif choice == '2':
            item_to_remove = input("What is your item name?")
            if item_to_remove in shopping_list:
                 shopping_list.remove(item_name)
            else:
                 print("item not found.")
            pass
        
                 
            # Prompt for and remove an item
            
        elif choice == '3':
            for item in shopping_list:
                print(item)
            pass
            # Display the shopping list
            
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
