from flask import request
from flask_restful import Resource
from Model import db, Event, EventSchema

events_schema = EventSchema(many=True)
event_schema = EventSchema()

class EventResource(Resource):
    def get(self):
        events = Event.query.all()
        events = events_schema.dump(events)
        return {'status': 'success', 'data': events}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = event_schema.load(json_data)
        if errors:
            return errors, 422
        event = Event(
            location=json_data['location'],
            created=json_data['created']
        )

        db.session.add(event)
        db.session.commit()

        result = event_schema.dump(event).data

        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = event_schema.load(json_data)
        if errors:
            return errors, 422
        event = Event.query.filter_by(id=data['id']).first()
        if not event:
            return {'message': 'Category does not exist'}, 400
        event.location = data['location']
        event.created = data['created']
        db.session.commit()

        result = event_schema.dump(event).data

        return {"status": 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 405
        # Validate and deserialize input
        data, errors = event_schema.load(json_data)
        if errors:
            return errors, 422
        event = Event.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = event_schema.dump(event).data

        return {"status": 'success', 'data': result}, 204
