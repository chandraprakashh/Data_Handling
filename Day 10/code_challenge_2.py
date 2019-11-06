# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:32:39 2019

@author: BSDU ADMIN
"""

import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

img = np.ones((9, 9))

img = [
       [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
       [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
       [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
       [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
       [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
       [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
       [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
       [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
       ]

print(type(img))


plt.imshow(img, "gray")


img_file = Image.fromarray(img, "I")
img_file.save("Smile.png")
img_file.show()