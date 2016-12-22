from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SQLContext

import pandas as pd
from pandas import DataFrame

import sys
import time

conf = SparkConf().setAppName("uber")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

boroughIds = []
firstWrite = True
data_limits = 1000000

def writeToCSV():
    global boroughIds
    global firstWrite
    
    df = DataFrame(boroughIds)
    # write all the boroughIds to test2.csv, which is a temp file to store all the ids
    if(firstWrite):            
        df.to_csv(path_or_buf='test2.csv', index=False)
        firstWrite = False
    else:
        df.to_csv(path_or_buf='test2.csv', mode='a', index=False)

    boroughIds = []

def writeBoroughIdsToCSV(row):
    global boroughIds
    
    boroughIds.append(row[3])

    if(len(boroughIds) >= data_limits):
        writeToCSV()

def selectMonthData():
    df = pd.read_csv('uber-jan-jun.csv')   
    m = df.as_matrix()

    for i in range(0,m.shape[0]):
        try:
            # only considering the data within a specific month
            if(m[i][1] >= sys.argv[1] and m[i][1] <= sys.argv[2]):
                _id = int(m[i][2])
                writeBoroughIdsToCSV(m[i])
        except:
            pass

    writeToCSV()

def main():
    text_file = sc.textFile("test2.csv")
    # key: boroughId    value: how many time it appears in test2.csv
    counts = text_file.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
    df = sqlContext.createDataFrame(counts).toPandas()
    # write to a temp tsv file, which will be passed to front-end for data visualization
    df.to_csv(path_or_buf= sys.argv[3] + '.tsv', index=False, sep='\t', header=None)

if __name__ == '__main__':
    start = time.time()
    selectMonthData()
    main()
    print 'time:', time.time() - start