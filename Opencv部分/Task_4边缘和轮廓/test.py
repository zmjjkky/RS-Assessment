import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

path = "/Users/jikeyan/Desktop/视觉二轮季柯言26061915/Opencv部分/边缘和轮廓/边缘轮廓.jpg"
img = cv2.imdecode(np.fromfile(path,dtype=np.uint8),-1)

if img is None:
    print("图片读取失败")
else:
    img_contours = img.copy()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges=cv2.Canny(img,100,200)#Canny 算法通过对图像进行梯度计算来找出边缘，返回一个二值图像，边缘处为白色，其他区域为黑色。
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img_contours, contours, -1, (0, 0, 255), 2)#画布，轮廓数据，颜色，线条粗细
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_contours_rgb = cv2.cvtColor(img_contours, cv2.COLOR_BGR2RGB)




    plt.figure(figsize=(18, 6))

    plt.subplot(1, 3, 1)
    plt.imshow(img_rgb)
    plt.title("Original")
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(edges, cmap='gray') # 边缘图是灰度的，用 cmap='gray'
    plt.title("Edges (Canny)")
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(img_contours_rgb)
    plt.title(f"Contours - {len(contours)} found") # 顺便打印找到了几个轮廓
    plt.axis('off')

    plt.tight_layout()
    plt.show()