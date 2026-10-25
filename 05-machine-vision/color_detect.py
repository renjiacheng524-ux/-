"""第一个机器视觉小练习：找出图里的红色圆点。

不需要摄像头、不需要另外找图片：脚本先自己生成一张测试图
（白底上有红、绿、蓝三个圆点），再用 OpenCV 找出红色圆点，
圈出来并打印中心坐标。

运行：
    pip install opencv-python numpy
    python color_detect.py

预期：生成 test_image.png 和 result.png；终端打印红色圆点数量为 1
及其中心坐标；result.png 里红圈正好套住红色圆点。
"""

import cv2
import numpy as np

# 1. 生成测试图：白底 400x400，三个实心圆点
img = np.full((400, 400, 3), 255, dtype=np.uint8)
cv2.circle(img, (100, 200), 40, (0, 0, 255), -1)    # 红色 (BGR)
cv2.circle(img, (200, 200), 40, (0, 255, 0), -1)    # 绿色
cv2.circle(img, (300, 200), 40, (255, 0, 0), -1)    # 蓝色
cv2.imwrite("test_image.png", img)

# 2. 转 HSV，用两个区间盖住红色的两端（红色在色环两头）
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower1 = np.array([0, 70, 50])
upper1 = np.array([10, 255, 255])
lower2 = np.array([170, 70, 50])
upper2 = np.array([180, 255, 255])
mask = cv2.bitwise_or(
    cv2.inRange(hsv, lower1, upper1),
    cv2.inRange(hsv, lower2, upper2),
)

# 3. 找轮廓，圈出红色圆点并打印中心坐标
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
result = img.copy()
centers = []
for cnt in contours:
    if cv2.contourArea(cnt) < 500:  # 过滤小噪点
        continue
    (x, y), radius = cv2.minEnclosingCircle(cnt)
    centers.append((int(x), int(y)))
    cv2.circle(result, (int(x), int(y)), int(radius), (0, 0, 255), 2)
    cv2.putText(result, f"({int(x)},{int(y)})", (int(x) - 30, int(y) - 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

cv2.imwrite("result.png", result)
print(f"找到红色圆点数量：{len(centers)}")
for cx, cy in centers:
    print(f"中心坐标：({cx}, {cy})")
