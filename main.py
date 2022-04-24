import sqlite3

db = sqlite3.connect("port.db")

c = db.cursor()

c.execute("""CREATE TABLE articles (
title_text text,
full_text text,
views integer,
avtor text""")




db.close()
