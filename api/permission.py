from flask import Response, request, jsonify
from flask_restx import Namespace, Resource
from werkzeug.exceptions import NotFound

from api.auth import auth
from config import api, db
from model import Permission
from schema import permission_model, permission_schema, permissions_schema

ns = Namespace('permissions', description='CRUD operations for Permission essence')
api.add_namespace(ns)


@ns.route('/post')
class CreatePermission(Resource):
    @ns.expect(permission_model)
    @ns.param(name='Authorization', description='Basic access authentication token', _in='header', required=True)
    @ns.response(201, description='Successfully created new Permission', model=permission_model)
    @ns.response(401, description='Customer is not authenticated!', model=permission_model)
    @ns.response(403, description='Customer is not authorized!', model=permission_model)
    @auth("CREATE_PERMISSION")
    def post(self):
        json = request.json

        permission = Permission(
            method=json.get('method')
        )
        try:
            db.session.add(permission)
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
        res = jsonify(permission_schema.dump(permission))
        res.status_code = 201
        return res


@ns.route('/<int:id>/get')
class GetPermission(Resource):
    @ns.param(name='Authorization', description='Basic access authentication token', _in='header', required=True)
    @ns.response(200, description='Successfully get Permission', model=permission_model)
    @ns.response(404, description='Permission not found!')
    @ns.response(401, description='Customer is not authenticated!', model=permission_model)
    @ns.response(403, description='Customer is not authorized!', model=permission_model)
    @auth("GET_PERMISSION_BY_ID")
    def get(self, id):
        try:
            permission = Permission.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Permission not found!'})
            res.status_code = 404
            return res

        return jsonify(permission_schema.dump(permission))


@ns.route('/get')
class GetPermissions(Resource):
    @ns.param(name='Authorization', description='Basic access authentication token', _in='header', required=True)
    @ns.response(200, description='Successfully get list of Permissions', model=permission_model)
    @ns.response(401, description='Customer is not authenticated!', model=permission_model)
    @ns.response(403, description='Customer is not authorized!', model=permission_model)
    @auth("GET_PERMISSIONS_LIST")
    def get(self):
        return jsonify(permissions_schema.dump(Permission.query.all()))


@ns.route('/<int:id>/update')
class UpdatePermission(Resource):
    @ns.expect(permission_model)
    @ns.param(name='Authorization', description='Basic access authentication token', _in='header', required=True)
    @ns.response(200, description='Successfully updated Permission', model=permission_model)
    @ns.response(404, description='Permission not found!')
    @ns.response(401, description='Customer is not authenticated!', model=permission_model)
    @ns.response(403, description='Customer is not authorized!', model=permission_model)
    @auth("UPDATE_PERMISSION")
    def put(self, id):
        json = request.json

        try:
            permission = Permission.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Permission not found!'})
            res.status_code = 404
            return res
        try:
            permission.method = json.get('method')
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
        return jsonify(permission_schema.dump(permission))


@ns.route('/<int:id>/delete')
class DeletePermission(Resource):
    @ns.param(name='Authorization', description='Basic access authentication token', _in='header', required=True)
    @ns.response(204, description='Successfully removed Permission')
    @ns.response(404, description='Permission not found!')
    @ns.response(401, description='Customer is not authenticated!', model=permission_model)
    @ns.response(403, description='Customer is not authorized!', model=permission_model)
    @auth("DELETE_PERMISSION")
    def delete(self, id):
        try:
            permission = Permission.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Permission not found!'})
            res.status_code = 404
            return res
        try:
            db.session.delete(permission)
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
