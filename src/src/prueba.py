#! /usr/bin/python
import random,sys
from math import *
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
   
if __name__=='__main__':
  
  if len(sys.argv) < 4 :
    print 'Has introducido menos argumentos de los necesarios'
    
  elif len(sys.argv) == 4 :
    A=int(sys.argv[1])
    B=int(sys.argv[2])
    n=int(sys.argv[3])
    print 'El resultado de la regla del trapecio simple es', trapecio_simple(f,A,B)
    print 'El resultado de la regla del trapecio compuesta es', trapecio_compuesto(f,A,B,n)
    
    