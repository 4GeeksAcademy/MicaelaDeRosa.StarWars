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
    likes=relationship("likes",back_populates="user")


class Likes(Base):
    __tablename__ ="favorites"
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey("users.id"))
    planet_id = Column(Integer,ForeignKey("planets.id"))
    vehicle_id = Column(Integer,ForeignKey("vehicles.id"))
    character_id = Column(Integer,ForeignKey("people.id"))
    film_id = Column(String,ForeignKey("species.id"))
    user = relationship("user",back_populates="likes")
    planet = relationship("Planet")
    character = relationship("Person")
    vehicle = relationship("Vehicle")
    starship = relationship("Starship")
    film = relationship("Film")

class Vehicle(Base):
    __tablename__ ="vehicles"
    id =Column(Integer,primary_key=True)
    name = Column(String)
    model = Column(String)
    manufacturer = Column(String)
    cost_in_credits = Column(String)
    vehicle_class = Column(String)
    pilots = Column(String,ForeignKey("people.id"))   
    films = Column(String,ForeignKey("films.id"))    

class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    classification = Column(String)
    designation = Column(String)
    average_height = Column(String)
    average_lifespan = Column(String)
    hair_colors = Column(String)
    homeworld = Column(Integer, ForeignKey('planets.id'))
    people = Column(String, ForeignKey('people.id'))

class Film(Base):
    __tablename__ ="films"
    id =Column(Integer,primary_key=True)
    title = Column(String)
    director = Column(String)
    opening_crawl = Column(String)
    episode_id = Column(Integer)
    planets = Column(Integer,ForeignKey("planets.id"))
    vehicles = Column(Integer,ForeignKey("vehicles.id"))
    characters = Column(Integer,ForeignKey("people.id"))
    species = Column(String,ForeignKey("species.id"))
    starships = Column(String,ForeignKey("starships.id"))


class Planet(Base):
    __tablename__ ="planets"
    id =Column(Integer,primary_key=True)
    population = Column(String)
    diameter = Column(String)
    terrain = Column(String)
    name = Column(String)
    rotation_period=Column(String)

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    model = Column(String)
    starship_class = Column(String)
    manufacturer = Column(String)
    cost_in_credits = Column(String)
    lenght = Column(String)
    passengers = Column(String)
    pilots = Column(String, ForeignKey('people.id'))
    name = Column (String)

class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    height = Column(String)
    mass = Column(String)
    hair_color = Column(String)
    skin_color = Column(String)
    birth_year = Column(String)
    gender = Column(String)
    name = Column(String)
    homeworld = Column(Integer, ForeignKey('planets.id'))




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
