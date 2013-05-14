#! /usr/bin/python
import random,sys
from math import *
import timeit

def f(x) :
  simple=1/sqrt(2*pi)*exp(-x**2/2)
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
  
def Tiempo1(trapecio_simple):
   t= timeit.Timer('trapecio_simple')
   x=t.timeit(10000000)
   return x
   
def Tiempo2(trapecio_compuesto):
   t2= timeit.Timer('trapecio_compuesto')
   x2=t2.timeit(10000000)
   return x2

if __name__=='__main__': 

  
    if len(sys.argv) == 5 :
        modulo=(sys.argv[0])
        A=int(sys.argv[1])
        B=int(sys.argv[2])
        n=int(sys.argv[3]) #numero de divisiones
        C=int(sys.argv[4]) #numero de test
        val=Tiempo1(trapecio_simple)
        val2=Tiempo2(trapecio_compuesto)
        i=1
        while i< C:
	  
          if val < val2:
	     print 'La Regla del Trapecio simple se evalua mas rapido que la Regla del Trapecio compuesta'
	     porcentaje= (val/val2)*100
	     print porcentaje
	  else: 
	     print  'La Regla del Trapecio compuesta se evalua mas rapido que la Regla del Trapecio Simple'
	     porcentaje= (val2/val)*100
	     print porcentaje
	 
    else :
        print 'Has introducido unos argumentos incorrectos, introduce:'
        print modulo.py, A, B, n, C 
        
        