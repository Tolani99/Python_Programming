contacts = {'Adeyinka':'08029323972', 'Tolani':'08025712356', 'Femi':'08081319622'}
def lookup(contacts, name):
    """
    Lookup name is contacts and return phone number.
    If name is not in contacts, return an empty string.
    """
    return contacts.get(name, "")
print(lookup(contacts, 'Tolani'))

