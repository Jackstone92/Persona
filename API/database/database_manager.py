import os
import pandas as pd
import numpy as np
import threading

from API.constants import PAGINATION_PER_PAGE, BASE_API_DATA_PATH, BASE_JSON_FILENAME


class DatabaseManager:
    def __init__(self, db, is_committing):
        '''
        While not allowed to use actual database for this task, this manager
        aims to handle simple database tasks required by the app (but reading from a
        pandas dataframe).
        '''
        self.db = db
        self.is_committing = is_committing

    def fetch_all_users(self, page: int = 0) -> dict:
        '''
        Returns all users found in the database. Note that this is paginated and returns
        x amount of users depending on the PAGINATION_PER_PAGE constant.
        '''
        pass

    def fetch_one_user(self, username: str = '') -> dict:
        '''
        Returns one user by their username.
        '''
        pass

    def delete_one_user(self, username: str = ''):
        '''
        Deletes one user from the database and updates the corresponding JSON file.
        Deletion is persistent and the JSON file is updated. It must be noted that whenever 
        the server is restarted and no JSON file is present (but a zip file is), 
        content is re-extracted from the zip file.
        '''
        pass
