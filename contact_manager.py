import json

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(name, phone, email):
    contacts = load_contacts()
    contacts[name] = {'phone': phone, 'email': email}
    save_contacts(contacts)
    print(f'Contact added: {name}')

def update_contact(name, phone=None, email=None):
    contacts = load_contacts()
    if name in contacts:
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        save_contacts(contacts)
        print(f'Contact updated: {name}')
    else:
        print('Contact not found.')

def delete_contact(name):
    contacts = load_contacts()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f'Contact deleted: {name}')
    else:
        print('Contact not found.')

def view_contacts():
    contacts = load_contacts()
    if contacts:
        print('Contacts:')
        for name, details in contacts.items():
            print(f'Name: {name}, Phone: {details["phone"]}, Email: {details["email"]}')
    else:
        print('No contacts found.')

def search_contact(name):
    contacts = load_contacts()
    if name in contacts:
        details = contacts[name]
        print(f'Name: {name}, Phone: {details["phone"]}, Email: {details["email"]}')
    else:
        print('Contact not found.')

def main():
    while True:
        print('\nContact Management System')
        print('1. Add contact')
        print('2. Update contact')
        print('3. Delete contact')
        print('4. View contacts')
        print('5. Search contact')
        print('6. Exit')

        choice = input('Choose an option: ')
        if choice == '1':
            name = input('Enter name: ')
            phone = input('Enter phone number: ')
            email = input('Enter email address: ')
            add_contact(name, phone, email)
        elif choice == '2':
            name = input('Enter name to update: ')
            phone = input('Enter new phone number (or press Enter to skip): ')
            email = input('Enter new email address (or press Enter to skip): ')
            update_contact(name, phone if phone else None, email if email else None)
        elif choice == '3':
            name = input('Enter name to delete: ')
            delete_contact(name)
        elif choice == '4':
            view_contacts()
        elif choice == '5':
            name = input('Enter name to search: ')
            search_contact(name)
        elif choice == '6':
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
