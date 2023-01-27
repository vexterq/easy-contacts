"""This module contains the Validator class."""
import sqlite3
import re


class Validator:
    """This class represents a validator."""

    def __init__(self, database: str):
        """Initialize the database connection.
            Args: database(str): The path to the database file."""
        self.connection = sqlite3.connect(database)

    def validate_name(self, name: str):
        """Validate the name.
            Args: name(str): The name to be validated."""
        while True:
            if not name.isalpha():
                print('The name must contain only letters')
                name = input('Enter the name: ')
            elif not 2 <= len(name) <= 30:
                print('The name must be beetween 2 and 30 characters')
                name = input('Enter the name:')
                continue
            elif self.check_if_name_exists(name.capitalize()):
                print('Name already exists in the phonebook, please enter a new name:')
                name = input(' ')
                continue
            break
        return name.capitalize()

    def check_if_name_exists(self, name: str):
        """Check if the name already exists in the database.
            Args: name(str): The name to be checked."""
        with self.connection as conn:
            res = conn.execute(
                'SELECT name FROM contacts WHERE name = ?', (name,))
        if res.fetchone():
            return True
        return False

    def validate_phone_number(self, phone_number: int):
        """Validate the phone number.
            Args: phone_number(int): The phone number to be validated."""
        while True:
            if not phone_number.isdigit():
                print('The phone number must contain only digits.')
                phone_number = input('Enter the phone number:')
                continue
            if not len(phone_number) == 9:
                print('The phone number must be 9 digits long')
                phone_number = input('Enter the phone number:')
            if self.check_if_phone_number_exists(phone_number):
                with self.connection as conn:
                    res = conn.execute(
                        '''SELECT name FROM contacts WHERE phone_number = ?''',
                        (phone_number,),
                    )
                    name = res.fetchone()[0]
                    print(
                        f'''Phone number already exists in the phonebook and belongs to {name},
                        please enter a new phone number:'''
                    )
                phone_number = input(' ')
                continue
            break
        return phone_number

    def check_if_phone_number_exists(self, phone_number: int):
        """Check if the phone number already exists in the database.
            Args: phone_number(int): The phone number to be checked."""
        with self.connection as conn:
            res = conn.execute(
                'SELECT phone_number FROM contacts WHERE phone_number = ?',
                (phone_number,),
            )
        if res.fetchone():
            return True
        return False

    def validate_email(self, email: str):
        """Validate the email.
            Args: email(str): The email to be validated."""
        while True:
            regex = re.compile(
                r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
            )
            if not re.fullmatch(regex, email):
                print('Invalid email')
                email = input('Enter the email: ')
                continue
            if self.check_if_email_exists(email):
                with self.connection as conn:
                    res = conn.execute(
                        '''SELECT name FROM contacts WHERE email= ?''', (
                            email,)
                    )
                    name = res.fetchone()[0]
                    print(
                        f'''Email already exists in the phonebook and belongs to {name},
                        please enter a new email:'''
                    )
                email = input(' ')
                continue
            break
        return email

    def check_if_email_exists(self, email: str):
        """Check if the email already exists in the database.
            Args: email(str): The email to be checked."""
        with self.connection as conn:
            res = conn.execute(
                'SELECT email FROM contacts WHERE email= ?', (email,))
        if res.fetchone():
            return True
        return False
