import os
import json
import pandas as pd

from API.database.helpers import decompress_zip, read_json_stream, check_json_file_exists
from API.core import create_response
from API.constants import BASE_API_DATA_PATH, BASE_JSON_FILENAME, BASE_ZIP_FILENAME, JSON_FILE_COLUMN_HEADERS


def create_database(zipfile=BASE_ZIP_FILENAME):
    '''
    Handles the creation of the mock 'database' from the zipped json file.
    The JSON file is converted to a pandas dataframe for easier manipulation.

    While one approach might be to injest data from the zipped json file into an SQLite3 database
    and handle the updating and teardown of said database before transforming it back into json format,
    this will attempt to utilise a pandas dataframe model representation (which would be scalable to SQL
    using its .to_sql() should the need arise).

    Return
    ------
    df: Pandas Dataframe object
        The dataframe representation of the JSON file
    '''
    # extract JSON file
    try:
        decompress_zip(zipfile)
    except Exception as e:
        return create_response(data={}, status=500, message=str(e))

    # check extracted file exists
    if check_json_file_exists(BASE_API_DATA_PATH, BASE_JSON_FILENAME) == False:
        return create_response(data={}, status=500, message='Database error!')

    # read JSON data from generator and convert to pandas dataframe
    try:
        df = pd.DataFrame([dic for lst in read_json_stream(
            BASE_API_DATA_PATH, BASE_JSON_FILENAME) for dic in lst], columns=JSON_FILE_COLUMN_HEADERS)
        return df

    except Exception as e:
        return create_response(data={}, status=500, message=str(e))
