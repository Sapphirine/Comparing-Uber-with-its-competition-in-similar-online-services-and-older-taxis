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
y1 = [12.748986, 12.450521, 13.351609, 13.071789, 13.158262, 12.324935]

ind = np.arange(N) 
width = 0.6      

ticks = ax.set_xticks([0.3, 1.3, 2.3, 3.3, 4.3, 5.3])  
labels = ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']) 

#ticks = ax.set_yticks([1.5, 2.0, 2.5, 3.0])   

plt.title('Uber vs Yellow Taxi on Pickups \n', fontdict = font)

plt.suptitle('First half year in 2015', fontsize = 16)

plt.ylabel('Pickups in log scale', fontsize = 16)


plt.semilogy(ind+0.3, y, '-ok', linewidth = 2.2, label='Uber Data')
plt.semilogy(ind+0.3, y1, '--ok', linewidth = 2.2, label='Taxi Data')
plt.semilogy(ind+0.3, np.array(y1)/np.array(y), ':ok', linewidth = 2.2, label='TData/UData')

plt.xlim(-0.4,6)
#plt.ylim(1.5,3.0)
ax.yaxis.grid(True)

ax.legend(loc='upper left', shadow=True)
#rects1 = plt.bar(ind, y, width, color='w', hatch="/")

fig.savefig('uber_months.png',dpi = 200, bbox_inches='tight')
