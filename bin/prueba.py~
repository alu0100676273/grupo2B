#! /usr/bin/python
import random,sys
from math import *
def f(x) :
  return 1/sqrt(2*pi)*exp(-(x**2)/2)

def trap_simple(expr,A,B) :
  trape=(B-A)*(f(A)+f(B))/2
  return trape
  
def trap_compuesta(expr,A,B,n) :
  h=(B-A)/n
  k=1
  valor=0
  while k <= n - 1 :
    c=A+k*(B-A)/n
    valor=f(c)
    valor+=valor
    k+=1
  trap_c=((B-A)/n)*( (f(A) + f(B))/2 + valor)
  return trap_c
   
if __name__=='__main__':
  
  if len(sys.argv) < 3 :
    print 'Has introducido menos argumentos de los necesarios'
    
  elif len(sys.argv) == 3 :
    A=-1
    B=1
    expr=sys.argv[1]
    n=int(sys.argv[2])
    print 'El resultado de la regla del trapecio simple es', trap_simple(expr,A,B)
    print 'El resultado de la regla del trapecio compuesta es', trap_compuesta(expr,A,B,n)
    
    