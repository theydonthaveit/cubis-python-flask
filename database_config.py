import sys
import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
# from passlib.hash import pbkdf2_sha512

Base = declarative_base()


class BaseMixin(object):

@declared_attr
    def id(self):
        return Column(Integer, primary_key=True, unique=True)

    @declared_attr
    def created_at(self):
        return Column(DateTime, default=datetime.datetime.utcnow)

    @declared_attr
    def updated_at(self):
        return Column(DateTime, default=datetime.datetime.utcnow)

class MenuItem(Base, BaseMixin):
    __tablename__ = 'menu_item'

    course = Column(String(250), nullable=False)
    description = Column(String(500), nullable=False)
    price = Column(String(8), nullable=False)
    ingredients = Column(String(250), nullable=False)
    allergies = Column(String(250), nullable=False)
    # subsidiary_restaurant = relationship(SubRestaurant, back_populates="menu_item")
    # subsidiary_restaurant_id = Column(Integer, ForeignKey('subsidiary_restaurant.id'))


Engine = create_engine('postgres://localhost:5434/cubis')
Base.metadata.create_all(Engine)