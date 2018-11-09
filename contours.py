#!/usr/local/bin/python2.7
# -*- coding:utf-8 -*-

import numpy as np
import cv2
#from matplotlib import pyplot as plt

#https://www.jianshu.com/p/3dbf108eaa32
#https://blog.csdn.net/A632189007/article/details/78126588

# 读取图片
#img = cv2.imread("h2p6.png")
img = cv2.imread("h6p8.png")
# 转灰度图片
#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imwrite('gray.png', gray)
#ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
binary = cv2.Canny(img, 64, 256)
#binary = cv2.Canny(img, 128, 256)
cv2.imwrite('binary.png', binary)

##thresh = np.ones_like(gray)
##ret = 168
##thresh[gray < ret] = 255
##thresh[gray > ret] = 0
##
##fig = plt.figure(figsize=(16, 6))
##plt.subplot(131),plt.imshow(img)
##plt.subplot(132),plt.imshow(gray,'gray')
##plt.subplot(133),plt.imshow(thresh,'gray')
##plt.show()

# 轮廓检测
#ret, contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
ret, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#ret, contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#ret, contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#print contours, hierarchy

# 画图
#cv2.drawContours(ret, contours, -1, (0,255,0), 3)
dst = np.copy(img)
cv2.drawContours(dst, contours, -1, (255,0,0), 1)
#for i in range(len(contours)-1):
#    cv2.drawContours(dst, contours[i+1], -1, (255,0,0), 1)
#for i in range(0,len(contours)):
#    x, y, w, h = cv2.boundingRect(contours[i])
#    cv2.rectangle(ret, (x,y), (x+w,y+h), (153,153,0), 5)

# 展示
cv2.imshow("img", dst)
cv2.imwrite('img.png', dst)
cv2.waitKey(149)
