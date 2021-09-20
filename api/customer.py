from datetime import datetime

from flask import Response, request, jsonify
from flask_restx import Namespace, Resource
from werkzeug.exceptions import NotFound

from config import api, db
from model import Customer
from schema import customer_schema, customers_schema, customer_model

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
            is_blocked=json.get('is_blocked')
        )
        db.session.add(customer)
        db.session.commit()

        res = jsonify(customer_schema.dump(customer))
        res.status_code = 201
        return res


@ns.route('/<int:id>/get')
class GetCustomer(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully get Customer', model=customer_model)
    @ns.response(404, description='Customer not found!')
    def get(self, id):
        try:
            customer = Customer.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Customer not found!'})
            res.status_code = 404
            return res

        return jsonify(customer_schema.dump(customer))


@ns.route('/get')
class GetCustomers(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully get list of Customers', model=customer_model)
    def get(self):
        return jsonify(customers_schema.dump(Customer.query.all()))


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

        db.session.delete(customer)
        db.session.commit()
        return Response(status=204)
