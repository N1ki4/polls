from app.database import DB
import json


class Film:
    """A class for film objects."""
    def __init__(self, name, *args):
        """Initializes film object.

        Args:
            name (str): film's name.
            args: arguments for film's genre.
        """
        self.name = name
        self.genre = list(args)
        self.db = DB()

    def insert_one_film(self):
        """Static method for inserting a single document to the database.
        If collection doesn't exist, creates it.
        """
        if not self.db.find_one("films", {"name": self.name}):
            self.db.insert_one(collection="films", data=self.json())

    def json(self) -> json:
        """Returns film information in json representation.

        Returns:
            film information in json representation.
        """
        return {
            "name": self.name,
            "genre": self.genre
        }
