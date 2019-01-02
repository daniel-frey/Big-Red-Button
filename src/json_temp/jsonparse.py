import json

file_data = open('jsonparse.json').read()
json_data = json.loads(file_data)

print(json_data)

temp_data = input('Enter a user_name')
json_data['name'] = temp_data

print(json_data)

with open('jsonparsenew.json', 'w') as f:
    json.dump(json_data, f)

