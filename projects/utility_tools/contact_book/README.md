# Contact Book Manager

A simple command-line application in Python for managing a contact list using a dictionary.

-----

## Description

This script provides a basic interactive command-line interface (CLI) for managing contacts. Contacts are stored in a Python **dictionary**, where the **contact's name** acts as the key and the **phone number** is the corresponding value.

The program runs in a loop, allowing the user to perform several operations:

  * **Add** a new contact.
  * **Delete** an existing contact.
  * **Search** for a contact's number by name.
  * **View** all saved contacts (sorted by name).
  * **Quit** the application.

-----

## How to Run

You need **Python 3.x** to execute this script.

**1. Save the Code:**
Save the provided code in a file, for example, `contact_manager.py`.

**2. Execute the Program:**
Open your terminal or command prompt, navigate to the file's location, and run:

```bash
python contact_manager.py
```

-----

## Features and Usage

Upon starting, the program displays a menu of options. You interact with the program by typing the corresponding number and pressing Enter.

| Option | Command | Description |
| :---: | :---: | :--- |
| **1** | **Add new contact** | Prompts for a name and number. If the name already exists, it asks the user if they want to update the number. |
| **2** | **Delete existing contact** | Prompts for a name and removes the contact if found. |
| **3** | **Search contacts** | Prompts for a name and displays the number if the contact exists. |
| **4** | **View contacts** | Displays all contacts in the dictionary, sorted alphabetically by name. |
| **5** | **Quit the program** | Exits the application loop. |

### **Example Interaction**

```
To add new contact press 1
To delete an existing contact press 2
To search contacts press 3
To view contacts press 4
And to quit the program press 5
Press your number: 1
Type your contact's name: Hossein
Type the new number: 555-1234
Press your number: 4
Hossein 555-1234
Press your number: 5
```

-----

## Implementation Details

  * **Data Structure:** Contacts are stored in the global dictionary `contacts = dict()`.
  * **Input Handling:** A `try...except` block is used to handle potential `ValueError` if the user enters non-integer input for the main menu choice.
  * **Contact Viewing (Option 4):** The contacts are displayed using a loop that iterates over `sorted(contacts)`, ensuring the output is always alphabetical.
