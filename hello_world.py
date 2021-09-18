from flask_restful import Resource


class HelloWorld(Resource):
    def get(self, variant):
        return f'Hello World {variant}'
