import skimage.io as io
import skimage.util as ut
import matplotlib.pyplot as plt
from scipy.ndimage import uniform_filter
import numpy as np
from scipy.ndimage import median_filter
# 讀取影像
image = io.imread("gull_gray.png")  # 灰階讀取

# 添加鹽和胡椒雜訊，amount 表示雜訊比例 (5% = 0.05)
photo = ut.random_noise(image, mode='s&p', amount=0.05)
#使用平均濾波去除雜訊
avg_photo = uniform_filter(photo, size=5)
#使用中值濾波去除雜訊
med_photo = median_filter(photo, size=5)
#使用離群值方法去除雜訊
# 定義窗口大小
window_size = 5
# 定義簡單的離群值去噪方法
def remove_outliers(image, threshold=0.5, window_size=3):
    filtered_image = np.copy(image)
    offset = window_size // 2
    rows, cols = image.shape
    for i in range(offset, rows - offset):
        for j in range(offset, cols - offset):
            # 提取鄰域窗口
            window = image[i - offset:i + offset + 1, j - offset:j + offset + 1]
            # 計算中值
            median_value = np.median(window)
            # 替換離群值
            if abs(image[i, j] - median_value) > threshold:
                filtered_image[i, j] = median_value
    return filtered_image


# 顯示圖片
plt.subplot(2, 2, 1)
plt.imshow(photo , cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(avg_photo, cmap='gray')
plt.title('Average')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(med_photo, cmap='gray')
plt.title('Median')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(remove_outliers(photo), cmap='gray')
plt.title('Outliers')
plt.axis('off')

plt.show()
