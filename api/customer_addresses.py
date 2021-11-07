from flask import Response, request, jsonify
from flask_restx import Namespace, Resource
from werkzeug.exceptions import NotFound

from config import api, db
from model import CustomerAddresses
from schema import customer_addresses_model, customer_addresses_schema, customer_addressess_schema

ns = Namespace('customer_addresses', description='CRUD operations for Customer addresses essence')
api.add_namespace(ns)


@ns.route('/post')
class CreateCustomerAddresses(Resource):
    @ns.expect(customer_addresses_model)
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(201, description='Successfully created new Customer addresses', model=customer_addresses_model)
    def post(self):
        json = request.json
        try:
            customer_addresses = CustomerAddresses(
                id=json.get('customer_id'),
                city_id=json.get('city_id'),
                zip_code=json.get('zip_code'),
                street=json.get('street'),
                house_number=json.get('house_number'),
                apartment_number=json.get('apartment_number'),
            )
            db.session.add(customer_addresses)
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
        res = jsonify(customer_addresses_schema.dump(customer_addresses))
        res.status_code = 201
        return res


@ns.route('/<int:id>/get')
class GetCustomerAddresses(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully get Customer addresses', model=customer_addresses_model)
    @ns.response(404, description='Customer addresses not found!')
    def get(self, id):
        try:
            customer_addresses = CustomerAddresses.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Customer addresses not found!'})
            res.status_code = 404
            return res

        return jsonify(customer_addresses_schema.dump(customer_addresses))


@ns.route('/get')
class GetCustomerAddressess(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully get list of Customer addressess', model=customer_addresses_model)
    def get(self):
        return jsonify(customer_addressess_schema.dump(CustomerAddresses.query.all()))


@ns.route('/<int:id>/update')
class UpdateCustomerAddresses(Resource):
    @ns.expect(customer_addresses_model)
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully updated Customer addresses', model=customer_addresses_model)
    @ns.response(404, description='Customer addresses not found!')
    def put(self, id):
        json = request.json

        try:
            customer_addresses = CustomerAddresses.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Customer addresses not found!'})
            res.status_code = 404
            return res
        try:
            customer_addresses.city_id = json.get('city_id')
            customer_addresses.zip_code = json.get('zip_code')
            customer_addresses.street = json.get('street')
            customer_addresses.house_number = json.get('house_number')
            customer_addresses.apartment_number = json.get('apartment_number')
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
        return jsonify(customer_addresses_schema.dump(customer_addresses))


@ns.route('/<int:id>/delete')
class DeleteCustomerAddresses(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(204, description='Successfully removed Customer addresses')
    @ns.response(404, description='Customer addresses not found!')
    def delete(self, id):
        try:
            customer_addresses = CustomerAddresses.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Customer addresses not found!'})
            res.status_code = 404
            return res
        db.session.delete(customer_addresses)
        db.session.commit()
        return Response(status=204)
