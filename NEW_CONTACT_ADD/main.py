import json


CONTACTS_FILE = "contacts.json"


def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")
def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts found.")
        return
    print("\nAll Contacts:")
    print(f"{'Name':<20}{'Phone':<15}{'Email':<25}")
    print("-" * 60)
    for contact in contacts:
        print(f"{contact['name']:<20}{contact['phone']:<15}{contact['email']:<25}")


def search_contact(contacts):
    search_name = input("Enter the name to search: ").strip().lower()
    found_contacts = [c for c in contacts if search_name in c['name'].lower()]
    if not found_contacts:
        print(f"No contacts found with the name '{search_name}'.")
        return
    print("\nSearch Results:")
    print(f"{'Name':<20}{'Phone':<15}{'Email':<25}")
    print("-" * 60)
    for contact in found_contacts:
        print(f"{contact['name']:<20}{contact['phone']:<15}{contact['email']:<25}")


def delete_contact(contacts):
    name_to_delete = input("Enter the name of the contact to delete: ").strip()
    for contact in contacts:
        if contact['name'].lower() == name_to_delete.lower():
            contacts.remove(contact)
            save_contacts(contacts)
            print(f"Contact '{name_to_delete}' deleted successfully!")
            return
    print(f"No contact found with the name '{name_to_delete}'.")


def main():
    contacts = load_contacts()
    while True:
        print("\nContact Book")
        print("1. Add a Contact")
        print("2. View All Contacts")
        print("3. Search for a Contact")
        print("4. Delete a Contact")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Thank you for using the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
