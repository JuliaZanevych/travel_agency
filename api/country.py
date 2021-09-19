from flask import Response, request, jsonify
from flask_restx import Namespace, Resource
from werkzeug.exceptions import NotFound

from config import api, db
from model import Country
from schema import country_model, country_schema, countries_schema

ns = Namespace('Country API', description='CRUD operations for Country essence')
api.add_namespace(ns)


@ns.route('/countries/post')
class CreateCountry(Resource):
    @ns.expect(country_model)
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(201, description='Successfully created new Country', model=country_model)
    def post(self):
        json = request.json

        country = Country(
            county_name=json.get('county_name'),
            official_language=json.get('official_language'),
            population=json.get('population'),
            details=json.get('details'),
        )
        db.session.add(country)
        db.session.commit()

        res = jsonify(country_schema.dump(country))
        res.status_code = 201
        return res


@ns.route('/countries/<int:id>/get')
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


@ns.route('/countries/get')
class GetCustomers(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully get list of Countries', model=country_model)
    def get(self):
        return jsonify(countries_schema.dump(Country.query.all()))


@ns.route('/countries/<int:id>/update')
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
        country.county_name = json.get('county_name')
        country.official_language = json.get('official_language')
        country.population = json.get('population')
        country.details = json.get('details')
        db.session.commit()
        return jsonify(country_schema.dump(country))


@ns.route('/countries/<int:id>/delete')
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
        db.session.delete(country)
        db.session.commit()
        return Response(status=204)
