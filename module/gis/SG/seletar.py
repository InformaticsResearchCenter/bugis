from blacksheep import json
import shapefile

def airport(gis):
    w = shapefile.Writer('static/shp/seletar/airport')
    w.field('name', 'C')
    w.point(gis.longitude, gis.latitude) 
    w.record(gis.name)
    w.close()
    msg='shp file '+gis.name+' was created'
    return json({"message" : msg})

def getairport(param):
    sf = shapefile.Reader("static/shp/seletar/airport")
    rec = sf.record(int(param))
    return json(
        {
            "shapeType" : sf.shapeType,
            "len shapes" : len(sf),
            "fields" : sf.fields,
            "record" : str(rec)
        }
    )
