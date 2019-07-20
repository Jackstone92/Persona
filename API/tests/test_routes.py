import os
import json
import pytest

from API import create_app
from API.core import create_response
from API.constants import JSON_FILE_COLUMN_HEADERS, PAGINATION_PER_PAGE

TEST_USERNAME = 'mauriceharris'
NOT_IN_DATABASE_USERNAME = 'asdflkjhweiruvad8f2e7r8ad8v87cvasdfhwe7d7d7d'


@pytest.fixture
def client():
    test_app, _ = create_app()

    with test_app.test_client() as client:
        yield client


def test_non_route(client):
    req = client.get('/')
    res = req.get_json()

    error_message = '404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.'
    assert res['message'] == error_message, 'Should gracefully prevent non-routes from being accessed'


def test_get_user(client):
    req = client.get('/search/{0}'.format(TEST_USERNAME))
    res = req.get_json()

    data = res.get('result')
    user = data.get('user')
    user_data = user[0]

    assert type(data) == dict, 'Should return data as a dictionary'
    assert type(user) == list and len(user) > 0, 'Should return a user'
    assert type(user_data) == dict, 'Should return user data as a dictionary'

    # check that all expected headers are present
    for header in JSON_FILE_COLUMN_HEADERS:
        assert header in user_data, 'Should include all expected headers in returned user data'


def test_get_all_users(client):
    req = client.get('/people')
    res = req.get_json()

    data = res.get('result')
    users = data.get('users')

    assert type(data) == dict, 'Should return data as a dictionary'
    assert type(users) == list and len(users) > 0, 'Should return users'

    assert 'total_users' in data, 'Should return total users in returned users data'

    assert len(
        users) == PAGINATION_PER_PAGE, 'Should return paginated list of users with a fixed number ({0})'.format(PAGINATION_PER_PAGE)

    for user in users:
        for header in JSON_FILE_COLUMN_HEADERS:
            assert header in user, 'Should include all expected headers for each user'


def test_pagination_with_get_all_users(client):
    req_page_1 = client.get('/people?page=1')
    res_page_1 = req_page_1.get_json()
    data_page_1 = res_page_1.get('result')
    users_page_1 = data_page_1.get('users')

    req_page_2 = client.get('/people?page=2')
    res_page_2 = req_page_2.get_json()
    data_page_2 = res_page_2.get('result')
    users_page_2 = data_page_2.get('users')

    # check different users are returned
    for i in range(PAGINATION_PER_PAGE):
        user_1 = users_page_1[i]
        user_2 = users_page_2[i]

        assert user_1 != user_2, 'Should return different results depending on given page parameter'

    # check users out of range are handled gracefully
    req_out_of_range = client.get('/people?page=123456789')
    res_out_of_range = req_out_of_range.get_json()

    error_message = 'Unable to fetch all users...'

    assert res_out_of_range.get(
        'message') == error_message, 'Should display graceful message when page is out of range'


def test_delete_user(client):
    # test user is available
    req = client.get('/search/{0}'.format(TEST_USERNAME))
    res = req.get_json()
    data = res.get('result')
    user = data.get('user')

    assert len(user) > 0, 'Should be able to find user by username before deletion'

    # check cannot delete user with username that is not in the database
    req_fail = client.delete('/people/{0}'.format(NOT_IN_DATABASE_USERNAME))
    res_fail = req_fail.get_json()

    assert res_fail.get('message') == 'Unable to find user to delete with username {0}'.format(
        NOT_IN_DATABASE_USERNAME)

    # test delete
    req = client.delete('/people/{0}'.format(TEST_USERNAME))
    res = req.get_json()

    deletion_message = 'User with username {0} was successfully deleted!'.format(
        TEST_USERNAME)

    assert res.get(
        'message') == deletion_message, 'Should successfully delete user and receive correct message'

    # test cannot get user after deletion
    req_check = client.get('/search/{0}'.format(TEST_USERNAME))
    res_check = req_check.get_json()

    check_message = 'Unable to find user with username {0}'.format(
        TEST_USERNAME)

    assert res_check.get(
        'message') == check_message, 'Should not be able to fetch user after deletion'
