inputfile = open('uber-raw-data-janjune-15.csv', 'r')

day_table = {}
time_table = {}

i = 0
for line in inputfile:

     if i == 0:
          i = i + 1
          continue
     
     lines = line.split(',')
     data_info = lines[1].split(' ')

     # month distribution
     day = data_info[0].split('-')
     s = (int)(day[1])
     #print s
     if not day_table.has_key(s):
         day_table[s] = 1
     else:
         day_table[s] = day_table[s] + 1
         
     # time distribution
     time = data_info[1].split(':')
     s = (int)(time[0])
     #print s
     if not time_table.has_key(s):
         time_table[s] = 1
     else:
         time_table[s] = time_table[s] + 1

print
print len(day_table)

for i in range(1,7):
    print day_table[i]

print len(time_table)

for i in range(0,24):
    print time_table[i]



inputfile.close()

