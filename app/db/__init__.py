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

def init_db():
    # creates tables that Base mapped, in class that inherits Base
    Base.metadata.create_all(engine)

# returns a new session-connection object
# Can perform additional logic before connection to db
def get_db():
    if 'db' not in g:
        # saves current connection on g object if not already there
        g.db = Session()
    # returns connection of g object instead of creating a new Session instance each time
    return g.db