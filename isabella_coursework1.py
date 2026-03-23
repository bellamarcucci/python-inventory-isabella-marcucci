inventory = {
    101: {"name": "Laptop",   "quantity": 5,  "price": 799.99, "category": "Electronics", "brand": "Dell"},
    102: {"name": "Mouse", "quantity": 20, "price": 35.99,   "category": "Office",      "brand": "Logitech"},
    103: {"name": "Bed Frame",    "quantity": 10, "price": 229.99,   "category": "Home",        "brand": "Ikea"},
}
 
categories = ["Electronics", "Home", "Office", "Food", "Clothing"]
 
product_ids = {101, 102, 103}
 
next_id = 104
 
FILE_NAME = "inventory.txt"
 
print("=== Sample Inventory Data ===")
for pid, item in inventory.items():
    print(f"ID: {pid} | Name: {item['name']} | Qty: {item['quantity']} | Price: ${item['price']:.2f} | Category: {item['category']}")
 
print(f"\nCategories available: {categories}")
print(f"Registered IDs (set): {product_ids}")
print(f"Next ID to assign: {next_id}")