import imaplib
import myconfig
import email
import time
import logging
import re

logging.basicConfig(level='DEBUG')

user = myconfig.gmail_user2
password = myconfig.gmail_pass2

conn = imaplib.IMAP4_SSL('imap.gmail.com', 993)
conn.login(user, password)
conn.select('INBOX')

r, d = conn.search(None, 'ALL')
mail_list = d[0].split()

r, data = conn.fetch(mail_list[0], '(RFC822)')


def parseEmail(data):
    msg = email.message_from_string(data[0][1])
    t = time.strptime(msg['Date'], '%a, %d %b %Y %H:%M:%S +0000')
    msg_date = "%s-%s-%s" % (str(t.tm_year), str(t.tm_mon).zfill(2), str(t.tm_mday).zfill(2))
    msg = email.message_from_string(data[0][1])
    msg_from_name, msg_from_addr = email.utils.parseaddr(msg['From'])
    return msg_from_addr, msg_date

def parseEmail():
    pass

##


class TestEmail(object):
    def __init__(self):
        self.user = myconfig.gmail_user2
        self.password = myconfig.gmail_pass2
        conn = imaplib.IMAP4_SSL('imap.gmail.com', 993)
        conn.login(self.user, self.password)
        conn.select('INBOX')  # INBOX
        r, d = conn.search(None, 'ALL')
        self.mailList = d[0].split()
        self.conn = conn
        self.uid = ''

    def get_mail(self, uid):
        r, d = self.conn.fetch(uid, '(RFC822)')  # (BODY.PEEK[HEADER])
        msg = email.message_from_string(d[0][1])
        return msg

    def parse_mail(self, msg):
        datestr = re.findall('\d+ [A-Za-z]{3} \d+', msg['Date'])
        t = time.strptime(datestr[0], '%d %b %Y')
        msg_date = "%s-%s-%s" % (str(t.tm_year), str(t.tm_mon).zfill(2), str(t.tm_mday).zfill(2))
        msg_from_name, msg_from_addr = email.utils.parseaddr(msg['From'])
        return msg_from_addr, msg_date

    def parse_all(self):
        result =[]
        cnt = 0
        for uid in self.mailList:
            cnt += 1
            logging.info("正在处理第"+ str(cnt)+"封邮件,uid="+uid)
            self.uid = uid
            msg = self.get_mail(uid)
            addr, date = self.parse_mail(msg)
            result.append((addr, date))
        return result

T = TestEmail()
#r = T.parse_all()