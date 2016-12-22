# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

font = {'family' : 'serif',  
        'weight' : 'bold',  
        'size'   : 20,  
        }  

fig, ax = plt.subplots()
N = 24
y = [2948498,2155327,1583063,1167038,863910,800476,1715864,2886801,3509314,3592012,3519526,3654461,3816040,3776017,3896784,3709936,3211052,3831576,4625970,4777537,4518114,4473727,4308976,3764083]
ind = np.arange(N) 
width = 0.6      

ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

ticks = ax.set_xticks([0.3, 4.3, 8.3, 12.3, 16.3, 20.3])  
labels = ax.set_xticklabels(['00', '04', '08', '12', '16', '20']) 

ax.set_yticks([1000000, 2000000, 3000000, 4000000, 5000000])  
ax.set_yticklabels(['1', '2', '3', '4', '5']) 

#ticks = ax.set_yticks([1.5, 2.0, 2.5, 3.0])   

plt.title('Yellow Taxi Pickups in NYC\n', fontdict = font)

plt.suptitle('Distribution in every hour', fontsize = 16)

plt.ylabel('Pickups (in million)', fontsize = 16)

plt.plot(ind+0.3, y, '-ok', linewidth = 2.2)
plt.xlim(-0.4,24)
plt.ylim(0,5000000)

rects1 = plt.bar(ind, y, width, color='w', hatch="/")

fig.savefig('taxi_time.png',dpi = 200, bbox_inches='tight')
