import os
import json
import pytest

import pandas as pd

from API import create_app
from API.config import config
from API.core import MyServer
from API.constants import DATABASE_ZIP_FILENAME, CSRF_SESSION_KEY, SECRET_KEY


def test_create_app():
    test_app, test_db = create_app()

    assert type(
        test_app) == MyServer, 'Should ensure app is of the correct type'

    assert type(
        test_db) == pd.DataFrame, 'Should ensure db is of the correct type'

    assert test_app.config.get(
        'DATABASE_ZIP_FILENAME') == DATABASE_ZIP_FILENAME, 'Should have correct DATABASE_ZIP_FILENAME value'
    assert test_app.config.get(
        'CSRF_ENABLED') == False, 'Should have correct CSRF_ENABLED value'
    assert len(test_app.config.get(
        'CSRF_SESSION_KEY')) == len(os.urandom(24)), 'Should have correct CSRF_SESSION_KEY type'
    assert len(test_app.config.get(
        'SECRET_KEY')) == len(os.urandom(24)), 'Should have correct SECRET_KEY type'
    assert test_app.config.get(
        'LOG_FILE') == 'api.log', 'Should have correct LOG_FILE value'


def test_development_create_app():
    test_app, _ = create_app(test_config=config['dev'])

    assert test_app.config.get(
        'DEBUG') == True, 'Should have correct DEBUG value for development'


def test_production_create_app():
    test_app, _ = create_app(test_config=config['prod'])

    assert test_app.config.get(
        'DEBUG') == False, 'Should have correct DEBUG value for production'
