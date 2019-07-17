import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    A class for environment setup.
    """

    SECRET_KEY = os.getenv('SECRET_KEY',
                           b')\xe8v\xbf\xdf\xac\x0e\xa4\x8a~\xe0q\xab\xc8X\xd6')
    DEBUG = False


class DevelopmentConfig(Config):
    """
    A class for development environment setup.
    """

    DEBUG = True
    MONGODB_DATABASE_URI = 'localhost:127.0.0.1:27017'


class TestingConfig(Config):
    """
    A class for testing environment setup.
    """

    DEBUG = True
    TESTING = True
    MONGODB_DATABASE_URI = 'localhost:127.0.0.1:27017'


class ProductionConfig(Config):
    """
    A class for production environment setup.
    """

    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
