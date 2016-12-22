'''
The code is used to grab related data in one typical day
'''
inputfile = open('yellow_tripdata_2015-01.csv', 'r')

# name the output file according to the day pick, here we pick date 20
outputfile = open('01-20.txt', 'w')
day_table = {}

i = 0
for line in inputfile:
     
     if i == 0:
          i += 1
          continue
     
     lines = line.split(',')
     data_info = lines[1].split(' ')
     day = data_info[0].split('-')

     s = (int)(day[2])
     # date 20
     if s == 20:
         outputfile.write(line)

inputfile.close()
outputfile.close()

