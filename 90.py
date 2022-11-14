import sqlite3
import csv

con = sqlite3.connect('database.db')

cur = con.cursor()

res = cur.execute('SELECT * FROM countries WHERE area >= 2000000')

col_names = [description[0] for description in cur.description]

with open('countries._big_area.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(col_names)
    for country in res:
        writer.writerow(country)
