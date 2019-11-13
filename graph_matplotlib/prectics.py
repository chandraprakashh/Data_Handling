# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:33:57 2019

@author: BSDU ADMIN
"""

import matplotlib.pyplot as plt


###################### plot and scatter chart ####################
x = [2,4,6,8,10]
y = [1,2,3,4,5]

plt.xlabel("members")
plt.ylabel("family")
plt.title("home")

plt.xlim(2,10)
plt.ylim(1,5)
plt.grid(True)

plt.scatter(x,y,)
plt.plot(x,y, color='Green', linestyle='dashed')

plt.savefig("scatter.jpg")
plt.show(x,y)


plt.scatter(x, y,label="marker") # o  .  , x  +  v  ^  <  >  s d 
plt.legend(numpoints=1)



##################### pie chart ########################################

labels = ("maths","hindi","english","sinces")
sizes = [14,30,25,11]
colors = ("green","red","blue","orange")
explode = [0,0,0.1,0]

plt.pie(sizes,explode=explode,colors=colors, autopct="%1.2f%%",shadow=True,startangle=90)
plt.axes('equal')
plt.show()


###################### bar  chart #####################################################

cal = ("manish","virat","rohit","sikhar")
mal = [2,1,3,1]

#pal =[0,11,22,33]

plt.bar(cal,mal)
#plt.xticks(pal,cal, fontsize = 10)

plt.title("cricket")
plt.xlabel("name")
plt.ylabel("number of team")
plt.show()

##################### histogram charts #########################################################

time = [39,43,54,65,175,34,45]
time.sort()
print (time)
plt.hist(time)

############################# numpy code random #################################


import numpy as np
import matplotlib.pyplot as plt
data = np.random.randn(1000)
plt.hist(data)

############################# numpy code arange

import matplotlib.pyplot as plt
import numpy as np

data = np.arange(0.1,2.0,0.1)
s = 3 + np.sin(8*np.pi*data)
plt.plot(data, s, color="red")


################################ checs bord code ######################################


import matplotlib.pyplot as plt
import numpy as np

from PIL import Image 
img = np.ones((8,8))

img = [
     [1,0,1,0,1,0,1,0],
     [0,1,0,1,0,1,0,1],
     [1,0,1,0,1,0,1,0],
     [0,1,0,1,0,1,0,1],
     [1,0,1,0,1,0,1,0],
     [0,1,0,1,0,1,0,1],
     [1,0,1,0,1,0,1,0],
     [0,1,0,1,0,1,0,1]
     ]
print(type(img))
plt.imshow(img, "gray")






















