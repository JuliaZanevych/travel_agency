from flask_restx import fields

from config import ma, api


class CustomerSchema(ma.Schema):
    class Meta:
        fields = (
            'id',
            'first_name',
            'middle_name',
            'last_name',
            'phone',
            'date_of_birthday',
            'gender',
            'is_covid_vaccinated',
            'is_blocked'
        )


customer_model = api.model('Customer_Demo', {
    'first_name': fields.String('Julia'),
    'middle_name': fields.String('Bogdanivna'),
    'last_name': fields.String('Zanevych'),
    'phone': fields.String('0731213007'),
    'date_of_birthday': fields.String('2002-07-14'),
    'gender': fields.String('FEMALE'),
    'is_covid_vaccinated': fields.Boolean(),
    'is_blocked': fields.Boolean()

})

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)


class CountrySchema(ma.Schema):
    class Meta:
        fields = (
            'id',
            'country_name',
            'official_language',
            'population',
            'details'
        )


country_model = api.model('Country_Demo', {
    'country_name': fields.String('Ukraine'),
    'official_language': fields.String('Ukrainian'),
    'population': fields.Integer(45000000),
    'details': fields.String('details')
})

country_schema = CountrySchema()
countries_schema = CountrySchema(many=True)


class TourSchema(ma.Schema):
    class Meta:
        fields = (
            'id',
            'name',
            'price',
            'person_count',
            'start_time',
            'end_time',
            'description',
            'recommended_pocket_money'
        )


tour_model = api.model('Tour_Demo', {
    'name': fields.String('Uni Sharm Aqua Park'),
    'price': fields.String(300),
    'person_count': fields.String(3),
    'start_time': fields.String('2021-09-19'),
    'end_time': fields.String('2002-09-25'),
    'description': fields.String('Cool tour on Egypt'),
    'recommended_pocket_money': fields.Integer(150)

})

tour_schema = TourSchema()
tours_schema = TourSchema(many=True)


class TouristAttractionSchema(ma.Schema):
    class Meta:
        fields = (
            'id',
            'city_id',
            'name',
            'type',
            'details'
        )


tourist_attraction_model = api.model('Tourist_Attraction_Demo', {
    'city_id': fields.Integer(1),
    'name': fields.String('Sharm'),
    'type': fields.String('EXCURSION'),
    'details': fields.String('Curious tour of the underground city'),

})

tourist_attraction_schema = TouristAttractionSchema()
tourist_attractions_schema = TouristAttractionSchema(many=True)


class CitySchema(ma.Schema):
    class Meta:
        fields = (
            'id',
            'city_name',
            'country_id',
            'city_latitude',
            'city_latitude',
            'details'
        )


city_model = api.model('city', {
    'city_name': fields.String('Lviv'),
    'country_id': fields.Integer(1),
    'city_latitude': fields.String(18.000),
    'city_longitude': fields.Integer(23.00),
    'details': fields.String('One of the most beautiful cities of Ukraine')
})

city_schema = CitySchema()
cities_schema = CitySchema(many=True)
