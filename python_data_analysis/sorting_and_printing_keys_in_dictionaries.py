"""
To print key and values in a dictionary
"""
contacts = {'Scott Rixner': '1-101-555-1234',
            'Joe Warren': '1-102-555-5678',
            'Jane Doe': '1-103-555-9012'}
def print_ordered(contact_info):
    """
    Print the names and phone numbers of the contacts
    in our contacts list in alphabetical order.
    """
    keys = contact_info.keys()
    names = sorted(keys)
    for name in names:
        print(name, ":", contact_info[name])
