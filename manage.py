import unittest

from api.main_mongoengine import app

app.app_context().push()


def run():
    app.run()


def test():
    tests = unittest.TestLoader().discover('api/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    run()
