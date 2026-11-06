import os

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 程序所在文件夹（无论从哪个目录运行都指向本文件所在处）
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def add_gaussian_noise(img, mean=0.0, sigma=25.0):#高斯噪声
    imgnoise=img.copy()
    noise = np.random.normal(mean, sigma, img.shape).astype(np.float32)
    output = imgnoise.astype(np.float32) + noise
    return np.clip(output, 0, 255).astype(np.uint8)
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


img=cv2.imread(os.path.join(BASE_DIR, 'test.jpeg'))
if img is None:
    print('图片读取失败')
else:
    img_gaussian=add_gaussian_noise(img)
    img_saltpepper=add_salt_pepper(img)

    #用 imwrite 把结果保存到程序所在文件夹
    combined_bgr = np.hstack((img, img_gaussian, img_saltpepper))
    outputs = {
        'Noise_original.jpg': img,
        'Noise_gaussian.jpg': img_gaussian,
        'Noise_saltpepper.jpg': img_saltpepper,
        'Noise_combined.jpg': combined_bgr,
    }
    for name, image in outputs.items():
        path = os.path.join(BASE_DIR, name)
        ok = cv2.imwrite(path, image)
        print(('已保存 ' if ok else '保存失败 ') + path)

    #这一块无法显示椒盐噪声，原因不清楚～～～
    #cv2.imshow('original',img)
    #cv2.imshow('gaussian_noise',img_gaussian)
    #cv2.imshow('img_saltpepper_noise',img_saltpepper)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
    
    #下用plt显示图片（纯好看）
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_gaussian_rgb = cv2.cvtColor(img_gaussian, cv2.COLOR_BGR2RGB)
    img_saltpepper_rgb = cv2.cvtColor(img_saltpepper, cv2.COLOR_BGR2RGB)

    
    plt.figure(figsize=(15, 5))

    
    plt.subplot(1, 3, 1)
    plt.imshow(img_rgb)
    plt.title("Original Image")
    plt.axis('off')

    # 绘制高斯噪声图
    plt.subplot(1, 3, 2)
    plt.imshow(img_gaussian_rgb)
    plt.title("Gaussian Noise")
    plt.axis('off')

    # 绘制椒盐噪声图
    plt.subplot(1, 3, 3)
    plt.imshow(img_saltpepper_rgb)
    plt.title("Salt & Pepper Noise")
    plt.axis('off')


    combined_img = np.hstack((img_rgb, img_gaussian_rgb, img_saltpepper_rgb))

    plt.figure(figsize=(18, 6))
    plt.imshow(combined_img)
    plt.title("Original | Gaussian Noise | Salt_Pepper Noise")
    plt.axis('off')
    plt.show()