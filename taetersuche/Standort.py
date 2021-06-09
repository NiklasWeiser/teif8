class Standort():
    
    def __init__(self, pKoordinaten, pUhrzeit):
        self.koordinaten = pKoordinaten
        self.uhrzeit = pUhrzeit
        pass
    
    def __repr__(self):
        temp = 'Koordinaten: (' + str(self.koordinaten[0]) + ',' + str(self.koordinaten[1]) + '); Uhrzeit: ' + self.uhrzeit
        return temp
    
    def gibKoordinaten(self):
        return self.koordinaten
    
    def gibUhrzeit(self):
        return self.uhrzeit
    
    pass