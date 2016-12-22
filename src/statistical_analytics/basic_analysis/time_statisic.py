'''
This code do time statistic on data of a typical date
'''
inputfile = open('01-20.txt', 'r')
day_table = {}

i = 0
for line in inputfile:
     
     if i == 0:
          i += 1
          continue
     
     lines = line.split(',')
     data_info = lines[1].split(' ')
     day = data_info[1].split(':')

     s = (int)(day[0])
     if not day_table.has_key(s):
         day_table[s] = 1
     else:
         day_table[s] = day_table[s] + 1

print len(day_table)

for i in range(0,24):
    print day_table[i]

inputfile.close()

