from app import application
from app.database import DB


@application.route('/films')
def films():
    """Returns all films in database in a representational string."""
    return DB.find_all("films").__repr__()
