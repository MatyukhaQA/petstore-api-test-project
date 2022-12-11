import allure
import requests
# from pytest_voluptuous import S

from helpers.test_data import create_pet_data, ID, URL, update_pet_data
from schemas.schemas import delete_pet_schema, pet_schema, pet_status_schema


@allure.tag('api')
def test_create_pet():
    with allure.step('Send request'):
        result = requests.post(f'{URL}/pet', json=create_pet_data)
    with allure.step('Check response code'):
        assert result.status_code == 200
    # with allure.step('Check schema'):
        # assert result.json() == S(pet_schema)
    with allure.step('Check data'):
        assert result.json()['name'] == 'fluffy'
        assert result.json()['status'] == 'available'


@allure.tag('api')
def test_get_pet():
    with allure.step('Send request'):
        result = requests.get(f'{URL}/pet/{ID}')
    with allure.step('Check response code'):
        assert result.status_code == 200
    # with allure.step('Check schema'):
        # assert result.json() == S(pet_schema)
    with allure.step('Check data'):
        assert result.json()['name'] == 'fluffy'
        assert result.json()['status'] == 'available'


@allure.tag('api')
def test_update_pet():
    with allure.step('Send request'):
        result = requests.put(f'{URL}/pet', json=update_pet_data)
    with allure.step('Check response code'):
        assert result.status_code == 200
    # with allure.step('Check schema'):
        # assert result.json() == S(pet_schema)
    with allure.step('Check data'):
        assert result.json()['name'] == 'doggie'
        assert result.json()['status'] == 'sold'


@allure.tag('api')
def test_get_by_status():
    with allure.step('Send request'):
        result = requests.get(f'{URL}/pet/findByStatus?status=sold')
    with allure.step('Check response code'):
        assert result.status_code == 200
    # with allure.step('Check schema'):
        # assert result.json() == S(pet_status_schema)
    with allure.step('Check data'):
        assert result.json()[0]["status"] == "sold"


@allure.tag('api')
def test_delete_pet():
    with allure.step('Send request'):
        result = requests.delete(f'{URL}/pet/{ID}')
    with allure.step('Check response code'):
        assert result.status_code == 200
    # with allure.step('Check schema'):
        # assert result.json() == S(delete_pet_schema)
