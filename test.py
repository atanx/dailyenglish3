# coding=utf-8
import os


from HTMLParser import HTMLParser
from bs4 import BeautifulSoup as bs
import re
import urllib

from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print('data')

    def handle_comment(self, data):
        print('<!-- -->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial...<br>END</p></body></html>')

url = 'http://www.51voa.com/VOA_Special_English/facebook-reactions-68422.html'
fid = urllib.urlopen(url)
html = fid.read()

# 查找链接
sp = bs(html)
a = sp.find_all('a', href = re.compile(r'\.mp3'))
mp3 = a[0].attrs['href']
