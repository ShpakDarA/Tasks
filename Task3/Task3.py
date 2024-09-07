import json
with open('tests.json', 'r') as file:
    data = json.load(file)
with open('values.json', 'r') as file:
    values = json.load(file)

value_dict = {item['id']: item['value'] for item in values['values']}

data_values = data.copy()
def input_values(lst):
    for item in lst:
        if item['id'] in value_dict:
            item['value'] = value_dict[item['id']]
        if 'values' in item:
            input_values(item['values'])

input_values(data_values['tests'])

with open('report.json', 'w') as json_file:
    json.dump(data_values, json_file, indent=4)