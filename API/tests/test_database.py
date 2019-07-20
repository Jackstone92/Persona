import os
import json
import pytest

import pandas as pd
from flask import jsonify

from API.constants import BASE_API_DATA_PATH
from API.database.helpers import decompress_zip, check_json_file_exists, read_json_stream
from API.database.base import create_database
from API.database.database_manager import DatabaseManager

EXISTING_JSON_FILENAME = 'fake_profiles.json'
EXISTING_ZIP_FILENAME = 'fake_profiles.zip'
TEST_JSON_FILENAME = '_test_json_file.json'


TEST_DATA = {
    'level1': {
        'level2': [
            'item1',
            'item2',
            'item3'
        ]
    }
}


# test helpers.py
def test_decompress_zip():
    assert decompress_zip(
        'nonexistentfile.zip') == False, 'Should return false for nonexistent zip file'

    # remove fake_profiles.json file for testing purposes if it already exists
    json_filename = 'fake_profiles.json'
    json_path = os.path.join(BASE_API_DATA_PATH, json_filename)

    if os.path.isfile(json_path):
        os.remove(json_path)

    assert os.path.isfile(
        json_path) == False, 'Existing JSON file should be removed (for testing purposes)'

    decompress_zip(EXISTING_ZIP_FILENAME)
    assert os.path.isfile(
        json_path) == True, 'Should return extracted JSON file from zip file'


def test_check_json_file_exists():
    assert check_json_file_exists(
        BASE_API_DATA_PATH, 'nonexistentfile.json') == False, 'Should return false for nonexistent JSON file'

    assert check_json_file_exists(
        BASE_API_DATA_PATH, EXISTING_JSON_FILENAME) == True, 'Should return true for existing JSON file'


def test_read_json_stream():
    # create test json file
    with open(os.path.join(BASE_API_DATA_PATH, TEST_JSON_FILENAME), 'w') as f:
        json.dump(TEST_DATA, f)
    f.close()

    output = [i for i in read_json_stream(
        BASE_API_DATA_PATH, TEST_JSON_FILENAME)][0]
    assert output == TEST_DATA, 'Should successfully stream json using generator'


# test base.py
def test_create_database():
    test_db = create_database()
    assert type(test_db) == type(pd.DataFrame())


# test database_manager.py
def test_database_manager():
    test_db = create_database()
    db_manager = DatabaseManager(test_db, False)

    assert db_manager.db.equals(
        test_db) == True, 'DatabaseManager db should have same values as create_database() values'

    # test fetch_one_user()
    test_username = 'mauriceharris'
    fetched_usernames = db_manager.fetch_one_user(username=test_username)
    assert len(db_manager.fetch_one_user(username=test_username)
               ) > 0, 'Should find user in database by username'


def test_teardown():
    # remove temp files
    if os.path.isfile(os.path.join(BASE_API_DATA_PATH, TEST_JSON_FILENAME)):
        os.remove(os.path.join(BASE_API_DATA_PATH, TEST_JSON_FILENAME))
