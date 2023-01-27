"""This module contains the Phonebook class."""
import sqlite3
from prettytable import PrettyTable


class Phonebook:
    """This class represents a phonebook."""

    def __init__(self, database: str):
        """Initialize the database connection.
            Args: database(str): The path to the database file.
        """
        self.connection = sqlite3.connect(database)

    def add_contact(self, name: str, phone_number: str, email: str):
        """Add a new contact to the database.
            Args:   name (str): The name of the contact.
                    phone_number (str): The phone number of the contact.
                    email (str): The email of the contact.
                    """
        with self.connection as conn:
            conn.execute(
                '''INSERT INTO contacts (name, phone_number, email) VALUES (?, ?, ?)''',
                (name, phone_number, email),
            )
        print('Contact added successfully')

    def edit_contact(self, new_name: str, new_phone_number: int, new_email: str, name: str):
        """Edit a contact in the database.
            Args:   new_name (str): The new name of the contact.
                    new_phone_number (int): The new phone number of the contact.
                    new_email (str): The new email of the contact.
                    name (str): The name of the contact to be edited."""

        with self.connection as conn:
            conn.execute(
                '''UPDATE contacts SET name= ?, phone_number= ?, email= ?WHERE name= ?''',
                (new_name, new_phone_number, new_email, name),
            )
        print('Contact edited successfully')

    def delete_contact(self, name: str):
        """Delete a contact from the database.
            Args: name (str): The name of the contact to be deleted."""
        with self.connection as conn:
            conn.execute('''DELETE FROM contacts WHERE name = ?''', (name,))
        print('Contact deleted successfully')

    def show_all_contacts(self):
        """Show all contacts in the database."""
        with self.connection as conn:
            res = conn.execute('''SELECT * FROM contacts''')
        table = PrettyTable()
        table.field_names = ['ID', 'Name', 'Phone number', 'Email']
        for row in res:
            table.add_row(row)
        print(table.get_string(fields=['Name', 'Phone number', 'Email']))

    def sort_contacts(self):
        """Sort all contacts in the database by name."""
        with self.connection as conn:
            res = conn.execute('''SELECT * FROM contacts ORDER BY name''')
            table = PrettyTable()
            table.field_names = ['ID', 'Name', 'Phone number', 'Email']
            for row in res:
                table.add_row(row)
            print(table.get_string(fields=['Name', 'Phone number', 'Email']))
