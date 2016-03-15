
import MySQLdb
S = []
for line in open('sentence900.txt', 'r'):
    x = line.split('.', 1)
    if len(x) == 2:
        S.append((int(x[0]), x[1]))

conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='fund', charset='UTF8')
curs = conn.cursor()
curs.executemany('insert into eng_sentence900(id,sentence) values(%s,%s)', S)
conn.commit()
curs.close()
conn.close()
conn.close()