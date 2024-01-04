import json

filename = 'contact.json'

def main():    
    """A contact book is a handy tool to keep all your contacts in one place. This python project will allow you to create a contact book and add, edit, and delete contacts. In addition, the user will be able to view all their contacts details in one place. This project is perfect for anyone who wants to keep their contacts organised and accessible."""

    while True:
        try:
            choice = get_choice()
        except KeyboardInterrupt:
            exit()

        if not choice:
            exit()

        match(choice):
            case '1': display_contacts()
            case '2': search_contact()
            case '3': create_contact()
            case '4': update_contact()
            case '5': remove_contact()


def get_choice() -> str | None:
    message = """
============ Contact Management System ============

1. View all contacts
2. Search contact
3. Create contact
4. Update contact
5. Remove contact

============ Press 'enter' to quit ============
> """

    while True:
        choice = input(message)

        if not choice:
            break

        if choice not in ['1', '2', '3', '4', '5']:
            continue

        return choice


def display_contacts() -> None:
    contacts = sorted(load_contacts(), key=lambda contact: contact['name'])
    
    empty_message = f"""
Total Contacts: {len(contacts)}

============ You have no contacts ============

Do you want to add new contacts?[Y/N] 
> """

    if not len(contacts):
        response = input(empty_message).lower()
        return create_contact() if (response == 'y') else main()

    contacts_str = ''.join(
        [f'{c["name"].title()} \t\t\t {c["mobile_no"]}\n' for c in contacts]
    )

    contacts_msg = f"""
==============================================
Total Contacts: {len(contacts)}

{contacts_str}
==============================================
""".strip()

    print(contacts_msg) 


def search_contact() -> str | None:
    name = input('Contact name: ').lower()

    contacts_list = find_contact(name, recurse=True)

    if not contacts_list:
        print(f'Sorry, {name} does not exist in the contact book')

    if len(contacts_list) < 2:
        contact = contacts_list[0]
        print(f'''
==============================================
Total Contacts: {len(contacts_list)}

{contact["name"].title()} \t\t\t {contact["mobile_no"]}
==============================================
        ''')

    contacts_str = ''.join(
        [f'{c["name"].title()} \t\t\t {c["mobile_no"]}\n' for c in contacts_list]
    )
    
    print(f'''
==============================================
Total Contacts: {len(contacts_list)}

{contacts_str}
==============================================
        ''')


def create_contact() -> None:
    contacts = load_contacts()

    while True:
        name = input('Name: ').lower()
        mobile_no = input('Mobile Number: ')

        if not name or not mobile_no: break

        contacts.append({'name': name, 'mobile_no': mobile_no})
        dump(contacts)

        answer = input('Do you want to add another contact?[Y/N]: ').lower()

        if answer != 'y': break


def update_contact() -> None:
    name = input('Contact name: ').lower()
    contact = find_contact(name)

    if not contact:
        print(f'\nSorry, {name.title()} does not exist in the contact book\n')
        return

    new_contacts = []

    new_name = input('Name (leave blank to keep the old name): ')
    new_mobile_no = input('Mobile Number (leave blank to keep the old number): ')

    if (not new_name) and (not new_mobile_no):
        return

    for c in load_contacts():
        if c['name'] == name:
            c = {
                'name': new_name or c['name'], 
                'mobile_no': new_mobile_no or c['mobile_no']
            }
            new_contacts.append(c)
        else:
            new_contacts.append(c)

    dump(new_contacts)


def remove_contact() -> None:
    name = input('Contact name: ').lower()
    contact = find_contact(name)
    contacts = load_contacts()

    if not contact:
        print(f'\nSorry, {name.title()} does not exist in the contact book')
        return

    new_contacts = [c for c in contacts if c['name'] != name]

    print('Contact removed succesfully')

    dump(new_contacts)


def find_contact(name: str, recurse=False) -> dict | list | None:
    contacts = load_contacts()

    if not len(contacts): return None

    contacts_list = []

    for contact in contacts:
        if contact['name'] == name and recurse:
            contacts_list.append(contact)
            continue

        if contact["name"] == name:
            return contact

    return contacts_list if len(contacts_list) > 0 else None


def load_contacts() -> list:
    try:
        with open(filename) as f:
            contacts = json.load(f)
    except FileNotFoundError:
        return []
    else:
        return contacts


def dump(data) -> None:
    with open(filename, 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    main()