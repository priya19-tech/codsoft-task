contacts = []

def add_contact():
    print("\n Add New Contact")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)
    print(" Contact added successfully.")

def view_contacts():
    print("\n📖 Contact List")
    if not contacts:
        print("No contacts found.")
        return
    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}:")
        print(f"Name    : {contact['name']}")
        print(f"Phone   : {contact['phone']}")
        print(f"Email   : {contact['email']}")
        print(f"Address : {contact['address']}")

def search_contact():
    print("\n Search Contact")
    query = input("Enter name or phone number to search: ").lower()
    found = False
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            print("\nContact Found:")
            print(f"Name    : {contact['name']}")
            print(f"Phone   : {contact['phone']}")
            print(f"Email   : {contact['email']}")
            print(f"Address : {contact['address']}")
            found = True
            break
    if not found:
        print(" Contact not found.")

def update_contact():
    print("\n Update Contact")
    name = input("Enter the name of the contact to update: ").lower()
    for contact in contacts:
        if contact['name'].lower() == name:
            print("Contact found. Enter new details (leave blank to keep existing):")
            phone = input(f"New phone (current: {contact['phone']}): ")
            email = input(f"New email (current: {contact['email']}): ")
            address = input(f"New address (current: {contact['address']}): ")

            if phone:
                contact['phone'] = phone
            if email:
                contact['email'] = email
            if address:
                contact['address'] = address

            print("Contact updated successfully.")
            return
    print(" Contact not found.")

def delete_contact():
    print("\nDelete Contact")
    name = input("Enter the name of the contact to delete: ").lower()
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == name:
            confirm = input(f"Are you sure you want to delete {contact['name']}? (yes/no): ").lower()
            if confirm == 'yes':
                contacts.pop(i)
                print("Contact deleted.")
            else:
                print(" Deletion cancelled.")
            return
    print(" Contact not found.")

def menu():
    while True:
        print("\n📱 Contact Management Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print(" Exiting Contact Manager. Goodbye!")
            break
        else:
            print(" Invalid option. Please try again.")

# Run the application
menu()
