class ContactBook:
    def _init_(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email, address):
        contact = {
            "name": name,
            "phone_number": phone_number,
            "email": email,
            "address": address
        }
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if self.contacts:
            print("Contact List:")
            for contact in self.contacts:
                print(f"Name: {contact['name']}, Phone: {contact['phone_number']}")
        else:
            print("Contact List is empty.")

    def search_contact(self, search_key):
        found_contacts = []
        for contact in self.contacts:
            if search_key.lower() in contact['name'].lower() or search_key in contact['phone_number']:
                found_contacts.append(contact)
        if found_contacts:
            print("Found Contacts:")
            for contact in found_contacts:
                print(f"Name: {contact['name']}, Phone: {contact['phone_number']}")
        else:
            print("No contacts found.")

    def update_contact(self, name, new_phone_number, new_email, new_address):
        for contact in self.contacts:
            if contact['name'] == name:
                contact['phone_number'] = new_phone_number
                contact['email'] = new_email
                contact['address'] = new_address
                print("Contact updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact['name'] == name:
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone_number, email, address)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_key = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_key)
        elif choice == '4':
            name = input("Enter name of the contact to update: ")
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            contact_book.update_contact(name, new_phone_number, new_email, new_address)
        elif choice == '5':
            name = input("Enter name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()
