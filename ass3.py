# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 20:26:55 2024

@author: swaro
"""

from numpy import *
import sys
import numpy as np

print('****************Task 1*******************')

L = [0,1,2,1,0,-1,-2,-1,0]

L[0]                      #0
L[-1]                     #0
L[:-1]                    #0,1,2,1,0,-1,-2,-1
L + L[1:-1] + L           #01210-1-2-101210-1-2-1001210-1-2-10
L[2:2] = [-3]             # probably assign -3 for the 3rd element in the list or syntax error
L[3:4] = []               #empty the 4th and 5th element in the List
                          # correct answe : does nothing
L[2:5] = [-5]             #syntax error
                          #changes only the third or index 2 in the list

print('****************Task 2*******************')

def f(x):
    return sin(x)

x = 3.
print(f(x))

print(f)

y = 2*pi
print(f(y))
    
print('****************Task 3*******************')
def f(m):
    L = [n-m/2 for n in range(m)]
    return 1 + L[0] + L[-1]

def f1(m):
    L1 = [n-m//2 for n in range(m)]
    return 1 + L1[0] + L1[-1]

for i in range(1,10):
    print(f'f value',f(i))
for i in range(1,10):
    print(f'f value with integer division',f1(i))
    
print('****************Task 4*******************')

print('***using for loops***')

listOfDistances = [0,20,30,40]
distance = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range(4):
    for j in range(4):
        if (i == j):
            distance[i][j] = 0
        else:
            distance[i][j] = listOfDistances[i] + listOfDistances[j]
print(distance)

reddistance = [[[],[],[]],[[],[],[]],[[],[],[]]]
        
for i in range(3):
    for j  in range(3):
        if (i>j):
            reddistance[i][j] = listOfDistances[i+1] + listOfDistances[j]
        elif (i == j):
            reddistance[i][j] = listOfDistances[i+1] + listOfDistances[j]
        else:
            reddistance[i][j] = []
    
print(reddistance)  

print('***using list comprehension***')
distance = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

distance[0][:] = [0 if i==0 else listOfDistances[i] for i in range(4)]
distance[1][:] = [0 if i==1 else listOfDistances[i] + listOfDistances[1] \
                  for i in range(4)]
distance[2][:] = [0 if i==2 else listOfDistances[i] + listOfDistances[2] \
for i in range(4)]
distance[3][:] = [0 if i==3 else listOfDistances[i] + listOfDistances[3] \
                  for i in range(4)]

print(distance)

reddistance = [[[],[],[]],[[],[],[]],[[],[],[]]]

reddistance[0][:] = [[] if i > 0 else listOfDistances[i] + listOfDistances[1] \
                     for i in range(3)]
reddistance[1][:] = [[] if i > 1 else listOfDistances[i] + listOfDistances[2] \
                     for i in range(3)]
reddistance[2][:] = [[] if i > 2 else listOfDistances[i] + listOfDistances[3] \
                     for i in range(3)]

print(reddistance) 


print('****************Task 5*******************')

A = [1,2,3,4,5,6,7,8,9]
A1 = {1,2,3,4,5,6,7,8,9}
B = [1,2,3,5,7,11,13,17,19]
B1 = {1,2,3,5,7,11,13,17,19}

def symmDiff(xList, yList):
    XminusY = []
    YminusX = []
    XsymDiffY = []
    for x in range(len(xList)):
        for y in range(len(yList)):
            if (xList[x] == yList[y]):
                break
        else:
            XminusY = XminusY + [xList[x]]

    for y1 in range(len(yList)):
        for x1 in range(len(xList)):
            if (yList[y1] == xList[x1]):
                break
        else:
            YminusX = YminusX + [yList[y1]]
    XsymDiffY = XminusY + YminusX
    return XsymDiffY

print(symmDiff(A,B))
print(A1.symmetric_difference(B1))

print('****************Task 6*******************')

# update can be said as A U B, and intersection update is like A n B
# both of them dont create a new set but operate on existing set, 
# So a set object is where this method works on,
# but the input to the method can be a list - need to verify this

print('****************Task 7*******************')

A11 = set()
B11 = {1,2,3}

print(A11.intersection_update(B11))
A11.update(B11)
print(A11)

A11 = set()
B11 = {1,2,3}

print(B11.intersection_update(A11))

print(len(A11))


print('****************Task 8&9*******************')

def f1(x):
    return arctan(x)
    
def f2(x):
    return 3 * (x**2) - 5

def bisec(f, interval, tol):
    midpt = 0
    newInt = interval
    
    while (newInt[1] - newInt[0] > tol):
        a = newInt[0]
        b = newInt[1]
        firstInt = [a,(a+b)/2]
        secondInt = [(a+b)/2,b]
        fa1 = f(firstInt[0])
        fb1 = f(firstInt[1])
        fa2 = f(secondInt[0])
        fb2 = f(secondInt[1])
        if fa1*fb1 < 0:
            newInt[0] = firstInt[0]
            newInt[1] = firstInt[1]
        elif fa2*fb2 < 0:
            newInt[0] = secondInt[0]
            newInt[1] = secondInt[1]
    midpt = (newInt[0] + newInt[1])/2
    
    return newInt,midpt

ans1 = [0,0]
midptnew = 0.0
ans1, midptnew = bisec(f1,[-0.5,0.6], 1e-6)
print(ans1)
print(midptnew)
            
# ans2 = [0,0]
# midptnew2 = 0.0
# ans2, midptnew2 = bisec(f1,[-1.5,-0.4], 1e-3)
# print(ans2)
# print(midptnew2)

# ans3 = [0,0]
# midptnew3 = 0.0
# ans3, midptnew3 = bisec(f2,[-0.5,0.6], 1e-3)
# print(ans3)
# print(midptnew3)

ans4 = [0,0]
midptnew4 = 0.0
ans4, midptnew4 = bisec(f2,[-1.5,-0.4], 1e-6)
print(ans4)
print(midptnew4)   
    



