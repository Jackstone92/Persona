import os

# constants
FLASK_ENV = 'FLASK_ENV'
CSRF_SESSION_KEY = 'CSRF_SESSION_KEY'
SECRET_KEY = 'SECRET_KEY'
LOG_FILE = 'LOG_FILE'
DATABASE_ZIP_FILENAME = 'DATABASE_ZIP_FILENAME'

BASE_ZIP_FILENAME = 'fake_profiles.zip'
BASE_JSON_FILENAME = 'fake_profiles.json'

BASE_API_PATH = os.getcwd() + '/API/'
BASE_API_DATA_PATH = os.getcwd() + '/API/data/'

PAGINATION_PER_PAGE = 10

JSON_FILE_COLUMN_HEADERS = [
    'job',
    'company',
    'ssn',
    'residence',
    'current_location',
    'blood_group',
    'website',
    'username',
    'name',
    'sex',
    'address',
    'mail',
    'birthdate'
]
