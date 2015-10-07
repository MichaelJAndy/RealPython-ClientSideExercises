# Using the Google Direction API, pull driving directions from San Francisco to Los Angeles in XML.
# Extract the step-by-step driving directions.


import requests
from xml.etree import ElementTree as et

output = "xml"
origin = "San+Francisco"
destination = "Los+Angeles"
sensor = "false"
mode = "driving"

url = "https://maps.googleapis.com/maps/api/directions/{}?origin={}&destination={}&sensor={}&mode={}".format(output, origin, destination, sensor, mode)

print(url)

r = requests.get(url)

parse = et.fromstring(r.text)

for route in parse.findall("route"):
    for leg in route.findall("leg"):
        for step in leg.findall("step"):
            print(step.find("html_instructions").text)
