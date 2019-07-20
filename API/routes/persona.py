import os

from flask import Blueprint, request


def create_persona_endpoints(app):
    persona = Blueprint(
        'persona',
        __name__,
        static_folder='./public',
        template_folder='./template'
    )

    # handle RESTful API routes
    @persona.route('/search/<username>', methods=['GET'])
    def get_user(username):
        '''
        Searches through data for specific username.
        '''
        return ''

    @persona.route('/people', methods=['GET'])
    def get_all_users():
        '''
        Returns all users with pagination.
        '''
        return ''

    @persona.route('/people/<username>', methods=['DELETE'])
    def delete_user(username):
        '''
        Deletes a user by their given username.
        '''
        return ''

    return persona
