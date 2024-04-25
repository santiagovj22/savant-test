import logging
from persistence.sql_db import init_db
from persistence.users_dao import user_exists, create_user

LOG = logging.getLogger('Auth Service')

def init_service(app):
    '''Configure service for auth'''
    LOG.info('Starting users service')
    # Init database
    init_db(app)

def register_user(new_user):
    '''Create a user if it doesn't exist'''
    LOG.info(f'Creating user with data {new_user}')
    
    # Check if the user already exists
    user_email = new_user['email']
    if user_exists(user_email):
        LOG.info('User already exists')
        return {"message":'User already exists'}
    
    # If the user doesn't exist, create it
    created_user = create_user(new_user)
    return created_user
