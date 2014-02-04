#!/usr/bin/python
'''
duplicates: lists identical files in a directory.

Usage: duplicates [-e] [--extension] [file extension],
                  [-d] [--directory] [directory]
                  [-o] [--outfile]   [output file]
                  |-h] [--help]
'''

import os, hashlib, sys, getopt


def find_duplicates(extension, directory):
    d = {}
    for root, dirs, files in os.walk(directory):
        for f in files:
            if not extension or os.path.splitext(f)[1][1:] == extension:
                p = os.path.join(root,f)
                if os.path.islink(p): continue
                try:
                    s = open(p,'r').read()
                    md5 = hashlib.md5(s).hexdigest()
                    if d.has_key(md5): d[md5].append(p)
                    else: d[md5] = [p]
                except: pass
    return d




def usage():
    'Print usage doc and exit.'
    print __doc__
    sys.exit()



if __name__ == '__main__':
    extension = None
    directory = os.environ['PWD']
    outfile = sys.stdout
    out = False

    try:
        optlist, arglist = getopt.getopt(sys.argv[1:],
                                         'he:d:o:',
                                         ['help', 'extension=',
                                          'directory=', 'outfile=' ])
    except:
        usage()
    for option in optlist:
        if option[0] in ['-h', '--help']: usage()
        if option[0] in ['-e', '--extension']: extension = option[1]
        if option[0] in ['-d', '--directory']: directory = option[1]
        if option[0] in ['-o', '--outfile']:
            outfile = open(option[1],'w')
            out = True
    d = find_duplicates(extension, directory)
    for x in d:
        if len(d[x])>1:
            for y in d[x]:
                outfile.write(y+'\n')
            outfile.write('\n')
    if out: outfile.close()

