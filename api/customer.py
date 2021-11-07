from datetime import datetime

import bcrypt
from flask import Response, request, jsonify
from flask_restx import Namespace, Resource
from werkzeug.exceptions import NotFound

from config import api, db
from model import Customer
from schema import customer_schema, customers_schema, customer_model, customer_schema_get, customers_schema_get, \
    customer_model_get
from flask_bcrypt import Bcrypt

ns = Namespace('customers', description='CRUD operations for Customer essence')
api.add_namespace(ns)


@ns.route('/post')
class CreateCustomer(Resource):
    @ns.expect(customer_model)
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(201, description='Successfully created new Customer', model=customer_model)
    def post(self):
        json = request.json

        customer = Customer(
            first_name=json.get('first_name'),
            middle_name=json.get('middle_name'),
            last_name=json.get('last_name'),
            phone=json.get('phone'),
            date_of_birthday=datetime.strptime(json.get('date_of_birthday'), "%Y-%m-%d"),
            gender=json.get('gender'),
            is_covid_vaccinated=json.get('is_covid_vaccinated'),
            is_blocked=json.get('is_blocked'),
            password_hash=json.get('password_hash')
        )
        hashed = bcrypt.hashpw(customer.password_hash.encode('utf-8'), bcrypt.gensalt())
        customer.password_hash = hashed
        db.session.add(customer)
        db.session.commit()

        res = jsonify(customer_schema.dump(customer))
        res.status_code = 201
        return res


@ns.route('/<int:id>/get')
class GetCustomer(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully get Customer', model=customer_model_get)
    @ns.response(404, description='Customer not found!')
    def get(self, id):
        try:
            customer = Customer.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Customer not found!'})
            res.status_code = 404
            return res

        return jsonify(customer_schema_get.dump(customer))


@ns.route('/get')
class GetCustomers(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully get list of Customers', model=customer_model_get)
    def get(self):
        return jsonify(customers_schema_get .dump(Customer.query.all()))


@ns.route('/<int:id>/update')
class UpdateCustomer(Resource):
    @ns.expect(customer_model)
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully updated Customer', model=customer_model)
    @ns.response(404, description='Customer not found!')
    def put(self, id):
        json = request.json

        try:
            customer = Customer.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Customer not found!'})
            res.status_code = 404
            return res

        customer.first_name = json.get('first_name')
        customer.middle_name = json.get('middle_name')
        customer.last_name = json.get('last_name')
        customer.phone = json.get('phone')
        customer.date_of_birthday = datetime.strptime(json.get('date_of_birthday'), "%Y-%m-%d")
        customer.gender = json.get('gender')
        customer.is_covid_vaccinated = json.get('is_covid_vaccinated')
        customer.is_blocked = json.get('is_blocked')
        customer.password_hash = json.get('password_hash')
        db.session.commit()
        return jsonify(customer_schema.dump(customer))


@ns.route('/<int:id>/delete')
class DeleteCustomer(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(204, description='Successfully removed Customer')
    @ns.response(404, description='Customer not found!')
    def delete(self, id):
        try:
            customer = Customer.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Customer not found!'})
            res.status_code = 404
            return res
        try:
            db.session.delete(customer)
            db.session.commit()
        except Exception as e:
            orig = e.orig
            if orig:
                args = orig.args
                if len(args) >= 2 and args[0] == 1451:
                    error_message = args[1]
                    if 'a foreign key constraint fails' in error_message:
                        res = jsonify({'message': 'Something attached to customer!'})
                        res.status_code = 409
                        return res
        return Response(status=204)
