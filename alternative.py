import json
from request import parser
from store import database


with open('request/resultTwo.json', encoding='utf-8') as file:
    items = json.load(file)

formatted = parser.extract(items)

database.insert_data(formatted)
