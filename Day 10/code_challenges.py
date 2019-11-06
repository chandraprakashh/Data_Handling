# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:00:36 2019

@author: BSDU ADMIN
"""

import numpy as np
import matplotlib.pyplot as plt



from PIL import Image
x = np.ones((8,8))

x =[
        [1,0,1,0,1,0,1,0],
       [0,1,0,1,0,1,0,1],
       [1,0,1,0,1,0,1,0],
       [0,1,0,1,0,1,0,1],
       [1,0,1,0,1,0,1,0],
       [0,1,0,1,0,1,0,1],
       [1,0,1,0,1,0,1,0],
       [0,1,0,1,0,1,0,1],

]


print(type(x))


plt.imshow(x, "gray")


img_file = Image.fromarray(x, "I")
img_file.save("Smile.png")
img_file.show()

