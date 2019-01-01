import json

file_data = open('jsonparse.json').read()
json_data = json.loads(file_data)

print(json_data)

json_data['name'] = 'roger'

print(json_data)

with open('jsonparsenew.json', 'w') as f:
    json.dump(json_data, f)

