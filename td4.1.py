#!/usr/bin/env python
# -*- encoding: utf8 -*-

# Exercice 1

"""
Client pour serveur d'injures du capitaine Haddock, en xmlrpc (imite un exemple classique de SOAP)
"""


from xmlrpclib import ServerProxy



server=ServerProxy("http://monge.univ-mlv.fr:8888")


if "__name__==__main__":
    print __doc__
    print "Methodes du serveur:\n"
    for m in  server.system.listMethods(): print m
    print
    print "Un appel de server.jure() donne: ", server.jure()
    print "C'est en base 64, il faut decoder: "
    print "\n\t"+server.jure().decode('base64').rstrip()+"!"
    open('insultes.txt','w').write(server.tous_les_jurons().decode('base64'))
    print "Liste récupérée!"
    
# Un peu de curiosité permet de récupérer le code du serveur
    print "\n\t"+server.__().decode('base64')