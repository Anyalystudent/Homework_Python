import requests
import pytest
from YouGileApi import YougileApi

api = YougileApi('https://yougile.com')


def test_add_project_positive():
    api.get_token()

    title = "Тестовый проект"
    result = api.create_project(title)

    assert result.status_code == 201
    assert result.json()['id'] is not None


def test_add_project_negative():
    '''
    ошибка в отсутствии title
    '''
    my_token = api.get_token()

    my_headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {my_token}'
    }
    resp = requests.post('https://yougile.com/api-v2/projects', headers=my_headers)

    assert resp.status_code == 400
    assert "title should not be empty" in resp.json()['message']


def test_edit_project_positive():
    '''
    проверяет, что после редактирования id не меняется
    '''
    title = "Москва"
    result = api.create_project(title)
    id_project = result.json()['id']

    new_title = "Саратов"
    edited = api.edit_project(new_title, id_project)

    assert edited.status_code == 200
    assert edited.json()['id'] == id_project


def test_edit_project_negative():
    '''
    ошибка в том, что в headers не передан token
    '''
    title = "4444"
    result = api.create_project(title)
    id_project = result.json()['id']

    new_title = "8888"
    my_token = api.get_token()
    my_headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer'
    }
    project = {
        'title': new_title
    }
    edited = requests.put('https://yougile.com/api-v2/projects/{id_project}', json=project, headers=my_headers)

    assert edited.status_code == 401
    assert "Unauthorized" in edited.json()['message']


def test_get_project_positive():
    '''
    проверяет, что после редактирования id не меняется
    '''
    title = "Первый"
    result = api.create_project(title)
    id_project = result.json()['id']

    project_id = api.get_project_id(id_project)
    assert project_id.status_code == 200
    assert project_id.json()['id'] == id_project


def test_get_project_negative():
    '''
    ошибка в неверном значении id
    '''
    id_project = '8edced58-b60b-4810-a32b-ce70fbfbe05a'

    my_token = api.get_token()
    my_headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {my_token}'
    }
    project_id = requests.get('https://yougile.com/api-v2/projects/{id_project}', headers=my_headers)
    assert project_id.status_code == 404
    assert "Проект не найден" in project_id.json()['message']
