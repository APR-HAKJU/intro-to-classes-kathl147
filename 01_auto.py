"""
Übung 1: Auto-Klasse mit Methoden

Aufgabe:
Erstelle eine Klasse `Auto` mit:
- Konstruktor mit Parametern: marke, modell, kilometerstand
- Methode fahren() ohne Parameter: Erhöht den Kilometerstand um 100
  und gibt aus: "Gefahren! Neuer Stand: X km"
- Methode zeige_info() ohne Parameter: Gibt Marke, Modell und 
  Kilometerstand aus

Erstelle ein Auto und lass es dreimal fahren.

💡 Tipp:
- In fahren() verwendest du self.kilometerstand += 100
- Denke daran, dass Methoden immer self als ersten Parameter haben!

Erwartetes Ergebnis:
VW Golf, Kilometerstand: 50000 km
Gefahren! Neuer Stand: 50100 km
Gefahren! Neuer Stand: 50200 km
Gefahren! Neuer Stand: 50300 km
VW Golf, Kilometerstand: 50300 km
"""

# TODO: Erstelle hier die Klasse Auto
class Auto:
    def __init__(self, marke, modell, kilometerstand): #Konstruktor
        self.marke=marke
        self.modell=modell
        self.kilometerstand=kilometerstand
    
    def zeige_info(self): #Eine Funktion in einer Klasse ist eine Methode
        print(f"{self.marke} hat Kilometerstand {self.kilometerstand}")
    
    def fahren(self):
        self.kilometerstand=self.kilometerstand + 100
        print(f"Gefahren! Neuer Stand {self.kilometerstand} ")
  

# TODO: Erstelle ein Auto-Objekt (z.B. VW Golf mit 50000 km)
auto1=Auto("VW","Golf", 50000)
auto1.zeige_info()
auto1.fahren()
auto1.fahren()

auto2=Auto("Audi", "A3", 400000)
auto2.zeige_info()
auto2.fahren()

auto3=Auto("BMW", "X6", 13)
auto3.zeige_info()
auto3.fahren()

# TODO: Zeige die Info


# TODO: Lass das Auto dreimal fahren


# TODO: Zeige die Info erneut