from datetime import datetime

from flask import Response, request, jsonify
from flask_restx import Namespace, Resource
from werkzeug.exceptions import NotFound

from api.auth import auth
from config import api, db
from model import Role, PermissionRoles
from schema import role_model, role_schema, roles_schema

from sqlalchemy import delete

ns = Namespace('roles', description='CRUD operations for Role essence')
api.add_namespace(ns)


@ns.route('/post')
class CreateRole(Resource):
    @ns.expect(role_model)
    @ns.param(name='Authorization', description='Basic access authentication token', _in='header', required=True)
    @ns.response(201, description='Successfully created new Role', model=role_model)
    @ns.response(401, description='Customer is not authenticated!', model=role_model)
    @ns.response(403, description='Customer is not authorized!', model=role_model)
    @auth("CREATE_ROLE")
    def post(self):
        json = request.json

        try:
            role = Role(
                name=json.get('name')

            )
            db.session.add(role)
            db.session.commit()

        except Exception as e:
            orig = e.orig
            if orig:
                args = orig.args
                if len(args) >= 2 and args[0] == 1062:
                    error_message = args[1]
                    if 'roles.name' in error_message:
                        res = jsonify({'message': 'There is already the role with this name!'})
                        res.status_code = 409
                        return res
            raise e

        role_id = role.id
        permission_ids = json.get('permission_ids')

        if permission_ids:
            for permission_id in set(permission_ids):
                permission_role = PermissionRoles(
                    role_id=role_id,
                    permission_id=permission_id
                )
                db.session.add(permission_role)
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

        role.permission_ids = permission_ids

        res = jsonify(role_schema.dump(role))
        res.status_code = 201
        return res


@ns.route('/<int:id>/get')
class GetRole(Resource):
    @ns.param(name='Authorization', description='Basic access authentication token', _in='header', required=True)
    @ns.response(200, description='Successfully get Role', model=role_model)
    @ns.response(404, description='Role not found!')
    @ns.response(401, description='Customer is not authenticated!', model=role_model)
    @ns.response(403, description='Customer is not authorized!', model=role_model)
    @auth("GET_ROLE_BY_ID")
    def get(self, id):
        try:
            role = Role.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Role not found!'})
            res.status_code = 404
            return res

        permission_roles = PermissionRoles.query.filter_by(role_id=id).all()
        permission_ids = [permission_role.permission_id for permission_role in permission_roles]

        role_dto = role_schema.dump(role)
        role_dto['permission_ids'] = permission_ids

        return jsonify(role_dto)


@ns.route('/get')
class GetRoles(Resource):
    @ns.param(name='Authorization', description='Basic access authentication token', _in='header', required=True)
    @ns.response(200, description='Successfully get list of Roles', model=role_model)
    @ns.response(401, description='Customer is not authenticated!', model=role_model)
    @ns.response(403, description='Customer is not authorized!', model=role_model)
    @auth("GET_ROLES_LIST")
    def get(self):
        return jsonify(roles_schema.dump(Role.query.all()))


@ns.route('/<int:id>/update')
class UpdateRole(Resource):
    @ns.expect(role_model)
    @ns.param(name='Authorization', description='Basic access authentication token', _in='header', required=True)
    @ns.response(200, description='Successfully updated Role', model=role_model)
    @ns.response(404, description='Role not found!')
    @ns.response(401, description='Customer is not authenticated!', model=role_model)
    @ns.response(403, description='Customer is not authorized!', model=role_model)
    @auth("UPDATE_ROLE")
    def put(self, id):
        json = request.json

        try:
            role = Role.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Role not found!'})
            res.status_code = 404
            return res
        try:
            role.name = json.get('name')
            db.session.commit()
        except Exception as e:
            orig = e.orig
            if orig:
                args = orig.args
                if len(args) >= 2 and args[0] == 1062:
                    error_message = args[1]
                    if 'roles.name' in error_message:
                        res = jsonify({'message': 'There is already the role with this name!'})
                        res.status_code = 409
                        return res
            raise e
        input_permissions_ids = set(json.get('permission_ids'))

        permission_roles = PermissionRoles.query.filter_by(role_id=id).all()
        existing_permissions_ids = {permission_role.permission_id for permission_role in permission_roles}

        removed_permissions_ids = existing_permissions_ids - input_permissions_ids
        if removed_permissions_ids:
            # deleted_attractions = TourAttraction.query.filter_by(
            #    tour_id=id and TourAttraction.tourist_attractions_id.in_(removed_attractions_ids)).delete()
            # deleted_attractions = TourAttraction.delete().where(
            #     TourAttraction.tour_id == id and TourAttraction.tourist_attractions_id.in_(removed_attractions_ids))
            db.session.query(PermissionRoles).filter(
                PermissionRoles.role_id == id).filter(PermissionRoles.permission_id.in_(
                removed_permissions_ids)).delete()
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

        new_permissions_ids = input_permissions_ids - existing_permissions_ids
        if new_permissions_ids:
            for permission_id in new_permissions_ids:
                permission_role = PermissionRoles(
                    role_id=id,
                    permission_id=permission_id
                )
                db.session.add(permission_role)
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

        return jsonify(role_schema.dump(role))


@ns.route('/<int:id>/delete')
class DeleteRole(Resource):
    @ns.param(name='Authorization', description='Basic access authentication token', _in='header', required=True)
    @ns.response(204, description='Successfully removed Role')
    @ns.response(404, description='Role not found!')
    @ns.response(401, description='Customer is not authenticated!', model=role_model)
    @ns.response(403, description='Customer is not authorized!', model=role_model)
    @auth("DELETE_ROLE")
    def delete(self, id):
        try:
            role = Role.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Role not found!'})
            res.status_code = 404
            return res
        try:
            db.session.delete(role)
            db.session.commit()
        except Exception as e:
            orig = e.orig
            if orig:
                args = orig.args
                if len(args) >= 2 and args[0] == 1451:
                    error_message = args[1]
                    if 'a foreign key constraint fails' in error_message:
                        res = jsonify({'message': 'Something attached to role!'})
                        res.status_code = 409
                        return res
        return Response(status=204)
