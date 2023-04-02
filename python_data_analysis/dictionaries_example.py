"""
This implement a simple contact list that maps
names to phone numbers.
"""
#Dictionary Structure
contacts = {'Scott Rixner': '1-101-555-1234',
            'Joe Warren': '1-102-555-5678',
            'Jane Doe': '1-103-555-9012'}

#Value Lookup
def lookup(contact, name):
    """
    Lookup name in contacts and return phone number.
    If name is not in contacts, return an empty string.
    """
    if name in contact:
        return contact[name]
    return ""
