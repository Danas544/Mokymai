import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///projektai.db')
Base = declarative_base()

class Projektas(Base):
    __tablename__ = 'Projektas'
    id = Column(Integer, primary_key=True)
    name = Column("Pavadinimas", String)
    price = Column("Kaina", Float)
    created_date = Column("Sukūrimo data", DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.id} {self.name} - {self.price}: {self.created_date}"

class table2(Base):
    __tablename__ = 'table2'
    id = Column(Integer, primary_key=True)
    name = Column("Pavadinimas", String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.id} {self.name} "


class table3(Base):
    __tablename__ = 'table3'
    id = Column(Integer, primary_key=True)


    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.id}"

class table5(Base):
    __tablename__ = 'table5'
    id = Column(Integer, primary_key=True)
    name = Column("name", String)

    def __repr__(self):
        return f"{self.id} {self.name}"

Base.metadata.create_all(engine)