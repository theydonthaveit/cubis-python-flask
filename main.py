import hug

@hug.get('/')
def root():
    return 'Hi'

@hug.get('/restaurants/')
def list_restaurants(output=hug.output_format.json):
    restaurants = [{
        'name': 'Goat House',
        'seating': 50,
        'location': 'SE1 6DE',
        'cusine': 'British Goats Only'
    },{
        'name': 'Jungle Boot',
        'seating': 25,
        'location': 'SE7 6FF',
        'cusine': 'British Jungle Boots Only'
    }]
    return restaurants