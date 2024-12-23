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
    image_gray = Image.open(imageName).convert ("L")
    return image_gray

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
            w_m[M//2 + x] = \
                np.array(row_difference[-2*x:] + row_difference[0:M-2*x])
    
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
image1 = readImageAndConvertToGray("Largehaarimage.jpg")
a = saveAsNumpyArray(image1)
a = checkShapeAndResize(a)
rows,cols = a.shape
leftWaveletMatrix = generateWmMatrices(rows)
tempMatrix = generateWmMatrices(cols)
rightWaveletMatrix = tempMatrix.T
hwt_task5 = leftWaveletMatrix @ a @ rightWaveletMatrix

# another way to do matrix multiplication
# leftMul = leftWaveletMatrix @ a
# rightMul = a @ rightWaveletMatrix
# hwt_task5 = leftMul @ rightWaveletMatrix

plt.figure("Task5")
im_task5 = plt.imshow(hwt_task5, cmap ='gray')

hwt_round = hwt_task5.round()
max_val = hwt_round.max()
min_val = hwt_round.min()
hwt_norm_0to1 = (hwt_round - min_val)/(max_val - min_val)
hwt_norm_0to255 = hwt_norm_0to1 * 255
hwt_norm_0to255_uint8 = hwt_norm_0to255.astype(np.uint8)
newimg = Image.fromarray(hwt_norm_0to255_uint8)
newimg.save("new_Largehaarimage.jpg")

"""
Task - 6 : working with the left upper subimage, continued algorithm
"""

hwt_compressed = hwt_task5[:rows//2,:cols//2]
hwt_compressed = checkShapeAndResize(hwt_compressed)
rows1,cols1 = hwt_compressed.shape
leftWaveletMatrix1 = generateWmMatrices(rows1)
tempMatrix1 = generateWmMatrices(cols1)
rightWaveletMatrix1 = tempMatrix1.T
leftMul = leftWaveletMatrix1 @ hwt_compressed
rightMul = hwt_compressed @ rightWaveletMatrix1
hwt_2 = leftWaveletMatrix1 @ hwt_compressed @ rightWaveletMatrix1

hwt_2_task6 = hwt_task5.copy()
hwt_2_task6[:rows1,:cols1] = hwt_2

plt.figure("Task6")
im_task6 = plt.imshow(hwt_2_task6, cmap ='gray')

"""
Task - 7 : Create a function that does Haar transformation by
            - Taking an array
            - cutting rows and columns if necessary
            - returning four smaller submatrices
"""
def haarTransformation(arrayName):
    rows,cols = arrayName.shape
    leftWaveletMatrix = generateWmMatrices(rows)
    rightWaveletMatrix = generateWmMatrices(cols).T
    # leftMul = leftWaveletMatrix @ arrayName
    # rightMul = arrayName @ rightWaveletMatrix
    # hwt = leftMul @ rightWaveletMatrix
    hwt = leftWaveletMatrix @ arrayName @ rightWaveletMatrix
    leftUpper, leftLower, rightUpper, rightLower = splitSubMatrices(hwt)
    
    return leftUpper, leftLower, rightUpper, rightLower, hwt

def splitSubMatrices(bigMatrix, i = 1):
    rows,cols = bigMatrix.shape
    r1 = rows//2**(i)
    r2 = rows//2**(i-1)
    if (rows%2**(i) != 0):
        # if (rows%2**(i-1) != 0):
        r2 = r2 - 1
    c1 = cols//2**(i)
    c2 = cols//2**(i-1)
    if (cols%2**(i) != 0):
        c2 = c2 - 1
    leftUpper = bigMatrix[:r1, :c1]
    leftLower = bigMatrix[r1:r2, :c1]
    rightUpper = bigMatrix[:r1, c1:c2]
    rightLower = bigMatrix[r1:r2, c1:c2]
    
    return leftUpper, leftLower, rightUpper, rightLower

"""
Task - 8 : Create a function that does inverse Haar transformation by
            - Taking 4 submatrice arrays
            - forms big matrix
            - applies inverse transformation
"""
def combineSubMatrices(leftUpper, leftLower, rightUpper, rightLower):
    rows_t,cols_t = leftUpper.shape
    bigMatrix = np.zeros((2 * rows_t, 2 * cols_t))
    bigMatrix[:rows_t, :cols_t] = leftUpper
    bigMatrix[rows_t:, :cols_t] = leftLower
    bigMatrix[:rows_t, cols_t:] = rightUpper
    bigMatrix[rows_t:, cols_t:] = rightLower
    
    return bigMatrix

def inverseHaarTransformation(leftUpper, leftLower, rightUpper, rightLower):
    bigMatrix = combineSubMatrices(leftUpper,
                                   leftLower,
                                   rightUpper,
                                   rightLower)
    rows,cols = bigMatrix.shape
    leftWaveletMatrixInv = generateWmMatrices(rows).T
    rightWaveletMatrixInv = generateWmMatrices(cols)
    invHwt = leftWaveletMatrixInv @ bigMatrix @ rightWaveletMatrixInv
    
    return invHwt

"""
Task - 9 : Write the program Haar compression
"""
image2 = readImageAndConvertToGray("kvinna.jpg")
arr_image2 = saveAsNumpyArray(image2)
arr_image2 = checkShapeAndResize(arr_image2)
leftU, leftL, rightU, rightL, hwt_t1 = haarTransformation(arr_image2)

plt.figure("Task7")
im_task7 = plt.imshow(hwt_t1, cmap ='gray')

decompressedImg = inverseHaarTransformation(leftU, leftL, rightU, rightL)

plt.figure("Task8")
im_task8 = plt.imshow(decompressedImg, cmap ='gray')
"""------------------------------------------------------------"""
def haarCompression(imageAsArray, nIterations):
    imageAsArray = checkShapeAndResize(imageAsArray)
    rows_hc, cols_hc = imageAsArray.shape
    arrayCopy = imageAsArray.copy()
    arrayCopy2 = np.zeros((rows_hc, cols_hc))
    for i in range(nIterations):
        arrayCopy = checkShapeAndResize(arrayCopy)
        leftUpper, *_, hwt = haarTransformation(arrayCopy)
        arrayCopy = leftUpper
        rowIdxend = rows_hc//2**(i)
        colIdxend = cols_hc//2**(i)
        if (rowIdxend % 2 != 0):
            rowIdxend = rowIdxend - 1
        if (colIdxend % 2 != 0):
            colIdxend = colIdxend - 1    
        arrayCopy2[:rowIdxend,:colIdxend] = hwt
    plt.figure("Haar Transformation - Task 9")
    im_task9_hc = plt.imshow(arrayCopy2, cmap ='gray')
    
    rowMod, colMod = arrayCopy2.shape
    for i in range(nIterations):
        topLeft, bottomLeft, topRight, bottomRight = \
            splitSubMatrices(arrayCopy2, nIterations - i)
        invTrans = inverseHaarTransformation(topLeft,
                                             bottomLeft,
                                             topRight,
                                             bottomRight)
        rowIndex = rowMod//2**(nIterations - i - 1)
        colIndex = colMod//2**(nIterations - i - 1)
        if (rowIndex % 2 != 0):
            rowIndex = rowIndex - 1
        if (colIndex % 2 != 0):
            colIndex = colIndex - 1   
        arrayCopy2[:rowIndex,:colIndex] = invTrans
    
    plt.figure("Haar deTransformation - Task 9")
    im_task10_hc = plt.imshow(arrayCopy2, cmap ='gray')
    
    return arrayCopy2
        
n_iterations = 6
image3 = readImageAndConvertToGray("kvinna.jpg")
arr_image3 = saveAsNumpyArray(image3)
# arr_image3 = arr_image3.T #only used this to debug issues
test = haarCompression(arr_image3, n_iterations)
plt.show ()

