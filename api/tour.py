from datetime import datetime

from flask import Response, request, jsonify
from flask_restx import Namespace, Resource
from werkzeug.exceptions import NotFound

from api.auth import auth
from config import api, db
from model import Tour, TourAttraction
from schema import tour_model, tour_schema, tours_schema

from sqlalchemy import delete

ns = Namespace('tours', description='CRUD operations for Tour essence')
api.add_namespace(ns)


@ns.route('/post')
class CreateTour(Resource):
    @ns.expect(tour_model)
    @ns.param(name='Authorization', description='Basic access authentication token', _in='header', required=True)
    @ns.response(201, description='Successfully created new Customer', model=tour_model)
    @ns.response(401, description='Customer is not authenticated!', model=tour_model)
    @ns.response(403, description='Customer is not authorized!', model=tour_model)
    @auth("CREATE_TOUR")
    def post(self):
        json = request.json

        try:
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

        except Exception as e:
            orig = e.orig
            if orig:
                args = orig.args
                if len(args) >= 2 and args[0] == 1062:
                    error_message = args[1]
                    if 'tours.name' in error_message:
                        res = jsonify({'message': 'There is already the tour with this name!'})
                        res.status_code = 409
                        return res
            raise e

        tour_id = tour.id
        tourist_attraction_ids = json.get('tourist_attraction_ids')

        if tourist_attraction_ids:
            for tourist_attraction_id in set(tourist_attraction_ids):
                tour_attraction = TourAttraction(
                    tour_id=tour_id,
                    tourist_attractions_id=tourist_attraction_id
                )
                db.session.add(tour_attraction)
            try:
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

        tour.tourist_attraction_ids = tourist_attraction_ids

        res = jsonify(tour_schema.dump(tour))
        res.status_code = 201
        return res


@ns.route('/<int:id>/get')
class GetTour(Resource):
    @ns.param(name='Authorization', description='Basic access authentication token', _in='header', required=True)
    @ns.response(200, description='Successfully get Tour', model=tour_model)
    @ns.response(404, description='Tour not found!')
    @ns.response(401, description='Customer is not authenticated!', model=tour_model)
    @ns.response(403, description='Customer is not authorized!', model=tour_model)
    @auth("GET_TOUR_BY_ID")
    def get(self, id):
        try:
            tour = Tour.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Tour not found!'})
            res.status_code = 404
            return res

        tour_attractions = TourAttraction.query.filter_by(tour_id=id).all()
        tourist_attractions_ids = [tour_attraction.tourist_attractions_id for tour_attraction in tour_attractions]

        tour_dto = tour_schema.dump(tour)
        tour_dto['tourist_attraction_ids'] = tourist_attractions_ids

        return jsonify(tour_dto)


@ns.route('/get')
class GetTours(Resource):
    @ns.param(name='Authorization', description='Basic access authentication token', _in='header', required=True)
    @ns.response(200, description='Successfully get list of Tours', model=tour_model)
    @ns.response(401, description='Customer is not authenticated!', model=tour_model)
    @ns.response(403, description='Customer is not authorized!', model=tour_model)
    @auth("GET_TOURS_LIST")
    def get(self):
        return jsonify(tours_schema.dump(Tour.query.all()))


@ns.route('/<int:id>/update')
class UpdateTour(Resource):
    @ns.expect(tour_model)
    @ns.param(name='Authorization', description='Basic access authentication token', _in='header', required=True)
    @ns.response(200, description='Successfully updated Tour', model=tour_model)
    @ns.response(404, description='Tour not found!')
    @ns.response(401, description='Customer is not authenticated!', model=tour_model)
    @ns.response(403, description='Customer is not authorized!', model=tour_model)
    @auth("UPDATE_TOUR")
    def put(self, id):
        json = request.json

        try:
            tour = Tour.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Tour not found!'})
            res.status_code = 404
            return res
        try:
            tour.name = json.get('name')
            tour.price = json.get('price')
            tour.person_count = json.get('person_count')
            tour.start_time = datetime.strptime(json.get('start_time'), "%Y-%m-%d")
            tour.end_time = datetime.strptime(json.get('end_time'), "%Y-%m-%d")
            tour.description = json.get('description')
            tour.recommended_pocket_money = json.get('recommended_pocket_money')
            db.session.commit()
        except Exception as e:
            orig = e.orig
            if orig:
                args = orig.args
                if len(args) >= 2 and args[0] == 1062:
                    error_message = args[1]
                    if 'tours.name' in error_message:
                        res = jsonify({'message': 'There is already the tour with this name!'})
                        res.status_code = 409
                        return res
            raise e
        input_attractions_ids = set(json.get('tourist_attraction_ids'))

        tour_attractions = TourAttraction.query.filter_by(tour_id=id).all()
        existing_attractions_ids = {tour_attraction.tourist_attractions_id for tour_attraction in tour_attractions}

        removed_attractions_ids = existing_attractions_ids - input_attractions_ids
        if removed_attractions_ids:
            # deleted_attractions = TourAttraction.query.filter_by(
            #    tour_id=id and TourAttraction.tourist_attractions_id.in_(removed_attractions_ids)).delete()
            # deleted_attractions = TourAttraction.delete().where(
            #     TourAttraction.tour_id == id and TourAttraction.tourist_attractions_id.in_(removed_attractions_ids))
            db.session.query(TourAttraction).filter(
                TourAttraction.tour_id == id).filter(TourAttraction.tourist_attractions_id.in_(
                    removed_attractions_ids)).delete()
        # db.session.delete(deleted_attractions)
        try:
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

        new_attractions_ids = input_attractions_ids - existing_attractions_ids
        if new_attractions_ids:
            for tourist_attraction_id in new_attractions_ids:
                tour_attraction = TourAttraction(
                    tour_id=id,
                    tourist_attractions_id=tourist_attraction_id
                )
                db.session.add(tour_attraction)
            try:
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

        return jsonify(tour_schema.dump(tour))


@ns.route('/<int:id>/delete')
class DeleteTour(Resource):
    @ns.param(name='Authorization', description='Basic access authentication token', _in='header', required=True)
    @ns.response(204, description='Successfully removed Tour')
    @ns.response(404, description='Tour not found!')
    @ns.response(401, description='Customer is not authenticated!', model=tour_model)
    @ns.response(403, description='Customer is not authorized!', model=tour_model)
    @auth("DELETE_TOUR")
    def delete(self, id):
        try:
            tour = Tour.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Tour not found!'})
            res.status_code = 404
            return res
        try:
            db.session.delete(tour)
            db.session.commit()
        except Exception as e:
            orig = e.orig
            if orig:
                args = orig.args
                if len(args) >= 2 and args[0] == 1451:
                    error_message = args[1]
                    if 'a foreign key constraint fails' in error_message:
                        res = jsonify({'message': 'Something attached to tour!'})
                        res.status_code = 409
                        return res
        return Response(status=204)
