# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

font = {'family' : 'serif',  
        'weight' : 'bold',  
        'size'   : 16,  
        }  
        
N = 6
mMeans = (0.0249, 0.152, 0.258, 0.0344, 0.0242, 0.022)


ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, mMeans, width, color='w')

wMeans = (0.029, 0.162, 0.287, 0.0283, 0.0292, 0.0232)
rects2 = ax.bar(ind+width, wMeans, width, color='w', hatch="\\")

# add some
ax.set_ylabel('Unit Distance(Calculated from location)')
ax.set_title('Travel Distance Comparison\n', fontdict = font)
ax.set_xticks(ind+width)
ax.set_xticklabels( ('R1', 'R2', 'R3', 'R4', 'R5', 'R6') )

ax.legend( (rects1[0], rects2[0]), ('Jan', 'June') )
ax.yaxis.grid(True)

plt.xlim(-0.3,6)
#plt.ylim(5,25)

plt.show()
fig.savefig('Distance_comparison.png',dpi = 200, bbox_inches='tight')
