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
            'name',
            'type',
            'city_id',
            'details'
        )


tourist_attraction_model = api.model('Tourist_Attraction_Demo', {
    'name': fields.String('Sharm'),
    'type': fields.String('EXCURSION'),
    'city_id': fields.Integer(1),
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


class TransportationSchema(ma.Schema):
    class Meta:
        fields = (
            'id',
            'tour_id',
            'transport_type',
            'start_time',
            'end_time',
            'start_city_id',
            'end_city_id',
            'details'
        )


transportation_model = api.model('transportation', {
    'tour_id': fields.Integer(1),
    'transport_type': fields.String('PLANE'),
    'start_time': fields.String('2021-09-19'),
    'end_time': fields.String('2002-09-25'),
    'start_city_id': fields.Integer(1),
    'end_city_id': fields.Integer(2),
    'details': fields.String('Plane is power!!!')
})

transportation_schema = TransportationSchema()
transportations_schema = TransportationSchema(many=True)


class CustomerAddressesSchema(ma.Schema):
    class Meta:
        fields = (
            'id',
            'city_id',
            'zip_code',
            'street',
            'house_number',
            'apartment_number'
        )


customer_addresses_model = api.model('customer_addresses', {
    'city_id': fields.Integer(1),
    'zip_code': fields.String('78AO1'),
    'street': fields.String('Ivan Mazepa'),
    'house_number': fields.String('9A'),
    'apartment_number': fields.Integer(9)
})

customer_addresses_schema = CustomerAddressesSchema()
customer_addressess_schema = CustomerAddressesSchema(many=True)


class HotelSchema(ma.Schema):
    class Meta:
        fields = (
            'id',
            'name',
            'hotel_class',
            'city_id',
            'is_animals_allowed',
            'details'
        )


hotel_model = api.model('hotel', {
    'name': fields.String('Grand'),
    'hotel_class': fields.String('USUAL'),
    'city_id': fields.Integer(1),
    'is_animals_allowed': fields.Boolean(),
    'details': fields.String('The best place!!!')
})

hotel_schema = HotelSchema()
hotels_schema = HotelSchema(many=True)


class UserSchema(ma.Schema):
    class Meta:
        fields = (
            'id',
            'first_name',
            'middle_name',
            'last_name',
            'phone',
            'date_of_birthday',
            'gender',
            'is_baned',
            'password_hash'
        )


user_model = api.model('User_Demo', {
    'first_name': fields.String('Julia'),
    'middle_name': fields.String('Bogdanivna'),
    'last_name': fields.String('Zanevych'),
    'phone': fields.String('0731213007'),
    'date_of_birthday': fields.String('2002-07-14'),
    'gender': fields.String('FEMALE'),
    'is_baned': fields.Boolean(),
    'password_hash':fields.String('Ju234lia')

})

user_schema = UserSchema()
users_schema = UserSchema(many=True)
