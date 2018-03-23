import sys
import datetime

from flask_login import LoginManager, UserMixin
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from passlib.hash import pbkdf2_sha512

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



class UserAccount(Base, BaseMixin, UserMixin):
    __tablename__ = 'user_account'

    def __init__(self, username, passcode, mobile, email, ip_address):
        self.username = username
        self.password = pbkdf2_sha512.hash(passcode)
        self.mobile = mobile
        self.email = email
        self.ip_address = ip_address

    username = Column(String(80), nullable=False)
    password = Column(String(1000), nullable=False)
    mobile = Column(String(15), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    ip_address = Column(String(15), nullable=False)
    is_verified = Column(Boolean, nullable=False, default=False)

    def is_verified_check(self):
        return self.is_verified

    def decode_password(self, password):
        return pbkdf2_sha512.verify(password, self.password)


class Restaurant(Base, BaseMixin):
    	__tablename__ = 'restaurant'

	name = Column(String(120), nullable=False)
	user = relationship(UserAccount, back_populates="user_account")
	user_id = Column(Integer, ForeignKey('user_account.id'))


class SubRestaurant(Base, BaseMixin):
    __tablename__ = 'subsidiary_restaurant'

    name = Column(String(80), nullable=False)
    restaurant = relationship(Restaurant, back_populates="subsidiary_restaurant")
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))


class Address(Base, BaseMixin):
    __tablename__ = 'addresses'

    subsidiary_restaurant = relationship(SubRestaurant, back_populates="addresses")
    subsidiary_restaurant_id = Column(Integer, ForeignKey('subsidiary_restaurant.id'))
    address_line_one = Column(String(80), nullable=False)
    address_line_two = Column(String(80), nullable=True)
    city = Column(String(80), nullable=False)
    country = Column(String(80), nullable=False)
    postcode = Column(String(80), nullable=False)
    long = Column(String(80), nullable=False)
    lat = Column(String(80), nullable=False)


class RestaurantInfo(Base, BaseMixin):
    __tablename__ = 'restaurant_info'

    subsidiary_restaurant = relationship(SubRestaurant, back_populates="restaurant_info")
    subsidiary_restaurant_id = Column(Integer, ForeignKey('subsidiary_restaurant.id'))
    addresses = relationship(Address, back_populates="restaurant_info")
    addresses_id = Column(Integer, ForeignKey('addresses.id'))
    seating = Column(Integer, nullable=False)
    cuisine = Column(String(100), nullable=False)


class MenuItem(Base):
    	__tablename__ = 'menu_item'

	course = Column(String(250))
	description = Column(String(500))
	price = Column(String(8))
	ingredients = Column(String(250), nullable=False)
	subsidiary_restaurant = relationship(SubRestaurant, back_populates="menu_item")
	subsidiary_restaurant_id = Column(Integer, ForeignKey('subsidiary_restaurant.id'))



Engine = create_engine('postgres://uzmbizckonpkrz:f98d7f3d375ce1cbdde41b455baa3586054bcf82caa6facb5d82dfacf9f3050a@ec2-79-125-12-27.eu-west-1.compute.amazonaws.com:5432/d833fj11bma730')
Base.metadata.create_all(Engine)