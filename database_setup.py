import sys

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Restaurant(Base):
	__tablename__ = 'restaurant'

	id = Column(Integer, primary_key=True)
	name = Column(String(120), nullable=False)


	@property
	def serialize(self):
		return {
			'id': self.id,
			'name': self.name,
			'_links': {
				'self': {
					'rel': 'Display Restaurant name and corresponding content',
					'href': '/restaurant/{id}/'
				}
			}
		}


# class SubRestaurant(Base):
#     __tablename__ = 'subsidiary_restaurant'

#     id = Column(Integer, primary_key=True)
#     name = Column(String(80), nullable=False)
#     restaurant = relationship(Restaurant, back_populates="subsidiary_restaurant")
#     restaurant_id = Column(Integer, ForeignKey('restaurant.id'))

#     @property
#     def serialize(self):
# 	    return {
# 			'id': self.id,
# 			'name': self.name,
# 			'parent_restaurant': self.restaurant,
# 		}


# class Address(Base):
#     __tablename__ = 'addresses'

#     id = Column(Integer, primary_key=True)
#     subsidiary_restaurant = relationship(SubRestaurant, back_populates="addresses")
#     subsidiary_restaurant_id = Column(Integer, ForeignKey('subsidiary_restaurant.id'))
#     address_line_one = Column(String(80), nullable=False)
#     address_line_two = Column(String(80), nullable=True)
#     city = Column(String(80), nullable=False)
#     country = Column(String(80), nullable=False)
#     postcode = Column(String(80), nullable=False)
#     long = Column(String(80), nullable=False)
#     lat = Column(String(80), nullable=False)

#     @property
#     def serialize(self):
# 	    return {
# 			'id': self.id,
# 			'subsidiary_restaurant': self.subsidiary_restaurant,
#             'address_line_one': self.address_line_one,
# 		    'address_line_two': self.address_line_two,
# 		    'city': self.city,
# 		    'country': self.country,
#             'postcode': self.postcode,
# 			'long': self.long,
# 			'lat': self.lat
# 		}


# class RestaurantInfo(Base):
#     __tablename__ = 'restaurant_info'

#     id = Column(Integer, primary_key=True)
#     subsidiary_restaurant = relationship(SubRestaurant, back_populates="restaurant_info")
#     subsidiary_restaurant_id = Column(Integer, ForeignKey('subsidiary_restaurant.id'))
#     addresses = relationship(Address, back_populates="restaurant_info")
#     addresses_id = Column(Integer, ForeignKey('addresses.id'))
#     seating = Column(Integer, nullable=False)
#     cuisine = Column(String(100), nullable=False)

#     @property
#     def serialize(self):
# 	    return {
# 			'id': self.id,
# 			'subsidiary_restaurant': self.subsidiary_restaurant,
# 			'addresses': self.addresses,
# 			'seating': self.seating,
# 			'cuisine': self.cuisine,
# 		}


# # class RestaurantQueue(Base):


# # class RestaurantTransactions(Base):


# # class RestaurantReviews(Base):


# # class RestaurantDisputes(Base):


# # class Menu(Base):


# class MenuItem(Base):
# 	__tablename__ = 'menu_item'

# 	id = Column(Integer, primary_key=True)
# 	course = Column(String(250))
# 	description = Column(String(500))
# 	price = Column(String(8))
# 	ingredients = Column(String(250), nullable=False)
# 	subsidiary_restaurant = relationship(SubRestaurant, back_populates="menu_item")
# 	subsidiary_restaurant_id = Column(Integer, ForeignKey('subsidiary_restaurant.id'))

# 	@property
# 	def serialize(self):
# 		return {
# 			'id': self.id,
# 			'course': self.course,
# 			'description': self.description,
# 			'price': self.price,
# 			'restaurant': self.subsidiary_restaurant
# 		}


# class Address(Base):
# 	__tablename__ = 'addresses'

# 	restaurant = relationship(Restaurant, back_populates="addresses")
# 	restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
# 	address_line_one = Column(String(80), nullable=False)
# 	address_line_two = Column(String(80), nullable=True)
# 	city = Column(String(80), nullable=False)
# 	country = Column(String(80), nullable=False)
# 	postcode = Column(String(80), nullable=False)

# 	@property
# 	def serialize(self):
# 		return {
# 			'address_line_one': self.address_line_one,
# 			'address_line_two': self.address_line_two,
# 			'city': self.city,
# 			'country': self.country,
# 			'postcode': self.postcode
# 		}

# class MenuItem(Base):
# 	__tablename__ = 'menu_item'

# 	id = Column(Integer, primary_key=True)
# 	course = Column(String(250))
# 	description = Column(String(250))
# 	price = Column(String(8))
# 	restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
# 	restaurant = relationship(Restaurant)

# 	@property
# 	def serialize(self):
# 		return {
# 			'course': self.course,
# 			'description': self.description,
# 			'id': self.id,
# 			'price': self.price,
# 		}


engine = create_engine('postgres://orajzfxrmovnsa:5b924f7d92c7faa14a0eafc35d9b05af4f62981f66583757a53513162f8a9081@ec2-54-247-101-191.eu-west-1.compute.amazonaws.com:5432/dsnmc7ts3e869')
Base.metadata.create_all(engine)