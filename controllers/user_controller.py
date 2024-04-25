import logging
from flask_restx import Resource
from flask import request

from utils.serialization import Serialize
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.user_service import get_user_data, update_user_data, delete_user, get_all_users_data

LOG = logging.getLogger('User Controller')

def init_user_controller(main_app, api):
    ''' Configure User controller '''
    LOG.info('Starting User Controller')
    
    class User(Resource):
        '''A resource controller for User'''
        @jwt_required()
        def get(self, user_id):
            LOG.info(f'Requesting user information for user ID: {user_id}')
            current_user_id = get_jwt_identity()
            if current_user_id != user_id:
                return {"message": "Unauthorized"}, 401
            user = get_user_data(user_id)
            user_data = Serialize.json_convert(user)
            if user:
                return {'data':user_data}, 200
            else:
                return {"message": "User not found"}, 404
        
        @jwt_required()
        def patch(self,user_id):
            try:
                current_user_id = get_jwt_identity()
                if current_user_id != user_id:
                    return {"message": "Unauthorized"}, 401
                data = request.get_json()
                updated_user  = update_user_data(user_id, data)
                return {"data":Serialize.json_convert(updated_user)} 
            except:
                LOG.error('Error updating user')
                return None, 401
            
        @jwt_required()
        def delete(self, user_id):
            try:
                LOG.info(f'Removing user information for user ID: {user_id}')
                current_user_id = get_jwt_identity()
                if current_user_id != user_id:
                    return {"message": "Unauthorized"}, 401
                
                deleted_user = delete_user(user_id)
                if deleted_user:
                    return {'message': f'User with ID {user_id} deleted successfully'}, 200
                else:
                    return {"message": "User not found"}, 404
            except:
                LOG.error('Error deleting user')
                return {"message": "Internal Server Error"}, 500


    class Users(Resource):
        '''A resource controller for Users'''
        def get(self):
            try:
                LOG.info('Requesting all user information')
                users = get_all_users_data()
                if users:
                    return {'data':Serialize.json_convert(users)}, 200
                else:
                    return {"message": "No users found"}, 404
            except:
                LOG.error('Error validating token')
                return None, 401

    # Handle user information
    api.add_resource(Users, '/api/users')
    api.add_resource(User, '/api/users/<string:user_id>')
