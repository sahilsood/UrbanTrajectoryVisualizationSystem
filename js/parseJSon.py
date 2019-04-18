import json

with open('trips.json') as json_file:
    data = json.load(json_file)

print data