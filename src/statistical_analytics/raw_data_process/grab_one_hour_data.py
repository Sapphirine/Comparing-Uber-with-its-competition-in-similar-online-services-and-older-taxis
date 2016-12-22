inputfile = open('01-20.txt', 'r')
outputfile = open('01-20_19-20.txt', 'w')
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
     if s == 19:
         outputfile.write(line)

inputfile.close()
outputfile.close()

