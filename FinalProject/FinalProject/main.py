# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 17:43:49 2024

@author: swaro
"""

from PIL import Image
# read image and convert to gray scale
image = Image.open("kvinna.jpg").convert ("L")

# convert to numpy array
import numpy as np
a = np.asarray(image)

# save an image from a numpy array
newimg = Image.fromarray(a)
newimg.save("new_kvinna.jpg")

# plot an image , use colormap gray
from matplotlib import pyplot as plt
imgplt = plt.imshow(a, cmap ='gray')
plt.show ()

# generating a w_m matrix
M = 8
w_m = np.zeros((M,M))
row_average = [(2**0.5)/2, (2**0.5)/2] + [0.0 for x in range(M-2)]
row_difference = [(2**0.5)/2, -(2**0.5)/2] + [0.0 for x in range(M-2)]
for x in range(M//2):
    if (x == 0):
        w_m[x] = np.array(row_average)
        w_m[M//2 + x] = np.array(row_difference)
    else:
        w_m[x] = np.array(row_average[-2*x:] + row_average[0:M-2*x])
        w_m[M//2 + x] = np.array(row_difference[-2*x:] + row_difference[0:M-2*x])
print(w_m)

w_m_t = w_m.T
print(w_m_t)