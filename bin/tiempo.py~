
#! /usr/bin/python
import random,sys
from math import *
import timeit

def f(x) :
  return 1/sqrt(2*pi)*exp(-(x**2)/2)
  
def simple(f,A,B) :
  simple=(B-A)*(f(A)+f(B))/2
  return simple
  
def compuesta(f,A,B) :
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
  
def Tiempo1(simple,C):
   t= timeit.Timer('simple', setup = 'from math import *; A=-1.0; B=1.0')
   x=t.timeit(10000000)
   return x
   
def Tiempo2(compuesta,C):
   t2= timeit.Timer('compuesta', setup = 'from math import *; A=-1.0; B=1.0m')
   x2=t2.timeit(10000000)
   return x2

if __name__=='__main__': 

  
    if len(sys.argv) == 3 :
        modulo=(sys.argv[0])
        n=int(sys.argv[1]) #numero de divisiones
        C=int(sys.argv[2]) #numero de test
        val=Tiempo1(simple,C)
        val2=Tiempo2(compuesta,C)
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
        print tiempo.py , num_test 
        
	 
	 