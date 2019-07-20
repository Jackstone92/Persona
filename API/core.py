import os
from typing import Tuple

from flask import Flask, current_app, jsonify, Response, request

from API.database.database_manager import DatabaseManager


def create_response(data: dict = None, status: int = 200, message: str = '') -> Tuple[Response, int]:
    '''
    Creates response in a consistent format throughout the API.

    Parameters
    ----------
    data: dict 
        The data to return
    status: int
        The status code to return
    message: str
        The message to return

    Return
    ------
    Tuple(Response, int)
        The jsonified response and status code
    '''
    # ensure data is of type dict
    if type(data) is not dict and data is not None:
        raise TypeError('Data parameter should be a dictionary!')

    res = {
        'success': 200 <= status < 300,
        'message': message,
        'result': data
    }
    return jsonify(res), status


def general_exception_handler(error: Exception) -> Tuple[Response, int]:
    '''
    A general exception handler to handle all exceptions.

    Parameters
    ----------
    error: Exception
        The error raised

    Return
    ------
    Tuple(Response, int)
        The jsonified response and status code
    '''
    return create_response(data={}, message=str(error), status=500)


class MyServer(Flask):
    def __init__(self, *args, **kwargs):
        '''
        Extends flask server in order to provide custom database manager functionality.
        '''
        super(MyServer, self).__init__(*args, **kwargs)

        # instanciate additional variables
        self.db_manager = None
        self.is_committing: bool = False

    def create_database_manager(self, db):
        '''
        Creates and assigns the app database manager.
        '''
        self.db_manager = DatabaseManager(
            db=db, is_committing=self.is_committing)
