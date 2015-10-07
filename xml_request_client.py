from xml.etree import ElementTree as et
import requests

r = requests.get("http://www.w3schools.com/xml/cd_catalog.xml")

# Old:
# with open("test.xml", "wb") as code:
#     code.write(r.content)
#
# doc = et.parse("test.xml")

# New:
doc = et.fromstring(r.text)

for cd in doc.findall("CD"):
    print("Title: {}".format(cd.find("TITLE").text))
    print("Artist: {}".format(cd.find("ARTIST").text))
    print("YEAR: {}\n".format(cd.find("YEAR").text))
