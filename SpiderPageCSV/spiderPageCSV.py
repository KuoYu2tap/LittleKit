# -*- coding: utf-8 -*-
#code at 2016年9月21日-22日

import urllib2
import re
import time

#获取html内容
def getHtml(url):
    page = urllib2.urlopen(url).read()
    html = page.decode('gbk') #decode解码为unicode
    return html

#批量提取<td></td>内内容
def getTd(html):
    key = []
    regFir = re.findall('<tbody>(.*)',html)
    for i in range(len(regFir)):
            regKey = re.findall('<td>(.{0,30}?)</td>',regFir[i])
            #print regKey
            for flag in range(len(regKey)):
                if regKey[flag]==u'':
                    regKey[flag] = u'  '
                if len(regKey[2])==2):
                    regKey[2] = (regKey[2]+'    ')
                if len(regKey[2]=3):
                    regKey[2]=(regKey[2]+'  ')
            key.append(regKey)
    return key

#数据写入
def openFile(*argv):
    fp = open("dataJC_.txt","a+")
    for x in range(len(argv)):
        for y in range(len(argv[0])):
            for z in range(argv[0][0]):
                #fp.write(str(argv[i][j]).encode('utf-8'))
                if z==argv[0][0]:
                    fp.write(argv[x][y][z].encode('utf-8')+'|\n')   #encode编码,Unicode-->utf-8
                else:
                             fp.write(argv[x][y][z].encode('utf-8')+'|')
    fp.close()

### 正则匹配最后一个页面,仅针对sh-ma,返回最后一页int
##def reBack(html):
##    regPage = re.match('">(.*?)</a>',html)
##    return int(regPage[-1])

#正式爬虫
query = raw_input("请输入要查询的内容:")
##html = getHtml("http://XXXXXX.com/data/query/5?&q="+query+"&p=1")
for page in range(1,216):
    url = "http://XXXXXX.com/data/query/4?&q="+query+"&p=%s"% page
    html = getHtml(url)
    key = getTd(html)
    openFile(key)
    print "已加载第%d页的数据"%page
print "done"
    
