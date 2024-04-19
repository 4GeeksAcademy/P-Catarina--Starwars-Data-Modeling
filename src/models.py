import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(25), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(50), nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    climate = Column(String(50), nullable=False)
    terrain = Column(String(50), nullable=False)
    population = Column(Integer, nullable=False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    char_name = Column(String(50), nullable=False)
    bio = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    gender = Column(String(50), nullable=False)
    movies = Column(String(250))
    homeworld = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    fav__char_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    fav_planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
