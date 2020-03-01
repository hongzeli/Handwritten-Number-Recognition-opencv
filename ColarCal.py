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
    TL = img[:50, :50].mean()
    BL = img[-50:,:50].mean()
    # TR = img[:50, -50:].mean()
    BR = img[-50:, -50:].mean()
    tile_size = 10 
#    tile = 200
    dim_0 = img.shape[0]
    dim_1 = img.shape[1]
    A = np.array([[0,0,1],[0,dim_0,1],[dim_1,dim_0,1]])
    b = np.array([TL,BL,BR])
    res = np.linalg.solve(A, b)     *********************until here, not finish
    for x in range(dim_x//tile_size + 1):
        for y in range(dim_x//tile_size + 1):
            adjustment[x*dim/tile:(x+1)*dim/tile, y*dim/tile:(y+1)*dim/tile] = int((BL-TL)*(x*dim/tile)/img.shape[0] + (BR-BL)*(y*dim/tile)/img.shape[0] + TL + 0.5)
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
