"""
Übung 4: Klassen importieren & Datentypen verstehen

Aufgabe:
In dieser Übung lernst du:
1. Wie man Klassen aus anderen Dateien importiert
2. Dass Klassen eigene Datentypen sind

Schritte:
1. Importiere die Klasse Song aus dem File 05_song.py
2. Erstelle mehrere Song-Objekte mit Titeln und Interpreten deiner Wahl
3. Verwende type() um zu zeigen, dass jedes Objekt vom Typ 'Song' ist
4. Vergleiche mit anderen Datentypen (String, Integer, Liste)

💡 Tipps:
- from dateiname import Klassenname importiert eine Klasse
- type(variable) gibt den Datentyp zurück
- Jede Klasse ist ein eigener Datentyp!
- Du kannst beliebige Songs, Titel und Interpreten verwenden!

Beispiel Ergebnis:
=== Datentypen Vergleich ===
Text: <class 'str'>
Zahl: <class 'int'>
Liste: <class 'list'>
Song1: <class '__main__.Song'>
Song2: <class '__main__.Song'>

Beide Songs haben denselben Datentyp: True

=== Song Playlist ===
▶️ Song 'Summer Vibes' wird gespielt...
▶️ Song 'Neon Lights' wird gespielt...
▶️ Song 'Ocean Wave' wird gespielt...
"""

# TODO: Importiere die Klasse Song aus 05_song
# from 05_song import Song
from song import Song

# TODO: Erstelle verschiedene Variablen mit unterschiedlichen Datentypen
# text = "Hallo"
# zahl = 42
# liste = [1, 2, 3]

text= "Hallo"
zahl = 42
liste = [1,2,3]

print(type(text))
print(type(zahl))
print(type(liste))


# TODO: Erstelle 3 Song-Objekte mit Titeln und Interpreten deiner Wahl
song1=Song("Africa","Toto")
song2=Song("Africa","Toto")
print(type(song1))


liste_songs=[song1,song2]
print(liste_songs[0].titel)

song3=Song("Fein", "Travis Scott")
liste_songs.append(song3)

song4=Song("brick by brick", "Imagency")
liste_songs.append(song3)

for song in liste_songs:
    print(song.titel)

# TODO: Zeige die Datentypen mit type()
# print("=== Datentypen Vergleich ===")
# print(f"Text: {type(text)}")
# print(f"Zahl: {type(zahl)}")
# print(f"Liste: {type(liste)}")
# print(f"Song1: {type(song1)}")
# print(f"Song2: {type(song2)}")
# print()


# TODO: Vergleiche, ob zwei Songs denselben Datentyp haben
# print(f"Beide Songs haben denselben Datentyp: {type(song1) == type(song2)}")
# print()


# TODO: Spiele alle Songs ab
# print("=== Song Playlist ===")
