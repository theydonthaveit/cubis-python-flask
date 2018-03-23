from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Engine, Restaurant, UserAccount
# SubRestaurant, Address, RestaurantInfo, MenuItem

Base.metadata.create_all(Engine)

DBsession = sessionmaker(bind=Engine)
session = DBsession()

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/')
def root():
    return 'HOME'

@app.route('/restaurants/list', methods=['GET'])
def list_restaurants():
    return render_template('restaurants.html')


@app.route('/restaurant_dashboard/<int: restaurant_id>')
def restaurant_dashboard(restaurant_id):
    

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)