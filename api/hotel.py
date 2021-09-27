from flask import Response, request, jsonify
from flask_restx import Namespace, Resource
from werkzeug.exceptions import NotFound

from config import api, db
from model import Hotel
from schema import hotel_model, hotel_schema, hotels_schema

ns = Namespace('hotels', description='CRUD operations for Hotel addresses essence')
api.add_namespace(ns)


@ns.route('/post')
class CreateHotel(Resource):
    @ns.expect(hotel_model)
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(201, description='Successfully created new Hotel', model=hotel_model)
    def post(self):
        json = request.json

        hotel = Hotel(
            name=json.get('name'),
            hotel_class=json.get('hotel_class'),
            city_id=json.get('city_id'),
            is_animals_allowed=json.get('is_animals_allowed'),
            details=json.get('details'),
        )
        db.session.add(hotel)
        db.session.commit()

        res = jsonify(hotel_schema.dump(hotel))
        res.status_code = 201
        return res


@ns.route('/<int:id>/get')
class GetHotel(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully get Hotel', model=hotel_model)
    @ns.response(404, description='Hotel not found!')
    def get(self, id):
        try:
            hotel = Hotel.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Hotel not found!'})
            res.status_code = 404
            return res

        return jsonify(hotel_schema.dump(hotel))


@ns.route('/get')
class GetHotels(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully get list of Hotels', model=hotel_model)
    def get(self):
        return jsonify(hotels_schema.dump(Hotel.query.all()))


@ns.route('/<int:id>/update')
class UpdateHotel(Resource):
    @ns.expect(hotel_model)
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully updated Hotel', model=hotel_model)
    @ns.response(404, description='Hotel  not found!')
    def put(self, id):
        json = request.json

        try:
            hotel = Hotel.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Hotel not found!'})
            res.status_code = 404
            return res
        hotel.name = json.get('name')
        hotel.hotel_class = json.get('hotel_class')
        hotel.city_id = json.get('city_id')
        hotel.is_animals_allowed = json.get('is_animals_allowed')
        hotel.details = json.get('details')
        db.session.commit()
        return jsonify(hotel_schema.dump(hotel))


@ns.route('/<int:id>/delete')
class DeleteHotel(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(204, description='Successfully removed Hotel')
    @ns.response(404, description='Hotel not found!')
    def delete(self, id):
        try:
            hotel = Hotel.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Hotel not found!'})
            res.status_code = 404
            return res
        db.session.delete(hotel)
        db.session.commit()
        return Response(status=204)
