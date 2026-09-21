import json
import os

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {"name": self.name, "phone": self.phone, "email": self.email}

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email}"


class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.contacts = [Contact(c["name"], c["phone"], c["email"]) for c in data]

    def save_contacts(self):
        with open(self.filename, "w") as f:
            json.dump([c.to_dict() for c in self.contacts], f, indent=4)

    def add_contact(self, name, phone, email):
        self.contacts.append(Contact(name, phone, email))
        self.save_contacts()
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        print("\n--- Contact List ---")
        for i, c in enumerate(self.contacts, start=1):
            print(f"{i}. {c}")

    def search_contact(self, name):
        results = [c for c in self.contacts if name.lower() in c.name.lower()]
        if not results:
            print(f"No contact found with name '{name}'.")
            return
        print("\n--- Search Results ---")
        for c in results:
            print(c)

    def update_contact(self, name, new_phone=None, new_email=None):
        for c in self.contacts:
            if c.name.lower() == name.lower():
                if new_phone:
                    c.phone = new_phone
                if new_email:
                    c.email = new_email
                self.save_contacts()
                print(f"Contact '{name}' updated successfully.")
                return
        print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        for c in self.contacts:
            if c.name.lower() == name.lower():
                self.contacts.remove(c)
                self.save_contacts()
                print(f"Contact '{name}' deleted successfully.")
                return
        print(f"Contact '{name}' not found.")


def main():
    book = ContactBook()

    while True:
        print("\n===== CONTACT BOOK MENU =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            book.add_contact(name, phone, email)

        elif choice == "2":
            book.view_contacts()

        elif choice == "3":
            name = input("Enter name to search: ")
            book.search_contact(name)

        elif choice == "4":
            name = input("Enter name to update: ")
            phone = input("Enter new phone (leave blank to skip): ")
            email = input("Enter new email (leave blank to skip): ")
            book.update_contact(name, phone if phone else None, email if email else None)

        elif choice == "5":
            name = input("Enter name to delete: ")
            book.delete_contact(name)

        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()