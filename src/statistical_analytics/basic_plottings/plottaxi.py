# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

font = {'family' : 'serif',  
        'weight' : 'bold',  
        'size'   : 20,  
        }  

fig, ax = plt.subplots()
N = 6
y = [12.748986, 12.450521, 13.351609, 13.071789, 13.158262, 12.324935]

ind = np.arange(N) 
width = 0.6      

ticks = ax.set_xticks([0.3, 1.3, 2.3, 3.3, 4.3, 5.3])  
labels = ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']) 

ticks = ax.set_yticks([10, 11, 12, 13, 14])   

plt.title('Yellow Taxi Pickups in NYC\n', fontdict = font)

plt.suptitle('First half year in 2015', fontsize = 16)

plt.ylabel('Pickups (in million)', fontsize = 16)

plt.plot(ind+0.3, y, '-ok', linewidth = 2.2)

plt.xlim(-0.4,6)
plt.ylim(10,14)
ax.yaxis.grid(True)

rects1 = plt.bar(ind, y, width, color='w', hatch="/")

fig.savefig('taxi_months.png',dpi = 200, bbox_inches='tight')
