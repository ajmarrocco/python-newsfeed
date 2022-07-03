from datetime import datetime
from select import select
from app.db import Base
from .Vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property

# inherits from Base class created in app/db
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    post_url = Column(String(100), nullable=False)
    # referecnes user table
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    # Prpoerty that performs a SELECT, together with func.count to add up votes
    vote_count = column_property(
        select([func.count(Vote.id)]).where(Vote.post_id == id)
    )

    # Query for post should also return info about user
    user = relationship('User')
    # Cascade delete, deletes all comments associated with posts
    comments = relationship('Comment', cascade='all,delete')
    # Cascade delete, deletes all votes associated with posts
    votes = relationship('Vote', cascade='all,delete')

