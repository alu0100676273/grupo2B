#!/usr/local/bin/python

import sys, os
from math import *
import time

def f(x) :
  simple=exp(-x**2/2)/sqrt(2*pi)
  return simple
  
def trapecio_simple(f,A,B) :
  a=f(A)
  b=f(B)
  simple=(B-A)*((a+b)/2)
  return simple
  
def trapecio_compuesto(f,A,B,n) :
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

def Tiempo_simple() :
  e0 = time.time() 
  c0 = time.clock() 
  r=trapecio_simple(f,A,B)
  elapsed_time = time.time() - e0
  cpu_time = time.clock() - c0
  tiempoa=cpu_time
  return tiempoa
  
def Tiempo_compuesto() :
  e0 = time.time() 
  c0 = time.clock() 
  r=trapecio_compuesto(f,A,B,n)
  elapsed_time = time.time() - e0
  cpu_time = time.clock() - c0
  tiempob=cpu_time
  return tiempob

if __name__=='__main__':
  
  if len(sys.argv) == 5 :
     modulo=(sys.argv[0])
     A=int(sys.argv[1])
     B=int(sys.argv[2])
     n=int(sys.argv[3]) #numero de divisiones
     C=int(sys.argv[4]) #numero de test
     a=Tiempo_simple()
     b=Tiempo_compuesto()
     if a < b :
       print 'La ejecucion de la Regla del trapecio simple es menor que la ejecucion de la regla del Trapecio compuesto'
       porcentaje=(a/b)*100
       print porcentaje
     elif a == b :
       print 'Tiempos iguales' 
     else :
       print 'La ejecucion de la Regla del trapecio simple es menor que la ejecucion de la regla del Trapecio compuesto'
       porcentaje=(b/a)*100
       print porcentaje
	 
  else :
     print 'Has introducido unos argumentos incorrectos, introduce:'
     print modulo.py, A, B, n, C 
        