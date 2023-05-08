from sqlalchemy.orm import relationship, sessionmaker
from model import engine

Session = sessionmaker(bind=engine)
session = Session()