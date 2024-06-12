from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Database setup
engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
