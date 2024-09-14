Task 3:contact book
# Contact Book Application

class ContactBook:
    def __init__(self):
        self.contacts = {}

    # Function to add a contact
    def add_contact(self, name, phone, email, address):
        self.contacts[phone] = {
            'Name': name,
            'Phone': phone,
            'Email': email,
            'Address': address
        }
        print(f"Contact for {name} added successfully!")

    # Function to view all contacts
    def view_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
            return
        print("Contact List:")
        for contact in self.contacts.values():
            print(f"Name: {contact['Name']}, Phone: {contact['Phone']}")

    # Function to search for a contact by name or phone number
    def search_contact(self, keyword):
        found = False
        for contact in self.contacts.values():
            if keyword.lower() in contact['Name'].lower() or keyword == contact['Phone']:
                print("\nContact Found:")
                self.display_contact(contact)
                found = True
                break
        if not found:
            print("Contact not found.")

    # Function to display full contact details
    def display_contact(self, contact):
        print(f"Name: {contact['Name']}")
        print(f"Phone: {contact['Phone']}")
        print(f"Email: {contact['Email']}")
        print(f"Address: {contact['Address']}")

    # Function to update a contact
    def update_contact(self, phone):
        if phone in self.contacts:
            print(f"Updating contact for {self.contacts[phone]['Name']}")
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            self.contacts[phone].update({
                'Name': name,
                'Email': email,
                'Address': address
            })
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    # Function to delete a contact
    def delete_contact(self, phone):
        if phone in self.contacts:
            del_contact = self.contacts.pop(phone)
            print(f"Contact for {del_contact['Name']} deleted successfully!")
        else:
            print("Contact not found.")

# User Interface for interaction
def contact_book_ui():
    contact_book = ContactBook()

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        
        elif choice == '2':
            contact_book.view_contacts()
        
        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            contact_book.search_contact(keyword)
        
        elif choice == '4':
            phone = input("Enter the phone number of the contact to update: ")
            contact_book.update_contact(phone)
        
        elif choice == '5':
            phone = input("Enter the phone number of the contact to delete: ")
            contact_book.delete_contact(phone)
        
        elif choice == '6':
            print("Exiting Contact Book.")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Running the Contact Book interface
if __name__ == "__main__":
    contact_book_ui()
