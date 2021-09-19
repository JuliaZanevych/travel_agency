from config import app

from api import \
    hello_world, \
    customer, \
    country, \
    tour, \
    tourist_attraction, \
    city

if __name__ == '__main__':
    app.run(debug=True)
