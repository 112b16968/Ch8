import skimage.io as io
import skimage.color as co
import numpy as np
import skimage
import matplotlib.pyplot as plt

image = io.imread("gull_gray.png")

r , c = image.shape
x , y = np.mgrid[0:r , 0:c].astype("float32")
p1 = np.sin(x/3 +y/5) + 1.0
p2 = np.sin(x/5 +y/1.5) + 1.0
p3 = np.sin(x/6 +y/6) + 1.0
a = image + p1
b = image + p2
c = image + p3

plt.subplot(1, 3, 1)
plt.imshow(a , cmap='gray')
plt.title("A")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(b , cmap='gray')
plt.title("B")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(c , cmap='gray')
plt.title("C")
plt.axis('off')
plt.show()