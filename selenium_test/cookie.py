# coding=utf-8
import urllib2
import cookielib

cookie = cookielib.CookieJar()

handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(handler)

response = opener.open('https://dev-bang.xinfushe.com')
for item in cookie:
    print 'Name = ' + item.name
    print 'Value = ' + item.value
