#! usr/bin/python
import random,sys
from math import *
def f(x) :
  funcion=(1/sqrt(2*pi))*exp(-(x**2)/2)
  return funcion

def trapecio_simple(f,A,B) :
  simple=(B-A)*((f(A)+f(B))/2)
  return simple
  
def trapecio_compuesto(f,A,B,n) :
  h=(B-A)/n
  k=1
  valor=0
  while k <= n-1 :
    c=A+k*(B-A)/n
    valor=f(c)
    valor+=valor
  compuesta=((B-A)/n)*((f(A) + f(B))/2 + valor)
  return compuesta
   
if __name__=='__main__':
  
  if len(sys.argv) < 4 :
    print 'Has introducido menos argumentos de los necesarios'
    
  elif len(sys.argv) == 4 :
    A=int(sys.argv[1])
    B=int(sys.argv[2])
    n=int(sys.argv[3])
    print 'El resultado de la regla del trapecio simple es', trapecio_simple(f,A,B)
    print f(A)
    print f(B)
    print sqrt(2*pi)
    print exp((1**2)/2)
    print 'El resultado de la regla del trapecio compuesta es', trapecio_compuesto(f,A,B,n)
    