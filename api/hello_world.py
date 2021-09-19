from config import api
from flask_restx import Namespace, Resource

ns = Namespace('Hello World API', description='First Hello World API for lab 4')
api.add_namespace(ns)


@ns.route('/api/v1/hello-world-<int:variant>')
class HelloWorld(Resource):
    def get(self, variant):
        return f'Hello World {variant}'