import os
import urlparse
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class User(Base):
    """
    User class to capture all necessary user info.
    """
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)


class Category(Base):
    """
    Category class that is related to User and Algorithms table.
    """
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    algorithms = relationship('Algorithms', cascade="all, delete-orphan")

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name
        }


class Algorithms(Base):
    """
    Algorithms class that contains all the details on a drink:
    - ID
    - Name
    - Category
    - User
    """
    __tablename__ = 'algorithms'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """
        Return object data in serializeable format
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

engine = create_engine('sqlite:///algorithms.db')
Base.metadata.create_all(engine)
