from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restx import Api

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:MySQL_password@localhost/travel_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(
    app,
    version="1.0.0",
    title="Travel Agency API",
    description="Swagger documentation of Travel Agency API",
)