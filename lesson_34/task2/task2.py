import json
from pprint import pprint
import requests

url = 'https://jsonplaceholder.typicode.com/posts'
r = requests.get(url)
json_data = r.json()
pprint(json_data)

with open("data.json", 'w') as f:
    print(json_data, file=f)
