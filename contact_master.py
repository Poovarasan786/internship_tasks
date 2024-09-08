# ContactMaster Program in Python

# Initialize an empty list to store contacts
contacts = []

# Function to add a new contact
def add_contact(name, phone, email):
    contact = {
        'Name': name,
        'Phone': phone,
        'Email': email
    }
    contacts.append(contact)
    print(f"Contact '{name}' added successfully!")

# Function to delete a contact by name
def delete_contact(name):
    global contacts
    # Filter out contacts that don't match the name to delete
    contacts = [contact for contact in contacts if contact['Name'].lower() != name.lower()]
    print(f"Contact '{name}' deleted (if it existed).")

# Function to search for a contact by name
def search_contact(name):
    for contact in contacts:
        if contact['Name'].lower() == name.lower():
            print(f"Found Contact: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")
            return
    print(f"No contact found with the name '{name}'.")

# Function to display all contacts
def display_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("All Contacts:")
        for contact in contacts:
            print(f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")

# Main program loop
def main():
    while True:
        print("\n--- ContactMaster Menu ---")
        print("1. Add New Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Display All Contacts")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            add_contact(name, phone, email)

        elif choice == '2':
            name = input("Enter the name of the contact to delete: ")
            delete_contact(name)

        elif choice == '3':
            name = input("Enter the name of the contact to search: ")
            search_contact(name)

        elif choice == '4':
            display_contacts()

        elif choice == '5':
            print("Exiting ContactMaster.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

# Run the ContactMaster application
if __name__ == "__main__":
    main()
