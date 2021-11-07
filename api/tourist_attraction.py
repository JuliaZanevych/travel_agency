from flask import Response, request, jsonify
from flask_restx import Namespace, Resource
from werkzeug.exceptions import NotFound

from config import api, db
from model import TouristAttraction
from schema import tourist_attraction_model, tourist_attraction_schema, tourist_attractions_schema

ns = Namespace('tourist-attractions', description='CRUD operations for Tourist Attraction essence')
api.add_namespace(ns)


@ns.route('/post')
class CreateTouristAttraction(Resource):
    @ns.expect(tourist_attraction_model)
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(201, description='Successfully created new Tourist Attraction', model=tourist_attraction_model)
    def post(self):
        json = request.json

        tourist_attraction = TouristAttraction(
            name=json.get('name'),
            type=json.get('type'),
            city_id=json.get('city_id'),
            details=json.get('details'),
        )
        try:
            db.session.add(tourist_attraction)
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
        res = jsonify(tourist_attraction_schema.dump(tourist_attraction))
        res.status_code = 201
        return res


@ns.route('/<int:id>/get')
class GetTouristAttraction(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully get Tourist Attraction', model=tourist_attraction_model)
    @ns.response(404, description='Tourist Attraction not found!')
    def get(self, id):
        try:
            tourist_attraction = TouristAttraction.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Tourist Attraction not found!'})
            res.status_code = 404
            return res
        return jsonify(tourist_attraction_schema.dump(tourist_attraction))


@ns.route('/get')
class GetTouristAttractions(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully get list of Tourist Attractions', model=tourist_attraction_model)
    def get(self):
        return jsonify(tourist_attractions_schema.dump(TouristAttraction.query.all()))


@ns.route('/<int:id>/update')
class UpdateTouristAttraction(Resource):
    @ns.expect(tourist_attraction_model)
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully updated Tourist Attraction', model=tourist_attraction_model)
    @ns.response(404, description='Tourist Attraction not found!')
    def put(self, id):
        json = request.json

        try:
            tourist_attraction = TouristAttraction.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Tourist Attraction not found!'})
            res.status_code = 404
            return res
        try:
            tourist_attraction.name = json.get('name')
            tourist_attraction.type = json.get('type')
            tourist_attraction.city_id = json.get('city_id'),
            tourist_attraction.details = json.get('details')
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
        return jsonify(tourist_attraction_schema.dump(tourist_attraction))


@ns.route('/<int:id>/delete')
class DeleteTouristAttraction(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(204, description='Successfully removed Tourist Attraction')
    @ns.response(404, description='Tourist Attraction not found!')
    def delete(self, id):
        try:
            tourist_attraction = TouristAttraction.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Tourist Attraction not found!'})
            res.status_code = 404
            return res
        db.session.delete(tourist_attraction)
        db.session.commit()
        return Response(status=204)
