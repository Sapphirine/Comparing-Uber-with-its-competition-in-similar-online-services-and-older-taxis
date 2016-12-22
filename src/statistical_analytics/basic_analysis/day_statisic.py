'''
This code is used to offer statistic of daily taxi service usage in 2015.01
'''

inputfile = open('yellow_tripdata_2015-01.csv', 'r')
day_table = {}

i = 0
for line in inputfile:
     
     # ignore first line
     if i == 0:
          i += 1
          continue
     
     lines = line.split(',')
     data_info = lines[1].split(' ')
     day = data_info[0].split('-')

     # focus on the day
     s = (int)(day[2])
     if not day_table.has_key(s):
         day_table[s] = 1
     else:
         day_table[s] = day_table[s] + 1

print len(day_table)

#std output
for i in range(1,32):
    print day_table[i]

inputfile.close()

