# -*- coding: iso-8859-15 -*-
#!/usr/bin/env python

# Exercice 3
# Version avec Flask

from flask import Flask
app = Flask(__name__)


jurons=open('jurons.txt','r').readlines()
from random import randint




@app.route('/haddock')
def jure():
        return jurons[randint(0,len(jurons))].decode('latin1')


@app.route('/jurons/<int:n>')
def fulmine(n):
    html = '''<html><body>
                   <h1 align="center">Les %d jurons demand&eacute;s :</h1>
                   <br>
                <br> %s </body/</html>
'''
    s = '\n'.join(['<br>'+jurons[randint(0,len(jurons))].decode('latin1') for i in
        range(n)])
    return html % (n,s)


@app.route('/')
def help():
    return '''<html><body>Commandes :\n<p> /haddock (renvoie une injure)\n
              <p>/jurons/n (renvoie n injures)\n</body></html>'''


if __name__ == '__main__':
    app.run()
