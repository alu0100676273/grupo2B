#! /usr/bin/python
import random,sys
from math import *
def f(x) :
  return (1/sqrt(2*pi))*exp(-(x**2)/2)

def trap_simple(f,A,B) :
  simple=(B-A)*(f(A)+f(B))/2
  return simple
  
def trap_compuesta(f,A,B,n) :
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
  
  if len(sys.argv) < 2 :
    print 'Has introducido menos argumentos de los necesarios'
    
  elif len(sys.argv) == 2 :
    A=-1
    B=1
    n=int(sys.argv[1])
    print 'El resultado de la regla del trapecio simple es', trap_simple(f,A,B)
    print 'El resultado de la regla del trapecio compuesta es', trap_compuesta(f,A,B,n)
    
    