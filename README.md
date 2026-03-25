# Python Inventory Management System

A simple command-line inventory management system built as a Python fundamentals assignment.
Allows users to add, view, update, and remove products, with data saved to a local text file.

---

## How to Run

```bash
python isabella_coursework1.py
```

No external libraries needed.

---

## Features

- Variables and data types (str, int, float, dict)
- User input with `input()` and formatted display with f-strings
- List (categories), Tuple (brand), Set (product IDs)
- Menu loop with `while` and `if/elif/else`
- Functions: `add_item()`, `view_inventory()`, `update_item()`, `remove_item()`
- OOP: `Product` class and `PerishableProduct` subclass with inheritance
- File handling: saves to `inventory.txt`, loads on startup
- Bonus: error handling with `try/except`

---

## Limitations

- Duplicate product names are allowed
- No support for editing a product's name or category after creation
