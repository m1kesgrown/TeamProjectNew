from address_book import address_book, Contactmanager
from notes import note_func, NoteManager
import os
from about_us import about_us
from sort import sort


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    clear_console()
    contact_manager = Contactmanager()
    note_manager = NoteManager()
    contacts_file = 'contacts.pkl'
    notes_file = 'notes.pkl'
    contact_manager.load_contacts(contacts_file)
    note_manager.load_notes(notes_file)
    while True:
        print('Main menu\n')
        print('1. Address book')
        print('2. Notes')
        print('3. Display upcoming birthdays')
        print('4. Sorting file')
        print('5. About us')
        print('0. Exit')
        choice = input('Please choose a function (1-5): ')
        if choice == '1':
            address_book(contacts_file)
        elif choice == '2':
            note_func(notes_file)
        elif choice == '3':
            contact_manager.get_upcoming_birthdays()
        elif choice == '4':
            sort()
        elif choice == '5':
            about_us()
        elif choice == '0' or choice == 'exit' or choice == 'quit':
            clear_console()
            print('Exiting the program...\n')
            new_string = '\n'*10
            print(
                'The main rule of strategic thinking says: in order to carefully analyze an object, you need to distance yourself from it.'
            )
            print(new_string)
            break
        else:
            print('Invalid choice. Please try again.')


if __name__ == '__main__':
    main()
