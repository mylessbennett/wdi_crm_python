from contact import Contact


class CRM:


    def main_menu(self):
        while True:
            self.print_main_menu()
            user_selected = int(input())
            self.call_option(user_selected)

    def print_main_menu(self):
        print('[1] Add a new contact')
        print('[2] Modify an existing contact')
        print('[3] Delete a contact')
        print('[4] Display all the contacts')
        print('[5] Search by attribute')
        print('[6] Exit')
        print('Enter a number: ')

    def call_option(self, user_selected):
        if user_selected == 1:
            self.add_new_contact()
        elif user_selected == 2:
            self.modify_existing_contact()
        elif user_selected == 3:
            self.delete_contact()
        elif user_selected == 4:
            self.display_all_contacts()
        elif user_selected == 5:
            self.search_by_attribute()
        elif user_selected == 6:
            quit()

    def add_new_contact(self):
        first_name = input("Enter Contact First Name: ")
        last_name = input("Enter Contact Last Name: ")
        email = input("Enter Contact Email: ")
        note = input("Enter Contact Note: ")
        new_contact = Contact.create(first_name, last_name, email, note)
        print('New Contact: Name: {} {} | Email: {} | Note: {} '.format(first_name, last_name, email, note))

    def modify_existing_contact(self):
        user_id = int(input("Enter the id of the contact you wish to update: "))
        selected_contact = Contact.find(user_id)

        print("Select an attribute to change")
        print("1 - First Name")
        print("2 - Last Name")
        print("3 - Email")
        print("4 - Note")
        attribute = int(input("Enter the number of attribute to be changed: "))

        new_value = input("Enter the new info:")

        if attribute == 1:
            selected_contact.update('first name', new_value)
        elif attribute == 2:
            selected_contact.update('last name', new_value)
        elif attribute == 3:
            selected_contact.update('email', new_value)
        elif attribute == 4:
            selected_contact.update('note', new_value)

    def display_all_contacts(self):
        all_contacts = Contact.all()
        for contact in all_contacts:
            print(contact)

    def search_by_attribute(self):
        print("Select an attribute to search for")
        print("1 - First Name")
        print("2 - Last Name")
        print("3 - Email")
        print("4 - Note")
        attribute = int(input("Enter the number of attribute you want to search for: "))

        search_value = input("Enter the value of the attribute: ")

        if attribute == 1:
            search_attribute = 'first name'
            print(Contact.find_by(search_attribute, search_value))
        elif attribute == 2:
            search_attribute = 'first name'
            print(Contact.find_by(search_attribute, search_value))
        elif attribute == 3:
            search_attribute = 'first name'
            print(Contact.find_by(search_attribute, search_value))
        elif attribute == 4:
            search_attribute = 'first name'
            print(Contact.find_by(search_attribute, search_value))

    def delete_contact(self):
        contact_id = input("Enter the id of the contact you want to delete: ")

        contact_to_delete = Contact.find(contact_id)
        Contact.delete(contact_to_delete)

        print("Successfully deleted contact")






my_crm_app = CRM()
my_crm_app.main_menu()
