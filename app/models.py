from app.database import DB


class Film:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.db = DB()

    def insert(self):
        if not self.db.find_one("films", {"name": self.name}):
            self.db.insert(collection="films", data=self.json())

    def films(self):
        return self.db.find_one("films", {"name": self.name})

    def json(self):
        return {
            "name": self.name,
            "genre": self.genre
        }
