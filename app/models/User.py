from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates

# inherits from Base class created in app/db
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)

    @validates('email')
    def validate_email(self, key, email):
        # make sure email address contains @ character
        # throws false if not happening
        assert '@' in email
        # returns value of email column
        return email

    @validates('password')
    def validate_password(self, key, password):
        # checks length of password
        assert len(password) > 4

        return password