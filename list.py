import sqlite3

# Database class for list of events
class List():
    
    def __init__(self, list):
        self.connect = sqlite3.connect(list)
        self.cursor = self.connect.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY, name text, priority int, due text)")

        self.connect.commit()


    def getEvents(self):
        self.cursor.execute("SELECT * FROM events ORDER BY priority DESC")        # ASC | DESC
        eventList = self.cursor.fetchall()
        return eventList

    def getName(self):
        self.cursor.execute("SELECT * FROM events ORDER BY priority DESC")        # ASC | DESC
        rows = self.cursor.fetchall()
        l=[]
        for i in rows:
            l.append(i[0])
        return l #rows.__getitem__(0)[0]

    def insert(self, name, priority, due):
        self.cursor.execute("INSERT INTO events VALUES (NULL, ?, ?, ?)", (name, priority, due))
        self.connect.commit()

                       
    def remove(self, id):
        self.cursor.execute("DELETE FROM events WHERE id=?", (id,))
        self.connect.commit()


    def __del__(self):
        self.connect.close()
