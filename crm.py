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
            self.remove()
        elif user_selected == 4:
            self.remove()
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
        return new_contact



  # def add_new_contact(self):
  #
  #
  # def modify_existing_contact(self):
  #
  #
  # def delete_contact(self):
  #
  #
  # def display_all_contacts(self):
  #
  # def search_by_attribute(self):

my_crm_app = CRM()
my_crm_app.main_menu()
