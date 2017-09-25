import urllib,urllib2
import re,os,sys
from bs4 import BeautifulSoup

#url http://www.greenteapress.com/thinkpython/code/
def getContent(url):
    temp = urllib2.urlopen(url)
    content = temp.read()
    return content

def getFile(url):
    keys = []

    html = getContent(url)
    soup = BeautifulSoup(html,"lxml")
    for link in soup.findAll('a',href=True):
        if re.findall('\.py', link['href']):
            keys.append(link['href'])

    if 'news' not in os.listdir(os.getcwd()):
        os.mkdir('news')
    for i,name in enumerate(keys):
        target = url + name
        if os.path.exists('./news/%s'%name):
            sys.stderr.write(name+" exists\n")
            continue
        try:
            urllib.urlretrieve(target,'./news/%s'%name)
            print i, ' download ', name
        except Exception, e:
            print 'download ', name, ' fault'
            i = str(int(i) - 1)
            continue
    print 'Done!'
        
url = 'http://www.greenteapress.com/thinkpython/code/'
getFile(url)
# print str(os.getcwd())
