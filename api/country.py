from flask import Response, request, jsonify
from flask_restx import Namespace, Resource
from werkzeug.exceptions import NotFound

from config import api, db
from model import Country
from schema import country_model, country_schema, countries_schema

ns = Namespace('countries', description='CRUD operations for Country essence')
api.add_namespace(ns)


@ns.route('/post')
class CreateCountry(Resource):
    @ns.expect(country_model)
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(201, description='Successfully created new Country', model=country_model)
    def post(self):
        json = request.json

        try:
            country = Country(
                country_name=json.get('country_name'),
                official_language=json.get('official_language'),
                population=json.get('population'),
                details=json.get('details'),
            )
            db.session.add(country)
            db.session.commit()
        except Exception as e:
            orig = e.orig
            if orig:
                args = orig.args
                if len(args) >= 2 and args[0] == 1062:
                    error_message = args[1]
                    if 'countries.country_name' in error_message:
                        res = jsonify({'message': 'There is already the country with this name!'})
                        res.status_code = 409
                        return res
        res = jsonify(country_schema.dump(country))
        res.status_code = 201
        return res


@ns.route('/<int:id>/get')
class GetCountry(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully get Country', model=country_model)
    @ns.response(404, description='Country not found!')
    def get(self, id):
        try:
            country = Country.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Country not found!'})
            res.status_code = 404
            return res

        return jsonify(country_schema.dump(country))


@ns.route('/get')
class GetCustomers(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully get list of Countries', model=country_model)
    def get(self):
        return jsonify(countries_schema.dump(Country.query.all()))


@ns.route('/<int:id>/update')
class UpdateCountry(Resource):
    @ns.expect(country_model)
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully updated Country', model=country_model)
    @ns.response(404, description='Country not found!')
    def put(self, id):
        json = request.json

        try:
            country = Country.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Country not found!'})
            res.status_code = 404
            return res
        try:
            country.country_name = json.get('country_name')
            country.official_language = json.get('official_language')
            country.population = json.get('population')
            country.details = json.get('details')
            db.session.commit()
        except Exception as e:
            orig = e.orig
            if orig:
                args = orig.args
                if len(args) >= 2 and args[0] == 1062:
                    error_message = args[1]
                    if 'countries.country_name' in error_message:
                        res = jsonify({'message': 'There is already the country with this name!'})
                        res.status_code = 409
                        return res
        return jsonify(country_schema.dump(country))


@ns.route('/<int:id>/delete')
class DeleteCountry(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(204, description='Successfully removed Country')
    @ns.response(404, description='Country not found!')
    def delete(self, id):
        try:
            country = Country.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Country not found!'})
            res.status_code = 404
            return res
        try:
            db.session.delete(country)
            db.session.commit()
        except Exception as e:
            orig = e.orig
            if orig:
                args = orig.args
                if len(args) >= 2 and args[0] == 1451:
                    error_message = args[1]
                    if 'a foreign key constraint fails' in error_message:
                        res = jsonify({'message': 'Something attached to country!'})
                        res.status_code = 409
                        return res
        return Response(status=204)
