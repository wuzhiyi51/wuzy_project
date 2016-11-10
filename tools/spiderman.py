# -*- coding: utf-8 -*-
import os
import re
import shutil

REJECT_FILETYPE = 'rar, 7z, css, js, jpg, jpeg, gif, bmp, png, swf, exe'


def getinfo(webaddress):
    global REJECT_FILETYPE

    url = 'https://' + webaddress + '/'
    print 'Getting>>>>>' + url
    websitefilepath = os.path.abspath('.') + '/' + webaddress

    if os.path.exists(websitefilepath):
        shutil.rmtree(websitefilepath)
    outputfilepath = os.path.abspath('.') + '/' + 'output.txt'
    fobj = open(outputfilepath, 'w+')
    command = 'wget -r -m -nv --reject=' + 'REJECT_FILETYPE' + ' -o ' + outputfilepath + ' ' + url
    tmp0 = os.popen(command).readlines()
    print >> fobj, tmp0
    allinfo = fobj.read()
    target_url = re.compile(r'\".*?\"', re.DOTALL).findall(allinfo)
    target_num = len(target_url)
    fobj1 = open('result.txt', 'w')
    for i in range(target_num):
        print >> fobj1, target_url[i][1:-1]
    fobj.close()
    fobj1.close()
    if os.path.exists(outputfilepath):
        os.remove(outputfilepath)


if __name__ == "__main__":
    webaddress = raw_input("Input the Website Address(without \"http:\")>")
    getinfo(webaddress)
    print "Well Done."
