from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import config

Base = declarative_base()

class User(Base):
    """Represents A User Entity."""
    
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

# create an engine and a session factory
engine = create_engine(config.database_url)
Session = sessionmaker(bind=engine)

def init_db():
    """Initialize the database and create tables."""
    Base.metadata.create_all(engine)
    print("Database initialized.")
