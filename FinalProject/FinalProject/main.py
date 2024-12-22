# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 17:43:49 2024

@author: swaroop
"""
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

"""
Task - 1: Reading task
"""

"""
Task - 2: Save the image as a numpy array 
"""
# read image and convert to gray scale
def readImageAndConvertToGray(imageName):    
    image = Image.open(imageName).convert ("L")
    return image

# convert to numpy array
def saveAsNumpyArray(image):    
    a = np.asarray(image)
    return a

"""
Task - 3 : Determine shape of array, if its not even numbers, delete a row, 
           a column, or both to make the shape a pair of even numbers 
"""
def checkShapeAndResize(arrayName):
    rowTemp, colTemp = arrayName.shape
    if (rowTemp % 2 != 0):
        if (colTemp % 2 != 0):
            arrayName = arrayName[:rowTemp - 1,:colTemp - 1]
        else:
            arrayName = arrayName[:rowTemp - 1,:]
    elif (colTemp % 2 != 0):
        arrayName = arrayName[:,:colTemp - 1]
    
    return arrayName

# Test code for task 3
# array_2d = np.zeros((3, 3))
# print(array_2d)
# array_2d = checkShapeAndResize(array_2d)
# print(array_2d)

"""
Task - 4 : Compute Wavelet matrices for multiplication, both left and right
"""
# generating a w_m matrix
def generateWmMatrices(M):
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
    
    return w_m

# Test code for left and right wavelet matrices
# array_2d = np.zeros((4, 6))
# rows1,cols1 = array_2d.shape
# left = generateWmMatrices(rows1)
# right = generateWmMatrices(cols1)
# print(left)
# print(right)

"""
Task - 5 : Make the wavelet transformation. Save the resulting image in a file
"""
image = readImageAndConvertToGray("Largehaarimage.jpg")
a = saveAsNumpyArray(image)
a = checkShapeAndResize(a)
rows,cols = a.shape
leftWaveletMatrix = generateWmMatrices(rows)
tempMatrix = generateWmMatrices(cols)
rightWaveletMatrix = tempMatrix.T
hwt_1 = leftWaveletMatrix @ a @ rightWaveletMatrix

# another way to do matrix multiplication
# leftMul = leftWaveletMatrix @ a
# rightMul = a @ rightWaveletMatrix
# hwt_1 = leftMul @ rightWaveletMatrix

plt.figure(1)
im1 = plt.imshow(hwt_1, cmap ='gray')

# hwt_round = hwt_1.round()
# max_val = hwt_round.max()
# min_val = hwt_round.min()
# hwt_norm_0to1 = (hwt_round - min_val)/(max_val - min_val)
# hwt_norm_0to255 = hwt_norm_0to1 * 255
# hwt_norm_0to255_uint8 = hwt_norm_0to255.astype(np.uint8)
# newimg = Image.fromarray(hwt_norm_0to255_uint8)
# newimg.save("new_Largehaarimage.jpg")

"""
Task - 6 : working with the left upper subimage, continued algorithm
"""

hwt_compressed = hwt_1[:rows//2,:cols//2]
hwt_compressed = checkShapeAndResize(hwt_compressed)
rows1,cols1 = hwt_compressed.shape
leftWaveletMatrix1 = generateWmMatrices(rows1)
tempMatrix1 = generateWmMatrices(cols1)
rightWaveletMatrix1 = tempMatrix1.T
leftMul = leftWaveletMatrix1 @ hwt_compressed
rightMul = hwt_compressed @ rightWaveletMatrix1
hwt_2 = leftWaveletMatrix1 @ hwt_compressed @ rightWaveletMatrix1

hwt_2test = hwt_1.copy()
hwt_2test[:rows1,:cols1] = hwt_2

"""
Task - 7 : Create a function that does Haar transformation by
            - Taking an array
            - cutting rows and columns if necessary
            - returning four smaller submatrices
"""
def haarTransformation(arrayName):
    arrayName = checkShapeAndResize(arrayName)
    rows,cols = arrayName.shape
    leftWaveletMatrix = generateWmMatrices(rows)
    rightWaveletMatrix = generateWmMatrices(cols).T
    # leftMul = leftWaveletMatrix @ arrayName
    # rightMul = arrayName @ rightWaveletMatrix
    # hwt_1 = leftMul @ rightWaveletMatrix
    hwt = leftWaveletMatrix @ arrayName @ rightWaveletMatrix
    leftUpper = hwt[:rows//2, :cols//2]
    leftLower = hwt[rows//2:, :cols//2]
    rightUpper = hwt[:rows//2, cols//2:]
    rightLower = hwt[rows//2:, cols//2:]
    
    return leftUpper, leftLower, rightUpper, rightLower, hwt

image2 = readImageAndConvertToGray("Largehaarimage.jpg")
arr1 = saveAsNumpyArray(image2)
leftU, leftL, rightU, rightL, hwt_t1 = haarTransformation(arr1)
plt.figure(2)
im2 = plt.imshow(hwt_t1, cmap ='gray')

"""
Task - 7 : Create a function that does inverse Haar transformation by
            - Taking 4 submatrice arrays
            - forms big matrix
            - applies inverse transformation
"""
def inverseHaarTransformation(leftUpper, leftLower, rightUpper, rightLower):
    rows_t,cols_t = leftUpper.shape
    bigMatrix = np.zeros((2 * rows_t, 2 * cols_t))
    bigMatrix[:rows_t, :cols_t] = leftUpper
    bigMatrix[rows_t:, :cols_t] = leftLower
    bigMatrix[:rows_t, cols_t:] = rightUpper
    bigMatrix[rows_t:, cols_t:] = rightLower
    
    rows,cols = bigMatrix.shape
    leftWaveletMatrixInv = generateWmMatrices(rows).T
    rightWaveletMatrixInv = generateWmMatrices(cols)
    invHwt = leftWaveletMatrixInv @ bigMatrix @ rightWaveletMatrixInv
    
    return invHwt

decompressedImg = inverseHaarTransformation(leftU, leftL, rightU, rightL)
plt.figure(3)
im3 = plt.imshow(decompressedImg, cmap ='gray')


plt.show ()

# # save an image from a numpy array
# newimg = Image.fromarray(a)
# newimg.save("new_kvinna.jpg")


# # plot an image , use colormap gray
# imgplt = plt.imshow(a, cmap ='gray')
# plt.show ()

