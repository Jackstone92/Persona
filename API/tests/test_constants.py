import os
import pytest

from API.constants import *


TEST_HEADERS = {
    'job': 0,
    'company': 0,
    'ssn': 0,
    'residence': 0,
    'current_location': 0,
    'blood_group': 0,
    'website': 0,
    'username': 0,
    'name': 0,
    'sex': 0,
    'address': 0,
    'mail': 0,
    'birthdate': 0
}


def test_FLASK_ENV():
    assert type(FLASK_ENV) == str, 'FLASK_ENV should be of type string'
    assert FLASK_ENV == 'FLASK_ENV', 'FLASK_ENV should have correct value'


def test_CSRF_SESSION_KEY():
    assert type(
        CSRF_SESSION_KEY) == str, 'CSRF_SESSION_KEY should be of type string'
    assert CSRF_SESSION_KEY == 'CSRF_SESSION_KEY', 'CSRF_SESSION_KEY should have correct value'


def test_SECRET_KEY():
    assert type(SECRET_KEY) == str, 'SECRET_KEY should be of type string'
    assert SECRET_KEY == 'SECRET_KEY', 'SECRET_KEY should have correct value'


def test_LOG_FILE():
    assert type(LOG_FILE) == str, 'LOG_FILE should be of type string'
    assert LOG_FILE == 'LOG_FILE', 'LOG_FILE should have correct value'


def test_DATABASE_ZIP_FILENAME():
    assert type(
        DATABASE_ZIP_FILENAME) == str, 'DATABASE_ZIP_FILENAME should be of type string'
    assert DATABASE_ZIP_FILENAME == 'fake_profiles.zip', 'DATABASE_ZIP_FILENAME should have correct value'


def test_BASE_ZIP_FILENAME():
    assert type(
        BASE_ZIP_FILENAME) == str, 'BASE_ZIP_FILENAME should be of type string'
    assert BASE_ZIP_FILENAME == 'fake_profiles.zip', 'BASE_ZIP_FILENAME should have correct value'


def test_BASE_JSON_FILENAME():
    assert type(
        BASE_JSON_FILENAME) == str, 'BASE_JSON_FILENAME should be of type string'
    assert BASE_JSON_FILENAME == 'fake_profiles.json', 'BASE_JSON_FILENAME should have correct value'


def test_BASE_API_PATH():
    assert type(BASE_API_PATH) == str, 'BASE_API_PATH should be of type string'
    assert BASE_API_PATH == os.getcwd() + '/API/', 'BASE_API_PATH should have correct value'


def test_BASE_API_DATA_PATH():
    assert type(
        BASE_API_DATA_PATH) == str, 'BASE_API_DATA_PATH should be of type string'
    assert BASE_API_DATA_PATH == os.getcwd(
    ) + '/API/data/', 'BASE_API_DATA_PATH should have correct value'


def test_PAGINATION_PER_PAGE():
    assert type(
        PAGINATION_PER_PAGE) == int, 'PAGINATION_PER_PAGE should be of type int'
    assert PAGINATION_PER_PAGE == 9, 'PAGINATION_PER_PAGE should have correct value'


def test_JSON_FILE_COLUMN_HEADERS():
    assert type(
        JSON_FILE_COLUMN_HEADERS) == list, 'JSON_FILE_COLUMN_HEADERS should be of type list'

    for item in JSON_FILE_COLUMN_HEADERS:
        assert type(
            item) == str, 'JSON_FILE_COLUMN_HEADERS items should be of type string'

        if item in TEST_HEADERS:
            TEST_HEADERS[item] += 1

    for header in TEST_HEADERS:
        assert TEST_HEADERS[header] == 1, 'JSON_FILE_COLUMN_HEADERS items should have a count of 1'


def test_teardown():
    # reset test headers
    for header in TEST_HEADERS:
        TEST_HEADERS[header] = 0
