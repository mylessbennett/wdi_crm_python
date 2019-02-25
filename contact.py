class Contact:

    contacts = []
    next_id = 1

    def __init__(self, first_name, last_name, email, note):
        """This method should initialize the contact's attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.note = note
        # each contact will have a unique id number upon creation
        self.id = Contact.next_id
        Contact.next_id += 1

    @classmethod
    def create(cls, first_name, last_name, email, note):
        """This method should call the initializer,
        store the newly created contact, and then return it"""
        new_contact = Contact(first_name, last_name, email, note)
        cls.contacts.append(new_contact)
        return new_contact

    @classmethod
    def all(cls):
        """This method should return all of the existing contacts"""
        all_contacts = []
        for item in cls.contacts:
            all_contacts.append(item)
        return all_contacts

    @classmethod
    def find(cls, id):
        """ This method should accept an id as an argument
        and return the contact who has that id"""
        requested_contact = 0
        for contact in cls.contacts:
            if contact.id == id:
                requested_contact = contact
        return requested_contact

    def update(self, attrib_to_change, new_value):
        """ This method should allow you to specify
        1. which of the contact's attributes you want to update
        2. the new value for that attribute
        and then make the appropriate change to the contact"""
        # info_to_change = updated_info
        attrib_to_change = attrib_to_change.lower()
        if attrib_to_change == 'first_name':
            self.first_name = new_value
        elif attrib_to_change == 'last_name':
            self.last_name = new_value
        elif attrib_to_change == 'email':
            self.email = new_value
        elif attrib_to_change == 'note':
            self.note = new_value
        else:
            print("Please enter a valid attribute to change.")

    @classmethod
    def find_by(cls):
        """This method should work similarly to the find method above
        but it should allow you to search for a contact using attributes other than id
        by specifying both the name of the attribute and the value
        eg. searching for 'first_name', 'Betty' should return the first contact named Betty"""

    @classmethod
    def delete_all(cls):
        """This method should delete all of the contacts"""

    def full_name(self):
        """Returns the full (first and last) name of the contact"""

    def delete(self):
        """This method should delete the contact
        HINT: Check the Array class docs for built-in methods that might be useful here
        """

# Feel free to add other methods here, if you need them.
    def __str__(self):
        return "Name: {} {} | Email: {} | Note: {}".format(self.first_name, self.last_name, self.email, self.note)


contact1 = Contact.create('Myles', 'Bennett', 'myles.bennett@hotmail.com', 'Sup?')
contact2 = Contact.create('Another', 'Friend', 'newguy@bitmakerlabs.com', 'howdy')
# print(len(Contact.contacts))
# print(contact1.id)
# print(contact2.id)
# print(Contact.all())
# print(Contact.find(1))
contact2.update('first_name', 'My')
contact2.update('email', 'newemail@bitmakerlabs.com')
print(contact2)
