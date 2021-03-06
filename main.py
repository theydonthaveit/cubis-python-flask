from flask import Flask, send_from_directory, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant
# SubRestaurant, Address, RestaurantInfo, MenuItem

Engine = create_engine('postgres://orajzfxrmovnsa:5b924f7d92c7faa14a0eafc35d9b05af4f62981f66583757a53513162f8a9081@ec2-54-247-101-191.eu-west-1.compute.amazonaws.com:5432/dsnmc7ts3e869')
Base.metadata.create_all(Engine)

DBsession = sessionmaker(bind=Engine)
session = DBsession()

app = Flask(__name__, static_folder='static')
app.secret_key = 'super secret key'

@app.route('/')
def root():
    return 'Hi'

@app.route('/restaurants/', methods=['GET'])
def list_restaurants():
    restaurants = session.query(Restaurant).all()
    return jsonify(Restaurants = [r.serialize for r in restaurants])


@app.route('/restaurants/JSON')
def list_restaurants():
    restaurant = session.query(Restaurant).all()
    return jsonify(Restaurant=[i.serialize for i in restaurant])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)