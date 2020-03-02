# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 21:07:08 2020

@author: lhzcom
"""
import cv2
import numpy as np

debug = 1

def surface_fitting(img):
    adjustment = np.zeros_like(img)
    corner_size = 50
    TL = img[:corner_size, :corner_size].mean()
    BL = img[-corner_size:,:corner_size].mean()
    # TR = img[:corner_size, -corner_size:].mean()
    BR = img[-corner_size:, -corner_size:].mean()

    tile_size = 10
    dim_0 = img.shape[0]
    dim_1 = img.shape[1]
    A = np.array([[0,0,1],[0,dim_0,1],[dim_1,dim_0,1]])
    b = np.array([TL,BL,BR])
    res = np.linalg.solve(A, b)

    for x in range(dim_1//tile_size + 1):
        for y in range(dim_0//tile_size + 1):
            adjustment[y*tile_size:min((y+1)*tile_size, dim_0), x*tile_size:min((x+1)*tile_size, dim_1)] = \
                x*tile_size*res[0]+y*tile_size*res[1]+res[2]
    return adjustment

if __name__=="__main__":
    img = cv2.imread("test4.jpg", cv2.IMREAD_GRAYSCALE)
    img = 255 - img
    adjustment = surface_fitting(img)
    img_ad = np.where(img >= adjustment, img - adjustment, 0)
    if debug:
        cv2.imshow("img_ad", img_ad)
        cv2.waitKey()
    print("over")
