#! /usr/bin/python

import sys
import os


# -*- encoding: utf8 -*-
# IMAC3 -- Python 2013-2014
# TD3

# Exercice 1 - a (1)
def listFiles(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            print os.path.join(dirpath,filename)
    
    return ""


# Exercice 1 - a (2)
def countFilesAndFolders(path):

    files = 0; dirs = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            files += 1
        for dirname in dirnames:
            dirs += 1
    return {'files' : files, 'dirs' : dirs}


# Main :
if __name__ == '__main__':
    args = []
    longestWord = 25
    exercices = [{"number":1, "name":"Listage des fichiers present dans Home", "function":"listFiles", "parameters":{'path':os.environ['HOME']}, "keywords":['path']},
        {"number":2, "name":"Affiche le nombre de fichiers et de dossiers", "function":"countFilesAndFolders", "parameters":{'path':os.environ['HOME']}, "keywords":['path']}]
    if len(sys.argv) < 2:
        print "Veuillez entrer le numero de l'exercice voulu"
        sys.exit(1)
    elif sys.argv[1] in ['-a', '--arg']:
        for i in range(2, len(sys.argv) - 1):
            print "argument %d : %s\n" % (i, sys.argv[i])
            args.append(sys.argv[i])
    if sys.argv[len(sys.argv)-1].isdigit():
        number = int(sys.argv[len(sys.argv)-1])
    else:
        print "Le numero de l'exercice doit etre un nombre entier compris entre 1 et %s" % len(exercices)
        sys.exit(1)
    
    for i in range(len(args)):
        exercices[number-1]["parameters"].update({exercices[number-1]["keywords"][i]: args[i]})

    result = locals()[exercices[int(number)-1]["function"]](**exercices[int(number)-1]["parameters"])
    
    print "Le resultat de l'exercice %d avec pour argument %s est : %s\n" % ( number, args, result )