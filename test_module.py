from module.gis.SG import seletar
from model import data

def inc(x):
    return x + 1


def test_answer():
    gis=data.Gis(103.87068815153685,1.4155690028533765,"seletar airport")
    assert seletar.airport() == 5