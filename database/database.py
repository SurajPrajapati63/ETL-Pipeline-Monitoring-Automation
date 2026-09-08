import sqlite3

class Database:

    def __init__(self, db_name):

        self.connection = sqlite3.connect(
            db_name
        )

        self.cursor = self.connection.cursor()

    def execute(self, query, values=None):

        if values:
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)

        self.connection.commit()

    def fetchall(self):

        return self.cursor.fetchall()

    def close(self):

        self.connection.close()