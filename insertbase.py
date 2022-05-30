import sqlite3

conn = sqlite3.connect('webbaza1.sqlite')
c=conn.cursor()

title = raw_input('podaj tytul: ')
print('title')
price = raw_input('podaj cene: ')
print('cena')

#title.encoding='uft-8'
#price.encoding='uft-8'
title_unicode=title.decode('utf8')
price_unicode=price.decode('utf8')
c.execute('''INSERT INTO filmy VALUES (?,?)''',(title_unicode,price_unicode))

conn.commit()
conn.close()
