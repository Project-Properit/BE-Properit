from functools import wraps

from flask import request, jsonify, make_response
from jwt import jwt
from jwt.jwk import OctetJWK

from app.models.tokenmodel import TokenModel
from app.settings import APP_SECRET_KEY

token_manager = jwt.JWT()


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
        if not token:
            return jsonify({'message': 'a valid token is missing'})
        try:
            if TokenModel.objects(token=token):
                raise
            token_manager.decode(token, OctetJWK(APP_SECRET_KEY))
        except:
            return jsonify({'message': 'token is invalid'})

        return f(*args, **kwargs)

    return decorator


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return make_response('could not verify', 401, {'Basic realm': 'login required'})
        return f(*args, **kwargs)
    return decorated
