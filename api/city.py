from flask import Response, request, jsonify
from flask_restx import Namespace, Resource
from werkzeug.exceptions import NotFound

from config import api, db
from model import City
from schema import city_model, city_schema, cities_schema

ns = Namespace('cities', description='CRUD operations for City essence')
api.add_namespace(ns)


@ns.route('/post')
class CreateCity(Resource):
    @ns.expect(city_model)
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(201, description='Successfully created new City', model=city_model)
    def post(self):
        json = request.json

        city = City(
            city_name=json.get('city_name'),
            country_id=json.get('country_id'),
            city_latitude=json.get('city_latitude'),
            city_longitude=json.get('city_longitude'),
            details=json.get('details'),
        )
        try:
            db.session.add(city)
            db.session.commit()
        except Exception as e:
            orig = e.orig
            if orig:
                args = orig.args
                if len(args) >= 2 and args[0] == 1451:
                    error_message = args[1]
                    if 'a foreign key constraint fails' in error_message:
                        res = jsonify({'message': 'Something attached to cities!'})
                        res.status_code = 409
                        return res
                if len(args) >= 2 and args[0] == 1452:
                    error_message = args[1]
                    if 'Cannot add or update a child row' in error_message:
                        res = jsonify({'message': 'There is no such father row!!'})
                        res.status_code = 409
                        return res
        res = jsonify(city_schema.dump(city))
        res.status_code = 201
        return res


@ns.route('/<int:id>/get')
class GetCity(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully get City', model=city_model)
    @ns.response(404, description='City not found!')
    def get(self, id):
        try:
            city = City.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'City not found!'})
            res.status_code = 404
            return res

        return jsonify(city_schema.dump(city))


@ns.route('/get')
class GetCitys(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully get list of Cities', model=city_model)
    def get(self):
        return jsonify(cities_schema.dump(City.query.all()))


@ns.route('/<int:id>/update')
class UpdateCity(Resource):
    @ns.expect(city_model)
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully updated City', model=city_model)
    @ns.response(404, description='City not found!')
    def put(self, id):
        json = request.json

        try:
            city = City.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'City not found!'})
            res.status_code = 404
            return res
        try:
            city.city_name = json.get('city_name')
            city.country_id = json.get('country_id'),
            city.city_latitude = json.get('city_latitude')
            city.city_longitude = json.get('city_longitude')
            city.details = json.get('details')
            db.session.commit()
        except Exception as e:
            orig = e.orig
            if orig:
                args = orig.args
                if len(args) >= 2 and args[0] == 1451:
                    error_message = args[1]
                    if 'a foreign key constraint fails' in error_message:
                        res = jsonify({'message': 'Something attached to cities!'})
                        res.status_code = 409
                        return res
                if len(args) >= 2 and args[0] == 1452:
                    error_message = args[1]
                    if 'Cannot add or update a child row' in error_message:
                        res = jsonify({'message': 'There is no such father row!!'})
                        res.status_code = 409
                        return res
        return jsonify(city_schema.dump(city))


@ns.route('/<int:id>/delete')
class DeleteCity(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(204, description='Successfully removed City')
    @ns.response(404, description='City not found!')
    def delete(self, id):
        try:
            city = City.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'City not found!'})
            res.status_code = 404
            return res
        try:
            db.session.delete(city)
            db.session.commit()
        except Exception as e:
            orig = e.orig
            if orig:
                args = orig.args
                if len(args) >= 2 and args[0] == 1451:
                    error_message = args[1]
                    if 'a foreign key constraint fails' in error_message:
                        res = jsonify({'message': 'Something attached to cities!'})
                        res.status_code = 409
                        return res
        return Response(status=204)
