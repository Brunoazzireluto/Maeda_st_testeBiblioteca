import os 
from app import Create_app, db
from app. models import Library, User
from flask_migrate import Migrate

app = Create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Library=Library)


@app.cli.command()
def test():
    """run the unit test"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)