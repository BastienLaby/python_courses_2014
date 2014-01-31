# -*- encoding: utf8 -*-
# -*- coding: iso-8859-15 -*-
#!/usr/bin/env python

# IMAC3 -- Python 2013-2014
# Corrigé du TD 2

# EXERCICE 1

# On peut avoir un pas négatif
def is_palindrome(w):
    return w == w[::-1]

# Un ensemble (set) c'est un dictionnaire dont les clés n'ont pas de valeur
# Pour python  2.7
def is_pangram(w):
    return len({x.lower() for x in w if x.isalpha()}) == 26
# Pour python  2.6
    return len(set([x.lower() for x in w if x.isalpha()])) == 26

# Noter l'astuce avec 'and' pour traiter la liste vide
def remove_adjacent(ll):
    return  ll and  [ll[i] for i in range(len(ll)-1) if ll[i+1]!=ll[i] ]+[ll[-1]]

# Remarquer les fonctions de conversion
def digits_sum(n):
    return sum([int(c) for c in str(n)])








# EXERCICE 2

import re, string

aa ='àâéèêëîïôùûü'.decode('utf8').encode('latin1')
bb ='aaeeeeiiouuu'.decode('utf8').encode('latin1')
t1 = string.maketrans(aa,bb)

ll= [string.translate(w,t1).decode('latin-1').encode('utf8')
        for w in
        open('liste.de.mots.francais.frgut.txt').readlines()]

pat=r'[ioeshbdlzg]+\n'
mm=[x for x in ll if re.match(pat,x)]
print "nombre de mots : ", len(mm)

t2 = string.maketrans('IOESHBDLZG', '1035480729')

for x in mm:
    print x[:-1].upper(), string.translate(x[:-1].upper(),t2)







# EXERCICE 3

'''
Mélange aléatoirement les lettres internes des mots d'un fichier
ou de l'entrée standard

Usage: blurr [<fichier> <encodage>]
'''
from random import shuffle


letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '\xa6', '\xa8', '\xaa', '\xb4', '\xb5', '\xb8', '\xba', '\xbc',
    '\xbd', '\xbe', '\xc0', '\xc1', '\xc2', '\xc3', '\xc4', '\xc5',
    '\xc6', '\xc7', '\xc8', '\xc9', '\xca', '\xcb', '\xcc', '\xcd',
    '\xce', '\xcf', '\xd0', '\xd1', '\xd2', '\xd3', '\xd4', '\xd5',
    '\xd6', '\xd8', '\xd9', '\xda', '\xdb', '\xdc', '\xdd', '\xde',
    '\xdf', '\xe0', '\xe1', '\xe2', '\xe3', '\xe4', '\xe5', '\xe6',
    '\xe7', '\xe8', '\xe9', '\xea', '\xeb', '\xec', '\xed', '\xee',
    '\xef', '\xf0', '\xf1', '\xf2', '\xf3', '\xf4', '\xf5', '\xf6',
    '\xf8', '\xf9', '\xfa', '\xfb', '\xfc', '\xfd', '\xfe', '\xff']



def blurr(s):
    ll = []; i=0
    while i in range(len(s)):
        mm=[]
        while i < len(s) and s[i] in letters:
            mm.append(s[i])
            i+=1
        if mm:
            if len(mm)>3:
                uu=mm[1:-1]; shuffle(uu)  # s'applique à une liste
                ll+=[mm[0]]+uu+[mm[-1]]   # et la modifie
            else:
                ll+=mm
            continue
        else:
            while i < len(s) and s[i] not in letters:
                ll.append(s[i])
                i+=1
    return ''.join(ll)


if __name__=="__main__":
# arguments: <fichier> <encodage>
    import sys

    if len(sys.argv)>2:
    s = open(sys.argv[1],'r').read()
    e = sys.argv[2]
    t = unicode(blurr(s), e)
        print t
# ou alors l'entrée standard
    else:
        s = raw_input('texte: ')
        print '--->  ', blurr(s)



#Le cours 2 suggère une solution plus efficace utilisant des expressions régulières.
#!/usr/bin/env python

import random, re, sys

p = re.compile('(\w)(\w+)(\w)', re.M|re.L|re.U)

def touille(m):
    milieu = list(m.group(2))
    random.shuffle(milieu)
    return m.group(1) + ''.join(milieu) + m.group(3)

if len(sys.argv)==4:
    s = open(sys.argv[1]).read().decode(sys.argv[2])
    t = p.sub(touille, s).encode(sys.argv[3])
    sys.stdout.write(t)
else:
    print "Usage: touille <fichier> <encodage> <encodage>"


#Pour construire la liste "letters" sans se fatiguer :


# A exécuter ligne à ligne dans l'intérpréteur
# On construit une liste de tous les caractères encodables en latin1
s=''.join([chr(i).decode('latin1') for i in range(256)])
# On l'imprime
print s
# On efface ce qui n'est pas une lettre
# C'est vite fait car ça marche par tranches
t='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ'
# et voilà la liste cherchée
letters = [x.encode('latin1') for x in t.decode('utf8')]

print letters