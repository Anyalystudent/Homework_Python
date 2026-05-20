import requests


class YougileApi:
    def __init__(self, url):
        self.url = url

    def get_token(self, login='', password=''):
        creds = {
            'login': login,
            'password': password
        }
        resp = requests.post(self.url + '/api-v2/auth/keys/get', json=creds)
        return resp.json()[0]['key']

    def create_project(self, title):
        my_token = self.get_token()

        my_headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {my_token}'
        }

        project = {
            'title': title
        }
        resp = requests.post(self.url + '/api-v2/projects', json=project, headers=my_headers)
        return resp

    def edit_project(self, new_title, id_project):
        my_token = self.get_token()
        my_headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {my_token}'
        }
        project = {
            'title': new_title
        }
        resp = requests.put(self.url + f'/api-v2/projects/{id_project}', json=project, headers=my_headers)
        return resp

    def get_project_id(self, id_project):
        my_token = self.get_token()
        my_headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {my_token}'
        }
        resp = requests.get(self.url + f'/api-v2/projects/{id_project}', headers=my_headers)
        return resp
