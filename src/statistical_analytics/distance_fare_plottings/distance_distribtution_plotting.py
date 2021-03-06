import matplotlib.pyplot as plt
import math

def get_distance(name, table):
     inputfile = open(name, 'r')
     i = 0
     for line in inputfile:
     
          if i == 0:
               i += 1
               continue
     
          lines = line.split(',')

          aa = (float)(lines[5])
          ab = (float)(lines[6])
          ba = (float)(lines[9])
          bb = (float)(lines[10])

          s = math.sqrt((aa-ba)*(aa-ba)+(ab-bb)*(ab-bb))

          if s < 0.0001 or s > 1:
               continue
     
          idnum = (int)(lines[-1])

          if table.has_key(idnum):
               table[idnum].append(s)
          else:
               table[idnum] = [s]
     inputfile.close()
     return table
     
faretable1 ={}
faretable6 ={}
faretable1 = get_distance('01-20_19-20.csv' ,faretable1)
faretable6 = get_distance('06-20_19-20.csv' ,faretable6)

fig, ax = plt.subplots()

font = {'family' : 'serif',  
        'weight' : 'bold',  
        'size'   : 16,  
        }      
 

plt.boxplot([faretable1[2], faretable6[2],faretable1[3], faretable1[3], faretable1[4], faretable6[4], faretable1[6], faretable6[6], faretable1[7], faretable6[7],faretable1[9], faretable6[9]],
            positions = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17], widths = 0.5)
plt.ylim(0,0.16)

ax.set_ylabel('Unit Distance(Calculated from location)')
ax.set_title('Travel Distance Distribution Comparison\n', fontdict = font)

ticks = ax.set_xticks([1.5, 4.5, 7.5, 10.5, 13.5, 16.5])  
labels = ax.set_xticklabels(['R1', 'R2', 'R3', 'R4', 'R5', 'R6']) 

fig.savefig('Travel_Distance_Distribution_Comparison.png',dpi = 200, bbox_inches='tight')
