#!/usr/local/bin/python2.7
# -*- coding:utf-8 -*-

import numpy as np
import cv2
import time
#from matplotlib import pyplot as plt

#https://www.jianshu.com/p/3dbf108eaa32
#https://blog.csdn.net/A632189007/article/details/78126588

# 读取图片
img = cv2.imread("h6p8.png")
cv2.imshow('source', img)
# 转灰度图片
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray.png', gray)

blur = cv2.GaussianBlur(gray, (5,5), 2)
cv2.imwrite('blur.png', blur)

canny = cv2.Canny(blur, 0, 256)
#canny = cv2.Canny(blur, 80, 150)
cv2.imwrite('canny.png', canny)

ret, contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

imageContours = np.zeros(img.shape, np.uint8)
marks = np.zeros(img.shape, np.uint8)

for i in range(0,len(contours)):
    cv2.drawContours(marks,contours,i,(i,0,0),1,8,hierarchy)
    cv2.drawContours(imageContours,contours,i,(255,0,0),1,8,hierarchy)

cv2.imwrite('tmp.png', imageContours)
cv2.imwrite('tmp1.png', marks)

#marks = cv2.watershed(img, marks)
#img[marks == -1] = [0,0,255]
#cv2.imwrite('maker.png', marks)

dst = np.copy(img)

w = img.shape[0]
h = img.shape[1]
c_max = []
for i in range(len(contours)):
    cnt = contours[i]
    area = cv2.contourArea(cnt)

    # 处理掉小的轮廓区域，这个区域的大小自己定义。
    if(area < (h/10*w/10)):
        c_min = []
        c_min.append(cnt)
        # thickness不为-1时，表示画轮廓线，thickness的值表示线的宽度。
        cv2.drawContours(dst, c_min, -1, (255,0,0), thickness=1)
        continue
    #
    c_max.append(cnt)

cv2.drawContours(dst, c_max, -1, (255,0,0), 1)

cv2.imwrite('dst.png', dst)

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
#ret, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#ret, contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#ret, contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#print contours, hierarchy

# 画图
#cv2.drawContours(ret, contours, -1, (0,255,0), 3)
#dst = np.copy(img)
#cv2.drawContours(dst, contours, -1, (255,0,0), 1)
#for i in range(len(contours)-1):
#    cv2.drawContours(dst, contours[i+1], -1, (255,0,0), 1)
#for i in range(0,len(contours)):
#    x, y, w, h = cv2.boundingRect(contours[i])
#    cv2.rectangle(ret, (x,y), (x+w,y+h), (153,153,0), 5)

# 展示
#cv2.imshow("img", dst)
#cv2.imwrite('img.png', dst)
