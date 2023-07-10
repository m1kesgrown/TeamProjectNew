import re
import pickle
import os.path
import time
from datetime import datetime


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


class Contact:

    def __init__(self, contact_id, name, address, email, birthday, number):
        self.contact_id = contact_id
        self.name = name
        self.address = address
        self.email = email
        self.birthday = birthday
        self.number = number

    @staticmethod
    def number_check(number):
        allowed_symbols = ['+', ' ', '(', ')', '-']
        for symbol in number:
            if not symbol.isdigit() and symbol not in allowed_symbols:
                print('Invalid phone number format. Phone number should consist only digit numbers and allowed symbols. Please try again.')
                return False
        number = number.strip().removeprefix('+').replace('(', '').replace(')',
                                                                           '').replace('-', '').replace(' ', '')
        return number

    @staticmethod
    def email_check(email):
        pattern = r'^([A-z0-9_-]+\.)*[A-z0-9_-]+@[A-z0-9_-]+(\.[A-z0-9_-]+)*\.[A-z]{2,6}$'
        if re.match(pattern, email):
            return True
        print('Invalid email address format. Please try again.')
        return False

    @staticmethod
    def birthday_check(birthday):
        pattern = r'^\d{2}-\d{2}-\d{4}$'
        if re.match(pattern, birthday):
            try:
                datetime.strptime(birthday, '%d-%m-%Y')
                return True
            except ValueError:
                print('Invalid date of birth format. Please provide dd-mm-yyyy.')
                return False
        print('Invalid date of birth format. Please provide dd-mm-yyyy.')
        return False


class Contactmanager:

    def __init__(self):
        self.contacts = []

    def handle_email(self, contact):
        new_email = input('Plese provide new email address: ')
        while not Contact.email_check(new_email):
            new_email = input('Plese provide new email address: ')
        contact.email = new_email

    def handle_number(self, contact):
        new_phone_number = input('Plese provide new phone number: ')
        while not Contact.number_check(new_phone_number):
            new_phone_number = input('Plese provide new phone number: ')
        contact.number = new_phone_number

    def handle_birthday(self, contact):
        new_birthday = input('Please provide new date of birthday: ')
        while not Contact.birthday_check(new_birthday):
            new_birthday = input('Please provide new date of birth: ')
        contact.birthday = new_birthday

    def handle_name(self, contact):
        new_name = input('Please provide new name: ')
        contact.name = new_name

    def handle_address(self, contact):
        new_address = input('Please provide new address: ')
        contact.address = new_address

    def add_contact(self):
        contact_id = len(self.contacts) + 1
        name = input('Please provide name: ')
        address = input('Please provide address: ')
        email = input('Please provide email address: ')
        while Contact.email_check(email) == False:
            email = input('Please provide email address: ')
        birthday = input('Please provide date of birth: ')
        while Contact.birthday_check(birthday) == False:
            birthday = input('Please provide date of birth: ')
        number = input('Please provide phone number: ')
        while Contact.number_check(number) == False:
            number = input('Please provide phone number: ')
        contact = Contact(contact_id, name, address, email, birthday, number)
        self.contacts.append(contact)
        print('Contact successfully added!')

    def delete_contact(self):
        try:
            contact_found = False
            contact_id = int(input('Please provide contact ID: '))
            for index, contact in enumerate(self.contacts):
                if contact_id == index+1:
                    contact_found = True
                    del self.contacts[contact_id-1]
                    print('Contact successfully deleted.')
                    break
            if not contact_found:
                print(
                    f'Contact with ID {contact_id} does not exist. Please try again.')
                self.delete_contact()
        except ValueError:
            print('Contact ID must be digits. Please try again.')
            self.delete_contact()

    def edit_contact(self):
        while True:
            try:
                contact_id = int(input('Please provide contact ID: '))
                contact_found = False
                for index, contact in enumerate(self.contacts):
                    if contact_id == index + 1:
                        contact_found = True
                        while True:
                            field = input(
                                'Please provide field to be changed: ').lower()
                            field_handlers = {
                                'name': self.handle_name,
                                'address': self.handle_address,
                                'email': self.handle_email,
                                'birthday': self.handle_birthday,
                                'number': self.handle_number,
                            }
                            if field in field_handlers:
                                field_handlers[field](contact)
                                print(
                                    f'{field.capitalize()} succesfully changed.')
                                break
                            else:
                                print(
                                    f'Field {field} does not exist. Please try again')
                        break
                if not contact_found:
                    print(
                        f'Contact with ID number {contact_id} not found. Please try again.')
            except ValueError:
                print('ID number must be digits. Please try again.')
            break

    def display_contacts(self):
        print('Contact List:')
        if not self.contacts:
            print('No contacts found.')
        else:
            for index, contact in enumerate(self.contacts):
                print(f"ID: {index + 1}, Name: {contact.name}")

    def display_contact_information(self):
        try:
            contact_id = int(input('Please provide contact ID: '))
            contact_found = False
            for index, contact in enumerate(self.contacts):
                if contact_id == index + 1:
                    contact_found = True
                    print(
                        f'Contact information: \nID: {index + 1}, Name: {contact.name}, Address: {contact.address}, Email: {contact.email}, Birthday: {contact.birthday}, Number: {contact.number}')
                    break
            if not contact_found:
                print(
                    f'Contact with ID {contact_id} does not exist. Please try again.')
                self.display_contact_information()
        except ValueError:
            print('Contact ID must be digits. Please try again.')
            self.display_contact_information()

    def get_upcoming_birthdays(self):
        while True:
            try:
                days = int(input('Please provide number of days: '))
                break
            except ValueError:
                print('Invalid input. Please enter a digit number of days.')
        upcoming_birthdays = []
        current_date = datetime.now()
        for contact in self.contacts:
            birthday = datetime.strptime(contact.birthday, '%d-%m-%Y')
            next_birthday = datetime(
                current_date.year, birthday.month, birthday.day)
            if next_birthday < current_date:
                next_birthday = next_birthday.replace(
                    year=current_date.year + 1)
            if (next_birthday - current_date).days <= days:
                upcoming_birthdays.append(contact)
        print(f'Upcoming birthdays within {days} days:')
        for contact in upcoming_birthdays:
            print(f'Name: {contact.name}, Birthday: {contact.birthday}')

    def search_contacts(self):
        search_query = input('Please provide search query: ')
        search_results = []
        for index, contact in enumerate(self.contacts):
            if (
                search_query.lower() in contact.name.lower()
                or search_query.lower() in contact.number.lower()
                or search_query.lower() in contact.email.lower()
            ):
                search_results.append((index, contact))
        if search_results:
            print(f'Search results for "{search_query}":')
            for index, contact in search_results:
                print(
                    f'ID: {index+1}, Name: {contact.name}, Number: {contact.number}, Email: {contact.email}')
        else:
            print(f'No contacts found for "{search_query}".')

    def save_contacts(self, contacts_file):
        with open(contacts_file, 'wb') as file:
            pickle.dump(self.contacts, file)
        print('Contacts saved successfully.')

    def load_contacts(self, contacts_file):
        if os.path.exists(contacts_file):
            with open(contacts_file, 'rb') as file:
                self.contacts = pickle.load(file)


KEY_WORDS = {
    ('add', 'expanse', 'write'): Contactmanager.add_contact,
    ('delete', 'remove'): Contactmanager.delete_contact,
    ('edit', 'change'): Contactmanager.edit_contact,
    ('display', 'see', 'show'): Contactmanager.display_contacts,
    ('save',): Contactmanager.save_contacts,
    ('search', 'find'): Contactmanager.search_contacts
}


def address_book(contacts_file):
    clear_console()
    print('Contacts loaded successfully.')
    contact_manager = Contactmanager()
    contact_manager.load_contacts(contacts_file)
    while True:
        print('Address Book\n')
        print('1. Add contact')
        print('2. Delete contact')
        print('3. Edit contact')
        print('4. Display contacts')
        print('5. Display contact information')
        print('6. Search contacts')
        print('0. Main menu')
        choice = input('Please choose a function (1-8): ')
        if choice == '1':
            contact_manager.add_contact()
        elif choice == '2':
            contact_manager.delete_contact()
        elif choice == '3':
            contact_manager.edit_contact()
        elif choice == '4':
            contact_manager.display_contacts()
        elif choice == '5':
            contact_manager.display_contact_information()
        elif choice == '6':
            contact_manager.search_contacts()
        elif choice == '0':
            clear_console()
            contact_manager.save_contacts(contacts_file)
            break
        else:
            print('Invalid choice. Please try again.')
        time.sleep(2)


if __name__ == '__main__':
    address_book()
