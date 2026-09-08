# OOP -  Objektorientierte Programmierung
# wir bilden Zustände/Dinge aus der
# realen Welt in unserem Programm ab

class Mathe:
    # initialisieren
    def __init__(self, zahl1, zahl2):
        self.zahl1 = zahl1
        self.zahl2 = zahl2

    def add(self):
        print("Addition:", self.zahl1 + self.zahl2)
        
    def subtract(self):
        print("Subtraction:", self.zahl1 - self.zahl2)
        
    def multiply(self):
        print("Multiplication:", self.zahl1 * self.zahl2)
        
    def divide(self):
        print("Division:", self.zahl1 / self.zahl2)

# bitte die Klasse fertig entwickeln
# und zwei Objekte erzeugen (Instanzen erzeugen):
# 'rechnung1' und 'rechnung2'

rechnung1 = Mathe(1, 2)
rechnung1.add()
rechnung1.multiply()

rechnung2 = Mathe(56464, 1000)
rechnung2.subtract()
rechnung2.divide()


