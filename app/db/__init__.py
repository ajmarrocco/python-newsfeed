from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Called because we need use a .env file
load_dotenv()

# connect to database using env variable
# engine manages connection of database
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
# Session creates temporary connections to perform CRUD methods
Session = sessionmaker(bind=engine)
# Base aps models to real MySQL tables
Base = declarative_base()