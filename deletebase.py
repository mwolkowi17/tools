import sqlite3

conn = sqlite3.connect('webbaza1.sqlite')
c=conn.cursor()

title = raw_input('podaj tytuldo skasowania: ')
print('title')

title_unicode=title.decode('utf8')

c.execute('''DELETE FROM filmy WHERE tytul=?''',(title_unicode,))

conn.commit()
conn.close()
