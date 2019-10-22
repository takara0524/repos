#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 13:16:02 2019

@author: TAKARA
"""

import numpy as np

def selectPivot(mat, b, p):
    maxNum = abs(mat[p][p])
    maxIndex = p
    for i in range(p+1, len(mat)):
        if(maxNum < abs(mat[i][p])): 
            maxIndex = i
            maxNum = abs(mat[i][p])
        
    temp = mat[p].copy()
    mat[p] = mat[maxIndex]
    mat[maxIndex] = temp
    temp = b[p].copy()
    b[p] = b[maxIndex]
    b[maxIndex] = temp
    
def gaussPivot(mat, b):
    rank = np.linalg.matrix_rank(mat)
    if (rank > len(b)): 
        print("error1")
        return
    elif(len(mat[0]) > len(b)):
        print("error2")
        return
    
    for i in range(rank):
        selectPivot(mat, b, i)
        for j in range(i+1, len(mat)):
            coef = mat[j][i] / mat[i][i]
            mat[j] -= mat[i] * coef
            b[j] -= b[i] * coef
        
    for i in range(rank - 1, 0, -1):
        b[i] /= mat[i][i]
        mat[i] /= mat[i][i]
        for j in range(i):
            b[j] -= b[i] * mat[j][i]
            mat[j][i] = 0
    b[0] /= mat[0][0]
    ans = b[:rank]
    return ans
    
    
