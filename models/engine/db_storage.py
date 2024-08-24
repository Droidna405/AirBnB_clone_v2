#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models in a database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a new DBStorage object"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(f"mysql+mysqldb://{user}:{password}@{host}/{db}", pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)

    def all(self, cls=None):
        """Query all objects in the database and return them"""
        if cls is None:
            objs = self.__session.query(User, Place, State, City, Amenity, Review).all()
        else:
            objs = self.__session.query(cls).all()
        return {f"{obj.__class__.__name__}.{obj.id}": obj for obj in objs}

    def new(self, obj):
        """Add a new object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload the current database session"""
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        """Remove the current session"""
        self.__session.remove()
