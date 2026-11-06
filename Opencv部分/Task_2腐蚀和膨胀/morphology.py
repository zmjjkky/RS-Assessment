from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np

BASE_DIR = Path(__file__).resolve().parent
IMG_PATH = BASE_DIR / "腐蚀膨胀.png"

KERNEL_SIZE = 9 


def main():
    img = cv2.imread(str(IMG_PATH))
    if img is None:
        print(f"图片读取失败：{IMG_PATH}")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT, (KERNEL_SIZE, KERNEL_SIZE)
    )

    img_eroded = cv2.erode(binary, kernel, iterations=1)
    img_dilated = cv2.dilate(binary, kernel, iterations=1)

    cv2.imwrite(str(BASE_DIR / "binary.png"), binary)
    cv2.imwrite(str(BASE_DIR / "eroded.png"), img_eroded)
    cv2.imwrite(str(BASE_DIR / "dilated.png"), img_dilated)

    print("腐蚀改变的像素数:", int(np.count_nonzero(img_eroded != binary)))
    print("膨胀改变的像素数:", int(np.count_nonzero(img_dilated != binary)))
    print(f"结果已保存到：{BASE_DIR}")

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    panels = [
        (img_rgb, "Original"),
        (binary, "Binary (Otsu)"),
        (img_eroded, "Eroded"),
        (img_dilated, "Dilated"),
    ]

    plt.figure(figsize=(16, 8))
    for i, (image, title) in enumerate(panels, start=1):
        plt.subplot(2, 2, i)
        plt.imshow(image, cmap="gray" if image.ndim == 2 else None)
        plt.title(title)
        plt.axis("off")

    plt.tight_layout()
    plt.savefig(str(BASE_DIR / "morphology_result.png"), dpi=150)
    plt.show()


if __name__ == "__main__":
    main()
