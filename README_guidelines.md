# Guidelines

Hier findet ihr die aktuellen Guidelines für eine gemeinsame standardisierte Verwendung von GitHub und Latex.

Eine ganz wichtige Aussage zuerst: bei der Benennung von Dateien, Ordnern oder Referenzen NIE Umlaute oder Leerzeichen verwenden!
Das kann sonst zu Problemen bei involvierten Programmen führen.
Weiterhin wegen Latex besser Minus "-" anstatt Unterstrich "_" verwenden.

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
Es gibt Vorlagen für diverse Dinge in den zwei Master-Dokumenten Handbuch.tex und Mechaniken.tex vor Beginn des Dokuments.
Diese sind natürlich auskommentiert, können sich aber an die entsprechende Stelle kopiert werden.
Um mit einem Mal einen ganzen Block an Zeilen auszukommentieren oder zu entkommentieren, kann man einfach die Tastenkombination Strg + t/u verwenden (macOS entsprechend).

### Zeilen und Absätze
Die .tex Dokumente sollen auch für unsere Augen so weit wie möglich angenehm zu lesen und damit zu bearbeiten sein. Daher:
-> ausreichend Leerzeilen einfügen, um Bereiche voneinander abzugrenzen (Leerzeilen werden idR vom Kompiler komplett ignoriert)


Damit in Github beim Kommentieren auch in Text-Bergen zu einzelnen Zeilen Anmerkungen gemacht werden können:
-> soweit möglich in etwa nur einen Satz pro Zeile im .tex Dokument machen


### Leerzeichen
Keine Leerzeichen um einen "bis" Strich -
Keine Leerzeichen um einen Schrägstrich /
Leerzeichen vor/nach abgekürzten Symbolen wie $, §

Das geschütztes Leerzeichen: die Tilde ~ (darf nicht von Leerzeichen umgeben sein!), sorgt dafür, dass die Leerstelle nicht zum Umbruch am Zeilenende verwendet wird.
So wird auch F.~Schiller nie getrennt.
Dadurch würde auch die Zahl nie von ihrer Einheit getrennt, _aber wir verwenden für Einheiten das Paket siunitx (siehe unten).

Leerzeichen müssen korrekterweise zwischen Abkürzungen wie bei "z. B." oder "A 9" da das für "zum Beispiel" oder "Autobahn 9" steht.
Hier sinnvollerweise auch das geschützte Leerzeichen verwenden.


### Darstellung von Zahlen
Wir verwenden das Paket siunitx zur verbesserten Darstellung von Zahlen, Wertebereichen und Einheiten.
Wer sich darüber genauer informieren will, findet eine gute übersichtliche Erläuterung unter https://www.namsu.de/Extra/pakete/Siunitx.html.
Das Wichtigste:
- Bei reinen Zahlen reicht es zu beachten, dass ein Komma (kein Punkt) verwendet wird (Das Paket kann trotzdem gerne verwendet werden).
- Für Einheiten die Befehle des Paketes verwenden: \SI{ZAHL}{EINHEIT} oder \SIrange{ZAHL}{ZAHL}{EINHEIT}: 2 kg oder 2 kg bis 7 kg
Die Eingabe der Einheit sollte am Besten nicht "kg" sein, sondern das Makro "\kilogram". 
Damit ist sichergestellt, dass immer die gleiche Schreibweise (groß/klein etc) genutzt wird.
Die wichtigsten sind: \g \kg \m \km \s \l \hour \minute bzw. dann als Präfix \giga \mega \kilo \hecto \deci \centi \milli etc (Motiv sollte klar sein, Google hilft)


### Wie markiere ich einen zu referenzierenden Bereich? (Label)
Zuerst muss ich dem Ort, den ich referenzieren möchte, ein Label zuweisen, damit Latex weiß, wohin es verweisen soll. 
Zu Beachten ist, dass das Label immer _NACH dem Punkt erfolgen muss, auf den ich verweise, damit das System das versteht.
Diese Punkte sind: \caption{} für Abbildungen & Tabellen und \chapter{} oder \section{} u.ä. für Überschriften.
Dies sind übrigens auch die besonderen Befehle, die Latex dazu nutzt, die Verzeichnisse zu erstellen.

Beim Erstellen von Labeln müssen wir uns an __Vorgaben halten:
- keine Leerzeichen
- keine Sonderzeichen
- keine Umlaute
- keine Unterstriche (nutze ein Minus -)

Weiterhin verwenden wir die folgenden gemeinsamen __Richtlinien:
- ein Tabellen-Label beginnt immer mit "tab:"
- ein Abbildungs-Label beginnt immer mit "fig:"
- ein Überschriften-Label beginnt immer mit "sec:"
- Namen tauchen nicht in Labeln auf, da sie sich bis zum Ende ändern könnten. Wir beziehen sie auf die Funktion dahinter: \label{planet} anstatt \label{Andar}.

Stelle ich fest, dass ich ein bestehendes Label anpassen muss (es folgt nicht den Richtlinien, ist nicht eindeutig etc), kann ich zuvor per Rechtsklick -> Nutzungen feststellen herausfinden, ob und wo dieses Label schon referenziert wird.
Dann kann ich ganz einfach alle auf einmal ändern.
Übrigens: wird ein Label doppelt verwendet, erscheint es zur Warnung in einer anderen Farbe (in TexStudio Windows lila anstatt grün).

### Wie referenziere ich korrekt?
Im Allgemeinen kürzen wir ab:
- Abbildung zu Abb. 
- Tabelle zu Tab.
- Seite zu S. (nur wenn nicht Teil des Fließtextes, beachte hier Lesefluss)

1. Ich möchte nur auf das __Element verweisen: \ref{label}
-> nun wird an dieser Stelle die Zahl des Elements eingefügt:
- für eine Überschrift ihre Nummerierung (1.3.5 oder 3.4 ...)
- für eine Tabelle oder eine Abbildung die Nummer (1.2 oder 5.9 ...)
Verwendung: "wie in Abb. \ref{fig:planet} dargestellt" -> "wie in Abb. 1.5 dargestellt"

2. Ich möchte nur auf die __Seite des Elements verweisen: \pageref{label}
-> nun wird an dieser Stelle die Seite eingefügt, auf der das Element erscheint
Verwendung (selten): "Wie auf Seite \pageref{sec:planet} gezeigt" -> "Wie auf Seite 10 gezeigt"
Hinweis: Bitte nur verwenden, wenn es wirklich als nötig angesehen wird. 
Solange man sich die PDF mit einem vernünftigen PDF-Viewer ansieht, kann man auf die Links klicken und wird direkt dort hingebracht.

3. Ich möchte auf nur auf den __Namen des Elements verweisen: \nameref{label}
-> nun wird hier der Name des Elements angezeigt
- für eine Überschrift die tatsächliche Überschrift wie sie in den geschweiften Klammern steht
- für eine Tabelle oder eine Abbildung die caption
Verwendung (häufig): "hier auf \nameref{sec:planet}" -> "hier auf Andar"
Tipp: damit könnt ihr auch den Namen in den Fließtext einbinden, ohne dass ihr wissen müsst, wie er am Ende lauten wird. 
ABER jedes Mal entsteht dort ein Link, der dich zur entsprechenden Seite bringt. 
Sinnvollerweise erfolgt diese Verlinkung also einmal in Textblöcken und nur an Stellen, an denen ein Link sinnvoll ist.

4. Ich möchte __sowohl auf den __Namen als auch die __Seite verweisen: \npref{label}
-> dieser Befehl ist vor Beginn des Dokumentes in Master.tex selbsterstellt und erklärt
Verwendung (seltener): "hier auf \npref{sec:planet}" -> "hier auf Andar (S. 10)"
Hinweis wie bei 2. zur Seite. Dies ist allerdings im Gegensatz zu 2. sinnvoll, immer bei der *ersten Referenz im Kapitel* zu verwenden.
Denn das Handbuch liegt ja mal ggf. gedruckt vor und man kann dann keinem Hyperlinks folgen.

5. Ich möchte __sowohl auf das __Element als auch die __Seite verweisen: \epref{label}
-> genau wie bei Nummer 4.
Verwendung (seltener): "wie in Abb. \epref{fig:planet} dargestellt" -> "wie in Abb. 1.5 (S. 8) dargestellt"
Hinweis wie bei Nummer 4.