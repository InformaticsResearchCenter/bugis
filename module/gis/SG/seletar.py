from blacksheep import json
import shapefile

def airport(gis):
    w = shapefile.Writer('static/shp/seletar/airport')
    w.field('name', 'C')
    w.point(gis.value.longitude, gis.value.latitude) 
    w.record(gis.value.name)
    w.close()
    msg='shp file '+gis.value.name+' was created'
    return json({"message" : msg})

def getairport(param):
    sf = shapefile.Reader("static/shp/seletar/airport")
    return json(
        {
            "shapeType" : sf.shapeType,
            "len shapes" : len(sf),
            "fields" : sf.fields
        }
    )
