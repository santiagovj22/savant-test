import logging
from sqlalchemy.exc import SQLAlchemyError
from persistence.sql_db import db
from models.models import User

LOG = logging.getLogger('Users Dao')


def user_exists(user_email):
    '''search if the user is registered'''
    LOG.info('Searching for user %s', user_email)
    try:
        return User.query.filter_by(email=user_email).first() is not None
    except SQLAlchemyError as e:
        LOG.error('Error in user_exists: %s', str(e))
        return None

def create_user(user):
    '''Create user in the database'''
    try:
        new_user = User(
        full_name=user['full_name'],
        email=user['email'],
        password=user['password'],
        cellphone=user['cellphone']
     )
        db.session.add(new_user)
        db.session.commit()
        return new_user
    except SQLAlchemyError as e:
        db.session.rollback()
        LOG.error('Error to create user: %s', str(e))
        return None

def get_user_by_id(user_id):
    '''Retrieve user information by user ID'''
    LOG.info(f'Querying user with ID: {user_id}')
    try:
        user_data = User.query.filter_by(id=user_id).first()
        if user_data:
            user = {
                'id': user_data.id,
                'full_name': user_data.full_name,
                'email': user_data.email,
                'cellphone': user_data.cellphone
            }
            LOG.info('User found: %s', user)
            return user
        else:
            return None
    except SQLAlchemyError as e:
        LOG.error('Error in get_user_by_id: %s', str(e))
        return None
    
def update_user(user_id, user):
    '''Update user information by user ID'''
    LOG.info(f'Updating user information for user ID: {user_id}')
    try:
        user_data = User.query.filter_by(id=user_id).first()
        LOG.info(user_data)
        if user_data:
            for key, value in user.items():
                if hasattr(user_data, key):
                    setattr(user_data, key, value)
            db.session.commit()
            user_updated = {
                'id': user_data.id,
                'full_name': user_data.full_name,
                'email': user_data.email,
                'cellphone': user_data.cellphone
            }
            return user_updated
        else:
            return None
    except SQLAlchemyError as e:
        db.session.rollback()
        LOG.error('Error in update_user: %s', str(e))
        return None
    
def remove_user(user_id):
    '''Remove user by user ID'''
    LOG.info(f'Removing user information for user ID: {user_id}')
    try:
        user_data = User.query.filter_by(id=user_id).first()
    
        if user_data:
            db.session.delete(user_data)
            db.session.commit()
            return "User removed successfully"
        else:
            return None
    except SQLAlchemyError as e:
        db.session.rollback()
        LOG.error('Error in remove_user: %s', str(e))
        return None

def get_all_users():
    '''Retrieve all users'''
    LOG.info('Querying all users')
    try:
        users = User.query.all()
        all_users = []
        for user in users:
            all_users.append({
                'id': user.id,
                'full_name': user.full_name,
                'email': user.email,
                'cellphone': user.cellphone
            })
        return all_users
    except SQLAlchemyError as e:
        LOG.error('Error in get_all_users: %s', str(e))
        return None