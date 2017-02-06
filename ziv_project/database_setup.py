from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()

class Recipes(Base):
	__tablename__ = 'recipes'
	id = Column(Integer, primary_key=True)
	catagory = Column(String)
	ingredients = Column(String)
	images = Column(string)
	instructors = Column(String)
	special = Column(String)
	comments = Column(String)
	like = Column(String)
	dislike = Column(String)
	caption = Column(String)


