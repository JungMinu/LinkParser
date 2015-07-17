# implemented by jmwsoft@gmail.com
from bs4 import BeautifulSoup
import urllib2

resp = urllib2.urlopen("")
soup = BeautifulSoup(resp, from_encoding="")
fo = open("result.txt", "w")
result = ""
for link in soup.find_all('a', href=True):
    result += link['href']+':'+link.text+"\n"
fo.write(result.encode('utf8') + '\n')
