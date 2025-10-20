def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# def display_items(shopping_list):
#     return f"Current items: {', '.join(shopping_list)}"

display_items = lambda shopping_list : f"Current items: {', '.join(shopping_list)}"

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            items = input("Enter the item to add: ")
            items = [item.strip().title() for item in items.split(",")]
            shopping_list.extend(items)
            print(f"{', '.join(items)} added!")
            print(display_items(shopping_list))        
        elif choice == '2':
            item = input("Please enter the item you want to remove: ").title()
            if item not in shopping_list:
                print(f"{item} not in shopping list. ", display_items(shopping_list))
            else:
                shopping_list.remove(item)
                print(f"{item} removed!!!")
                print(display_items(shopping_list))
        elif choice == '3':
            print(display_items(shopping_list))
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()