import requests


class GitHub:
    """ first code without variables and fixture
    def get_users_defunkt(self):
        r = requests.get('https://api.github.com/users/defunkt')
        body = r.json()

        return body
    
    def get_non_exist_users(self):
        r = requests.get('https://api.github.com/users/buutenkosergii')
        body = r.json()

        return body
"""
    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            'https://api.github.com/search/repositories', params={'q': name}
            )
        body = r.json()

        return body

