import sqlite3


class DatabaseHandler:
    def __init__(self):
        con = sqlite3.connect('bannedwords.db')
        self.cur = con.cursor()

    def load_words(self):
        result = []
        res = self.cur.execute("SELECT word FROM bannedwords").fetchall()
        for word in res:
            result.append(word[0])
        return result
