"""This module contains the Database class"""
import sqlite3


class Database:
    """This class represents a database."""

    def __init__(self, database: str):
        """Initialize the database connection.
            Args: database(str): The path to the database file."""
        self.connection = sqlite3.connect(database)

    def _create_table(self):
        """Create a table in the database."""
        with self.connection as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS contacts(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR,
                phone_number VARCHAR(9),
                email VARCHAR)''')

