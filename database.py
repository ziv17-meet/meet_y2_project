from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey 

#from database_setup import Base, Recipies
Base = declarative_base()




class Recipes(Base):
	__tablename__ = 'recipes'
	id = Column(Integer, primary_key=True)
	category = Column(String)
	ingredients = Column(String)
#	image = Column(String)
	instructors = Column(String)
#	special = Column(String)
	comments = Column(String)
#	like = Column(String)
#	dislike = Column(String)
	caption = Column(String)

#class Like(base):
#	__tablename__= 'like'
#	id= column(Integer, primary_key=True)
#   status_id = column(Integer)
#  like = column(Integer)
# un_like = column(Integer)

#ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;  ?
	
engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

