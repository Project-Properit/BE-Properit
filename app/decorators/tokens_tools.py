from functools import wraps

from flask import request, jsonify
from jwt import jwt
from jwt.jwk import OctetJWK

from app.models.user import User, LogoutToken
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
            if LogoutToken.query.filter_by(token=token).first():
                raise
            data = token_manager.decode(token, OctetJWK(APP_SECRET_KEY))
            current_user = User.query.filter_by(name=data['name']).first()
        except:
            return jsonify({'message': 'token is invalid'})

        return f(current_user, *args, **kwargs)

    return decorator
