from flask import Response, request, jsonify
from flask_restx import Namespace, Resource
from werkzeug.exceptions import NotFound

from api.auth import auth
from config import api, db
from model import Hotel
from schema import hotel_model, hotel_schema, hotels_schema

ns = Namespace('hotels', description='CRUD operations for Hotel addresses essence')
api.add_namespace(ns)


@ns.route('/post')
class CreateHotel(Resource):
    @ns.expect(hotel_model)
    @ns.param(name='Authorization', description='Basic access authentication token', _in='header', required=True)
    @ns.response(201, description='Successfully created new Hotel', model=hotel_model)
    @ns.response(401, description='Customer is not authenticated!', model=hotel_model)
    @ns.response(403, description='Customer is not authorized!', model=hotel_model)
    @auth("CREATE_HOTEL")
    def post(self):
        json = request.json

        hotel = Hotel(
            name=json.get('name'),
            hotel_class=json.get('hotel_class'),
            city_id=json.get('city_id'),
            is_animals_allowed=json.get('is_animals_allowed'),
            details=json.get('details'),
        )
        try:
            db.session.add(hotel)
            db.session.commit()
        except Exception as e:
            orig = e.orig
            if orig:
                args = orig.args
                if len(args) >= 2 and args[0] == 1062:
                    error_message = args[1]
                    if 'Duplicate entry' in error_message:
                        res = jsonify({'message': 'There is already address for this customer!!'})
                        res.status_code = 409
                        return res
                if len(args) >= 2 and args[0] == 1452:
                    error_message = args[1]
                    if 'Cannot add or update a child row' in error_message:
                        res = jsonify({'message': 'There is no such father row!!'})
                        res.status_code = 409
                        return res
            raise e
        res = jsonify(hotel_schema.dump(hotel))
        res.status_code = 201
        return res


@ns.route('/<int:id>/get')
class GetHotel(Resource):
    @ns.param(name='Authorization', description='Basic access authentication token', _in='header', required=True)
    @ns.response(200, description='Successfully get Hotel', model=hotel_model)
    @ns.response(404, description='Hotel not found!')
    @ns.response(401, description='Customer is not authenticated!', model=hotel_model)
    @ns.response(403, description='Customer is not authorized!', model=hotel_model)
    @auth("GET_HOTEL_BY_ID")
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
    @ns.param(name='Authorization', description='Basic access authentication token', _in='header', required=True)
    @ns.response(200, description='Successfully get list of Hotels', model=hotel_model)
    @ns.response(401, description='Customer is not authenticated!', model=hotel_model)
    @ns.response(403, description='Customer is not authorized!', model=hotel_model)
    @auth("GET_HOTELS_LIST")
    def get(self):
        return jsonify(hotels_schema.dump(Hotel.query.all()))


@ns.route('/<int:id>/update')
class UpdateHotel(Resource):
    @ns.expect(hotel_model)
    @ns.param(name='Authorization', description='Basic access authentication token', _in='header', required=True)
    @ns.response(200, description='Successfully updated Hotel', model=hotel_model)
    @ns.response(404, description='Hotel  not found!')
    @ns.response(401, description='Customer is not authenticated!', model=hotel_model)
    @ns.response(403, description='Customer is not authorized!', model=hotel_model)
    @auth("UPDATE_HOTEL")
    def put(self, id):
        json = request.json

        try:
            hotel = Hotel.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Hotel not found!'})
            res.status_code = 404
            return res
        try:
            hotel.name = json.get('name')
            hotel.hotel_class = json.get('hotel_class')
            hotel.city_id = json.get('city_id')
            hotel.is_animals_allowed = json.get('is_animals_allowed')
            hotel.details = json.get('details')
            db.session.commit()
        except Exception as e:
            orig = e.orig
            if orig:
                args = orig.args
                if len(args) >= 2 and args[0] == 1062:
                    error_message = args[1]
                    if 'Duplicate entry' in error_message:
                        res = jsonify({'message': 'There is already address for this customer!!'})
                        res.status_code = 409
                        return res
                if len(args) >= 2 and args[0] == 1452:
                    error_message = args[1]
                    if 'Cannot add or update a child row' in error_message:
                        res = jsonify({'message': 'There is no such father row!!'})
                        res.status_code = 409
                        return res
            raise e
        return jsonify(hotel_schema.dump(hotel))


@ns.route('/<int:id>/delete')
class DeleteHotel(Resource):
    @ns.param(name='Authorization', description='Basic access authentication token', _in='header', required=True)
    @ns.response(204, description='Successfully removed Hotel')
    @ns.response(404, description='Hotel not found!')
    @ns.response(401, description='Customer is not authenticated!', model=hotel_model)
    @ns.response(403, description='Customer is not authorized!', model=hotel_model)
    @auth("DELETE_HOTEL")
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
