from sympy import *
h=Symbol('h')
v=Symbol('v')
b=Symbol('b')
n=Symbol('n')
print( solve([2*v+b+n-60,2*h+n+b-32,2*v+n+h-66,2*h+v+b-40],[h,v,b,n]))
