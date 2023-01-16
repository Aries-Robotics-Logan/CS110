import sys
import json


def load_state(filename):
    with open(filename, encoding='UTF-8') as file:
        return json.load(file)


def main_menu():
    menu = [
        'List items',
        'Check item in/out',
        'Quit'
    ]
    show_menu(menu)
    return get_valid_input(range(len(menu)))


def show_menu(menu):
    for index, option in enumerate(menu):
        print(f'({index}) {option}')


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


def get_status(bool_status):
    if bool_status:
        return "[Checked Out]"
    else:
        return "[Available]"


def show_system_status(inventory):
    print()
    for description_name, status in inventory.items():
        availability = get_status(status["checked out"])
        description = status["description"]
        print(f'{availability} {description_name}: {description}')


def change_availability(inventory):
    print()
    print("Which item do you want to check in/out?")
    menu = list(inventory.keys())
    show_menu(menu)
    option = get_valid_input(range(len(menu)))
    key = menu[option]
    inventory[key]["checked out"] = not inventory[key]["checked out"]
    return inventory


def save_state(inventory, lights_file):
    with open(lights_file, 'w') as file:
        json.dump(inventory, file)


def main(filename):
    inventory = load_state(filename)
    while True:
        print("\nWhat would you like to do?")
        option = main_menu()
        if option == 0:
            show_system_status(inventory)
        elif option == 1:
            inventory = change_availability(inventory)
        else:
            save_state(inventory, sys.argv[1])
            return

if __name__ == '__main__':
    main(sys.argv[1])
