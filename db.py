from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


# create database engine with sessionmaker 
engine = create_engine('sqlite:///manager.db')
Session = sessionmaker(bind=engine)
session = Session()

# create base model 
Base = declarative_base()