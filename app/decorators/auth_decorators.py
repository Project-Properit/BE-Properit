from functools import wraps

from flask import request, jsonify, make_response
from jwt import jwt
from jwt.jwk import OctetJWK

from app.models.tokenmodel import TokenModel
from app.settings import APP_SECRET_KEY

token_manager = jwt.JWT()


def token_required(return_user=False):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = None
            if 'x-access-tokens' in request.headers:
                token = request.headers['x-access-tokens']
            if not token:
                return jsonify('valid token is missing.', 403)
            try:
                if TokenModel.objects(token=token):
                    raise
                user = token_manager.decode(token, OctetJWK(APP_SECRET_KEY))
                if return_user:
                    kwargs['token_user_id'] = user['id']
            except:
                return jsonify('token is invalid', 403)
            return f(*args, **kwargs)

        return wrapper

    return decorator


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return make_response('login required', 401)
        return f(*args, **kwargs)

    return decorated
