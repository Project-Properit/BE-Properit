import json

from flask import request, jsonify
from flask_restful_swagger_3 import Resource, swagger

from app.adapters.db_adapter import insert
from app.decorators.auth_decorators import requires_auth
from app.models.property import Property
from app.resources.properties.prop_docs import prop_post_doc


class PropertyResource(Resource):
    # @requires_auth
    @swagger.doc(prop_post_doc)
    def post(self):
        data = json.loads(request.data)
        new_property = Property(address=data['address'],
                                owner=data['owner'],
                                prop_type=data['prop_type'],
                                room_num=data['room_num'],
                                rent_fee=data['rent_fee'],
                                tenants_list=None,
                                promissory=None,
                                comments=data['comments'])
        insert(new_property)
        return jsonify({'message': 'Property added successfully'})

