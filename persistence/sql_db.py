import logging
from flask_sqlalchemy import SQLAlchemy
from config.settings import DATABASE_URL

db = SQLAlchemy()
LOG = logging.getLogger('Database Connection')

def init_db(app):
    LOG.info('Start production database')
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
