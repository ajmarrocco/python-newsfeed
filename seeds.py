from app.models import User
from app.db import Session, Base, engine

# drop tables
Base.metadata.drop_all(engine)
# creates tables that Base mapped, in class that inherits Base
Base.metadata.create_all(engine)

# Must establish a temporary session connection creating a db object
db = Session()

# insert users
db.add_all([
    User(username='alesmonde0', email='nwestnedge0@cbc.ca', password='password123'),
    User(username='jwilloughway1', email='rmebes1@sogou.com', password='password123'),
    User(username='iboddam2', email='cstoneman2@last.fm', password='password123'),
    User(username='dstanmer3', email='ihellier3@goo.ne.jp', password='password123'),
    User(username='djiri4', email='gmidgley4@weather.com', password='password123')
])

# runs the insert users statements
db.commit()

# Closes connection if you don't need to make another db transaction
db.close()