"""
Aufgabe 04-02: OS

Schreiben Sie ein Programm, das überprüft, ob eine von Ihnen per Eingabe            #abgehakt
bestimmte Datei im Downloads-Ordner bereits existiert.                              #abgehakt
Falls dies der Fall ist, geben Sie eine entsprechende Meldung aus und fordern 
Sie erneut zur Eingabe eines anderen Dateinamens auf.
Falls der Dateipfad noch nicht existiert, öffnen Sie die Datei im Schreibmodus 
und speichern Sie den Dateipfad in der Datei.

Beispiel: Eingabe existing_file.txt
Meldung: Die Datei existing_file.txt existiert bereits.
Neue Eingabe: nonexisting_file.txt
Meldung: Die Datei nonexisting_file.txt wird angelegt.

"""

filename = "testobjekt.txt"

with open(filename, "w") as outfile:
    content = input("Hier wird ein Testobjekt erstellt:\n")     #per Eingabe bestimmte Datei im Downloads Ordner 
    print(content, file=outfile)
    print("Daten wurden in der Datei " + filename + " gespeichert!")
"""
import os

filepath = input("Geben Sie einen Dateipfad ein: ")
if os.path.isfile(filepath):
    with open(filepath, "r") as infile:                     #gucken ob Datei existiert 
        for line in infile:
            print(line)
            if line == filename:
                print("Die Datei existiert bereits.")
else:
    print("Die Datei konnte nicht gefunden werden.")
"""

import os
def nonexisting_file():
    filepath = input("Geben Sie einen Dateipfad ein: ")
    if os.path.isfile(filepath):
        print("Der Pfad exisiert bereits, geben sie einen anderen Dateipfad ein.")
        nonexisting_file()
    else: 
        with open(filename, "w") as outfile:
            content = input("Die neue Datei wird angelegt:\n")     
            print(content, file=outfile)
            print("Daten wurden in der Datei " + filename + " gespeichert!")




