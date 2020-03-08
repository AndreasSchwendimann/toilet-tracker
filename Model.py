from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import datetime


ma = Marshmallow()
db = SQLAlchemy()

# make requests with requests.post(URL, json = {'id': 3, 'name': 'test3'})

class Session(db.Model):
    __tablename__ = 'toilet_sessions'
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.Integer, nullable=False)
    end = db.Column(db.Integer, nullable=False)

    def __init__(self, start, end):
        self.start = start
        self.end = end


class Event(db.Model):
    __tablename__ = 'toilet_events'
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    action = db.Column(db.String, nullable=False)

    def __init__(self, created, location, action):
        self.created = created
        self.location = location
        self.action = action


class SessionSchema(ma.Schema):
    id = fields.Integer()
    start = fields.Integer(required=True)
    end = fields.Integer(required=True)


class EventSchema(ma.Schema):
    id = fields.Integer()
    created = fields.String()
    location = fields.String(required=True)
    action = fields.String(required=True)
