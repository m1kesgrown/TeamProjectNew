import os
import pickle


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


class Note:

    def __init__(self, note_id, title, content):
        self.note_id = note_id
        self.title = title
        self.content = content


class NoteManager:

    def __init__(self):
        self.notes = []

    def load_notes(self, notes_file):
        if os.path.exists(notes_file):
            with open(notes_file, 'rb') as file:
                self.notes = pickle.load(file)

    def save_notes(self, notes_file):
        with open(notes_file, 'wb') as file:
            pickle.dump(self.notes, file)
        print('Notes saved successfully.')

    # def update_note_ids(self):
    #     for index, note in enumerate(self.notes_list):
    #         note.note_id = index + 1

    def handle_title(self, note):
        new_title = input('Please provide new title: ')
        note.title = new_title

    def handle_content(self, note):
        new_content = input('Please provide new content: ')
        note.content = new_content

    def add_note(self):
        note_id = len(self.notes) + 1
        title = input('Please provide title: ')
        content = input('Please provide content: ')
        note = Note(note_id, title, content)
        self.notes.append(note)
        print('Note added successfully.')

    def delete_note(self):
        try:
            note_found = False
            note_id = int(input('Please provide note ID: '))
            for index, note in enumerate(self.notes):
                if note_id == index + 1:
                    note_found = True
                    del self.notes[note_id - 1]
                    print('Note successfully deleted.')
                    break
            if not note_found:
                print(
                    f'Note with ID {note_id} does not exist. Please try again.'
                )
                self.delete_note()
        except ValueError:
            print('Note ID must be digits. Please try again.')
            self.delete_note()

    def edit_note(self):
        while True:
            try:
                note_id = int(input('Please provide note ID: '))
                note_found = False
                for index, note in enumerate(self.notes):
                    if note_id == index + 1:
                        note_found = True
                        while True:
                            field = input(
                                'Please provide field to be changed: ').lower(
                                )
                            field_handlers = {
                                'title': self.handle_title,
                                'content': self.handle_content,
                            }
                            if field in field_handlers:
                                field_handlers[field](note)
                                print(
                                    f'{field.capitalize()} succesfully changed.'
                                )
                                break
                            else:
                                print(
                                    f'Field {field} does not exist. Please try again'
                                )
                        break
                if not note_found:
                    print(
                        f'Note with ID number {note_id} not found. Please try again.'
                    )
            except ValueError:
                print('ID number must be digits. Please try again.')
            break

    def display_note(self):
        print('Notes List:')
        if not self.notes:
            print('No notes found.')
        else:
            for index, note in enumerate(self.notes):
                print(f"ID: {index + 1}, Name: {note.title}")

    def search_notes(self):
        search_query = input('Please provide search query: ')
        search_results = []
        for index, note in enumerate(self.notes):
            if (search_query.lower() in note.title.lower()
                    or search_query.lower() in note.content.lower()):
                search_results.append((index, note))
        if search_results:
            print(f'Search results for "{search_query}":')
            for index, note in search_results:
                print(
                    f'ID: {index+1}, Title: {note.title}, Concent: {note.content}'
                )
        else:
            print(f'No notes found for "{search_query}".')

    # def exit(self):
    #     self.save_notes()

    # def run(self, notes_file):
    #     self.notes_file = notes_file
    #     self.load_notes()


def note_func(notes_file):
    note_manager = NoteManager()
    note_manager.load_notes(notes_file)

    while True:
        clear_console()
        print('Notes load successfully.')
        print('Note Manager\n')
        print("1. Add a Note")
        print("2. Delete a Note")
        print("3. Edit a Note")
        print("4. Display Notes")
        print("5. Search for Notes")
        print("0. Main menu")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            clear_console()
            note_manager.add_note()
            input("Press Enter to continue...")
        elif choice == "2":
            clear_console()
            note_manager.delete_note()
            input("Press Enter to continue...")
        elif choice == "3":
            clear_console()
            note_manager.edit_note()
            input("Press Enter to continue...")
        elif choice == "4":
            clear_console()
            note_manager.display_note()
            input("Press Enter to continue...")
        elif choice == "5":
            clear_console()
            note_manager.search_notes()
            input("Press Enter to continue...")
        elif choice == "0":
            clear_console()
            note_manager.save_notes(notes_file)
            break
        else:
            clear_console()
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    note_func()