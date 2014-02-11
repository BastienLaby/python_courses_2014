# -*- coding: iso-8859-15 -*-
#!/usr/bin/env python

# Exercice 1
# Côté serveur

"""
Serveur d'injures du capitaine Haddock. Utilise le
protocole xmlrpc. Le données sont encodées en
base 64 à cause des caracteres accentués.
"""


from SimpleXMLRPCServer import SimpleXMLRPCServer as Server
from random import randint        

jurons=open('jurons.txt','r').readlines()

def jure():
        return jurons[randint(0,len(jurons))].encode('base64')

def help(): return  "ENCODAGE=BASE64"

def __():
    s=open('haddockServer.py','r').read()
    return s.encode('base64')

def tous_les_jurons():
    s=open('jurons.txt','r').read()
    return s.encode('base64')

server = Server(('193.55.63.80', 8888))

server.register_function(tous_les_jurons)
server.register_function(jure)
server.register_function(help)
server.register_function(__)
server.register_introspection_functions()

try:
    server.serve_forever()
finally:
    server.server_close()