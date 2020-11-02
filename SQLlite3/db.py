import sqlite3

con = sqlite3.connect('/Users/gaegul/PycharmProjects/pythonProject/test.db')

cur=con.cursor()
con.close()

