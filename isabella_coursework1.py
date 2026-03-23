inventory = {
    101: {"name": "Laptop",   "quantity": 5,  "price": 799.99, "category": "Electronics", "brand": "Dell"},
}
 
categories = ["Electronics", "Home", "Office", "Food", "Clothing"]
 
product_ids = {101}
 
next_id = 102
 
FILE_NAME = "inventory.txt"
 
def show_menu():
    print("\n" + "=" * 43)
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Update Item")
    print("4. Remove Item")
    print("5. Exit")

def add_item():
    print("Not set yet.")
 
def view_inventory():
    print("Not set yet.")
 
def update_item():
    print("Not set yet.")
 
def remove_item():
    print("Not set yet.")
 
def main():
    print("Welcome to my Inventory Management System!")
    print("=" * 43)
 
   
    while True:
        show_menu()
        print("Select an option: ", end="")
        choice = input("> ").strip()
 
        if choice == "1":
            add_item()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            update_item()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            print("Exiting system. Bye!")
            break
        else:
            print("  [!]ERROR[!] Invalid option. Please select 1-5.")
 
 
if __name__ == "__main__":
    main()