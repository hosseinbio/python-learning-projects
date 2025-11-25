print("Hello!")
print("Welcome to shopping list manager!")
print("To add item to your list press 1")
print("To delete an item from your list press 2")
print("To view your shopping list press 3")
print("And to quit the program press 4")

shopping_list = []
counter = 0
choice = 0

while choice != 4:
    try:
        choice = int(input("Choose your number: "))
    except Exception:
        print("Wrong input!")

    if choice == 1:
        new_item = input("Type your item's name: ").lower()
        if new_item in shopping_list:
            print("This item was added to your list!")
        else:
            counter += 1
            shopping_list.append(f"{counter}. {new_item}")
            print("Item added to your list successfully!")

    elif choice == 2:
        item = input("Type your item's name: ").lower()
        for x in shopping_list:
            if item in x:
                shopping_list.remove(x)
                print("Item deleted successfully!")
            else:
                print("No item with such name found!")

    elif choice == 3:
        if shopping_list == []:
            print("Your shopping list is empty!")
        else:
            print(shopping_list)

    elif choice == 4:
        print("Have a nice day!")
        break

    else:
        print("Wrong input!")
