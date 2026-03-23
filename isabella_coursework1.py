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
    """Adds a new item to the inventory."""
    global next_id
 
    print("\nEnter product name: ", end="")
    name = input("> ").strip()
 
    print(f"Enter category ({', '.join(categories)}): ", end="")
    category = input("> ").strip()
 
    if category not in categories:
        print("  [!] Category not found.")
        category = "Office"
 
    # TUPLE multiples values in one variable
    print("Enter brand name: ", end="")
    brand_tuple = (input("> ").strip(),)
    brand = brand_tuple[0]
 
    print("Enter quantity: ", end="")
    quantity = int(input("> "))
 
    print("Enter price: ", end="")
    price = float(input("> "))
 
    new_id = next_id
    next_id += 1
    product_ids.add(new_id)
 
    inventory[new_id] = {
        "name": name,
        "quantity": quantity,
        "price": price,
        "category": category,
        "brand": brand,
    }
 
    print("\nItem added successfully!")
 
def view_inventory():
    if not inventory:
        print("\n  [!] Inventory is empty.")
        return
 
    print("\nCurrent Inventory:")
    print("-" * 40)
 
    for pid, item in inventory.items():
        print(f"  ID: {pid} | Name: {item['name']} | Brand: {item['brand']} | Category: {item['category']}")
        print(f"  Price: ${item['price']:.2f} | Quantity: {item['quantity']}")
        print()
 
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