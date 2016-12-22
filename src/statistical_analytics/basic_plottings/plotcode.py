# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

font = {'family' : 'serif',  
        'weight' : 'bold',  
        'size'   : 20,  
        }  

fig, ax = plt.subplots()
N = 6
y = [1.953801, 2.263620, 2.259773, 2.280837, 2.695553, 2.816895]

ind = np.arange(N) 
width = 0.6      

ticks = ax.set_xticks([0.3, 1.3, 2.3, 3.3, 4.3, 5.3])  
labels = ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']) 

ticks = ax.set_yticks([1.5, 2.0, 2.5, 3.0])   

plt.title('Uber Pickups in NYC\n', fontdict = font)

plt.suptitle('First half year in 2015', fontsize = 16)

plt.ylabel('Pickups (in million)', fontsize = 16)

plt.plot(ind+0.3, y, '-ok', linewidth = 2.2)

plt.xlim(-0.4,6)
plt.ylim(1.5,3.0)
ax.yaxis.grid(True)

rects1 = plt.bar(ind, y, width, color='w', hatch="/")

fig.savefig('uber_months.png',dpi = 200, bbox_inches='tight')
