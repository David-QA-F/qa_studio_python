import requests

url = 'https://api.pokemonbattle.ru/v2'
token = 'my_token'
header = {'Content-Type': 'application/json', "trainer_token": token}
trainerID = 4255


body_creat = {
    "name": "Donat",
    "photo_id": 92
}
changeName = {
    "pokemon_id": "45051",
    "name": "Donat10",
    "photo_id": 92
}
addPokebal = {
    "pokemon_id": "45066"
}

response_creat = requests.post(url = f'{url}/pokemons', headers = header, json = body_creat)
print(response_creat.text)

response_changeName = requests.put(url = f'{url}/pokemons', headers = header, json = changeName)
print(response_changeName.text)

response_addPokebal = requests.post(url = f'{url}/trainers/add_pokeball', headers = header, json = addPokebal)
print(response_addPokebal.text)