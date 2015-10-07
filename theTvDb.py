import requests
import sqlite3
from xml.etree import ElementTree as et

r = requests.get("http://thetvdb.com/api/GetSeries.php?seriesname=Horror")

data = et.fromstring(r.text)

with sqlite3.connect("tv.db") as connection:
    c = connection.cursor()

    # iterate through each movie and write to the database
    for show in data.findall('Series'):

        c.execute("INSERT INTO horror_shows VALUES(?, ?, ?, ?)",
                  (show.find("SeriesName").text,
                   show.find("FirstAired").text,
                   show.find("Network").text,
                   show.find("Overview").text))

    # retrieve data
    c.execute("SELECT * FROM horror_shows ORDER BY series_name ASC")

    # fetchall() retrieves all records from the query
    rows = c.fetchall()

    # output the rows to the screen, row by row
    for r in rows:
        print(r[0], r[1], r[2], r[3])
