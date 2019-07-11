from app import application
from app.models import Film


@application.route('/films')
def films():
    new_film = Film("spider-man: far from home", ["fantasy", "sci-fi"])
    new_film.insert()
    return new_film.films().__repr__()
