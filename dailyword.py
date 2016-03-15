# -*- coding: utf-8 -*-
# 发送邮件

import pymail
import MySQLdb
import time

##
today = time.strftime('%Y-%m-%d')
conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='fund', charset='UTF8')
curs = conn.cursor()
curs.execute('select * FROM eng_sentence900 order by rand() limit 10')
sentence_10 = curs.fetchall()

sentence_10_date = []
msg = u''
for i in sentence_10:
    msg += u'[%d] %s' % i
    sentence_10_date.append((i[0], i[1], today))
curs.executemany('insert into eng_sentence900_sent(id, sentence, recorddate) values(%s,%s,%s)',
                 sentence_10_date)
conn.commit()
curs.close()
conn.close()


e = pymail.email(u'每日句子<07jiangbin@163.com>')
to_addr = u'每日句子 <07jiangbin@163.com>'
subject = u'每日句子推送'
e.send(to_addr, subject, msg)  # 默认使用07jiangbin@163.com发送





