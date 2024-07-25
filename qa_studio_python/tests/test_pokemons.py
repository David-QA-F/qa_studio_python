import requests
import pytest

url = 'https://api.pokemonbattle.ru/v2'
token = 'my_token'
header = {'Content-Type' : 'application/json', "trainer_token": token}
trainerID = 4255


def test_status_code():
    response = requests.get(url = f'{url}/trainers', params = {"trainer_id": trainerID})
    assert response.status_code == 200

def test_trainer_list():
    response_get = requests.get(url = f'{url}/trainers', params = {"trainer_id": trainerID})
    assert response_get.json()['data'][0]['trainer_name'] == "David"

@pytest.mark.parametrize('key, value', [('trainer_name', 'David'), ("id", '4255'), ('level', '5')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{url}/trainers', params = {"trainer_id": trainerID})
    assert response_parametrize.json()['data'][0][key] == value