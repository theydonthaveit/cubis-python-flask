import hug

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base

Engine = create_engine('postgres://orajzfxrmovnsa:5b924f7d92c7faa14a0eafc35d9b05af4f62981f66583757a53513162f8a9081@ec2-54-247-101-191.eu-west-1.compute.amazonaws.com:5432/dsnmc7ts3e869')
Base.metadata.create_all(Engine)

DBsession = sessionmaker(bind=Engine)
session = DBsession()

@hug.get('/')
def root():
    return 'Hi'

@hug.get('/restaurants/')
def list_restaurants(output=hug.output_format.json):
    restaurants = session.query(Restaurant).all()
    Restaurants = [r.serialize for r in restaurants]
    return Restaurants