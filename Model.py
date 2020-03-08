from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()

# make requests with requests.post(URL, json = {'id': 3, 'name': 'test3'})

class Session(db.Model):
    __tablename__ = 'toilet_session'
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.String, nullable=False)
    end = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    def __init__(self, start, end, duration):
        self.start = start
        self.end = end
        self.duration = duration


class SessionSchema(ma.Schema):
    id = fields.Integer()
    start = fields.Str(required=True)
    end = fields.Str(required=True)
    duration = fields.Integer(required=True)
