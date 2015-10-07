import json

output = json.load(open("cars.json"))

print(output["CARS"][0]["MODEL"])

# Wrong
# print(output[0]["CAR"][0]["MODEL"])

