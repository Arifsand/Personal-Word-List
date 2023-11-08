import requests

api_key = 'a24daa00-9d69-44ec-b425-356872bb7da4'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)
definitions = res.json()

# print(definitions)
for definition in definitions:
    print(definition)
