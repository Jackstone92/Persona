import os

from flask import Blueprint, request

from API.core import create_response


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
        # user = app.db_manager.fetch_one_user(username=username)
        user = app.db_manager.fetch_one_user(username='mauriceharris')

        if not user:
            return create_response(
                data={}, status=404, message='Unable to find user with username {0}'.format(username))

        return create_response(data={'user': user}, status=200, message='Success')

    @persona.route('/people', methods=['GET'])
    def get_all_users():
        '''
        Returns all users with pagination.
        '''
        page = request.args.get('page', 1)

        users, total_users = app.db_manager.fetch_all_users(page=page)

        if not users or len(users) == 0:
            return create_response(data={}, status=404, message='Unable to fetch all users...')

        return create_response(data={'users': users, 'total_users': total_users}, status=200, message='Success')

    @persona.route('/people/<username>', methods=['DELETE'])
    def delete_user(username):
        '''
        Deletes a user by their given username.
        '''
        user = app.db_manager.fetch_one_user(username=username)

        if not user:
            return create_response(data={}, status=404, message='Unable to find user to delete with username {0}'.format(username))

        # user exists -> delete user
        user = app.db_manager.delete_one_user(username=username)

        if user:
            return create_response(data={}, status=500, message='Something went wrong...')

        return create_response(data={}, status=200, message='User with username {0} was successfully deleted!'.format(username))

    return persona
