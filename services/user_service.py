import logging

from persistence.users_dao import get_user_by_id, user_exists, update_user, remove_user, get_all_users

LOG = logging.getLogger('User Service')

def get_user_data(user_id):
    '''Retrieve user information by user ID'''
    LOG.info(f'Retrieving user information for user ID: {user_id}')
    user = get_user_by_id(user_id)
    return user

def update_user_data(user_id, user):
    '''Update user information by user ID'''
    LOG.info(f'Updating user information for user ID: {user_id}')
    updated_user = update_user(user_id, user)
    return updated_user


def delete_user(user_id):
    '''Remove user by user ID'''
    LOG.info(f'Removing user information for user ID: {user_id}')
    user = remove_user(user_id)
    return user


def get_all_users_data():
    '''Retrieve all users'''
    LOG.info('Retrieving all users')
    users = get_all_users()
    return users