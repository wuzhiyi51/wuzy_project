# coding=utf-8
import urllib2
import urllib
import cookielib

filename = 'cookie1.txt'

cookie = cookielib.MozillaCookieJar(filename)

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

postdata = urllib.urlencode({
    'input1': 'wuzhiyi51',
    'input2': '649911812'
})
loginUrl = 'https://passport.cnblogs.com/user/signin'

result = opener.open(loginUrl, postdata)

cookie.save(ignore_discard=True, ignore_expires=True)

gradUrl = 'https://home.cnblogs.com/set/account/'
result = opener.open(gradUrl)

print result.read()
