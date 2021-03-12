import cv2

# from matplotlib import pyplot as plt
from pylab import *

import numpy

# 载入图像
im = cv2.imread('Middlebury_01_clean_color.png')

# 颜色空间转换
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# 显示原始图像
fig = plt.figure()
subplot(121)
plt.gray()
imshow(im)
axis('off')
# 显示灰度化图像
plt.subplot(122)
plt.gray()
imshow(gray)
axis('off')

show()



