

'''
单图识别试验代码
import cv2
import matplotlib.pyplot as plt
import numpy as np

path = "/Users/jikeyan/Desktop/视觉二轮季柯言26061915/Opencv部分/形状区分/检测图形.png"
img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), -1)

if img is None:
    print('涂片读取失败')
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#灰度图
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)#平滑边缘，防止检测出多的点
    edges = cv2.Canny(blurred, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    img_result = img.copy()

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            perimeter = cv2.arcLength(cnt,True)
            #多边形逼近
            approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)
            x, y, w, h = cv2.boundingRect(cnt)
            aspect_ratio = float(w) / h#区分正方形和长方形

            color_square = (0, 255, 0)   # 绿色 - 正方形
            color_rect = (255, 0, 0)     # 蓝色 - 长方形
            color_tri = (0, 0, 255)      # 红色 - 三角形
            color_other = (0, 255, 255)  # 黄色 - 其他（比如圆）


            shape_name = "Unknown"
            draw_color = color_other
            if len(approx) == 3:
                shape_name = "Triangle" # 三角形
                draw_color = color_tri
            elif len(approx) == 4:
                if 0.95 <= aspect_ratio <= 1.05:
                    shape_name = "Square" # 正方形
                    draw_color = color_square
                else:
                    shape_name = "Rectangle" # 长方形
                    draw_color = color_rect
            else:
                shape_name = "Circle/Other"


            cv2.rectangle(img_result, (x, y), (x + w, y + h), draw_color, 2)
            cv2.putText(img_result, shape_name, (x, y - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, draw_color, 2)


    plt.figure(figsize=(15, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(img_result, cv2.COLOR_BGR2RGB))
    plt.title("Shape Detection")
    plt.axis('off')

    plt.tight_layout()
    plt.show()
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt


path = "/Users/jikeyan/Desktop/视觉二轮季柯言26061915/Opencv部分/形状区分/检测图形.png"
img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), -1)

if img is None:
    print("❌ 图片读取失败，请检查路径！")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    _, thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    img_result = img.copy()
    count_dict = {"Triangle": 0, "Square": 0, "Rectangle": 0, "Circle": 0}

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 200: 
            
            perimeter = cv2.arcLength(cnt, True)
            
            approx = cv2.approxPolyDP(cnt, 0.03 * perimeter, True)
            
            x, y, w, h = cv2.boundingRect(cnt)
            aspect_ratio = float(w) / h

            shape_name = "Other"
            draw_color = (0, 255, 255) # 黄色

            if len(approx) == 3:
                shape_name = "Triangle"
                draw_color = (0, 0, 255)   # 红色
                
            elif len(approx) == 4:
                # 【关键升级 3】：放宽比例限制 (0.85 ~ 1.15)，容错率更高
                if 0.85 <= aspect_ratio <= 1.15:
                    shape_name = "Square"
                    draw_color = (0, 255, 0)   # 绿色
                else:
                    shape_name = "Rectangle"
                    draw_color = (255, 0, 0)   # 蓝色
                    
            elif len(approx) > 4:
                shape_name = "Circle"
                draw_color = (255, 255, 0) # 青色

            if shape_name in count_dict:
                count_dict[shape_name] += 1

            cv2.rectangle(img_result, (x, y), (x + w, y + h), draw_color, 2)
            cv2.putText(img_result, shape_name, (x, y - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, draw_color, 2)

    print(f"✅ 识别结果统计: {count_dict}")

    plt.figure(figsize=(15, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(img_result, cv2.COLOR_BGR2RGB))
    plt.title("Shape Detection")
    plt.axis('off')

    plt.tight_layout()
    plt.show()