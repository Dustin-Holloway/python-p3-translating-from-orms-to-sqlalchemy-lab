from datetime import datetime

from sqlalchemy import (create_engine, desc, func,
    CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,
    Index, Column, DateTime, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from models import Dog

def create_table(base, engine):
    base.metadata.bind = engine
    base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
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
    return session.query(Dog.name, Dog.breed).filter(Dog.name == name, Dog.breed == breed).first()

def update_breed(session, dog, breed):
    for dog in session.query(Dog):
        dog.breed = breed

    