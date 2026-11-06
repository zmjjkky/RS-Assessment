import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "/Users/jikeyan/Desktop/视觉二轮季柯言26061915/Opencv部分/计算轮廓特征/计算轮廓特征.jpg"
img = cv2.imdecode(np.fromfile(path,dtype=np.uint8),-1)

if img is None:
    print("图片读取失败")

else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    img_result = img.copy()

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100:
            perimeter = cv2.arcLength(cnt, True)
            x, y, w, h = cv2.boundingRect(cnt)

            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)
            box = np.int32(box)
            cv2.drawContours(img_result, [cnt], 0, (0, 255, 0), 2)
            cv2.rectangle(img_result, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.drawContours(img_result, [box], 0, (0, 0, 255), 2)
            text = f"A:{int(area)} P:{int(perimeter)}"#面积周长信息显示
            cv2.putText(img_result, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)


            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_result_rgb = cv2.cvtColor(img_result, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(15, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(img_rgb)
    plt.title("Original")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(img_result_rgb)
    plt.title("Contour Features (Green: Contour, Blue: Rect, Red: MinRect)")
    plt.axis('off')

    plt.tight_layout()
    plt.show()
