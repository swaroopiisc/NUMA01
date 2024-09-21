# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from numpy import *
import sys
import numpy as np

print(0.25 + 0.2)
print("-------------------------------")
print(0.1 + 0.2)
print("-------------------------------")
x = 3
print(x)
print("-------------------------------")
y = 4.5
print(y)
print("-------------------------------")

print(y+x)
print(y-x)
print(y*x)
print(y/x)
print("-------------------------------")

def absolute_value(x):
    if x >= 0:
        print(x)
    else:
        print(-x)

absolute_value(-4.567)
print("-------------------------------")

def quadratic(a,b,c,x):
    if a*x**2 + b*x + c == 0:
       print(x)
       print("is a zero")
    else:
       print(x)
       print("is not a zero")
           

quadratic(1,0.25,-5,2.3)
print("-------------------------------")
def xpowerk(x,k):
    temp = 1
    for var in range (k):
        temp = temp * x
    print(temp)
    
def xpowerkWithWhileLoop(x,k):
    ans = 1
    while k != 0:
        ans = ans * x
        k = k - 1
    print(ans)
    
        
xpowerk(2.78,3)    
xpowerkWithWhileLoop(2.78,3)
print("-------------------------------")

for x in np.linspace(-0.89816,-0.898161,100000):
    if abs(4 * x**3 - x + 2) < 0.00000001:
        print(x)
        
      
        
        
        
        
        
        
        
        
        
        
        
    
