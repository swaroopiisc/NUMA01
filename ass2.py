# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 12:40:07 2024

@author: swaro
"""
from numpy import *
import sys
from matplotlib.pyplot import *

x=0.5 # x_0
for i in range(200):
    x=x**2 # x_i
print(f'The result after {i+1} iterations is {x}')

x = 2.3
val = x**2 + 0.25*x - 5
if val == 0:
    print(f'This value {x} is a zero for the given equation')
else:
    print(f'This value {x} is not a zero for the given equation')

L = [1,2]
L3 = 3*L
L3[0]
L3[-1]
#L3[10]

L4 = [k**2 for k in L3]
print(L4)

L5 = L3 + L4
print(L5)

# =============================================================================
# L5 = zeros((len(L3) + len(L4),), dtype=int)
# concatenate((L3,L4),0,L5)
# print(L5)
# =============================================================================

startn = 0
endn = 1
n = 99
diff = (endn - startn)/n

equalList = [startn + (y)*diff for y in range(n+1)]
equalList2 = linspace(0,1,100)

s = 0
for i in range (0 , 500 ):
    s = s + i
print(s)
print(i)


ss = [0]
for i in range (1 , 500 ):
    ss . append ( ss[i-1] + i )
#print(ss)
print(i)

xplot = [0]
for q in range(1,100):
    xplot.append(q * diff)
    
yplot = arctan(xplot)

plot(xplot, yplot, '-')
title('My first plot')
xlabel('100 equidistant values between 0 and 1')
ylabel('arctan(x)')
show()

endn = 200
temp = 0.0
for u in range(1,endn+1):
    temp += sqrt(u)
    
print(temp)
