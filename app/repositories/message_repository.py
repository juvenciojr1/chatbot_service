import sqlite3

class MessageRepository:

    def __init__(self, db_path: str = "messages.db"):
        self.db_path = db_path
        self._create_table()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _create_table(self):
        command = """
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message TEXT NOT NULL
)
"""
        connection = self._connect()
        cursor = connection.cursor()
        cursor.execute(command)
        connection.commit()
        connection.close()


    def save(self, message: str):
        command = f"INSERT INTO messages (message) VALUES (?)"
        connection = self._connect()
        cursor = connection.cursor()
        cursor.execute(command, (message,))
        connection.commit()
        connection.close()

    def list(self):
        command = f"SELECT * FROM messages"
        connection = self._connect()
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(command)
        for message in cursor.fetchall():
            yield dict(message)

        connection.close()

