import json
import requests

output = "json"
origin = "Central+Park"
destination = "Times+Square"
sensor = "false"
mode = "walking"

url = "https://maps.googleapis.com/maps/api/directions/{}?origin={}&destination={}&sensor={}&mode={}".format(output, origin, destination, sensor, mode)

print(url)

r = requests.get(url)
json_output = json.loads(r.text)

print(json_output['status'])

for route in json_output['routes']:
    for leg in route['legs']:
        for step in leg['steps']:
            print(step["html_instructions"])
