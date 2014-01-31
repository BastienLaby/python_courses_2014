# -*- encoding: utf8 -*-
# IMAC3 -- Python 2013-2014
# Corrigé du TD 1


# Il fallait suivre à la lettre les instructions :
# Une fenêtre d'éditeur, une fenêtre d'interpréteur
# Essayer les bouts de code un par un et dans l'ordre
# et explorer à l'aide de dir(...) et help(...)


# Exercice 1:
# Les premiers exemples du TD rappellent l'existence de + et * pour les chaînes
msg = 'coin coin'
s = '* '+msg+' *'
t = '*'*len(s)+'\n'
print t+s+'\n'+t

# Exercice 2: dir("") permet de découvrir la méthode "center" ...
print '*'*79+'\n*'+msg.center(77)+'*\n'+'*'*79

# Exercice 3: ... et aussi la méthode "strip"
message="*"*13+"\n* coin coin *\n"+"*"*13
print message
print message.strip('* \n')

# Exercice 4: On s'autorise une instruction pour déterminer
# la longueur m de la plus courte ...
s1="abcdef"
s2="0123456789"
m=min(len(s1),len(s2))
# ... puis on combine "list comprehension" et tableaux (m:, :m etc)
print ''.join([s1[i]+s2[i] for i in range(m)])+s1[m:]+s2[m:]
# ou encore:
print "".join([x[0]+x[1] for x in zip(s1,s2)])+s1[m:]+s2[m:]
# Il fallait observer que s[m:] renvoie '' si s[m] n'existe pas

# Exercice 5:
# Ensuite, on peut récuperer les caractères d'indices pairs ou impairs
s='a0b1c2d3e4f56789'
print s[::2]
print s[1::2]

# Exercice 6:
daltons=[{"nom":"joe","taille":140,"caractere":"teigneux"},
         {"nom":"jack","taille":155,"caractere":"idiot"},
         {"nom":"william","taille":170,"caractere":"stupide"},
         {"nom":"averell","taille":185,"caractere":"abruti"}]
# les fonctions de comparaison doivent retourner (<0), 0 ou (>0)
def compare_taille(x,y):
    return x['taille'] - y['taille']

# la liste est triée en place
daltons.sort(compare_taille)
print daltons
# On pourrait coder celle-ci, mais en fouinant un peu, on trouve "cmp"
def compare_nom(x,y):
    return cmp(x['nom'], y['nom'])

daltons.sort(compare_nom)
print daltons

# Exercice 7:
ll=open('liste.de.mots.francais.frgut.txt','r').readlines()
print ll[:20] # pour voir à quoi ça ressemble

def dico(w):
   ll=open('liste.de.mots.francais.frgut.txt','r').readlines()
   if w+'\n' in ll: print "%s est dans le dictionnaire" % w
   else: print "%s n'est pas dans le dictionnaire" % w

dico('zythum')
# Avec les lettres accentuées, ça ne marche pas forcément
dico('déjà')
# Dans ce cas il faut connaitre les encodages du système et du dictionnaire et les décoder:
# dir("") propose une méthode "decode": help("".decode) puis voir doc en ligne
def dico2(w):
   ll=[x.decode('latin1') for x in open('liste.de.mots.francais.frgut.txt','r').readlines()]
   if w.decode('utf8')+'\n' in ll: print "%s est dans le dictionnaire" % w
   else: print "%s n'est pas dans le dictionnaire" % w

dico2('déjà')

# Un script complet
############### dic.py #################"
#! /usr/bin/python

import sys


def dico(w,d='utf8', e='latin1'):
    ll= open('liste.de.mots.francais.frgut.txt').readlines()
    if w.decode(d).encode(e)+'\n' in ll: print "%s est dans le dictionnaire" % w
    else: print "%s n'est pas dans le dictionnaire" % w



if __name__ == '__main__':
    d = sys.getfilesystemencoding()
    if len(sys.argv) < 2:
        print "dic prend au moins un argument"
        sys.exit(1)
    elif sys.argv[1] in ['-e', '--encoding']:
        e = sys.argv[2]
        for w in sys.argv[3:]: dico(w,d,e)
    else:
        for w in sys.argv[1:]: dico(w,d)