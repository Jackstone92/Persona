import os
import pandas as pd

from flask import request
from flask_cors import CORS

from API.config import config
from API.constants import FLASK_ENV
from API.core import MyServer, general_exception_handler, create_response
from API.database.base import create_database

from API.routes.persona import create_persona_endpoints
from API.views.frontend import frontend


def create_app(test_config=None):
    '''
    The main application factory where the flask app is created.
    It was achieved this way in order to support containerisation.

    Parameters
    ----------
    test_config: Config object
        The test configuration that can be injected for testing purposes

    Return
    ------
    app: Flask app
        The flask app

    db: Pandas dataframe
        The database
    '''
    print('Creating App...')
    # setup app
    app = MyServer(
        __name__,
        static_folder='./public',
        template_folder='./template'
    )

    CORS(app)

    # check environment to load config accordingly
    env = os.environ.get(FLASK_ENV, 'dev')

    if test_config:
        # used in order to inject configurations for testing purposes
        app.config.from_object(test_config)
    else:
        app.config.from_object(config[env])

    # create 'database' from zip file
    print('Creating Database...')
    db = create_database()
    app.create_database_manager(db)

    # register blueprints
    persona = create_persona_endpoints(app)

    app.register_blueprint(persona)
    app.register_blueprint(frontend)

    # register error handler
    app.register_error_handler(Exception, general_exception_handler)

    return app, db
