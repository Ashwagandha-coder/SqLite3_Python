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

#c.execute("INSERT INTO articles VALUES ('Facebook is cool!', 'Meta is realy cool', 50, 'Mora')")

# Выборка значений




db.commit()



db.close()
