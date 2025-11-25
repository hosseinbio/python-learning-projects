# Shopping List Manager

A simple command-line application in Python for managing a personal shopping list.

-----

## Description

This script provides a basic interactive command-line interface (CLI) for managing items on a shopping list. The items are stored in a Python **list** (`shopping_list`).

The program runs in a continuous loop until the user chooses to quit, allowing the user to perform the following operations:

  * **Add** a new item to the list.
  * **Delete** an item from the list.
  * **View** the current list of items.
  * **Quit** the application.

Each item added is automatically numbered.

-----

## How to Run

You need **Python 3** (recommended) to execute this script.

**1. Save the Code:**
Save the provided code in a file, for example, `shopping_list_manager.py`.

**2. Execute the Program:**
Open your terminal or command prompt, navigate to the file's location, and run:

```bash
python shopping_list_manager.py
```

-----

## Features and Usage

Upon starting, the program displays a welcome message and a menu of options. You interact with the program by typing the corresponding number and pressing Enter.

| Option | Command | Description |
| :---: | :---: | :--- |
| **1** | **Add item** | Prompts for an item's name. It checks if the item is already on the list (case-insensitive) and adds it if it's new. |
| **2** | **Delete item** | Prompts for an item's name and removes the corresponding item from the list. |
| **3** | **View list** | Prints all items currently in the shopping list. |
| **4** | **Quit the program** | Exits the application. |

### **Example Interaction**

```
Hello!
Welcome to shopping list manager!
To add item to your list press 1
To delete an item from your list press 2
To view your shopping list press 3
And to quit the program press 4
Choose your number: 1
Type your item's name: milk
Item added to your list successfully!
Choose your number: 1
Type your item's name: eggs
Item added to your list successfully!
Choose your number: 3
['1. milk', '2. eggs']
Choose your number: 2
Type your item's name: milk
Item deleted successfully!
No item with such name found!  <-- Note: This 'No item found' message is displayed incorrectly by the current code if the item is not found in *subsequent* list elements.
Choose your number: 4
Have a nice day!
```

-----

## Note on Deletion Logic

Be aware that the deletion logic (Option 2) in the current code will print **"No item with such name found\!"** for every item remaining in the list **after** the requested item is deleted. This behavior is due to how the `for` loop is currently implemented to check for the item.
