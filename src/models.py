import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String,unique=True, nullable=False)
    password=Column(String,nullable=False)

class Film(Base):
    __tablename__ ="films"
    id =Column(Integer,primary_key=True)
    Name = Column(String)
    Duration = Column(String)
    Director = Column(String)
    planets=Column(Integer,ForeignKey("planets.id"))
    vehicles=Column(Integer,ForeignKey("vehicles.id"))
    characters=Column(Integer,ForeignKey("person.id"))

class Planet(Base):
    __tablename__ ="planets"
    id =Column(Integer,primary_key=True)
    population = Column(String)
    clime = Column(String)
    color = Column(String)
    name = Column(String)
    homeworld=Column(Integer,ForeignKey("planets.id"))

class Vehicle(Base):
    __tablename__ ="vechicles"
    id =Column(Integer,primary_key=True)
    name = Column(String)
    model = Column(String)
    color = Column(String)
    pilots = Column(String,ForeignKey("person.id"))




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
