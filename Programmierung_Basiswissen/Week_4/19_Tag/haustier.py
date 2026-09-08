class Haustier:
    def __init__(self, rufname, art, alter, farbe, besitzer):
        self.rufname = rufname
        self.art = art
        self.alter = alter
        self.farbe = farbe
        self.besitzer = besitzer
        
    def vorstellung(self):
        print(f"Mein Name ist {self.rufname} und ich bin ein(e) {self.art}")
    
    def wemseintier(self):
        print("Ich gehöre", self.besitzer)
        
shadow = Haustier("Shadow", "Katze", 13, "schwarz", "Yasmine")
shadow.vorstellung()
shadow.wemseintier()