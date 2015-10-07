from xml.etree import ElementTree as et

doc = et.parse("cars.xml")

for element in doc.findall("CAR"):
    print("{} {} ${}".format(element.find("MAKE").text, element.find("MODEL").text, element.find("COST").text))

