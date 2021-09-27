from sqlalchemy import UniqueConstraint

from config import db


class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    middle_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    date_of_birthday = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String, nullable=False)
    is_covid_vaccinated = db.Column(db.Boolean, nullable=False, default=False)
    is_blocked = db.Column(db.Boolean, default=False)


class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country_name = db.Column(db.String, nullable=False)
    official_language = db.Column(db.String, nullable=False)
    population = db.Column(db.String, nullable=False)
    details = db.Column(db.Integer, nullable=False)
    __table_args__ = tuple((UniqueConstraint('country_name')))


class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city_name = db.Column(db.String, nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)
    city_latitude = db.Column(db.Float, nullable=False)
    city_longitude = db.Column(db.Float, nullable=False)
    details = db.Column(db.String)


class Tour(db.Model):
    __tablename__ = 'tours'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    person_count = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.Date, nullable=False)
    end_time = db.Column(db.Date, nullable=False)
    description = db.Column(db.String, nullable=False)
    recommended_pocket_money = db.Column(db.Integer)
    __table_args__ = tuple((UniqueConstraint('name')))


class TouristAttraction(db.Model):
    __tablename__ = 'tourist_attractions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'), nullable=False)
    details = db.Column(db.String, nullable=False)


class Transportation(db.Model):
    __tablename__ = 'transportation'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tour_id = db.Column(db.Integer, db.ForeignKey('tours.id'), nullable=False)
    transport_type = db.Column(db.String, nullable=False)
    start_time = db.Column(db.Date, nullable=False)
    end_time = db.Column(db.Date, nullable=False)
    start_city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))
    end_city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))
    details = db.Column(db.String, nullable=False)


class CustomerAddresses(db.Model):
    __tablename__ = 'customer_addresses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'), nullable=False)
    zip_code = db.Column(db.String, nullable=False)
    street = db.Column(db.String, nullable=False)
    house_number = db.Column(db.String, nullable=False)
    apartment_number = db.Column(db.Integer)


class Hotel(db.Model):
    __tablename__ = 'hotels'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    hotel_class = db.Column(db.String)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))
    is_animals_allowed = db.Column(db.Boolean, default=False)
    details = db.Column(db.String)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    middle_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    date_of_birthday = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String, nullable=False)
    is_baned = db.Column(db.Boolean, default=False, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
