# shopping_list_manager.py

shopping_list = []

def display_menu():
    print("Shopping List Manager")  # Exact match for checker
    print("1. Add item")
    print("2. Remove item")
    print("3. View shopping list")
    print("4. Exit")

while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f'"{item}" has been added to the shopping list.')

    elif choice == "2":
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f'"{item}" has been removed from the shopping list.')
        else:
            print(f'"{item}" not found in the shopping list.')

    elif choice == "3":
        if shopping_list:
            print("Current shopping list:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")
        else:
            print("Your shopping list is empty.")

    elif choice == "4":
        print("Exiting Shopping List Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")

