import fiona
import json
from pyproj import Proj, transform

features = []

def convertCoord(x1, x2):
    inProj = Proj(init='epsg:2263')
    outProj = Proj(init='epsg:4326')
    x1,y1 = x1*0.3048006096012192, y1*0.3048006096012192
    x2,y2 = transform(inProj,outProj,x1,y1)
    return (x2,y2)

with fiona.collection("~/taxi_zones/taxi_zones.shp", "r") as source:
    for feat in source:
        if (feat['geometry']['type'] == 'Polygon'):
            coordinates = feat['geometry']['coordinates'][0]
            for i in range(0,len(coordinates)):
                coordinates[i] = convertCoord(coordinates[i][0],coordinates[i][1])
        else:
            multi_coodr = feat['geometry']['coordinates']
            for i in range(0,len(multi_coodr)):
                coordinates = multi_coodr[i][0]
                for j in range(0,len(coordinates)):
                    coordinates[j] = convertCoord(coordinates[j][0],coordinates[j][1])
       
        features.append(feat)

    geojson = {
    "type": "FeatureCollection",
    "features": features
    }


with open("geo.geojson", "w") as f:
    f.write(json.dumps(geojson))




