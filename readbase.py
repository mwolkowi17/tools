import sqlite3
import io

conn = sqlite3.connect('webbaza1.sqlite')
c=conn.cursor()
with io.open('utf-8.txt', 'w', encoding='utf-8') as file:
    for row in c.execute('SELECT * FROM filmy'):
        print(row[0]+row[1])
print('jeszcze raz wyswietlic?')
answer = raw_input('i co?(t/n) ')

ans='t'
if answer is ans:
    with io.open('utf-8.txt', 'w', encoding='utf-8') as file:
        for row in c.execute('SELECT * FROM filmy'):
            print(row[0]+row[1])
else:
    print('koniec')
