from datetime import datetime

from flask import Response, request, jsonify
from flask_restx import Namespace, Resource
from werkzeug.exceptions import NotFound

from config import api, db
from model import Vouchers, VoucherCustomers
from schema import voucher_model, voucher_schema, vouchers_schema

ns = Namespace('vouchers', description='CRUD operations for Voucher essence')
api.add_namespace(ns)


@ns.route('/post')
class CreateVoucher(Resource):
    @ns.expect(voucher_model)
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(201, description='Successfully created new Voucher', model=voucher_model)
    def post(self):
        json = request.json

        voucher = Vouchers(
            tour_id=json.get('tour_id')
        )
        try:
            db.session.add(voucher)
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

        voucher_id = voucher.id
        customer_ids = json.get('customer_ids')

        if customer_ids:
            for customer_id in set(customer_ids):
                voucher_customer = VoucherCustomers(
                    voucher_id=voucher_id,
                    customer_id=customer_id
                )
                db.session.add(voucher_customer)
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

        voucher.customer_ids = customer_ids

        res = jsonify(voucher_schema.dump(voucher))
        res.status_code = 201
        return res


@ns.route('/<int:id>/get')
class GetVoucher(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully get Voucher', model=voucher_model)
    @ns.response(404, description='Voucher not found!')
    def get(self, id):
        try:
            voucher = Vouchers.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Voucher not found!'})
            res.status_code = 404
            return res

        voucher_customers = VoucherCustomers.query.filter_by(voucher_id=id).all()
        customer_ids = [voucher_customer.customer_id for voucher_customer in voucher_customers]

        voucher_dto = voucher_schema.dump(voucher)
        voucher_dto['customer_ids'] = customer_ids

        return jsonify(voucher_dto)


@ns.route('/get')
class GetVouchers(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully get list of Vouchers', model=voucher_model)
    def get(self):
        return jsonify(vouchers_schema.dump(Vouchers.query.all()))


@ns.route('/<int:id>/update')
class UpdateVoucher(Resource):
    @ns.expect(voucher_model)
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(200, description='Successfully updated Voucher', model=voucher_model)
    @ns.response(404, description='Voucher not found!')
    def put(self, id):
        json = request.json

        try:
            voucher = Vouchers.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Voucher not found!'})
            res.status_code = 404
            return res
        try:
            voucher.tour_id = json.get('tour_id')
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
        input_customers_ids = set(json.get('customer_ids'))

        voucher_customers = VoucherCustomers.query.filter_by(voucher_id=id).all()
        existing_customers_ids = {voucher_customer.customer_id for voucher_customer in voucher_customers}

        removed_customers_ids = existing_customers_ids - input_customers_ids
        if removed_customers_ids:
            db.session.query(VoucherCustomers).filter(VoucherCustomers.voucher_id == id).filter(
                VoucherCustomers.customer_id.in_(removed_customers_ids)).delete()
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

        new_customers_ids = input_customers_ids - existing_customers_ids
        if new_customers_ids:
            for customer_id in set(new_customers_ids):
                voucher_customer = VoucherCustomers(
                    voucher_id=id,
                    customer_id=customer_id
                )
                db.session.add(voucher_customer)
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
        return jsonify(voucher_schema.dump(voucher))


@ns.route('/<int:id>/delete')
class DeleteVoucher(Resource):
    @ns.param(name='Auth', description='Auth JWT token', _in='header', required=True)
    @ns.response(204, description='Successfully removed Voucher')
    @ns.response(404, description='Voucher not found!')
    def delete(self, id):
        try:
            voucher = Vouchers.query.get_or_404(id)
        except NotFound:
            res = jsonify({'message': 'Voucher not found!'})
            res.status_code = 404
            return res
        db.session.delete(voucher)
        db.session.commit()
        return Response(status=204)
