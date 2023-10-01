"""
To add new key-value pairs and update the values
associated with existing keys
"""
contacts = {'Scott Rixner': '1-101-555-1234',
            'Joe Warren': '1-102-555-5678',
            'Jane Doe': '1-103-555-9012'}
def add_contact(contact, name, number):
    """
    Add a new contact (name, number) to the contacts list.
    """
    if name in contact:
        print(name, "is already in contacts list!")
    else:
        contact[name] = number
add_contact(contacts, 'Femi Lawal', '08081319622')
print(contacts)
