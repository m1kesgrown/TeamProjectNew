from setuptools import setup, find_namespace_packages

setup(
    name='Personalbot',
    version='1.0.4',
    description='This is project made by team "Bugs fixers"',
    authors=['Oleksii Chygrin', 'Сергей Цапков',
             'Volodymyr Kurov', 'Игорь Гроза', 'Oleksandr Martyniuk'],
    author_email='czygrin.oleksii@gmail.com',
    url='https://github.com/m1kesgrown/TeamProjectNew',
    license='MIT',
    packages=find_namespace_packages(),
    data_files=[('personalbot', ['personalbot/notes.pkl',
                 'personalbot/contacts.pkl', 'personalbot/address_book.py', 'personalbot/notes.py', 'personalbot/search.py',
                'personalbot/main.py', 'personalbot/sort.py', 'personalbot/about_us.py'])],
    include_package_data=True,
    classifiers=['Programming Language :: Python :: 3',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent'],
    install_requires=[''],
    entry_points={'console_scripts': [
        'personalbot=personalbot.main:main']}
)
