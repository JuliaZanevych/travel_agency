from datetime import datetime

from flask import Response, request, jsonify
from flask_restx import Namespace, Resource
from werkzeug.exceptions import NotFound

from config import api, db
from model import Tour
from schema import tour_model, tour_schema, tours_schema

ns = Namespace('Tour API', description='CRUD operations for Tour essence')
api.add_namespace(ns)


@ns.route('/tours/post')
class CreateTour(Resource):
    @ns.expect(tour_model)
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(201, description='Successfully created new Customer', model=tour_model)
    def post(self):
        json = request.json

        tour = Tour(
            name=json.get('name'),
            price=json.get('price'),
            person_count=json.get('person_count'),
            start_time=datetime.strptime(json.get('start_time'), "%Y-%m-%d"),
            end_time=datetime.strptime(json.get('end_time'), "%Y-%m-%d"),
            description=json.get('description'),
            recommended_pocket_money=json.get('recommended_pocket_money')
        )
        db.session.add(tour)
        db.session.commit()

        res = jsonify(tour_schema.dump(tour))
        res.status_code = 201
        return res


@ns.route('/tours/<int:id>/get')
class GetTour(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully get Tour', model=tour_model)
    @ns.response(404, description='Tour not found!')
    def get(self, id):
        try:
            tour = Tour.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Tour not found!'})
            res.status_code = 404
            return res
        return jsonify(tour_schema.dump(tour))


@ns.route('/tours/get')
class GetTours(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully get list of Tours', model=tour_model)
    def get(self):
        return jsonify(tours_schema.dump(Tour.query.all()))


@ns.route('/tours/<int:id>/update')
class UpdateTour(Resource):
    @ns.expect(tour_model)
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully updated Tour', model=tour_model)
    @ns.response(404, description='Tour not found!')
    def put(self, id):
        json = request.json

        try:
            tour = Tour.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Tour not found!'})
            res.status_code = 404
            return res
        tour.name = json.get('name')
        tour.price = json.get('price')
        tour.person_count = json.get('person_count')
        tour.start_time = datetime.strptime(json.get('start_time'), "%Y-%m-%d")
        tour.end_time = datetime.strptime(json.get('end_time'), "%Y-%m-%d")
        tour.description = json.get('description')
        tour.recommended_pocket_money = json.get('recommended_pocket_money')
        db.session.commit()
        return jsonify(tour_schema.dump(tour))


@ns.route('/tours/<int:id>/delete')
class DeleteTour(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(204, description='Successfully removed Tour')
    @ns.response(404, description='Tour not found!')
    def delete(self, id):
        try:
            tour = Tour.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Tour not found!'})
            res.status_code = 404
            return res
        db.session.delete(tour)
        db.session.commit()
        return Response(status=204)
