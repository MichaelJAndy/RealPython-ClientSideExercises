import sqlite3

with sqlite3.connect("tv.db") as connection:
    c = connection.cursor()

    # create a table
    c.execute("""CREATE TABLE horror_shows
                        (series_name TEXT, first_aired DATE, network TEXT,
                        overview TEXT)""")
