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
        self.is_committing_event = threading.Event()

    def fetch_all_users(self, page: int = 0) -> dict:
        '''
        Returns all users found in the database. Note that this is paginated and returns
        x amount of users depending on the PAGINATION_PER_PAGE constant.
        '''
        # handle page edge cases
        page = int(page)
        if page < 1:
            page = 1

        total_users = self.db.shape[0]
        if page > total_users:
            page = total_users - PAGINATION_PER_PAGE

        # determine current page and page limit values
        offset = (page - 1) * PAGINATION_PER_PAGE
        page_limit = offset + PAGINATION_PER_PAGE

        try:
            paginated_users = self.db.iloc[offset: page_limit, :].to_dict(
                orient='records')
            return paginated_users, total_users

        except Exception as e:
            return create_response(data={}, status=404, message='Unable to fetch all users... {0}'.format(e))

    def fetch_one_user(self, username: str = '') -> dict:
        '''
        Returns one user by their username.
        '''
        if username == '':
            return create_response(data={}, status=404, message='Unable to find user as username was not specified.')

        user = self.db.loc[self.db['username'] ==
                           username].to_dict(orient='records')
        return user

    def _wait_until_done_committing(self):
        if not self.is_committing:
            self.is_committing_event.set()

    def delete_one_user(self, username: str = ''):
        '''
        Deletes one user from the database and updates the corresponding JSON file.
        Deletion is persistent and the JSON file is updated. It must be noted that whenever 
        the server is restarted and no JSON file is present (but a zip file is), 
        content is re-extracted from the zip file.
        '''
        if username == '':
            return create_response(data={}, status=404, message='Unable to delete user as username was not specified.')

        try:
            user_to_delete = self.db.loc[self.db['username'] == username]

            thread = threading.Thread(target=self._wait_until_done_committing)
            thread.start()

            # wait for any committing to complete
            self.is_committing_event.wait()

            # remove user from db and update json file
            self.is_committing = True
            self.db.drop(user_to_delete.index, inplace=True)
            self._update_json()
            return None

        except Exception as e:
            self.is_committing = False
            return create_response(data={}, status=404, message='Unable to delete user as username was not specified. {0}'.format(e))

    async def _update_json(self):
        '''
        Updates raw JSON file to reflect database deletions. 
        Sets is_committing to False upon completion.
        '''
        try:
            json_path = os.path.join(BASE_API_DATA_PATH, BASE_JSON_FILENAME)
            self.db.to_json(json_path)
            self.is_committing = False

        except Exception as e:
            self.is_committing = False
            return create_response(data={}, status=500, message='Error saving deletion changes to database... {0}'.format(e))
