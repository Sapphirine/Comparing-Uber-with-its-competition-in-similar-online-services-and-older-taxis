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
y = np.array(y)*1.0


y1 = [2948498,2155327,1583063,1167038,863910,800476,1715864,2886801,3509314,3592012,3519526,3654461,3816040,3776017,3896784,3709936,3211052,3831576,4625970,4777537,4518114,4473727,4308976,3764083]
y1 = np.array(y1)*1.0

ind = np.arange(N) 
width = 0.6      

ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

ticks = ax.set_xticks([0.3, 4.3, 8.3, 12.3, 16.3, 20.3])  
labels = ax.set_xticklabels(['00', '04', '08', '12', '16', '20']) 




plt.title('Uber vs Yellow Taxi on Pickups \n', fontdict = font)
plt.suptitle('Distribution in every hour', fontsize = 16)
plt.ylabel('Pickups proportion', fontsize = 16)

plt.plot(ind+0.3, y/y.sum(), '-ok', linewidth = 2.2, label = 'Uber Distr.')
plt.plot(ind+0.3, y1/y1.sum(), '--ok', linewidth = 2.2, label = 'Taxi Distr.')

print min(y1/y1.sum())
print min(y/y.sum())
plt.xlim(-0.4,24)
#plt.ylim(0.01, 0,07)

ax.legend(loc='upper left', shadow=True)

fig.savefig('taxi_time.png',dpi = 200, bbox_inches='tight')
