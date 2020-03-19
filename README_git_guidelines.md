# Git Guidelines

## Fetchen

Damit überprüft das Programm, ob online Änderungen im aktuelln Branch vorliegen. 
Sollte dem so sein, wird das angezeigt und ihr bekommt die Option, diese Änderungen zu "pullen" (siehe unten).
Dies solltet ihr IMMER für den Master ausführen, bevor ihr einen neuen Branch erstellt.


## Pullen

Mit Pullen bezeichnet man das Kopieren eines remote-Repositorys (also der online Version des Projekt-Ordners) auf den eigenen Rechner.
Änderungen, die am remote-Repository gemacht werden, werden nicht automatisch auch bei euch durchgeführt. Dafür müsst ihr erneut pullen.
Ihr könnt immer nur einen Branch des Repository (also eine Version des Projekt-Ordners) pullen (s.unten).

--> Ihr zieht/kopiert euch die aktuelle Version des Projekts auf euren Rechner.


## Branches

Ein Branch stellt immer eine Version eines git-Repositorys dar.
Dabei können beliebig viele Branches gleichzeitig in einem Repository existieren. 
Ein neuer Branch ist erst einmal eine Kopie eines bereits bestehenden Branches.
Wenn der neue Branch bearbeitet wird, bleibt der alte jedoch unberührt.
Der default-Branch nennt sich "master" und darf nicht angefasst werden. Von diesem werden normalerweise die Kopien erstellt.
Es gibt lokale und remote Branches. Es kann also sein, dass ein Branch nur bei euch lokal existiert, aber nicht online. Oder umgekehrt.

--> Beispiel: ihr bekommt einen Aufgabenzettel überreicht. Das Original liegt beim Lehrer, der euch Kopien davon gegeben hat. Jeder kann nun also seinen Zettel nehmen und was anderes drauf und dazu schreiben. Die Zettel der anderen bleiben davon unberührt.

Die Namen von Branches werden grundsätzlich in der Form "thema/abschnitt" geschrieben.
Mögliche Themen wären dabei "charakter", "quest", "religion", "welt" etc. (Wenn ihr euch unsicher seid ob ihr den Begriff verwendet könnt: Fragt nach!)
Ein Beispiel Branch wäre: "charakter/herbertDerSchmied" oder "religion/religionsgebäude".


## Commits

Gemachte lokale Änderungen werden immer zu sogenannten Commits zusammen gefasst.
Commits sind Versionen, also auf diese Schritte lässt sich später diese einzelne Datei auch zurücksetzen.
An welchem Punkt alle bisher gemachten Änderungen zusammengefasst und "commitet" werden, entscheidet der Autor.
Es sollte aber immer am Ende eines logischen Abschnittes auch ein Commit gemacht werden.
Warum? Denn man kann sich online von jeder einzelnen Datei ansehen, welche Commits gemacht wurden. 
Und da diese kommentiert werden müssen (siehe unten), kann man so bei jeder Datei die Entwicklung und vor allem die letzten Schritte nachlesen.
Also lieber kleinschrittiger committen, als zu großschrittig!

Zu jedem Commit MUSS es eine Nachricht geben. 
Die Commitnachrichten werden grundsätzlich der Übersicht halber in der Form "AKTION: [was habe ich getan]" geschrieben.
Aktionen sind dabei immer in der Befehlsform zu benutzen.

### Mögliche Aktionen sind "FÜGE HINZU", "ENTFERNE", "UPDATE".

Ein Beispiel Commit wäre: "ENTFERNE: Kapitel 1" oder "FÜGE HINZU: Sagen & Legenden".
Das Feld mit der Beschreibung kann dann zusätzliche Informationen enthalten.

--> Beispiel: ihr teilt die Aufgaben des Zettels in eurer Gruppe auf und du bekommst Aufgabe 1 und 2: Nennen Sie zwei Tiere(1)/Pflanzen(2). Während du dich über mögliche Antworten beliest, ist es dir überlassen, ab wann du die anderen über deine bisherigen Lösungen informierst. In der Präsentation vor deiner Gruppe würdest du kurz (wenn auch ausführlicher) sagen, was du gemacht hast... "FÜGE HINZU: Antworten Frage 1" -> Biene, Elefant. "FÜGE HINZU: Antworten Frage 2" -> "Eiche, Gänseblümchen"
Angenommen, die Aufgaben sind komplexer und du musst etwas erläutern. Dann möchtest du deine Lösung den anderen auch schrittweise erklären können. Deshalb strukturierst du deine Antwort auch in einzelne Einheiten (Commits), die du nacheinander deiner Gruppe erklärst.


## Pushen

Wenn man gemachte Commits veröffentlichen (also online stellen) möchte tut man dies über einen Push. 
Der Push lädt die gemachten Commits im aktuellen Branch ins remote-Repository (zum GutHub-Server) hoch.

--> Beispiel: ihr habt alle Aufgaben bearbeitet und gebt die Blätter an den Lehrer ab.


## Pull Requests

Nachdem man alle obigen Schritte (commit, push) abgeschlossen hat, kann man nun fordern, dass die gemachten Änderungen innerhalb des Branches dem Ursprungsbranch (normalerweise dem master) hinzugefügt werden sollen.
Dazu muss eine Pull Request erstellt werden (nur auf der Website möglich).
Damit wird beim jeweiligen Administrator angefragt, ob die gemachten Änderungen in Ordnung sind. Wenn dieser bestätigt (approved), kann der Branch mit dem Ursprungsbranch wieder gemerged (verschmolzen) werden.
Damit sind die Änderungen im master angekommen und somit vollendet: sie werden sozusagen offiziell für angenommen und richtig erklärt und tauchen zukünftig auch bei allen anderen in allen Versionen auf.

All diese Aktionen bilden einen Kreis, der für jede Komponente wiederholt wird.


## Handhabung
Das klingt jetzt erstmal alles sehr umständlich, aber nur, weil es zur Erläuterung dient.
Der Handlungskreis während der Arbeit besteht demnach aus:

1. Fetchen ung ggf. Pullen (aktuellste Versionen ran holen; über rechten Button in schwarzer Zeile)
2. ggf. neuen Branch erstellen

3. am Projekt arbeiten
-> dabei fertig bearbeitete logische Einheiten committen
Achtung: nur commits können veröffentlicht werden. Einzelne Änderungen, die nicht committet sind, werden nicht hochgeladen!
4. pushen (jedes Mal wenn die Arbeit beendet wird)

5. wenn man mit der Arbeit fertig ist, für die man den Branch geöffnet hat, dann 
Pull Request
