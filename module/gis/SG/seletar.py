from blacksheep import json
import shapefile

def airport(gis):
    w = shapefile.Writer('static/shp/seletar/airport')
    w.field('name', 'C')
    w.point(gis.value.longitude, gis.value.latitude) 
    w.record(gis.value.name)
    w.close()
    msg='shp file'+gis.value.name+' created'
    return json({"message" : msg})