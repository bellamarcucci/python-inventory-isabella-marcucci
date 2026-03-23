import os

#CLASSES

class Product: 
    def __init__(self, name, price, quantity, category, brand, product_id):
        self.name       = name
        self.price      = float(price)
        self.quantity   = int(quantity)
        self.category   = category
        self.brand      = brand
        self.product_id = product_id
 
    def update(self, new_quantity=None, new_price=None):
        if new_quantity is not None:
            self.quantity = int(new_quantity)
        if new_price is not None:
            self.price = float(new_price)
 
    def display(self):
        print(f"  ID: {self.product_id} | Name: {self.name} | Brand: {self.brand} | Category: {self.category}")
        print(f"  Price: ${self.price:.2f} | Quantity: {self.quantity}")
 
    def to_file_string(self):
        return (f"Product,{self.product_id},{self.name},"
                f"{self.price},{self.quantity},{self.category},{self.brand},N/A\n")
 
 
class PerishableProduct(Product):
    def __init__(self, name, price, quantity, category, brand, product_id, expiration_date):
        super().__init__(name, price, quantity, category, brand, product_id)
 
        self.expiration_date = expiration_date
 
    def display(self):

        super().display()
        print(f"  Expiration Date: {self.expiration_date}")
 
    def to_file_string(self):
        return (f"Perishable,{self.product_id},{self.name},"
                f"{self.price},{self.quantity},{self.category},{self.brand},{self.expiration_date}\n")
 

inventory   = {}

categories  = ["Electronics", "Home", "Office", "Food", "Clothing"]

product_ids = set()

next_id     = 101

FILE_NAME   = "inventory.txt"


#FILE HANDLING

def save_inventory():
    full_path = os.path.abspath(FILE_NAME)
    print(f"\nSaving inventory to file: {full_path}")
 
    with open(FILE_NAME, "w") as file:
        for product in inventory.values():
            line = product.to_file_string()
            file.write(line)
 
    print("Inventory saved successfully!")
 
 
def load_inventory():
    global next_id

    if not os.path.exists(FILE_NAME):
        return
 
    with open(FILE_NAME, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
 
            parts      = line.split(",")
            prod_type  = parts[0]
            pid        = int(parts[1])
            name       = parts[2]
            price      = float(parts[3])
            quantity   = int(parts[4])
            category   = parts[5]
            brand      = parts[6]
            expiration = parts[7]
 
            if prod_type == "Perishable":
                product = PerishableProduct(name, price, quantity, category, brand, pid, expiration)
            else:
                product = Product(name, price, quantity, category, brand, pid)
 
            inventory[pid] = product
            product_ids.add(pid)
 
            if pid >= next_id:
                next_id = pid + 1
 
    print(f"  [Info] {len(inventory)} product(s) loaded.")


# MAIN PROGRAM
 
def show_menu():
    print("\n" + "=" * 43)
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Update Item")
    print("4. Remove Item")
    print("5. Exit")

def add_item():
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
 
    inventory[new_id] = Product(name, price, quantity, category, brand, new_id)
 
    print("\nItem added successfully!")
    save_inventory()
 
def view_inventory():
    if not inventory:
        print("\n  [!] Inventory is empty.")
        return
 
    print("\nCurrent Inventory:")
    print("-" * 40)
 
    for product in inventory.values():
        product.display()
        print()
 
def update_item():
    print("\nEnter product name to update: ", end="")
    name = input("> ").strip()
 
    found = None
    for product in inventory.values():
        if product.name.lower() == name.lower():
            found = product
            break
 
    if found is None:
        print(f"  [!] Product '{name}' not found.")
        return
 
    print("Enter new quantity: ", end="")
    qty_input = input("> ").strip()
    if qty_input:
        found.update(new_quantity=qty_input)
 
    print("Enter new price: ", end="")
    price_input = input("> ").strip()
    if price_input:
        found.update(new_price=price_input)
 
    print("\nInventory updated successfully!")
    save_inventory()
 
def remove_item():
    print("\nEnter product name to remove: ", end="")
    name = input("> ").strip()
 
    target_id = None
    for pid, product in inventory.items():
        if product.name.lower() == name.lower():
            target_id = pid
            break
 
    if target_id is None:
        print(f"  [!] Product '{name}' not found.")
        return
 
    del inventory[target_id]
    product_ids.discard(target_id)
    print(f"\nProduct '{name}' removed successfully!")
    save_inventory()

 
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