import json
from pprint import pprint

with open('trips.json') as f:
    data = json.load(f)
    for i in range(0,100):
    	for j in data["features"][i]["properties"]['streetnames']:
    		pprint(j)