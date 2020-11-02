import sqlite3 as s

conn = s.connect('/Users/gaegul/PycharmProjects/pythonProject/test.db')
cur = conn.cursor()
c = conn.cursor()
foodName = input('food name : ')
foodPrice = input('food price : ')


c.execute('drop table if exists MenuPan2')
c.execute('create table MenuPan2(menuName char(50), price int)')
cur.execute('insert into MenuPan2(menuName, price) values(?,?)', (foodName, foodPrice))




conn.commit()

c.execute('select * from MenuPan2')
rows = c.fetchall()

for row in rows:
    print('{} {}'.format(row[0], row[1]))