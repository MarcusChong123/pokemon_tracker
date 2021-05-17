import requests
from datetime import datetime

def main():
    for i in range(1, 151):
        pokemon_req = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}/')
        pokemon_req = pokemon_req.json()
        print (pokemon_req['name'])

main()
print (datetime.now())
