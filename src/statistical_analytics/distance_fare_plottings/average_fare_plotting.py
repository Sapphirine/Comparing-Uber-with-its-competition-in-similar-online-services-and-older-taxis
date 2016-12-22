# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

font = {'family' : 'serif',  
        'weight' : 'bold',  
        'size'   : 16,  
        }  
        
N = 6
mMeans = (22.55, 13.86, 13.19, 15.13, 15.34, 11.48)


ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, mMeans, width, color='w')

wMeans = (15.16, 12.96, 11.66, 13.20, 13.65, 11.75)
rects2 = ax.bar(ind+width, wMeans, width, color='w', hatch="\\")

# add some
ax.set_ylabel('Fare(dollars)')
ax.set_title('Taxi Fare Comparison\n', fontdict = font)
ax.set_xticks(ind+width)
ax.set_xticklabels( ('R1', 'R2', 'R3', 'R4', 'R5', 'R6') )

ax.legend( (rects1[0], rects2[0]), ('Jan', 'June') )
ax.yaxis.grid(True)

plt.xlim(-0.3,6)
plt.ylim(5,25)

plt.show()
fig.savefig('fare_comparison.png',dpi = 200, bbox_inches='tight')
