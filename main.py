import sqlite3

db = sqlite3.connect("port.db")

c = db.cursor()

#c.execute("""CREATE TABLE articles (
#title_text text,
#full_text text,
#views integer,
#avtor text""")

c.execute("INSERT INTO articles VALUES ('Google is cool!', 'Google is realy cool', 100, 'Admin')")


db.commit()



db.close()
