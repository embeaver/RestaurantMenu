# Creating a database with SQLAlchemy

# Part 1: Configuration

# Import Libraries
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

# Part 2 Classes
class Restaurant(Base):
    # Creating a table
    __tablename__ = 'restaurant'
    # Mapper
    # nullable = False means this cannot be created without a name
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key=True)

class MenuItem(Base):
    # Creating a table
    __tablename__ = 'menu_item'
    # Mapper
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)



#### insert at end of file ####
engine = create_engine(
    'sqlite:///restaurantmenu.db'
)

Base.metadata.create_all(engine)