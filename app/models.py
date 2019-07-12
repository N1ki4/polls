from app.database import DB
import json


class Film:
    """A class for film objects."""
    def __init__(self, name):
        """Initializes film object.
        Arguments:
            name (str): film's name.
        """
        self.name = name
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
        return {"name": self.name}

class Genre:
	def __init__(self, title):
		self.title = title
		self.db = DB()
	
	def insert_one_genre(self):
		if not self.db.find_one("genres", {"title": self.title}):
		self.db.insert_one(collection="genres", data=self.json())
	
	def json(self): -> json:
		return {"title": self.title}


class Question: # probably have to add a time of creation 
	def __init__(self, question_text):
		self.question_text = question_text
		self.db = DB()


class Choice: # issue with question relations
	def __init__(self, choice_text, votes = 0):
		self.choice_text = choice_text
		self.votes = votes
		self.db = DB()
