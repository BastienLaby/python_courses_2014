from urllib import urlopen
from urllister import URLLister
s = urlopen('http://igm.univ-mlv.fr/~jyt').read()
p = URLLister()
p.feed(s)
p.close()
print p.urls