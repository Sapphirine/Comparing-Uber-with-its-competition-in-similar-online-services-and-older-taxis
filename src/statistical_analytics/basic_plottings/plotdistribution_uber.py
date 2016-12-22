# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

font = {'family' : 'serif',  
        'weight' : 'bold',  
        'size'   : 20,  
        }  

fig, ax = plt.subplots()
N = 24
y = [602178, 394510, 260603, 183655, 173038, 193523, 288533, 443543, 583348, 593437, 520092, 516716, 533021, 537909, 584463, 649414, 737170, 863990, 987093, 1007464, 948574, 930462, 922954, 814789]

ind = np.arange(N) 
width = 0.6      

ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

ticks = ax.set_xticks([0.3, 4.3, 8.3, 12.3, 16.3, 20.3])  
labels = ax.set_xticklabels(['00', '04', '08', '12', '16', '20']) 

ax.set_yticks([200000, 400000, 600000, 800000, 1000000, 1200000])  
ax.set_yticklabels(['0.2', '0.4', '0.6', '0.8', '1.0', '1.2']) 

#ticks = ax.set_yticks([1.5, 2.0, 2.5, 3.0])   

plt.title('Uber Pickups in NYC\n', fontdict = font)

plt.suptitle('Distribution in every hour', fontsize = 16)

plt.ylabel('Pickups (in million)', fontsize = 16)

plt.plot(ind+0.3, y, '-ok', linewidth = 2.2)
plt.xlim(-0.4,24)
plt.ylim(0,1200000)

#plt.ylim(1.5,3.0)
#ax.yaxis.grid(True)

rects1 = plt.bar(ind, y, width, color='w', hatch="/")

fig.savefig('uber_time.png',dpi = 200, bbox_inches='tight')
