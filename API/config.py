import os

from API.constants import CSRF_SESSION_KEY, SECRET_KEY, DATABASE_ZIP_FILENAME


class Config:
    '''
    Base Configurations
    '''
    DATABASE_ZIP_FILENAME = os.environ.get(
        DATABASE_ZIP_FILENAME,
        'fake_profiles.zip'
    )

    CSRF_ENABLED = False
    CSRF_SESSION_KEY = os.environ.get(
        CSRF_SESSION_KEY,
        os.urandom(24)
    )

    SECRET_KEY = os.environ.get(
        SECRET_KEY,
        os.urandom(24)
    )
    LOG_FILE = "api.log"  # where logs are outputted to


class DevelopmentConfig(Config):
    '''
    Development Configurations
    '''
    DEBUG = True


class ProductionConfig(Config):
    '''
    Production Configurations
    '''
    DEBUG = False
    CSRF_ENABLED = True


# map to configuration based on FLASK_ENV type
config = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}
