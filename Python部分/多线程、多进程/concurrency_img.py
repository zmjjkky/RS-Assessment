import cv2
import time
import numpy as np
import os
import concurrent.futures
from loguru import logger

def read_single_img(img_path):
    img = cv2.imdecode(np.fromfile(img_path, dtype = np.uint8),-1)
    if img is not None:
        return img.shape
    else:
        return None

if __name__ =="__main__":
    data_dir = "data"

    if not os.path.exists(data_dir):
        logger.error(f"找不到文件夹{data_dir},请先创建data放入图片")
        exit()

    img_path = []
    for f in os.listdir(data_dir):
        if f.lower().endswith((".jpg", ".png"," .jpeg")):
            img_path.append(os.path.join(data_dir, f))

    if len(img_path) == 0:
        logger.warning("data文件夹中无图片!")
        exit()
    logger.info(f"共找到 {len(img_path)} 张图片")

    #单线程
    logger.info("开始测试【单线程读图】...")
    start_time = time.perf_counter()
    for path in img_path:
        read_single_img(path)
    end_time = time.perf_counter()
    logger.success(f"单线程耗时: {end_time - start_time:.4f} 秒\n")
    #多线程
    logger.info("开始测试【多线程读图】...")
    start_time = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        # 注意：这里我们没有用 submit，而是用了 map
        # map 会自动把 img_paths 里的每一个元素传给 read_single_image
        list(executor.map(read_single_img, img_path))
    end_time = time.perf_counter()
    logger.success(f"多线程耗时: {end_time - start_time:.4f} 秒\n")
    #多进程
    logger.info("开始测试【多进程读图】...")
    start_time = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        list(executor.map(read_single_img, img_path))
    end_time = time.perf_counter()
    logger.success(f"多进程耗时: {end_time - start_time:.4f} 秒\n")
