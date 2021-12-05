from config import app

from api import \
    hello_world, \
    customer, \
    country, \
    tour, \
    tourist_attraction, \
    city, \
    transportation, \
    customer_addresses, \
    hotel, \
    voucher, \
    role, \
    permission

if __name__ == '__main__':
    app.run(debug=True)
