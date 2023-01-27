import sqlite3


class Database:
    def __init__(self, database):
        self.connection = sqlite3.connect(database)

    def create_table(self):
        with self.connection as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS contacts(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR,
                phone_number VARCHAR(9),
                email VARCHAR)''')
