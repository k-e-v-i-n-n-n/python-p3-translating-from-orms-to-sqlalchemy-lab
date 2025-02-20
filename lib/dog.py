from models import Dog
# import sqlalchemy

from sqlalchemy import (create_engine, desc,
    Index, Column, DateTime, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# if __name__ == '__main__':
#     engine = create_engine('sqlite:///:memory:')
#     Base.metadata.create_all(engine)

#     # use our engine to configure a 'Session' class
#     Session = sessionmaker(bind=engine)
#     # use 'Session' class to create 'session' object
#     session = Session()

def create_table(base, engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    base.metadata.create_all(engine)
    return session
       
def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()


def find_by_name(session, name):
   return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name).filter(Dog.breed == breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()

