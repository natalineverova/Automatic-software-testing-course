import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api): #add fixture
    user = github_api.get_user('defunkt')#add variable and use fixture
    assert user['login'] == 'defunkt'
    """
def test_user_exists(): #first code without fixture
    api = GitHub()
    user = api.get_users_defunkt()
    assert user['login'] == 'defunkt'
"""

@pytest.mark.api
def test_user_nnon_exist(github_api): #add fixture
    api = GitHub()
    r = github_api.get_user('butenkosergii') #add variable and use fixture
    assert r['message'] == 'Not Found'

    """
def test_user_non_exist():#first code without fixture
    api = GitHub()
    r = api.get_non_exist_users()
    #print(r) -see on message
    assert r['message'] == 'Not Found'"""

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    #print(r) - check total count
    assert r['total_count'] == 30
    assert 'become-qa-auto' in r['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0
