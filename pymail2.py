# -*- coding: utf-8 -*-
'''
 发送邮件：
        import pymail
        e = pymail.email()
        to_addr = '每日新词<07jiangbin@163.com>'
        subject = '每日新词推送'
        msg = 'hello world'
        e.send(to_addr, subject, msg)  # 默认使用07jiangbin@163.com发送，但可扩展
'''
# from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import poplib

class email(object):
    def __init__(self, from_addr=u'07jiangbin@163.com', password='********',
                 smtp_server='smtp.163.com', smtp_port=25,
                 pop_server = 'pop3.163.com'):  # 指定发件人邮箱，以及smtp服务器
        name, addr = parseaddr(from_addr)
        self.from_addr = addr
        self.from_addr_long = from_addr
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.pop_server = pop_server

    def _format_addr(self, s):  # 格式化地址
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(),
                            addr.encode('utf-8') if isinstance(addr, unicode) else addr))

    def send(self, to_addr, subject, content):  # 发送邮件给指定的邮箱地址
        if isinstance(to_addr, str):
            to_addr = [to_addr]
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = self._format_addr(self.from_addr_long)
        msg['To'] = self._format_addr(to_addr)
        msg['Subject'] = Header('%s' % subject, 'utf-8').encode()

        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.set_debuglevel(1)
        server.login(self.from_addr, self.password)
        server.sendmail(self.from_addr, to_addr, msg.as_string())
        server.quit()
        return None

    def readmail(self):
        server = poplib.POP3(self.pop_server)
        server =

