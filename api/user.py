from datetime import datetime

from flask import Response, request, jsonify
from flask_restx import Namespace, Resource
from werkzeug.exceptions import NotFound

from config import api, db
from model import User
from schema import user_model, user_schema, users_schema

ns = Namespace('users', description='CRUD operations for User essence')
api.add_namespace(ns)


@ns.route('/post')
class CreateUser(Resource):
    @ns.expect(user_model)
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(201, description='Successfully created new User', model=user_model)
    def post(self):
        json = request.json

        user = User(
            first_name=json.get('first_name'),
            middle_name=json.get('middle_name'),
            last_name=json.get('last_name'),
            phone=json.get('phone'),
            date_of_birthday=datetime.strptime(json.get('date_of_birthday'), "%Y-%m-%d"),
            gender=json.get('gender'),
            is_baned=json.get('is_baned'),
            password_hash=json.get('password_hash')
        )
        db.session.add(user)
        db.session.commit()

        res = jsonify(user_schema.dump(user))
        res.status_code = 201
        return res


@ns.route('/<int:id>/get')
class GetUser(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully get User', model=user_model)
    @ns.response(404, description='User not found!')
    def get(self, id):
        try:
            user = User.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'User not found!'})
            res.status_code = 404
            return res

        return jsonify(user_schema.dump(user))


@ns.route('/get')
class GetUsers(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully get list of Users', model=user_model)
    def get(self):
        return jsonify(users_schema.dump(User.query.all()))


@ns.route('/<int:id>/update')
class UpdateUser(Resource):
    @ns.expect(user_model)
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully updated User', model=user_model)
    @ns.response(404, description='User not found!')
    def put(self, id):
        json = request.json

        try:
            user = User.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'User not found!'})
            res.status_code = 404
            return res

        user.first_name = json.get('first_name')
        user.middle_name = json.get('middle_name')
        user.last_name = json.get('last_name')
        user.phone = json.get('phone')
        user.date_of_birthday = datetime.strptime(json.get('date_of_birthday'), "%Y-%m-%d")
        user.gender = json.get('gender')
        user.is_baned = json.get('is_baned')
        user.password_hash = json.get('password_hash')
        db.session.commit()
        return jsonify(user_schema.dump(user))


@ns.route('/<int:id>/delete')
class DeleteUser(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(204, description='Successfully removed User')
    @ns.response(404, description='User not found!')
    def delete(self, id):
        try:
            user = User.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'User not found!'})
            res.status_code = 404
            return res

        db.session.delete(user)
        db.session.commit()
        return Response(status=204)
