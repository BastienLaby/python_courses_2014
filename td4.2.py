# -*- coding: iso-8859-15 -*-
#!/usr/bin/env python

# Exercice 2

import xmlrpclib
import pprint
client = xmlrpclib.ServerProxy('http://pypi.python.org/pypi')
print client.package_releases('roundup')
pprint.pprint(client.release_urls('roundup', '1.4.10'))

print client.system.listMethods()

s='Framework :: Flask'

ll = client.browse([s])

for x in ll:
        print x[0], ': ',client.release_data(*x)['summary']


print client.release_data(*['flask_simplerest', '1.0.3'])['description']