from Standort import *
import pandas

class Daten():
    
    def __init__(self, pDateipfad):
        self.dateipfad = pDateipfad
        self.daten = []
        with open(self.dateipfad) as datei:
            daten = datei.readlines()
            for zeile in daten:
                data = zeile.split(';') 
                tempStandort = Standort((float(data[0]),float(data[1])),data[2].split('\n')[0])
                self.daten.append(tempStandort)
                pass
            pass                           
        pass
    
    def gibStandort(self, pPosition):
        return self.daten[pPosition]
    
    def gibKoordinaten(self, pPosition):
        return self.daten[pPosition].gibKoordinaten()
    
    def gibUhrzeit(self, pPosition):
        return self.daten[pPosition].gibUhrzeit()
    
    def anzahlStandorte(self):
        return len(self.daten)

    def gibAlleKoordinatenAus(self):
        koordinaten = []
        for punkt in self.daten:
            koordinaten.append(self.gibKoordinaten(punkt))
            pass
        pass
    pass