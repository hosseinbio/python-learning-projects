print("To add new contact press 1")
print("To delete an existing contact press 2")
print("To search contacts press 3")
print("To view contacts press 4")
print("And to quit the program press 5")

contacts = dict()

while True:
    choice = 0

    try:
        choice = int(input("Press your number: "))
    except Exception:
        print("Wrong input!")

    if choice != 0:
        if choice == 1:
            name = input("Type your contact's name: ")
            if name in contacts.keys():
                print("This name exist in your contact book")
                print("Would you like to change the contact's number?")
                print("y: Yes")
                print("n: No")
                answer = input("Please choose: ").lower()
                while answer != "y" and answer != "n":
                    print("Wrong input!")
                    answer = input("Please choose: ").lower()
                if answer == "n":
                    pass
                if answer == "y":
                    try:
                        number = str(input("Type the new number: "))
                    except Exception:
                        print("Wrong input!")
                    else:
                        contacts.update({name: number})
            else:
                try:
                    number = str(input("Type the new number: "))
                except Exception:
                    print("Wrong input!")
                else:
                    contacts.update({name: number})

        elif choice == 2:
            name = input("Type your contact's name: ")
            if name in contacts.keys():
                contacts.pop(name)
            else:
                print("Contact not found!")

        elif choice == 3:
            name = input("Type your contact's name: ")
            searched = contacts.get(name)
            if searched is None:
                print("Contact not found!")
            else:
                print(searched)

        elif choice == 4:
            if contacts == {}:
                print("You don't have any contacts!")
            else:
                for name in sorted(contacts):
                    print(name, contacts.get(name))

        elif choice == 5:
            break

        else:
            print("Wrong input!")
