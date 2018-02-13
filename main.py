import hug

@hug.get('/')
def root():
    return 'Hi'