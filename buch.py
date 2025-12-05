# TODO: 
# Aufgabe 1:
"""Erstelle eine Klasse Buch mit folgenden Attributen:

- titel
- autor
- seiten
- gelesen (Boolean )

Erstelle zwei Bücher: Eines, das du gelesen hast (setze gelesen=True), 
und eines, das du noch nicht gelesen hast.
"""

# TODO: Aufgabe 2:
# Gib für jedes Buch eine Nachricht aus, die angibt, ob du das Buch gelesen hast oder nicht.

class Buch:
    def __init__(self, titel, autor, seiten, gelesen):
        self.titel=titel
        self.autor=autor
        self.seiten=seiten
        self.gelesen=gelesen
        print("Neues Buch wurde erstellt")

buch1=Buch(titel="Harry Potter", autor="J.K. Rowling",seiten=144,gelesen=True)
buch2=Buch(titel="Nibelungenlied",autor="Herr Unteregger",seiten=200, gelesen=False)

print(buch1.titel)

buch3=Buch("Die drei Fragezeichen", "Horst Unteregger", 300, True)

print(f"{buch1.titel} wurde gelesen: {buch1.gelesen}")
print(f"{buch2.titel} wurde gelesen: {buch2.gelesen}")
print(f"{buch3.titel} wurde gelesen: {buch3.gelesen}")