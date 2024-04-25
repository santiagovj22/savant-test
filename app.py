import logging

from flask_restx import Api
from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from persistence.sql_db import db
from flask_cors import CORS

from config.settings import DATABASE_URL, JWT_SECRET_KEY

from controllers.auth_controller import init_auth_controller
from controllers.user_controller import init_user_controller


# Init flask app
app = Flask(__name__)

# Configuration from .env
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
app.config['DATABASE_URL'] = DATABASE_URL
migrate = Migrate(app, db)
jwt = JWTManager(app)

#configure_jwt(main_app)

# Handling Logs
LOG_FILENAME = './logs/app.log'
logging.basicConfig(level=logging.INFO,
                    filename=LOG_FILENAME,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app.logger.debug('Server running..')

# Configure api
api = Api(app, validate=True, title='Savant API',
          description='Rest Api for Savant')

# Configure cors
CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})

# Configure controller
init_auth_controller(app, api)
init_user_controller(app, api)

# Launch app local mode
if __name__ == "__main__":
    app.run(debug=False)
