import sys

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Restaurant(Base):
	__tablename__ = 'restaurant'

	id = Column(Integer, primary_key=True)
	name = Column(String(80), nullable=False)


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