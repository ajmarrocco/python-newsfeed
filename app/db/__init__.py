from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g

# Called because we need use a .env file
load_dotenv()

# connect to database using env variable
# engine manages connection of database
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
# Session creates temporary connections to perform CRUD methods
Session = sessionmaker(bind=engine)
# Base maps models to real MySQL tables
Base = declarative_base()

def init_db(app):
    # creates tables that Base mapped, in class that inherits Base
    Base.metadata.create_all(engine)
    # runs close_db()
    app.teardown_appcontext(close_db)

# returns a new session-connection object
# Can perform additional logic before connection to db
def get_db():
    if 'db' not in g:
        # saves current connection on g object if not already there
        g.db = Session()
    # returns connection of g object instead of creating a new Session instance each time
    return g.db

def close_db(e=None):
    # Attempts to find and remove db from g object
    db = g.pop('db', None)
    # If db doesn't equal None then it will close the db making its value None
    if db is not None:
        # ends connection
        db.close()