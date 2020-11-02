import sqlite3 as s

conn = s.connect('/Users/gaegul/PycharmProjects/pythonProject/test.db')
c = conn.cursor()

c.execute('drop table if exists MenuPan2')
c.execute('create table MenuPan2(menuName char(50), price int)')
c.execute('insert into menupan2 values("김밥", 3000) ')
c.execute('insert into menupan2 values("순두부", 6000) ')
c.execute('insert into menupan2 values("육개장", 7500) ')
c.execute('insert into menupan2 values("칼국수", 5500) ')
c.execute('insert into menupan2 values("자짱밥", 5500) ')
c.execute('insert into menupan2 values("김치찌게", 8000) ')


while True:
    su = int(input('조회 : 0, 저장 : 1, 가격변경 : 2, 상품명변경 : 3, 삭제 : 4, 종료 : 5 >'))

    if su == 0:
        c.execute('select * from MenuPan2')
    elif su == 1:
        foodName = input('food name : ')
        foodPrice = int(input('food price : '))
        c.execute('insert into MenuPan2 values(?,?)', [foodName, foodPrice])
        conn.commit()
    elif su == 2:
        foodPrice = int(input('food price : '))
        changeFoodPrice = int(input('food price : '))
        c.execute('update MenuPan2 set price =? where menuName = ?', [changeFoodPrice, foodName])
    elif su == 3:
        foodName = int(input('food name : '))
        changeFoodName = int(input('change food name : '))
        c.execute('update MenuPan2 set menuName =? where menuName = ?', [changeFoodName, foodName])
        conn.commit()
    elif su == 4:
        foodName = int(input('delete food name : '))
        c.execute('delete from MenuPan2 where menuName = ?', [foodName])
        conn.commit()
    elif su == 5:
        print('종료합니다.')
        break

    c.execute('select * from MenuPan2')
    rows = c.fetchall()
    for row in rows:
        print('{} {}'.format(row[0], row[1]))

c.close()
conn.close()