import sqlite3
conn = sqlite3.connect('godziny3d.sqlite')

c = conn.cursor()

# Utworz tabele
c.execute('''CREATE TABLE godziny
             (nazwa TEXT, czas INTEGER, data TEXT)''')

# Wstaw dane
c.execute("""INSERT INTO godziny VALUES 
        ('test', 1, '29.05.22')""")


# Zapisz zmiany
conn.commit()

# Zamkniecie polaczenia z baza danych
conn.close()
