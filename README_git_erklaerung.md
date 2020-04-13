# Git Erklärung

## Fetchen (= Überprüfen)

Damit überprüft das Programm, ob online Änderungen im aktuellen Branch (siehe unten) vorliegen. 
Sollte dem so sein, wird das angezeigt und ihr bekommt die Option, diese Änderungen zu "pullen" (siehe unten).
Dies solltet ihr IMMER für den Master ausführen, bevor ihr einen neuen Branch erstellt.


## Pullen (= lokale Dateien aktualisieren -> Gegenstück zum Pushen)

Mit Pullen bezeichnet man das Kopieren eines remote-Repositorys (also der online Version des Projekt-Ordners) auf den eigenen Rechner.
Änderungen, die am remote-Repository (aka online) gemacht wurden, werden nicht automatisch auch bei euch durchgeführt. 
Das heißt, wenn der master verändert wurde, dann müsst ihr euch immer wieder die aktuelle Version anfordern.
In eurem Branch ist das nur der Fall, wenn jemand explizit in diesem Änderungen gemacht hat. 
Dafür müsstet ihr diesen dann auch erneut pullen, wenn das aufgetreten ist.

Ihr könnt gleichzeitig immer nur einen Branch des Repository (also eine Version des Projekt-Ordners) pullen.
Ihr könnt aber gleichzeitig mehrere auf eurem Rechner haben und über GitHub Desktop zwischen den verschiedenen Branches wechseln. 

--> Ihr zieht/kopiert euch die aktuelle Version des Projekts auf euren Rechner.


## Branches (= eine (Arbeits-)Version)

Ein Branch stellt immer eine Version eines git-Repositorys dar.
Dabei können beliebig viele Branches gleichzeitig in einem Repository existieren. 
Ein neuer Branch ist erst einmal eine Kopie eines bereits bestehenden Branches.
Wenn der neue Branch bearbeitet wird, bleibt der alte jedoch unberührt.
Der default-Branch nennt sich "master" und darf nicht angefasst werden. Von diesem werden normalerweise die Kopien erstellt.
Es gibt lokale und remote (online) Branches. Es kann also sein, dass ein Branch nur bei euch lokal existiert, aber nicht online. Oder umgekehrt!

--> Beispiel: ihr bekommt einen Aufgabenzettel überreicht. Das Original liegt beim Lehrer, der euch Kopien davon gegeben hat. 
Jeder kann nun also seinen Zettel nehmen und was anderes drauf und dazu schreiben. Die Zettel der anderen bleiben davon unberührt.

Die Namen von Branches werden grundsätzlich in der Form "thema/abschnitt" geschrieben.
Mögliche Themen wären dabei "charakter", "quest", "religion", "welt" etc. (Wenn ihr euch unsicher seid ob ihr den Begriff verwendet könnt: Fragt nach!)
Ein Beispiel Branch wäre: "charakter/herbertDerSchmied" oder "religion/religionsgebäude".
Die aktuellen Guidelines findet ihr in der Readme_Guidelines.md.


## Commits (= zusammenhängende Einheit an Änderungen)

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
Mögliche Aktionen sind z.B. "FÜGE HINZU", "ENTFERNE", "UPDATE". 
Ein Beispiel Commit wäre: "ENTFERNE: Kapitel 1" oder "FÜGE HINZU: Sagen & Legenden".
Das Feld mit der Beschreibung kann dann zusätzliche Informationen enthalten.
Die aktuellen Guidelines findet ihr in der Readme_Guidelines.md.

--> Beispiel: ihr teilt die Aufgaben des Zettels in eurer Gruppe auf und du bekommst Aufgabe 1 und 2: Nennen Sie zwei Tiere(1)/Pflanzen(2). 
Während du dich über mögliche Antworten beliest, ist es dir überlassen, ab wann du die anderen über deine bisherigen Lösungen informierst. 
In der Präsentation vor deiner Gruppe würdest du kurz (wenn auch ausführlicher) sagen, was du gemacht hast... 
"FÜGE HINZU: Antworten Frage 1" -> Biene, Elefant. "FÜGE HINZU: Antworten Frage 2" -> "Eiche, Gänseblümchen"
Angenommen, die Aufgaben sind komplexer und du musst etwas erläutern. Dann möchtest du deine Lösung den anderen auch schrittweise erklären können. 
Deshalb strukturierst du deine Antwort auch in einzelne Einheiten (Commits), die du nacheinander deiner Gruppe erklärst.


## Pushen (= online Dateien aktualisieren -> Gegenstück zum Pullen)

Wenn man gemachte Commits veröffentlichen (also online stellen) möchte tut man dies über einen Push. 
Der Push lädt die gemachten Commits im aktuellen Branch ins remote-Repository (zum GutHub-Server) hoch.
So könntet ihr zB. auch zusammen an einer Version arbeiten, wenn ihr eh nicht zeitgleich arbeiten könnt. 
Oder ihr könntet an verschiedenen Rechnern am Projekt arbeiten und nach dem Pushen sind eure Inhalte je auf Beiden verfügbar.

--> Beispiel: ihr habt alle Aufgaben bearbeitet und gebt die Blätter an den Lehrer ab.


## Pull Requests (= Anfrage zur Veröffentlichung)

Nachdem man die obigen Schritte (commit, push) abgeschlossen hat, kann man nun eine Forderung stellen.
Die gemachten Änderungen innerhalb des Branches sollen dem Ursprungsbranch (dem master) hinzugefügt werden.
Das heißt in unserem Projekt, dass die neuen Inhalte damit "anerkannt" werden und im öffentlichen Handbuch stehen.
Dazu muss eine Pull Request erstellt werden. Dies ist nur auf der Website möglich (aber ein Button in der App leitet euch da hin).
Damit wird angefragt, ob die gemachten Änderungen in Ordnung sind. 

Wenn ihr eine Pull Request auf der Website erstellt, könnt ihr folgende Dinge machen:
- einen aussagekräftigen Titel wählen, damit die anderen wissen, worum es geht
- anfordern, wer sich das ansehen soll (Reviewer anfordern).
- Assignees auswählen. Fügt euch selbst dort ein.
- ein Label hinzufügen, das eurem Thema entspricht. "Allgemein" bezieht sich auf alles, was nicht mit dem tatsächlichen Inhalt des Handbuchs zu tun hat.
- ein Projekt zuordnen. Zum Zeitpunkt der Erstellung dieses Guides lautet der Name "Inhalt".
- Kommentieren, was ihr eigentlich alles so gemacht habt. 
In der Beschriebung/dem Kommentar könnt ihr auch die Nummer eines Issues eintragen (im Stil von #1), dessen Bearbeitung ihr damit als abgeschlossen erklärt.
Das führt dazu, dass es im Projekt automatisch als erledigt markiert wird, sobald euer Branch mit dem master verschmolzen wurde.

Nun können alle Mitglieder des Lore-Teams sich die Änderungen ansehen und ggf. kommentieren oder sogar fordern, dass etwas geändert wird.
Wenn mindestens zwei Leute bestätigen (approven) und alle Änderungs-Forderungen erfüllt (resolved) sind, dann kann ein Mitglied des Lore-Teams die Verschmelzung vornehmen.
Verschmelzen aka Mergen heißt, dass dieser Branch mit dem Master wieder gemerged wieder zusammengeführt wird.
Damit sind die Änderungen im master angekommen und somit vollendet: sie werden sozusagen offiziell für angenommen und richtig erklärt und tauchen zukünftig auch bei allen anderen Versionen auf.

Achtung: fordert jemand eine Änderung ein, so muss GENAU DIESE Person sich dann auch wieder die neue Änderung ansehen und nun bestätigen (approven).
Die einzige Person, die alle Beschränkungen umgehen kann, ist der Administrator.

Achtung: wenn es viele Leute sind, die parallel arbeiten, kann es sein, dass jemand "schneller" mit seiner Arbeit war.
Dann kommt es dazu, dass seine Änderungen vor deinen dem Master hinzugefügt werden.
Das führt dazu, dass sich der aktuelle Stand des Masters von dem Stand, als du deine Kopie erstellt hast, unterscheidet.
Tritt dieser Fall ein, kann GitHub wegen der PDF zickig werden. Um das Aufzulösen solltest du Folgendes tun, wenn du mit deiner Arbeit komplett fertig bist:
Während du dich in GitHub Desktop in deinem Branch befindest, klicke oben in der Leiste (Windows: direkt am Fenster, Mac: oben am Bildschirm) auf "Branch".
Dort wähle "Update from Master". Wenn alle neuen Dinge im Master andere Dateien betreffen als die, die du verändert hast, dann geht das ganz fix und ohne weitere Anmerkungen.
Sollte es einen Konflikt geben, weil jemand auch in der Datei geschrieben hat, mit der du arbeitest, wirst du aufgefordert, das Problem händisch zu lösen. 
Wende dich dazu an uns. Es ist nicht schwer, aber einfacher per Gespräch zu klären.
Das wird im Übrigen immer für die PDF auftreten. Für diese müsst ihr aber nur anklicken, dass ihr die PDF aus dem Master übernehmen wollt. 
Denn solche Dokumente ("binary files": pdf, png, jpeg, ...) kann das System nicht in Teilen verstehen und nimmt sie nur im Ganzen.



## Handhabung
All diese Aktionen bilden einen Kreis, der für jede Komponente wiederholt wird.

Das klingt jetzt erstmal alles sehr umständlich, aber nur, weil es zur Erläuterung dient.
Der Handlungskreis während der Arbeit besteht demnach aus:

1. Fetchen ung ggf. Pullen (aktuellste Versionen ran holen; über rechten Button in schwarzer Zeile)
2. ggf. neuen Branch erstellen

3. am Projekt arbeiten
-> dabei fertig bearbeitete logische Einheiten committen
Achtung: nur commits können veröffentlicht werden. Einzelne Änderungen, die nicht committet sind, werden nicht hochgeladen!
4. pushen (jedes Mal wenn die Arbeit beendet/pausiert wird)

Wenn man mit der Arbeit fertig ist, für die man den Branch geöffnet hat, dann
5. Master in den eigenen Branch mergen
6. Pull Request stellen
7. Discord: lore-todo: Link posten und das Lore Team zum angucken auffordern


## Work in Progress
Sind bereits Anmerkungen von anderen gewünscht, so kann man auch eine Pull Request erstellen, wenn man noch nicht fertig ist. 
Weißt du nämlich direkt zur Erstellung der Request, dass du noch nicht mit dem Branch fertig bist, kannst du die Anfrage beim grünen Button "Create Pull Request" über den grünen Pfeil als "Draft Pull Request" erstellen.
Bis du den Branch nicht als bereit markierst, kann ihn keiner (versehentlich) mergen, auch wenn schon zwei Leute ihr Approve gegeben haben.

Weiterhin ist es gut, zu Verdeutlichung vor den Namen ein "WIP" für Work in Progress einzufügen.
Dann kannst du auch schon andere auffordern, sich die ersten Punkte deiner Arbit anzusehen und ggf. zu korrigieren oder diskutieren.
Alles, was man in seinem Branch dann weiter bearbeitet, committet und pushed wird automatisch mit hinzugefügt und eure Pull Request aktualisiert sich!
Wenn du später soweit bist, kannst du das WIP aus dem Namen streichen und bestätigen, dass du bereit bist.

Möchtest du rückwirkend aus einer normalen Request eine Draft Request machen, so musst du auf einen Link klicken.
Der versteckt sich beim Bereich "Reviewers" hinter "Still in progress? Convert to draft".