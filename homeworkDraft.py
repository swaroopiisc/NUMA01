# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 03:33:51 2024

@author: swaro
"""

from numpy import *
import sys
import numpy as np
from matplotlib.pyplot import *

switch_backend('Qt5Agg')

"""         # Task 1                 """

def approxLnFunc(x,n):
    
    a = [0 for y in range(n+1)]
    g = [0 for y in range(n+1)]
    
    a[0] = (1+x)/2
    g[0] = sqrt(x)
    
    for i in range(0,n):
        a[i+1] = (a[i] + g[i])/2
        g[i+1] = sqrt(a[i+1] * g[i])
        
    return (x-1)/a[n]

x = 20
n = 10
ans_userDefinedFunction = approxLnFunc(x,n)
ans_pythonFunc = log(x)


"""        # Task 2                 """

xAxisSamples = 5000
xaxis = linspace(0.01, 5, xAxisSamples)

lnFromPython = log(xaxis)
nValues = [1,2,3,4,5,10,100]
lnFromApprox = [[0 for q in range(xAxisSamples)] for w in range((len(nValues)))]

lnDiff = [[0 for q in range(xAxisSamples)] for w in range((len(nValues)))]

for y in range(len(nValues)):
    for x in range(xAxisSamples):
        lnFromApprox[y][x] = approxLnFunc(xaxis[x],nValues[y])
        lnDiff[y][x] = lnFromPython[x] - lnFromApprox[y][x]

figure(dpi=300)
plot(xaxis, lnFromPython, label="Ln", linewidth=1.5)
for i in range(len(nValues)):
    plot(xaxis, lnFromApprox[i][:],'-.', label=f"Ln approx n = {nValues[i]}", linewidth=1)

xlabel('x values')
ylabel('ln(x)')
title('Ln from python and approximation')
legend()
show()

figure(dpi=150)
for i in range(len(nValues)):
    plot(xaxis, lnDiff[i][:],'-.', label=f"Ln diff n = {nValues[i]}", linewidth=1)

xlabel('x values')
ylabel('ln(x) - Ln_approx(x)')
title('Ln Diff between python and approximation for different n')
legend()
show()

"""        # Task 3                 """
x_val = 1.41
nValues = [e for e in range(1,101)]
lnAprrox_n = [0 for e in range(100)]
lnDiffAbs_n = [0 for e in range(100)]

for r in range(len(nValues)):
    lnAprrox_n[r] = approxLnFunc(x_val, nValues[r])
    lnDiffAbs_n[r] = abs(log(x_val) - lnAprrox_n[r])
    
figure(dpi=300)
plot(nValues, lnDiffAbs_n, label="Abs(Ln_Diff)", linewidth=1)
xlabel('n values')
ylabel('|ln(x) - Ln_approx(x)|')
title('|Ln Diff| for different n')
show()


"""        # Task 4                 """

def fastApproxLnFunc(x,n):
    
    a = [0 for p in range(n+2)]
    g = [0 for p in range(n+2)]
    d = [[0 for p in range(n+1)] for p in range(n+1)]
    
    a[0] = (1+x)/2
    g[0] = sqrt(x)
    
    for i in range(0,n+1):
        d[0][i] = a[i]
        a[i+1] = (a[i] + g[i])/2
        g[i+1] = sqrt(a[i+1] * g[i])
        if (i > 0):
            for k in range(1,i+1):
                d[k][i] = (d[k-1][i] - d[k-1][i-1] * 4**(-k)) / (1 - 4**(-k))           
        
    return (x-1)/d[n][n]


"""        # Task 5                 """
#test1 = concatenate(linspace(0.1, 3, 5000),linspace(3, 8, 100))
xaxis1 = linspace(0.1, 8, 5000)
lnFromPython1 = log(xaxis1)
nValues1 = [2,3,4,5,6]
lnFromFastApprox = [[0 for g in range(len(xaxis1))] for f in range(len(nValues1))]
errorFromFastApprox = [[0 for g in range(len(xaxis1))] for f in range(len(nValues1))]

for k in range(len(nValues1)):
    for j in range(len(xaxis1)):
        lnFromFastApprox[k][j] = fastApproxLnFunc(xaxis1[j], nValues1[k])
        errorFromFastApprox[k][j] = abs(lnFromPython1[j] - lnFromFastApprox[k][j])

figure(dpi=150)
for i in range(len(nValues1)):
    plot(xaxis1, errorFromFastApprox[i][:],'.', label=f"Ln diff n = {nValues1[i]}", linewidth=1)
ylim([10**(-25), 10**(-13)])
xlabel('x values')
ylabel('ln(x) - Ln_fast_approx(x)')
title('Error approximation for different n')
legend()
show()






















