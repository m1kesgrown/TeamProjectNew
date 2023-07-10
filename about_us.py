import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def about_us():
    clear_console()
    while True:
        print('Cast:\n')
        print('Oleksii          as Team lead            github: m1kesgrown')
        print('Сергей Цапков    as Scrum master         github: OLoloms')
        print('Volodymyr Kurov  as developer            github: vokur13')
        print('Игорь Гроза      as developer            github: igorgroni')
        print('O. Martyniuk     as developer            github: CadejoBlanko')
        print('Kirill           as mentor')
        print('Клієнт менеджер Аліна as Клієнт менеджер Аліна\n')

        input('Press Enter for the Main menu. ')
        clear_console()
        break
