from flask import request, jsonify
from flask_restful import Resource
from app.utils import token_required, roles_accepted

class Test(Resource):
    @token_required
    @roles_accepted('hr')
    def get(self):
        auth_header = request.headers.get('Authorization', 'No Auth header')
        print(f"Headers: {dict(request.headers)}")
        print(f"Auth header: {auth_header}")
        data = {
            "token_data" : request.token_data,
            "clerk_id": request.clerk_id,
            "public_metadata": request.public_metadata}
        print(f"Token data: {data}")
        return jsonify({'message': 'Hello, World!', 'headers': dict(request.headers), "data": data})