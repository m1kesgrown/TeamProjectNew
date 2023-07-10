import os



def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


class Notes:
    def __init__(self, note_id, title, content):
        self.note_id = note_id
        self.title = title
        self.content = content


class NoteManager:
    def __init__(self):
        self.notes_list = []
        self.file_name = "notes.txt"

    def load_notes(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                for line in file:
                    note_data = line.strip().split(";")
                    note_id = int(note_data[0])
                    title = note_data[1]
                    content = note_data[2]
                    note = Notes(note_id, title, content)
                    self.notes_list.append(note)

    def save_notes(self):
        with open(self.file_name, "w") as file:
            for note in self.notes_list:
                line = f"{note.note_id};{note.title};{note.content}\n"
                file.write(line)
            self.update_note_ids()

    def update_note_ids(self):
        for index, note in enumerate(self.notes_list):
            note.note_id = index + 1

    def handle_title(self, note):
        new_title = input('Please provide new title: ')
        note.title = new_title


    def handle_content(self, note):
        new_content = input('Please provide new content: ')
        note.content = new_content

    def add_note(self):
        note_id = len(self.notes_list) + 1
        title = input('Please provide title: ')
        content = input('Please provide content: ')
        note = Notes(note_id, title, content)
        self.notes_list.append(note)
        print('Note added successfully.')

    def delete_note(self):
        if len(self.notes_list):
            try:
                note_id = int(input('Please provide note ID or enter 0 to return: '))
                note_found = False
                for note in self.notes_list:
                    if note_id == 0:
                        note_found = True
                        print('Note not removed.')
                        break
                    elif note_id == note.note_id:
                        note_found = True
                        self.notes_list.remove(note)
                        self.update_note_ids()
                        print('Note deleted successfully.')
                        break
                    

                if not note_found:
                    print(f'Note with ID {note_id} does not exist. Please try again.')
                    self.delete_note()
            except ValueError:
                print('Note ID must be digits. Please try again.')
                self.delete_note()
        else:
            print('No notes.')

    def edit_note(self):
        while True:
            try:
                note_id = int(input('Please provide note ID: '))
                note_found = False
                for note in self.notes_list:
                    if note_id == note.note_id:
                        while True:
                            field_handlers = {'title': self.handle_title,
                                            'content': self.handle_content}
                            field = input('Please provide field to be changed: ').lower()
                            if field in field_handlers:
                                field_handlers[field](note)
                                print(f'{field.capitalize()} successfully changed.')
                                note_found = True
                                break
                            else:
                                print(f'Field {field} does not exist. Please try again')
                        break
                if not note_found:
                    print(f'Note with ID number {note_id} not found. Please try again.')
            except ValueError:
                print('Note ID must be digits. Please try again.')
            else:
                break

    def search_note(self):
        search_query = input('Please provide search query: ')
        search_results = []
        for index, note in enumerate(self.notes_list):
            if (
                search_query.lower() in note.title.lower()
                or search_query.lower() in note.content.lower()
            ):
                search_results.append((index, note))
        if search_results:
            print(f'Search results for "{search_query}":')
            for index, note in search_results:
                print(f'ID: {index + 1}, Title: {note.title}, Content: {note.content}')
        else:
            print(f'No notes found for "{search_query}".')

    def exit(self):
        self.save_notes()

    def run(self):
        self.load_notes()

        while True:
            clear_console()

            print("\n _____       _           _____                               \n|   | | ___ | |_  ___   |     | ___  ___  ___  ___  ___  ___ \n| | | || . ||  _|| -_|  | | | || .'||   || .'|| . || -_||  _|\n|_|___||___||_|  |___|  |_|_|_||__,||_|_||__,||_  ||___||_|  \n                                              |___|          ")
            print("1. Add a Note")
            print("2. Delete a Note")
            print("3. Edit a Note")
            print("4. Search for Notes")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                clear_console()
                self.add_note()
                input("Press Enter to continue...")
            elif choice == "2":
                clear_console()
                self.delete_note()
                input("Press Enter to continue...")
            elif choice == "3":
                clear_console()
                self.edit_note()
                input("Press Enter to continue...")
            elif choice == "4":
                clear_console()
                self.search_note()
                input("Press Enter to continue...")
            elif choice == "5":
                clear_console()
                print("Exiting Note Manager...")
                self.exit()
                break
            else:
                clear_console()
                print("Invalid choice. Please try again.")
                input("Press Enter to continue...")


def notes():
    notemanager = NoteManager()
    notemanager.run()


if __name__ == "__main__":
    notes()