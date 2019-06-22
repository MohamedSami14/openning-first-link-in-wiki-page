import urllib2
import urllib
import re
import webbrowser
import datetime
url="https://en.wikipedia.org/wiki/Special:Random"
website=urllib2.urlopen(url)
html=website.read()

links=re.findall('"(http.*?)"', html)

eee=list(links)
z=eee[0]
print(eee)
s=str(z)
y=s.replace('http//','')
#a=s.encode('utf-8')
#c=re.request.urlopen(a)
m=webbrowser.open(y,new=2,autoraise=True)
print("first link is :",s)
#can't loop the project as it's my first one
#for i<5:
#links=re.findall('"(http.*?)"', l)

#i+=1
#if s="https://en.wikipedia.org/wiki/"
    #break