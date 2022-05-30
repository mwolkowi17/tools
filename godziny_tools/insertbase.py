import sqlite3

conn = sqlite3.connect('godziny3d.sqlite')
c=conn.cursor()

title = raw_input('podaj tytul: ')

godziny = raw_input('podaj ile czasu: ')

data = raw_input('podaj date ukonczenia: ')



#title.encoding='uft-8'
#price.encoding='uft-8'
title_unicode=title.decode('utf8')
godziny_unicode=godziny.decode('utf8')
data_unicode=data.decode('utf8')
c.execute('''INSERT INTO godziny VALUES (?,?,?)''',(title_unicode,godziny_unicode,data))

conn.commit()
conn.close()
