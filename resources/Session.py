from flask import request
from flask_restful import Resource
from Model import db, Session, SessionSchema

sessions_schema = CategorySchema(many=True)
session_schema = CategorySchema()

class SessionResource(Resource):
    def get(self):
        sessions = Session.query.all()
        sessions = sessions_schema.dump(session)
        return {'status': 'success', 'data': sessions}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = session_schema.load(json_data)
        if errors:
            return errors, 422
        session = Session.query.filter_by(name=data['name']).first()
        if session:
            return {'message': 'Category already exists'}, 400
        session = Session(
            name=json_data['name']
        )

        db.session.add(session)
        db.session.commit()

        result = session_schema.dump(session).data

        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = session_schema.load(json_data)
        if errors:
            return errors, 422
        session = Session.query.filter_by(id=data['id']).first()
        if not session:
            return {'message': 'Category does not exist'}, 400
        session.name = data['name']
        db.session.commit()

        result = session_schema.dump(session).data

        return {"status": 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 405
        # Validate and deserialize input
        data, errors = session_schema.load(json_data)
        if errors:
            return errors, 422
        session = Session.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = session_schema.dump(session).data

        return {"status": 'success', 'data': result}, 204
