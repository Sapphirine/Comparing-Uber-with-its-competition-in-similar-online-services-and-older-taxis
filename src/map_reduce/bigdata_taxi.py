from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SQLContext

import pandas as pd
from pandas import DataFrame

import shapely
import shapely.geometry
import json
import time
import sys

conf = SparkConf().setAppName("taxi")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

boroughIds = []
firstWrite = True
data_limits = 1000000

with open('geo.geojson') as data_file:
    shapefile_dict = json.load(data_file)
    shapes = []
    for shape in shapefile_dict['features']:
        # Top 10 boroughs with most services        
        # if(shape['id'] in ['161','231','234','79','230','68','163','170','246','237']):
        #     shapes.append(shapely.geometry.asShape(shape['geometry']))
        shapes.append(shapely.geometry.asShape(shape['geometry']))

print 'finished importing geojson, shapes len:', len(shapes)

def searchId(point):
    i = 1
    for shape in shapes:
        # if any polygon (borough) contains this point, return the corresponding borough Id
        if(shape.contains(point)):
            return i
        i += 1
    return -1

def writeToCSV():
    global boroughIds
    global firstWrite
    
    df = DataFrame(boroughIds)
    # write all the boroughIds to test2.csv, which is a temp file to store all the ids
    if(firstWrite):            
        df.to_csv(path_or_buf= 'test2.csv', index=False)
        firstWrite = False
    else:
        df.to_csv(path_or_buf= 'test2.csv', mode='a', index=False)

    boroughIds = []

def convertGeoLocToBoroughId(row):
    global boroughIds
    # convert Geo location to a point by giving latitude and longitude
    point = shapely.geometry.Point(float(row[5]),float(row[6]))
    boroughIds.append(searchId(point))

    if(len(boroughIds) >= data_limits):
        writeToCSV()

def convertData():
    # ex: yellow_tripdata_2015-01.csv
    # we have the first half year yellow taxi trip data of 2015
    df = pd.read_csv(sys.argv[1] + '.csv')
    m = df.as_matrix()

    for i in range(0,m.shape[0]):
        # if i % 100 == 0:
        #     print 'finished 100 lines'
        convertGeoLocToBoroughId(m[i])

    writeToCSV()

    print 'finished converting data'

def main():
    text_file = sc.textFile("test2.csv")
    # key: boroughId    value: how many time it appears in test2.csv
    counts = text_file.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
    df = sqlContext.createDataFrame(counts).toPandas()
    # write to a temp tsv file, which will be passed to front-end for data visualization
    df.to_csv(path_or_buf= sys.argv[1] + '.tsv', index=False, sep='\t', header=None)

if __name__ == '__main__':
    start = time.time()
    convertData()
    main()
    print 'time:', time.time() - start