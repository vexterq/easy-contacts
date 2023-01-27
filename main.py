from database import Database
from phonebook import Phonebook
from validator import Validator


def setup():
    database = "phonebook.db"
    db = Database(database)
    phonebook = Phonebook(database)
    validator = Validator(database)
    db.create_table()
    return phonebook, validator


def get_user_choice():
    print('''
Welcome to the Easy Contacts application! 
With this application, you can easily manage and organize your contacts. 
Please select from the following options to continue: 
    * Add a contact
    * Remove a contact
    * Update a contact
    * View all contacts
    * View contacts by group
    *Exit''')
    choice = input('''
What would you like to do?
Add/Remove/Modify/Sort/Show/Exit
Enter your choice: ''')
    return choice.lower()


def main_menu():
    while True:
        choice = get_user_choice()
        if choice == 'add':
            name = validator.validate_name(input("Enter the name: "))
            phone_number = validator.validate_phone_number(
                input("Enter the phone number: "))
            email = validator.validate_email(input("Enter the email: "))
            phonebook.add_contact(name, phone_number, email)
        elif choice == 'remove':
            name = validator.validate_name(input("Enter the name: "))
            phonebook.delete_contact(name)
        elif choice == 'modify':
            name = validator.validate_name(input("Enter the name: "))
            new_name = validator.validate_name(input("Enter the new name: "))
            new_phone_number = validator.validate_phone_number(
                input("Enter the new phone number: "))
            new_email = validator.validate_email(
                input("Enter the new email: "))
            phonebook.edit_contact(new_name, new_phone_number, new_email, name)
        elif choice == 'sort':
            phonebook.show_all_contacts()
        elif choice == 'show':
            phonebook.show_all_contacts()
        elif choice == 'exit':
            exit()
        else:
            print('Invalid input. Please try again.')
            main_menu()


if __name__ == "__main__":
    phonebook, validator = setup()
    main_menu()
