#!/usr/local/bin/python

import sys, os, random
from math import *
import timeit


def f(x) :
  simple=exp(-x**2/2)/sqrt(2*pi)
  return simple
  
def trapecio_simple(f) :
  simple=(B-A)*((f(A)+f(B))/2)
  return simple
  
def trapecio_compuesto(f,n) :
  h=(B-A)/n
  k=1
  valor=0
  while k <= n - 1 :
    c=A+k*(B-A)/n
    valor=f(c)
    valor+=valor
    k+=1
  compuesta=((B-A)/n)*( (f(A) + f(B))/2 + valor)
  return compuesta


def Tiempo1(trapecio_simple,C):
   t= timeit.Timer()
   x=t.timeit(10000000)
   tiempo1=x
   return tiempo1
def Tiempo2(trapecio_compuesto,C):
   t= timeit.Timer()
   x=t.timeit(10000000)
   tiempo2=x
   return tiempo2

if __name__=='__main__':
  
  if len(sys.argv) == 6 :
     modulo=(sys.argv[0])
     A=int(sys.argv[1])
     B=int(sys.argv[2])
     n=int(sys.argv[3]) #numero de divisiones
     C=int(sys.argv[4]) #numero de test
     nombre=(sys.argv[5])
     fichero=open(nombre,'w')
     a=Tiempo1(trapecio_simple,C)
     b=Tiempo2(trapecio_compuesto,C)
     
     for i in range(C):
       if a < b :
	 fichero.write('La ejecucion de la Regla del trapecio simple es menor que la ejecucion de la regla del Trapecio compuesto')
	 porcentaje=(a/b)*100
	 fichero.write('{0}\n'.format(Tiempo1(trapecio_simple,C)))
	 fichero.write('{0}\n'.format(porcentaje))
       elif a == b :
          fichero.write('Tiempos iguales')
       else :
	 fichero.write('La ejecucion de la Regla del trapecio compuesto es menor que la ejecucion de la regla del Trapecio simple')
         porcentaje=(b/a)*100
         fichero.write('{0}\n'.format(Tiempo2(trapecio_compuesto,C)))
         fichero.write('{0}\n'.format(porcentaje))
         
     fichero.close()    
        
  else :
     print 'Has introducido unos argumentos incorrectos, introduce:'
     print modulo.py, A, B, n, C, resultados.txt