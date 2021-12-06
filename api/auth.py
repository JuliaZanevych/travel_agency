import base64

from flask import request, jsonify
from flask_bcrypt import check_password_hash

from config import db
from model import Customer, Permission


def auth(api_permission):
    def create_auth_handler(api_method_func):
        def process_auth(*args, **kwargs):
            headers = request.headers
            auth_header = headers.get('Authorization')
            if auth_header is None:
                res = jsonify({'message': 'Missing Authorization header!'})
                res.status_code = 401
                return res

            basic_auth_token_parts = auth_header.split(' ')

            if len(basic_auth_token_parts) != 2 or basic_auth_token_parts[0] != 'Basic':
                res = jsonify({'message': 'Invalid Basic Auth token!'})
                res.status_code = 401
                return res

            try:
                encoded_credentials = basic_auth_token_parts[1]
                decoded = str(base64.b64decode(encoded_credentials), 'utf8')
            except Exception:
                res = jsonify({'message': 'Failed decode base64 payload of Basic Auth token!'})
                res.status_code = 401
                return res

            decoded_token_parts = decoded.split(':')
            if len(decoded_token_parts) != 2:
                res = jsonify({'message': 'Invalid Basic Auth token payload!'})
                res.status_code = 401
                return res
            
            username = decoded_token_parts[0]
            password = decoded_token_parts[1]
            Permission.method = api_permission

            customer = db.session.query(Customer.password_hash, Customer.role_id).filter_by(username=username).first()
            if customer is None:
                res = jsonify({'message': 'Invalid username!'})
                res.status_code = 401
                return res

            is_valid_password = check_password_hash(customer.password_hash, password)
            if not is_valid_password:
                res = jsonify({'message': 'Invalid password!'})
                res.status_code = 401
                return res

            have_permission = db.session.execute(
                'SELECT EXISTS(SELECT 1 '
                'FROM permission_roles pr JOIN permissions p ON(p.id = pr.permission_id) '
                'WHERE pr.role_id = :role_id AND p.method = :method)', {
                    'role_id': customer.role_id,
                    'method': api_permission
                }).fetchall()[0][0]

            if not have_permission:
                res = jsonify({'message': 'Customer is not authorized to call this API!'})
                res.status_code = 403
                return res
            
            return api_method_func(*args, **kwargs)

        return process_auth

    return create_auth_handler
