def remove(self, pattern):
    flag = False
    for account in self.data:
        if account['name'] == pattern:
            self.data.remove(account)
            self.log(f"Contact {account['name']} has been removed!")
            flag = True
        '''if pattern in account['phones']:
                    account['phones'].remove(pattern)
                    self.log.log(f"Phone number of {account['name']} has been removed!")'''
    return flag