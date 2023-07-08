def edit(self, contact_name, parameter, new_value):
    names = []
    try:
        for account in self.data:
            names.append(account['name'])
            if account['name'] == contact_name:
                if parameter == 'birthday':
                    new_value = Birthday(new_value).value
                elif parameter == 'email':
                    new_value = Email(new_value).value
                elif parameter == 'status':
                    new_value = Status(new_value).value
                elif parameter == 'phones':
                    new_contact = new_value.split(' ')
                    new_value = []
                    for number in new_contact:
                        new_value.append(Phone(number).value)
                if parameter in account.keys():
                    account[parameter] = new_value
                else:
                    raise ValueError
        if contact_name not in names:
            raise NameError
    except ValueError:
        print('Incorrect parameter! Please provide correct parameter')
    except NameError:
        print('There is no such contact in address book!')
    else:
        self.log(f"Contact {contact_name} has been edited!")
        return True
    return False