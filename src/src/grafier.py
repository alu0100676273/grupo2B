#!/usr/bin/python

import random, sys
from math import *
import matplotlib.pyplot as pl

def error(c):
  yu=9+c
  er=(2/(3*sqrt(2*pi)))*exp(u**2/-2)*(1-u**2)
  return er

if __name__=='__main__':
  if (len(sys.argv))==2:
    ff=sys.argv[0]
    c=int(sys.argv[1])
    x=[-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    fichero=open('datos.txt','w')
    for u in x:
      fichero.write('{0}\n'.format(error(c)))
    fichero.close()
    
    ficher=open('datos.txt','r')
    v1=float(ficher.readline())
    v2=float(ficher.readline())
    v3=float(ficher.readline())
    v4=float(ficher.readline())
    v5=float(ficher.readline())
    v6=float(ficher.readline())
    v7=float(ficher.readline())
    v8=float(ficher.readline())
    v9=float(ficher.readline())
    v10=float(ficher.readline())
    v11=float(ficher.readline())
    v12=float(ficher.readline())
    v13=float(ficher.readline())
    v14=float(ficher.readline())
    v15=float(ficher.readline())
    v16=float(ficher.readline())
    v17=float(ficher.readline())
    v18=float(ficher.readline())
    v19=float(ficher.readline())
    v20=float(ficher.readline())
    v21=float(ficher.readline())
    ficher.close()
    y=[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21]
    
    pl.xlabel('Valores de Epsilon')
    pl.ylabel('Errores correspondientes')
    pl.plot(range(len(x)),y,'rd')
    pl.xlim(1.1,-1.1)
    pl.xticks(range(len(x)), x)
    pl.savefig('imgraf.eps')
    pl.show()
    
    
    
  else:
    print "La forma de uso es fichero.py,c"