import os
import json
import zipfile

from API.constants import BASE_API_DATA_PATH


def decompress_zip(filename: str = '') -> bool:
    '''
    Decompresses a zip file and returns the json content.
    '''
    path = os.path.join(BASE_API_DATA_PATH, filename)

    if os.path.isfile(path):
        with zipfile.ZipFile(path, 'r') as z:
            z.extractall(BASE_API_DATA_PATH)
        z.close()
        return True

    return False


def check_json_file_exists(path: str, filename: str) -> bool:
    '''
    Checks whether a json file exists given a path and the filename.
    '''
    return os.path.isfile(os.path.join(path, filename))


def read_json_stream(path: str, filename: str):
    '''
    Generator for streaming content of a JSON file.
    '''
    start_pos = 0

    with open(os.path.join(path, filename), 'r') as f:
        while True:
            try:
                obj = json.load(f)
                yield obj
                return

            except json.JSONDecodeError as e:
                f.seek(start_pos)
                json_str = f.read(e.pos)
                obj = json.loads(json_str)
                start_pos += e.pos
                yield obj
    f.close()
