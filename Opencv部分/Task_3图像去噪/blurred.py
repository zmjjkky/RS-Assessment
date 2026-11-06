'''
这部分需要用到的新知识：
1、均值滤波
blurred_image = cv2.blur(image, (kernel_size, kernel_size))
2、高斯滤波
blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), sigmaX)
'''


import cv2
import matplotlib.pyplot as plt
import numpy as np

def add_salt_pepper(img, ratio=0.02):#椒盐噪声
    out = img.copy()
    h, w = img.shape[:2]
    n = int(h * w * ratio)
    half = n // 2

    # 盐：白点
    ys = np.random.randint(0, h, half)
    xs = np.random.randint(0, w, half)
    out[ys, xs] = 255
    
    # 椒：黑点
    ys = np.random.randint(0, h, half)
    xs = np.random.randint(0, w, half)
    out[ys, xs] = 0
    return out

path = '/Users/jikeyan/Desktop/视觉二轮季柯言26061915/Opencv部分/图像去噪/去噪.jpg'
img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), -1)
if img is None:
    print("图片读取失败！")
else:
    img_saltpepper=add_salt_pepper(img)
     # 1. 均值滤波去噪 (窗口大小 5x5)
    img_mean_blur = cv2.blur(img_saltpepper, (5, 5))
    # 2. 高斯滤波去噪 (窗口大小 5x5)
    img_gaussian_blur = cv2.GaussianBlur(img_saltpepper, (5, 5), 0)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_sp_rgb = cv2.cvtColor(img_saltpepper, cv2.COLOR_BGR2RGB)
    img_mean_rgb = cv2.cvtColor(img_mean_blur, cv2.COLOR_BGR2RGB)
    img_gaussian_rgb = cv2.cvtColor(img_gaussian_blur, cv2.COLOR_BGR2RGB)

    
    plt.figure(figsize=(20, 5))

    plt.subplot(1, 4, 1)
    plt.imshow(img_rgb)
    plt.title("Original")
    plt.axis('off')

    plt.subplot(1, 4, 2)
    plt.imshow(img_sp_rgb)
    plt.title("Salt & Pepper Noise")
    plt.axis('off')

    plt.subplot(1, 4, 3)
    plt.imshow(img_mean_rgb)
    plt.title("Mean Blur")
    plt.axis('off')

    plt.subplot(1, 4, 4)
    plt.imshow(img_gaussian_rgb)
    plt.title("Gaussian Blur")
    plt.axis('off')

    plt.tight_layout()
    plt.show()
