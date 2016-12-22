month_table = {}
month_num = []
for k in range(1,2):
    namestr = "yellow_tripdata_2015-0"+str(k)+".csv"
    
    
    inputfile = open(namestr,'r')
    i = 0
    for line in inputfile:

        i = i + 1

        if i == 1:
            continue
        
        lines = line.split(',')
        time_info = lines[1].split(' ')
        time = time_info[1].split(':')

        s = (int)(time[0])
        if not month_table.has_key(s):
            month_table[s] = 1
        else:
            month_table[s] = month_table[s] + 1

    month_num.append(i-1)
    inputfile.close()
    
    print str(k) + " finished!"
    

print month_num
for i in month_table:
    print month_table[i]
