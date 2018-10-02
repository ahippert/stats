#!/usr/bin/env python

# Statistics in python
#
# AH 07-09-2018
# Last update : 28-09-2018

import numpy as np

# compute the Root-Mean-Square Error (RMSE) between prediction and observation fields
#
def rmse(pred, obs, nt, nx, ny, col=True):
    sum_of_dif = 0
    for i in range(0, nt):
        if col :
            sum_of_dif += np.linalg.norm(pred[:,i] - obs[:,i])**2
        else :
            sum_of_dif += np.linalg.norm(pred[i] - obs[i])**2
    return np.sqrt(sum_of_dif/(nt*nx*ny))

# Compute RMSE between the mean of prediction and observation fields
#
def rmse_zero_mode(pred, obs, nt, nx, ny):
    sum_of_dif = 0
    for i in range(0, nt):
        sum_of_dif += np.linalg.norm(np.mean(pred[:,i])-obs[:,i])**2
    return np.sqrt(sum_of_dif/(nt*nx*ny))

# Compute cross-RMSE between prediction and observation fields
#
def rmse_cross_v(pred, obs, N):
    sum_of_dif = 0 
    for i in range(0, N):
        sum_of_dif += np.linalg.norm(pred[i] - obs[i])**2
    return np.sqrt(sum_of_dif/N)

# Compute cross-RMSE between the mean of prediction and observation fields
#
def rmse_cv_zero_mode(pred, obs, N):
    sum_of_dif = 0 
    for i in range(0, N):
        sum_of_dif += np.linalg.norm(np.mean(pred) - obs[i])**2
    return np.sqrt(sum_of_dif/(t*N))

# Compute RMSE between two images
#
def compute_image_rmse(im1, im2, nx, ny):
    rmse_im = 0
    for i in range(nx):
        for j in range(ny):
            rmse_im += np.linalg.norm(im1[i][j] - im2[i][j])**2
    return np.sqrt(rmse_im/(nx*ny))

# Compute the column/line mean of a matrix without NaNs
#
def compute_mean(matrix, n, col, nozeros=True):
    matrix_mean = []
    for i in range(0, n):
        if col :
            if nozeros:
                matrix_mean.append(np.nanmean(matrix[:,i]))
            else:
                matrix_mean.append(np.mean(matrix[:,i]))
        else :
            if nozeros:
                matrix_mean.append(np.nanmean(matrix[i]))
            else:
                matrix_mean.append(np.mean(matrix[i]))
    return matrix_mean

# Compute the column/line mean of a matrix without zeros
#
def compute_mean0(matrix, n, col, nozeros=True):
    matrix_mean = []
    for i in range(0, n):
        if col:
            if nozeros:
                matrix_mean.append(matrix[:,i][matrix[:,i].nonzero()].mean())
            else:
                matrix_mean.append(np.mean(matrix[:,i]))
        else:
            if nozeros:
                matrix_mean.append(matrix[i][matrix[i].nonzero()].mean())
            else:
                matrix_mean.append(np.mean(matrix[i]))
    return matrix_mean
    
# Remove the column/line mean of a matrix
#
def remove_mean(matrix, t_mean, n, col):
    if col: 
        for i in range(0, n):
            matrix[:,i] -= t_mean[i]
    else:
        for i in range(0, n):
            matrix[i] -= t_mean[i]
    return matrix

# Add the column/line mean of a matrix
#
def add_mean(data, mean, n, col):
    if col:
        for i in range(0, n):
            if np.isnan(mean[i]):
                data[:,i] += 0.
            else:
                data[:,i] += mean[i]
    else:
        for i in range(0, n):
            if np.isnan(mean[i]):
                data[i] += 0. 
            else:
                data[i] += mean[i]
    return data

# Compute statistical Chi-2 between observations and predictions
#
def chi2(obs, pred, n):
    chi = 0.
    for i in range(n):
        if pred[i]==0. or obs[i]==0. or (pred[i]==0. and obs[i]!=0.):
            print ("Bad expected number in chi-2")
        else :
            chi += (1/np.var(obs))*(obs[i] - pred[i])**2
    return chi

# Compute the F-Test between the variances of two datasets
#
def ftest(data1, data2):
    var1, var2 = np.var(data1), np.var(data2)
    if var1 > var2:
        return var1/var2
    else:
        return var2/var1
