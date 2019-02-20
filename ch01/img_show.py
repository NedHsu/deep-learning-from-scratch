# coding: utf-8
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('../dataset/lena.png') # 載入影像（請設定適當路徑）
plt.imshow(img)

plt.show()