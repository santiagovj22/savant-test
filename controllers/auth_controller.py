import logging

from flask_restx import Resource
from flask import request
from flask_jwt_extended import create_access_token
from services.auth_service import init_service, register_user
from utils.auth import set_password

LOG = logging.getLogger('Auth Controller')

def init_auth_controller(main_app, api):
    ''' Configure Auth controller '''
    LOG.info('Starting Auth Controller')

    init_service(main_app)

    class Auth(Resource):
        '''A resource controller for Authentication'''
        def post(self):
            LOG.info('Entering to login user')
            try:
                LOG.info(request)
                data = request.get_json()
                LOG.info('data input-->  %s', data)
                new_user = {
                    'full_name':  data['full_name'],
                    'cellphone': data['cellphone'],
                    'email': data['email'],
                    'password': set_password(data['password'])
                }
                LOG.info('New user %s', new_user)
                user = register_user(new_user)
                if user is None:
                    return None, 401
                access_token = create_access_token(identity=user.id)
                return {'token': access_token}, 200
            except:
                LOG.error('Error in auth')
                return None, 401

    # Handle users collections
    api.add_resource(Auth, '/api/auth/login')
