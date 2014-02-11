# -*- coding: iso-8859-15 -*-
#!/usr/bin/env python

# Exercice 3

# Minimalist RESTful Haddock server
# start_response est une methode de BaseHandler,
# defini dans wsgiref.handlers.py

import restlite, wsgiref.simple_server

def juron_handler(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    j = juron()
    return j.decode('latin1').encode('utf8')

def jurons_handler(env, start_response):
    try:
        nombre = int(env['wsgiorg.routing_args']['nombre'])
        start_response('200 OK', [('Content-Type', 'text/html')])
        j = jurons(nombre)
        return j.decode('latin1').encode('utf8')
    except Exception, e: print e


liste_jurons=open('jurons.txt','r').readlines()
from random import randint

def juron():
    return liste_jurons[randint(0,len(liste_jurons))]

def jurons(n):
    html = '''<html><body>
        <meta http-equiv="content-type" content="text/html; charset=utf-8">
        <h1 align="center">Les %d jurons demand&eacute;s :</h1>
                   <br><br> %s </body/</html>
'''
    s = '\n'.join(['<br>'+liste_jurons[randint(0,len(liste_jurons))] for i in range(n)])
    return html % (n,s)


def portrait_handler(env, start_response):
    start_response('200 OK', [('Content-Type', 'image/jpeg')])
    return open('haddock.jpg').read()



routes = [
 (r'GET /juron$', juron_handler),
 (r'GET /jurons\?nombre=(?P<nombre>\d*)', jurons_handler),
 (r'GET /portrait$',  portrait_handler)
]


httpd = wsgiref.simple_server.make_server('193.55.63.80', 8889, restlite.router(routes))
httpd.serve_forever()