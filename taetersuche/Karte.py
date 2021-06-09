import folium
from Standort import *
from IPython.display import display
from folium.plugins import HeatMap, FastMarkerCluster, FeatureGroupSubGroup

class Karte(folium.Map):
    
    def __init__(self, pMittelpunkt, *pInteraktiv):
        super().__init__(location = pMittelpunkt)
        if(len(pInteraktiv) == 0):
            self.interaktiv = False
            self.schicht = folium.plugins.FastMarkerCluster(data = [])
            pass
        else:
            self.interaktiv = pInteraktiv[0]
            pass
        self.schichten = [folium.plugins.FastMarkerCluster(data=[]), []]
        pass
    
    def zeichneHeatmappunktEin(self, pKoordinaten):
        heatmap = folium.plugins.HeatMap(data = pKoordinaten, name = 'Heatmap')
        if(self.interaktiv):
            self.schichten.append([heatmap, 'Heatmap'])
            pass
        else:
            heatmap.add_to(self)
            pass
        return self

    # Methode von zeichneHetmapEin die das Erstellen der Liste direkt integriert
    def zeichneHeatmapEin(self, pDaten):
        koordinaten = []
        for punkt in pDaten.daten:
            koordinaten.append(punkt.gibKoordinaten())
            pass
        heatmap = folium.plugins.HeatMap(data = koordinaten, name = 'Heatmap')
        if(self.interaktiv):
            self.schichten.append([heatmap, 'Heatmap'])
            pass
        else:
            heatmap.add_to(self)
            pass
        return self
    
    # Methode zum einzeichnen eines Standorts. Wenn Standort bereits vorhanden, so soll geclustert werden mit FastMarkerCluster
    def zeichneStandortEin(self, pStandort, pFarbe = 'red', *pPerson):
        koordinaten = pStandort.gibKoordinaten()
        uhrzeit = pStandort.gibUhrzeit()
        uhrzeittool = folium.Tooltip(uhrzeit)
        farbe = folium.Icon(color = pFarbe)
        # hier richtigen Marker einfügen
        standort = folium.Marker(location = koordinaten, tooltip = uhrzeittool, icon = farbe)
        if(self.interaktiv):
            if(len(pPerson) == 0):
                print('Bei einer interaktiven Karte muss der Standort einer Person zugewiesen werden. Übergib den Namen der Person hinten in der Parameterliste.')
                pass
            # Marker soll zu "Schicht" hinzugefügt werden und falls schon vorhanden geclustert werden
            else:
                name = pPerson[0]
                i = 0
                gefunden = False
                while(i < len(self.schichten) and not gefunden):
                    if(name == self.schichten[i][1]):
                        gefunden = True
                        pass
                    i = i + 1
                    pass
                if(gefunden):
                    standort.add_to(self.schichten[i-1][0])
                    pass
                else:
                    temp = folium.plugins.FastMarkerCluster(data = [])
                    self.schichten.append([temp, name])
                    standort.add_to(self.schichten[len(self.schichten)-1][0])
                    pass
                pass
            pass
        else:
            standort.add_to(self.schicht)
            self.schicht.add_to(self)
            pass
        return self

    # Bearbeitet
    def zeichneStandorteEin(self, pDaten, pFarbe='green', *pPerson):
        for punkt in pDaten.daten:
            self.zeichneStandortEin(punkt, pFarbe = pFarbe)
            
            pass
        return self
    
    def verbindeStandorte(self, pStart, pZiel, pFarbe='blue', *pPerson):
        koordinaten = [pStart.gibKoordinaten(), pZiel.gibKoordinaten()]
        linie = folium.PolyLine(locations = koordinaten, color = pFarbe)
        if(self.interaktiv):
            if(len(pPerson) == 0):
                print('Bei einer interaktiven Karte muss der Standort einer Person zugewiesen werden. Übergib den Namen der Person hinten in der Parameterliste.')
                pass
            else:
                name = pPerson[0]
                i = 0
                gefunden = False
                while(i < len(self.schichten) and not gefunden):
                    if(name == self.schichten[i][1]):
                        gefunden = True
                        pass
                    i = i + 1
                    pass
                if(gefunden):
                    linie.add_to(self.schichten[i-1][0])
                    pass
                else:
                    temp = folium.plugins.FastMarkerCluster(data = [], name = name)
                    self.schichten.append([temp, name])
                    linie.add_to(self.schichten[len(self.schichten)-1][0])
                    pass
                pass
            pass
        else:
            linie.add_to(self)
            pass
        return self

    # Neu um alle Standorte miteinander zu verbinden
    def verbindeAlleStandorte(self, pDaten, pFarbe ='blue', *pPerson):
        anzahlStandorte = pDaten.anzahlStandorte()
        for i in range(0,anzahlStandorte-2):
            self.verbindeStandorte(pStart=pDaten.daten[i], pZiel=pDaten.daten[i+1], pFarbe = pFarbe)
            pass
        return self
        

    def zeigeKarteAn(self):
        if(self.interaktiv):
            for schicht in self.schichten:
                schicht[0].add_to(self)
                pass
            folium.LayerControl().add_to(self)
            pass
        else:
            self.schicht.add_to(self)
            folium.LayerControl().add_to(self)
            pass
        return self