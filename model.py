from sqlalchemy import UniqueConstraint

from config import db


# vouchers = db.Table('vouchers',
#                     db.Column('id', db.Integer, primary_key=True, autoincrement=True),
#                     db.Column('tour_id', db.Integer, db.ForeignKey('tours.id'))
#                     )
#
# voucher_customers = db.Table('voucher_customers',
#                              db.Column('voucher_id', db.Integer, db.ForeignKey('vouchers.id')),
#                              db.Column('customer_id', db.Integer, db.ForeignKey('customers.id'))
#                              )
#
# tour_attractions = db.Table('tour_attractions',
#                             db.Column('tour_id', db.Integer, db.ForeignKey('tours.id')),
#                             db.Column('tourist_attractions_id', db.Integer, db.ForeignKey('tourist_attractions.id'))
#                             )
# tour_hotels = db.Table('tour_hotels',
#                        db.Column('tour_id', db.Integer, db.ForeignKey('tours.id')),
#                        db.Column('hotel_id', db.Integer, db.ForeignKey('hotels.id'))
#                        )


class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(64), nullable=False)
    middle_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(124), nullable=False)
    phone = db.Column(db.String(16), nullable=False)
    date_of_birthday = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(64), nullable=False)
    is_covid_vaccinated = db.Column(db.Boolean, nullable=False, default=False)
    is_blocked = db.Column(db.Boolean, default=False)
    password_hash = db.Column(db.String(64), nullable=False)
    # v_customers = db.relationship('v_customers', secondary=voucher_customers)


class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country_name = db.Column(db.String(64), nullable=False)
    official_language = db.Column(db.String(64), nullable=False)
    population = db.Column(db.String(64), nullable=False)
    details = db.Column(db.Integer, nullable=False)
    __table_args__ = tuple((UniqueConstraint('country_name')))


class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city_name = db.Column(db.String(64), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)
    city_latitude = db.Column(db.Float, nullable=False)
    city_longitude = db.Column(db.Float, nullable=False)
    details = db.Column(db.String(64))


class Tour(db.Model):
    __tablename__ = 'tours'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    person_count = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.Date, nullable=False)
    end_time = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(64), nullable=False)
    recommended_pocket_money = db.Column(db.Integer)
    # voucher = db.relationship('voucher', secondary=vouchers)
    # t_attractions = db.relationship('t_attractions', secondary=tour_attractions)
    # t_hotels = db.relationship('t_hotels', secondary=tour_hotels)
    __table_args__ = tuple((UniqueConstraint('name')))


class TouristAttraction(db.Model):
    __tablename__ = 'tourist_attractions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    type = db.Column(db.String(64), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'), nullable=False)
    details = db.Column(db.String(64), nullable=False)


class Transportation(db.Model):
    __tablename__ = 'transportation'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tour_id = db.Column(db.Integer, db.ForeignKey('tours.id'), nullable=False)
    transport_type = db.Column(db.String(64), nullable=False)
    start_time = db.Column(db.Date, nullable=False)
    end_time = db.Column(db.Date, nullable=False)
    start_city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))
    end_city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))
    details = db.Column(db.String(64), nullable=False)


class CustomerAddresses(db.Model):
    __tablename__ = 'customer_addresses'
    id = db.Column(db.Integer, db.ForeignKey('customers.id'), primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'), nullable=False)
    zip_code = db.Column(db.String(16), nullable=False)
    street = db.Column(db.String(34), nullable=False)
    house_number = db.Column(db.String(7), nullable=False)
    apartment_number = db.Column(db.Integer)


class Hotel(db.Model):
    __tablename__ = 'hotels'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    hotel_class = db.Column(db.String(64))
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))
    is_animals_allowed = db.Column(db.Boolean, default=False)
    details = db.Column(db.String(64))


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(64), nullable=False)
    middle_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(124), nullable=False)
    phone = db.Column(db.String(16), nullable=False)
    date_of_birthday = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(64), nullable=False)
    is_baned = db.Column(db.Boolean, default=False, nullable=False)
    password_hash = db.Column(db.String(64), nullable=False)


class Vouchers(db.Model):
    __tablename__ = 'vouchers'
    id = db.Column(db.Integer, primary_key=True)
    tour_id = db.Column(db.Integer, db.ForeignKey("tours.id"), nullable=False)

    tours = db.relationship("Tour")


class VoucherCustomers(db.Model):
    __tablename__ = 'voucher_customers'
    # column_not_exist_in_db = db.Column(db.Integer, primary_key=True)
    voucher_id = db.Column(db.Integer, db.ForeignKey("vouchers.id"), primary_key=True, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"),  primary_key=True, nullable=False)

    vouchers = db.relationship("Vouchers")
    customers = db.relationship("Customer")


class TourHotels(db.Model):
    __tablename__ = 'tour_hotels'
    column_not_exist_in_db = db.Column(db.Integer, primary_key=True)
    tour_id = db.Column(db.Integer, db.ForeignKey("tours.id"), nullable=False)
    hotel_id = db.Column(db.Integer, db.ForeignKey("hotels.id"), nullable=False)

    tours = db.relationship("Tour")
    hotels = db.relationship("Hotel")


class TourAttraction(db.Model):
    __tablename__ = 'tour_attractions'
    # column_not_exist_in_db = db.Column(db.Integer, primary_key=True)
    tour_id = db.Column(db.Integer, db.ForeignKey("tours.id"), primary_key=True, nullable=False)
    tourist_attractions_id = db.Column(db.Integer, db.ForeignKey("tourist_attractions.id"), primary_key=True,
                                       nullable=False)

    tours = db.relationship("Tour")
    tourist_attractions = db.relationship("TouristAttraction")
