import sqlite3
from prettytable import PrettyTable


class Phonebook:
    def __init__(self, database):
        self.connection = sqlite3.connect(database)

    def add_contact(self, name, phone_number, email):
        with self.connection as conn:
            conn.execute(
                f"""INSERT INTO contacts (name, phone_number, email) VALUES (?, ?, ?)""",
                (name, phone_number, email),
            )
        print("Contact added successfully")

    def edit_contact(self, new_name, new_phone_number, new_email, name):
        with self.connection as conn:
            conn.execute(
                """UPDATE contacts SET name= ?, phone_number= ?, email= ?WHERE name= ?""",
                (new_name, new_phone_number, new_email, name),
            )
        print("Contact edited successfully")

    def delete_contact(self, name):
        with self.connection as conn:
            conn.execute("""DELETE FROM contacts WHERE name = ?""", (name,))
        print("Contact deleted successfully")

    def show_all_contacts(self):
        with self.connection as conn:
            res = conn.execute("""SELECT * FROM contacts""")
        table = PrettyTable()
        table.field_names = ["ID", "Name", "Phone number", "Email"]
        for row in res:
            table.add_row(row)
        print(table.get_string(fields=["Name", "Phone number", "Email"]))

    def sort_contacts(self):
        with self.connection as conn:
            res = conn.execute("""SELECT * FROM contacts ORDER BY name""")
            table = PrettyTable()
            table.field_names = ["ID", "Name", "Phone number", "Email"]
            for row in res:
                table.add_row(row)
            print(table.get_string(fields=["Name", "Phone number", "Email"]))
