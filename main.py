import sqlite3

db = sqlite3.connect("port.db")

c = db.cursor()

# Создание таблицы

#c.execute("""CREATE TABLE articles (
#title_text text,
#full_text text,
#views integer,
#avtor text""")

# Добавление значений в таблицу

#c.execute("INSERT INTO articles VALUES ('Amazon is cool!', 'Amazon is realy cool', 50, 'Mora')")



# Выборка значений
c.execute("SELECT rowid, * FROM articles WHERE rowid < 5 ORDER BY views DESC")
items = c.fetchall()

for el in items:
    print(el[1] + "\n" + el[4])


db.commit()



db.close()
