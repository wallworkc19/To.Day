import sqlite3

# Database class for list of events
class Setting():
    
    def __init__(self, settings):
        self.connect = sqlite3.connect(settings)
        self.cursor = self.connect.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS settings (id INTEGER PRIMARY KEY, number text, email text)")

        self.connect.commit()


    def getNames(self):
        self.cursor.execute("SELECT * FROM settings ORDER BY id DESC")        # ASC | DESC
        nameList = self.cursor.fetchone()
        return nameList


    def insert(self, number, email):
        self.cursor.execute("INSERT INTO settings VALUES (NULL, ?, ?)", (number, email))
        self.connect.commit()

                 
    def __del__(self):
        self.connect.close()