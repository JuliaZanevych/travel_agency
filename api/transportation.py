from datetime import datetime

from flask import Response, request, jsonify
from flask_restx import Namespace, Resource
from werkzeug.exceptions import NotFound

from api.auth import auth
from config import api, db
from model import Transportation
from schema import transportation_model, transportation_schema, transportations_schema

ns = Namespace('transportations', description='CRUD operations for Transportation essence')
api.add_namespace(ns)


@ns.route('/post')
class CreateTransportation(Resource):
    @ns.expect(transportation_model)
    @ns.param(name='Authorization', description='Basic access authentication token', _in='header', required=True)
    @ns.response(201, description='Successfully created new Transportation', model=transportation_model)
    @ns.response(401, description='Customer is not authenticated!', model=transportation_model)
    @ns.response(403, description='Customer is not authorized!', model=transportation_model)
    @auth("CREATE_TRANSPORTATION")
    def post(self):
        json = request.json

        transportation = Transportation(
            tour_id=json.get('tour_id'),
            transport_type=json.get('transport_type'),
            start_time=datetime.strptime(json.get('start_time'), "%Y-%m-%d"),
            end_time=datetime.strptime(json.get('end_time'), "%Y-%m-%d"),
            start_city_id=json.get('start_city_id'),
            end_city_id=json.get('end_city_id'),
            details=json.get('details'),
        )
        try:
            db.session.add(transportation)
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
        res = jsonify(transportation_schema.dump(transportation))
        res.status_code = 201
        return res


@ns.route('/<int:id>/get')
class GetTransportation(Resource):
    @ns.param(name='Authorization', description='Basic access authentication token', _in='header', required=True)
    @ns.response(200, description='Successfully get Transportation', model=transportation_model)
    @ns.response(404, description='Transportation not found!')
    @ns.response(401, description='Customer is not authenticated!', model=transportation_model)
    @ns.response(403, description='Customer is not authorized!', model=transportation_model)
    @auth("GET_TRANSPORTATION_BY_ID")
    def get(self, id):
        try:
            transportation = Transportation.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Transportation not found!'})
            res.status_code = 404
            return res

        return jsonify(transportation_schema.dump(transportation))


@ns.route('/get')
class GetTransportations(Resource):
    @ns.param(name='Authorization', description='Basic access authentication token', _in='header', required=True)
    @ns.response(200, description='Successfully get list of Transportations', model=transportation_model)
    @ns.response(401, description='Customer is not authenticated!', model=transportation_model)
    @ns.response(403, description='Customer is not authorized!', model=transportation_model)
    @auth("GET_TRANSPORTATIONS_LIST")
    def get(self):
        return jsonify(transportations_schema.dump(Transportation.query.all()))


@ns.route('/<int:id>/update')
class UpdateTransportation(Resource):
    @ns.expect(transportation_model)
    @ns.param(name='Authorization', description='Basic access authentication token', _in='header', required=True)
    @ns.response(200, description='Successfully updated City', model=transportation_model)
    @ns.response(404, description='Transportation not found!')
    @ns.response(401, description='Customer is not authenticated!', model=transportation_model)
    @ns.response(403, description='Customer is not authorized!', model=transportation_model)
    @auth("UPDATE_TRANSPORTATION")
    def put(self, id):
        json = request.json

        try:
            transportation = Transportation.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Transportation not found!'})
            res.status_code = 404
            return res
        try:
            transportation.tour_id = json.get('tour_id')
            transportation.transport_type = json.get('transport_type')
            transportation.start_time = datetime.strptime(json.get('start_time'), "%Y-%m-%d")
            transportation.end_time = datetime.strptime(json.get('end_time'), "%Y-%m-%d")
            transportation.start_city_id = json.get('start_city_id')
            transportation.end_city_id = json.get('end_city_id')
            transportation.details = json.get('details')
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
        return jsonify(transportation_schema.dump(transportation))


@ns.route('/<int:id>/delete')
class DeleteTransportation(Resource):
    @ns.param(name='Authorization', description='Basic access authentication token', _in='header', required=True)
    @ns.response(204, description='Successfully removed Transportation')
    @ns.response(404, description='Transportation not found!')
    @ns.response(401, description='Customer is not authenticated!', model=transportation_model)
    @ns.response(403, description='Customer is not authorized!', model=transportation_model)
    @auth("DELETE_TRANSPORTATION")
    def delete(self, id):
        try:
            transportation = Transportation.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Transportation not found!'})
            res.status_code = 404
            return res
        db.session.delete(transportation)
        db.session.commit()
        return Response(status=204)
