import sys
import json


def load_state(filename):
    with open(filename, encoding='UTF-8') as file:
        return json.load(file)


def main_menu():
    menu = [
        'Add an item',
        'View cart',
        'Checkout',
        'Quit'
    ]
    show_menu(menu)
    return get_valid_input(range(len(menu)))


def second_menu(menu):
    show_menu(menu)
    return get_valid_input(range(len(menu)))


def show_menu(menu):
    for index, option in enumerate(menu):
        print(f'({index}) {option}')


def sec_show_menu(items, inventory):
    for index, option in enumerate(items):
        print(f'({index}) {option} ({inventory[option]["description"]}) @ ${inventory[option]["price"]} ({inventory[option]["quantity"]} in stock)')

def get_valid_input(valid_inputs):
    while True:
        response = input('Option: ').strip()
        if not response.isdigit():
            print(f'Invalid option: {response}')
            continue
        response = int(response)
        if response not in valid_inputs:
            print(f'Invalid option: {response}')
            continue

        return response


def save_state(inventory, lights_file):
    with open(lights_file, 'w') as file:
        json.dump(inventory, file)


def add_items(inventory, cart):
    items = get_items(inventory)
    if items != []:
        print()
        print("Which item do you want to add to your cart?")
        sec_show_menu(items, inventory)
        option = get_valid_input(range(len(items)))
        selected_food = items[option]
        if selected_food not in cart:
            cart[selected_food] = 0
        cart[selected_food] += 1
        inventory[selected_food]['quantity'] -= 1
    elif items == []:
        print("No items match that query")


def display_cart(inventory, cart):
    print()
    total = 0
    for item in cart:
        print(f'{item} ({inventory[item]["description"]}) x {cart[item]} @ ${inventory[item]["price"]} = ${float(float(cart[item]) * float(inventory[item]["price"]))}')
        total += float(float(cart[item]) * float(inventory[item]["price"]))
    print(f'  Total: ${total}')


def checkout(inventory, cart, filename):
    print()
    total = 0
    for item in cart:
        print(
            f'{item} ({inventory[item]["description"]}) x {cart[item]} @ ${inventory[item]["price"]} = ${float(float(cart[item]) * float(inventory[item]["price"]))}')
        total += float(float(cart[item]) * float(inventory[item]["price"]))
    print(f'  Total: ${total}')
    print()
    response = input(f'Confirm purchase of ${total}? (y/n): ')
    if response.lower() == 'y':
        with open(filename, 'w') as file:
            json.dump(inventory, file)


def get_items(inventory):
    query = input("Item search term: ")
    items = []
    for item in inventory:
        if int(inventory[item]['quantity']) >= 1:
            if query in inventory[item]['name'].lower() or query in inventory[item]['description'].lower():
                items.append(item)
    return items
    pass


def main(filename):
    inventory = load_state(filename)
    cart = {}
    while True:
        print("\nWhat do you want to do?")
        option = main_menu()
        if option == 0:
            print()
            add_items(inventory, cart)
        elif option == 1:
            display_cart(inventory, cart)
        elif option == 2:
            checkout(inventory, cart, filename)
            cart = {}
            continue
        else:
            break

if __name__ == '__main__':
    main(sys.argv[1])
    #main('add_item.inventory.json')