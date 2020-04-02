# Guidelines

Hier findet ihr die aktuellen Guidelines für eine gemeinsame standardisierte Verwendung von GitHub und Latex.

Eine ganz wichtige Aussage zuerst: bei der Benennung von Dateien, Ordnern oder Referenzen NIE Umlaute oder Leerzeichen verwenden!
Das kann sonst zu Problemen bei involvierten Programmen führen.

## GitHub
### Branch Namen
Die Namen von Branches werden grundsätzlich in der Form "Bereich/Thema" geschrieben:
-> Bereich: Kapitel oder Abschnitt. 
Soll zeigen, in welchem .tex Dokument ihr herumschreibt bzw. wenn dieses mehrere Themen umfasst, in welchem Abschnitt ihr bleibt 
(Religion, Wirtschaft, Lebensformen, etc)

-> Thema: z.B. die niedrigste Überschrift unter der ihr bleibt oder eine Zusammenfassung für das, woran ihr arbeitet 
(Götter, Menschenarten, Genetik, Rollenbild)


### Commit-Nachrichten
Die Commit-Nachrichten werden grundsätzlich der Übersicht halber in der Form "AKTION: [was habe ich getan]" geschrieben. 
Aktionen sind dabei immer in der "tue dies"-Befehlsform (ohne das tun) zu benutzen. 
Bedenke: die Nachricht taucht nur an den markierten Dokumenten auf: die Nachricht muss also in diesem Zusammenhang verständlich sein. 
Am Dokument über Magie musst du nicht darauf hinweisen, dass es um Magie geht, sondern kannst davon ausgehen, dass deine Nachricht darauf bezogen wird. 
In dem Zusammenhang kann man von "Arten erweitert" sprechen ohne dass es mit den Lebensformen verwechselt werden könnte!

-> Mögliche Aktionen sind "FÜGE HINZU", "ENTFERNE", "UPDATE", "KORRIGIERE", "ORDNE UM"
(z.B. FÜGE HINZU: böse Götter; UPDATE: Götter ausgefeilt; KORRIGIERE: Rechtschreibung; ORDNE UM: Sektion A hinter Sektion D geschoben)



## Latex
### Zeilen und Absätze
Die .tex Dokumente sollen auch für unsere Augen so weit wie möglich angenehm zu lesen und damit zu bearbeiten sein. Daher:
-> ausreichend Leerzeilen einfügen, um Bereiche voneinander abzugrenzen (Leerzeilen werden idR vom Kompiler komplett ignoriert)


Damit in Github beim Kommentieren auch in Text-Bergen zu einzelnen Zeilen Anmerkungen gemacht werden können:
-> soweit möglich in etwa nur einen Satz pro Zeile im .tex Dokument machen


### Leerzeichen
Leerzeichen müssen korrekterweise zwischen Abkürzungen wie bei "z. B." oder "A 9" da das für "zum Beispiel" oder "Autobahn 9" steht.
Keine Leerzeichen um einen "bis" Strich -
Keine Leerzeichen um einen Schrägstrich /
Leerzeichen vor/nach abgekürzten Symbolen wie $, §

Das geschütztes Leerzeichen: die Tilde ~ (darf nicht von Leerzeichen umgeben sein!), sorgt dafür, dass die Leerstelle nicht zum Umbruch am Zeilenende verwendet wird.
So wird auch F.~Schiller nie getrennt.
Dadurch würde auch die Zahl nie von ihrer Einheit getrennt, _aber wir verwenden für Einheiten das Paket siunitx (siehe unten).


### Darstellung von Zahlen
Wir verwenden das Paket siunix zur verbesserten Darstellung von Zahlen, Wertebereichen und Einheiten.
Wer sich darüber genauer informieren will, findet eine gute übersichtliche Erläuterung unter https://www.namsu.de/Extra/pakete/Siunitx.html.
Das Wichtigste:
- Bei reinen Zahlen reicht es zu beachten, dass ein Komma (kein Punkt) verwendet wird (Das Paket kann trotzdem gerne verwendet werden).
- Für Einheiten die Befehle des Paketes verwenden: \SI{ZAHL}{EINHEIT} oder \SIrange{ZAHL}{ZAHL}{EINHEIT}: 2 kg oder 2 kg bis 7 kg
Die Eingabe der Einheit sollte am Besten nicht "kg" sein, sondern das Makro "\kilogram". 
Damit ist sichergestellt, dass immer die gleiche Schreibweise (groß/klein etc) genutzt wird.
Die wichtigsten sind: \g \kg \m \km \s \l \hour \minute bzw. dann als Präfix \giga \mega \kilo \hecto \deci \centi \milli etc (Motiv sollte klar sein, Google hilft)


