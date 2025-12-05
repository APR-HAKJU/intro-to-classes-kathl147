"""
Übung 3: Song mit Listen

Aufgabe:
Erstelle eine Klasse `Song` mit:
- Konstruktor mit Parametern: titel (String) und interpreten (Liste, z.B. ["Artist1", "Artist2"])
- Methode interpret_hinzufuegen(name) mit Parameter:
  - Fügt einen neuen Interpreten zur Liste hinzu
  - Gibt aus "🎤 {name} wurde hinzugefügt"
- Methode zeige_info() ohne Parameter:
  - Zeigt Titel und alle Interpreten an
- Methode anzahl_interpreten() ohne Parameter:
  - Gibt die Anzahl der Interpreten zurück
- Methode play() ohne Parameter:
  - Gibt aus "▶️ Song '{titel}' wird gespielt..."

Erstelle einen Song mit einem Titel und 2 Interpreten deiner Wahl,
zeige die Info, füge einen weiteren Interpreten hinzu, zeige die Anzahl und die Info nochmal.
Spiele dann den Song ab.

💡 Tipps:
- self.interpreten.append(name) fügt ein Element zur Liste hinzu
- len(self.interpreten) gibt die Anzahl der Elemente zurück
- Mit einer for-Schleife kannst du alle Interpreten ausgeben
- Du kannst beliebige Interpreten und Titel verwenden!

Beispiel Ergebnis:
🎵 Song: Summer Vibes
   Interpreten: DJ Max, Sarah Sound
🎤 Beat Producer wurde hinzugefügt
👥 Anzahl Interpreten: 3
🎵 Song: Summer Vibes
   Interpreten: DJ Max, Sarah Sound, Beat Producer
▶️ Song 'Summer Vibes' wird gespielt...
"""

# TODO: Erstelle hier die Klasse Song
class Song:
    def __init__(self,titel,interpreten,):
        self.titel=titel
        self.interpreten=interpreten
        print(f"Neuer Song mit Titel {self.titel} und Interpreten {self.interpreten} wurde erstellt.")
    
    def zeige_info(self):
        print(f"Neuer Song mit Titel {self.titel} und Interpreten {self.interpreten} wurde erstellt.")

    def interpret_hinzufügen(self, neuer_interpret):
        self.interpreten.append(neuer_interpret)
        print(f"{neuer_interpret} wurde hinzugefügt")
        print(f"Alle Interpreten: {self.interpreten}")

    def anzahl_interpreten(self):
        return len(self.interpreten)
    
    def play(self):
        print(f"{self.titel} wird gespielt.")


# TODO: Erstelle einen Song mit einem Titel und 2 Interpreten deiner Wahl
song1=Song("Die with a smile",["Bruna Mars", "Lady Gaga"])
song2=Song("Carry you home",["Alex Warren"])
song3=Song("Perfect",["Ed Sherran", "Lady Gaga"])

# TODO: Zeige die Song-Info
song1.zeige_info()

# TODO: Füge einen weiteren Interpreten hinzu
song1.interpret_hinzufügen("DJ Lenzi")
song1.interpret_hinzufügen("DJ Obdocha")

# TODO: Zeige die Anzahl der Interpreten
nr_artists=song1.anzahl_interpreten()
print(nr_artists)
print(song1.anzahl_interpreten) #Das gleiche wie oben, nur wird das Ergebnis nicht zwischengespeichert.

# TODO: Zeige die Song-Info erneut
song1.zeige_info

# TODO: Spiele den Song ab
song1.play()