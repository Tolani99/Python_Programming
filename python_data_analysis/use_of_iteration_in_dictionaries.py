"""
To use iteration on Dictionaries
"""
contacts = {'Scott Rixner': '1-101-555-1234',
            'Joe Warren': '1-102-555-5678',
            'Jane Doe': '1-103-555-9012'}
def print_contacts(contact):
    """
    print the names of the contacts in our contacts list
    """
    for name in contact:
        print(name)
print_contacts(contacts)
