""" 
Aufgabe 04-01: OS, Dateien lesen

Öffnen Sie die Datei "Teilen_und_Herrschen.txt" im Lese-Modus.
Für jede Zeile der Datei, ermittlen sie die Anzahl der Wörter und geben Sie die 
Zeile aus.

Der Text enthält Sonderzeichen, z.B. Umlaute. Eventuell werden diese Zeichen bei
der Ausgabe inkorrekt angezeigt. Geben Sie beim Öffnen der Datei das zusätzliche
Argument encoding="utf8" an, um die Sonderzeichen korrekt zu verarbeiten.

Bonus: Wenn Sie die Aufgabe lösen, fällt Ihnen vielleicht auf, dass die Ausgabe
des Dateiinhalts zwischen je zwei Zeilen eine Leerzeile einfügt. Warum ist das
so? Können Sie Stringmethoden anwenden, um diesen zusätzlichen Zeilenumbruch zu
umgehen?

"""

filename = "Teilen_und_Herrschen.txt"
filename = filename.encode("utf8")    
with open(filename, "r") as infile:         #len befehl #in liste splitten, dann wird ausgezählt
    for line in infile: 
        line = line.split()
        print(len(line))
                                            #oder so
filename = "Teilen_und_Herrschen.txt"
filename2 = filename.encode("utf8")
with open(filename2, "r") as infile:
    for line in infile:
        line = line.split()
        print(len(line))

        