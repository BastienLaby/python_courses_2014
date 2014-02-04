# TD3
import os
#########
### ex. 1
for root, dir_, files in os.walk('.'):
    for file_ in files:
        print root+os.sep+file_
##########
#### ex. 2
f=d=0
for root, dir_, files in os.walk('.'):
    f+=len(files); d+=len(dir_)
print "%d files, %d directories" % (f,d)

# ne compte pas "."

#########
### ex. 3
# utiliser os.path.islink(path)

f=s=d=0
for root, dirs, files in os.walk('.'):
    for dir_ in dirs:
        if os.path.islink(root+os.sep+dir_): s+=1
        else: d+=1
    for file_ in files:
        if os.path.islink(root+os.sep+file_): s+=1
        else: f+=1

print "%d directories, %d files, %d symlinks" % (d,f,s)



#########
### ex. 4

# Un lien vers un fichier non existant peut generer une erreur
# On gere avec try/except

fpriv=fpub=spriv=spub=dpriv=dpub=0
for root, dirs, files in os.walk(os.environ['HOME']):
    for dir_ in dirs:
        try:
            pub = os.stat(root+os.sep+dir_) % 64
            if os.path.islink(root+os.sep+dir_):
                if pub: spub+=1
                else: spriv+=1
            else:
                if pub: dpub+=1
                else: dpriv+=1
        except Exception, e :
            print roor+os.sep+dir+' --> broken link!'
            print e
    for file_ in files:
        try:
            pub  = os.stat(root+os.sep+file_) % 64
            if os.path.islink(root+os.sep+file_):
                if pub: spub+=1
                else: spriv+=1
            else:
                if pub: fpub+=1
                else: fpriv+=1
        except Exception, e:
            print root+os.sep+file_ + ' --> broken link'
            print e
print
print "Statistics of %s:" % (os.environ['HOME'])
print
print "Public directories: %d" % (dpub,)
print "Private directories: %d" % (dpriv,)
print "Public files: %d" % (fpub,)
print "Private files: %d" % (fpriv,)
print "Public symlinks: %d" % (spub,)
print "Private symlinks: %d" % (spriv,)

