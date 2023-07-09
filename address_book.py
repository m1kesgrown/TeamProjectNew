import re
import pickle
import os.path
from datetime import datetime


class Contact:

    def __init__(self, contact_id, name, phone, birthday, email, address):
        self.contact_id = contact_id
        self.name = name
        self.phone = phone
        self.email = email
        self.birthday = birthday
        self.address = address

    @staticmethod
    def phone_check(phone):
        allowed_symbols = ['+', ' ', '(', ')', '-']
        for symbol in phone:
            if not symbol.isdigit() and symbol not in allowed_symbols:
                print('Invalid phone number format. Phone number should consist only digit numbers and allowed symbols. Please try again.')
                return False
        phone = phone.strip().removeprefix('+').replace('(', '').replace(')',
                                                                         '').replace('-', '').replace(' ', '')
        return phone

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

    def add_contact(self):
        contact_id = len(self.contacts) + 1
        name = input('Please provide name: ')
        address = input('Please provide address: ')
        email = input('Please provide email: ')
        while Contact.email_check(email) == False:
            email = input('Please provide email address: ')
        birthday = input('Please provide date of birth: ')
        while Contact.birthday_check(birthday) == False:
            birthday = input('Please provide date of birth: ')
        phone = input('Please provide phone number: ')
        while Contact.phone_check(phone) == False:
            number = input('Please provide phone number: ')
        contact = Contact(contact_id, name, phone, address, email, birthday)
        self.contacts.append(contact)
        print('Contact successfully added!')

    def save_contacts(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.contacts, file)
        print('Contacts saved successfully.')

    def load_contacts(self, filename):
        if os.path.exists(filename):
            with open(filename, 'rb') as file:
                self.contacts = pickle.load(file)
            print('Contacts loaded successfully.')


def main():
    address_book = Contactmanager()
    filename = 'contacts.pkl'
    address_book.load_contacts(filename)
    while True:
        print('1. Add contact')
        print('8. Exit')
        choice = input('Please choose a function (1-8): ')
        if choice == '1':
            address_book.add_contact()
        elif choice == '8':
            address_book.save_contacts(filename)
            print('Exiting the program...')
            break


if __name__ == '__main__':
    main()


