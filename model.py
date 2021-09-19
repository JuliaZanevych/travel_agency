from config import db


class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String)
    middle_name = db.Column(db.String)
    last_name = db.Column(db.String)
    phone = db.Column(db.String)
    date_of_birthday = db.Column(db.Date)
    gender = db.Column(db.String)
    is_covid_vaccinated = db.Column(db.Boolean, default=False)
    is_blocked = db.Column(db.Boolean, default=False)


class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    county_name = db.Column(db.String)
    official_language = db.Column(db.String)
    population = db.Column(db.String)
    details = db.Column(db.Integer)


class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city_name = db.Column(db.String)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    city_latitude = db.Column(db.Float)
    city_longitude = db.Column(db.Float)
    details = db.Column(db.String)


class Tour(db.Model):
    __tablename__ = 'tours'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    person_count = db.Column(db.Integer)
    start_time = db.Column(db.Date)
    end_time = db.Column(db.Date)
    description = db.Column(db.String)
    recommended_pocket_money = db.Column(db.Integer)


class TouristAttraction(db.Model):
    __tablename__ = 'tourist-attractions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))
    name = db.Column(db.String)
    type = db.Column(db.String)
    details = db.Column(db.String)
