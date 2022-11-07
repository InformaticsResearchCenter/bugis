from module.gis.SG import seletar
from model import data

def test_seletar_airport():
    gis=data.Gis(103.87068815153685,1.4155690028533765,"seletar airport")
    assert seletar.airport(gis).status == 200

def test_seletar_getairport():
    assert seletar.getairport(0).status == 200