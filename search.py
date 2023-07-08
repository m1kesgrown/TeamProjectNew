def search(self, pattern, category):
    result = []
    category_new = category.strip().lower().replace(' ', '')
    pattern_new = pattern.strip().lower().replace(' ', '')

    for account in self.data:
        if category_new == 'phones':

            for phone in account['phones']:

                if phone.lower().startswith(pattern_new):
                    result.append(account)
        elif account[category_new].lower().replace(' ', '') == pattern_new:
            result.append(account)
    if not result:
        print('There is no such contact in address book!')
    return result
