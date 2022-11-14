import sqlite3

con = sqlite3.connect('database.db')

cur = con.cursor()

res = cur.execute('SELECT * FROM countries WHERE area >= 2000000')

listCountries = res.fetchall()

for country in listCountries:
    print(country[1])
