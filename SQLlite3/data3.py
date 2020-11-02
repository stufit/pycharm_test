import sqlite3 as s

conn = s.connect('/Users/gaegul/PycharmProjects/pythonProject/test.db')
c = conn.cursor()
foodName = input('food name : ')
foodPrice = input('food price : ')

c.execute('insert into MenuPan2(menuName, price) values(?,?)', (foodName, foodPrice))
conn.commit()

c.execute('select * from MenuPan2')
rows = c.fetchall()


for row in rows:
    print('{} {}'.format(row[0], row[1]))



c.close()
conn.close()
