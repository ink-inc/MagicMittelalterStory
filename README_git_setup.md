# Git/GitHub Setup
Diese README beschreibt, wie du Git auf deinem Rechner installierst und unser Projekt herunterlädst.
Relevante Voraussetzungen: du hast einen GitHub Account erstellt und bis aktiv dem Team beigetreten, zu dem du per Mail eingeladen wurdest.


## Installation
Zur Installation von GitHub auf eurem Rechner nutzt bitte GitHub Desktop von folgender Website:
https://desktop.github.com/
Das hat mehrere Gründe: Zum einen arbeiten wir alle auf die gleiche Art und Weise. Zum anderen ist das die Möglichkeit, mit einer GUI (Graphic User Interface = Grafische Benutzeroberfläche) zu arbeiten -> alle ohne Ahnung vom Programmieren und von Git können so einfach mitarbeiten.


## Einrichtung
1. Meldet euch mit dem Account an, mit dem ihr in unser Team aufgenommen wurdet.

2. Diese Seite entscheidet, was andere Leute sehen können. Achtung: JEDER Nutzer im Internet kann theoretisch unser Projekt finden und sich ansehen -> und damit auch den Namen, den ihr jetzt hier eintragt:
    a. Tragt bei Name NICHT euren tatsächlichen Namen ein, sondern nutzt ein Pseudonym, zB euren Account-Namen oder den Namen, unter dem wir euch auf Discord kennen.
    b. Lasst die kryptische E-Mail so stehen, wie sie ist.


## Herunterladen des Projekts
1. Klicke auf "Clone a Repository from the Internet..."

2. Wähle im Reiter "GitHub.com" unser Projekt (Repository) aus der Liste: "ink-inc/MagicMittelalterStory" und lege ggf. einen anderen Ordnerpfad fest. Hier wird das ganze Projekt gespeichert. Klicke nun auf "Clone".

-> habt ihr versehentlich auf das Falsche geklickt, könnt ihr es entfernen, indem ihr nun oben links auf "Current Repository" und dann mit Rechtsklick -> "Remove..." auf das Falsche klickt. 
Nun unbedingt auch den Haken in "Also move this repository to Trash" setzen.

-> die Dokumente zum Projekt findet ihr nun im entsprechenden Verzeichnis, wo ihr diese bearbeiten könnt. ABER davor weiterlesen und unbedingt das Beispiel ausführen!


## Begrifflichkeiten
An dieser Stelle bitte einmal die README_git_guidlines.md lesen. Diese erklären einige wichtige Begrifflichkeiten. Wenn euch danach noch etwas unverständlich diesbezüglich ist, dann fragt uns bitte :)

Kurz:
- Fetch = mit der online Version vergleichen: gibt es Änderungen?
- Pull = bei Änderungen diese herunterladen
- Commit = Änderungen in Paketen mit Kommentaren zusammenfassen
- Push = Alle Commits hochladen in den Online-Speicher
- Pull Request = Verschmelzen mit dem Original einfordern


## Erklärung Interface 
Im Großen und Ganzen ist die Oberfläche selbsterklärend.

Schwarzer Button 1: Current Repository
-> hier ist bereits unser Projekt ausgewählt. Wenn du nicht noch andere Projekte hast, ist diese Auswahlfläche für dich irrelevant.

Schwarzer Button 2: Current Branch
-> Hier findet ihr alle Branches, die sich lokal und "Remote", also auf den GitHub Servern, befinden.
Der Haken ist bei dem Branch, in dem ihr euch gerade befindet und arbeitet. Achtung: bevor ihr den Branch wechselt, solltet ihr keine der Dateien mehr offen haben!
Das System funktioniert nun folgendermaßen: je nachdem, welcher Branch hier ausgewählt wurde, ändern sich auch die Dateien im Ordner.
Es gibt einen versteckten Ordner ".git", in dem all das Nötige dazu gespeichert wird. Hier darfst du NICHTS VERÄNDERN, sonst funktioniert bei dir nichts mehr, wie es soll. 
Die weitere versteckte Datei ".gitignore" sorgt übrigens dafür, dass bestimmte Dateien und Ordner nicht abgeglichen werden. 
Damit werden nur die wichtigen Dateien übertragen und alles, was durch Latex oder durch euer Betriebssystem an z.B. temporären Dateien entsteht bleibt bei euch und stört nicht die anderen. 
Am Besten: unverändert lassen!

Schwarzer Button 3: Fetch origin
-> dieser Button ist für verschiedenes da. 
1. Fetchen: Ihr könnt euch damit die aktuelle online Version eures Branches (falls ihr auf mehreren Rechnern arbeitet oder zu zweit in einem Branch) und/oder des Masters (allgemein relevant) holen. 
2. Pushen: Sobald ihr commits links unten gemacht habt, könnt ihr über diesen Button auch eure bisherigen Commits zum online Server pushen.

Bitte guckt euch ansonsten aufmerksam um. 
Die meisten Möglichkeiten findet man einfach über die Befehlszeile (File, Edit, View...) oder ergeben sich während der Bearbeitung. 
Ansonsten scheut euch nicht davor, zu fragen.


## Beispiel
Damit ihr den ganzen Zyklus einmal umsetzen könnt, werdet ihr jetzt euren Namen in das Dokument mit den Autoren eintragen und online stellen.

1. Klicke auf den mittleren schwarzen Button "Current Branch"
2. Gib ein: "beispiel/name" (exakt so) und klicke auf "New Branch". 
Dieser soll auf master basieren, denn du weißt nicht, was andere in ihrem Branch machen und der master ist die aktuellste Version.
Deshalb erstellst du eine Kopie von master. Du befindest dich nun automatisch im neuen Branch.

3. Nun klicke auf "Publish branch" in der schwarzen Zeile oben ganz rechts. Dort wird später auch mal "Push" stehen.
Damit ist dein Branch nun auch offiziell online existent.

4. Öffne im Dateisystem (Explorer oder Finder) die Datei "Autoren.txt".
Der schnellste Weg wäre über GitHub Desktop: auf der rechten Seite findest du "Öffne im Explorer". 
Ansonsten weißt du ja, wo du alles abspeicherst (Standard: Eigene Dateien) und kannst alleine dort hin navigieren.

5. Schreibe deinen Namen ans Ende der Liste und speichere die Datei.
6. Gehe in GitHub Desktop: es sollte nun auf der linken Seite die geänderte Datei und auf der rechten Seite deine Änderung zu sehen sein.
7. Sieh zu, dass ein Haken bei "Autoren.txt" drin ist 
(Alles mit Haken wird im Commit zusammengefasst -> somit kann man genau festlegen, was alles die gleiche Beschreibung bekommt)
8. Gib neben deinem Profilbild die kurze knackige Beschreibung wie im README gelernt ein, z.B.:
"FÜGE HINZU: meinen Namen"
9. Optional: gib einen kurzen Beschreibungstext ein.
10. Klicke auf die blaue Fläche "Commit to beispiel/name".
11. Klicke auf "Push". Damit werden deine Änderungen hochgeladen.

12. Klicke nun auf der rechten Seite im weißen Bereich auf die blaue Fläche "Create Pull Request". Du wirst auf die Website weitergeleitet.
13. Ändere den Namen zu "Autor hinzufügen".
14. Schreibe in den Kommentar, dass du du als neues Mitglied nun deinen Namen der Autoren.txt hinzugefügt hast.
15. Wähle rechts bei "Reviewers" mind. 2 Mitglieder des Lore-Teams aus, z.B. DDeckert, Medsmiley, miafy oder MineSchokokeks.
Dadurch werden diese sogar eine E-Mail mit der Aufforderung erhalten, sich das anzusehen.
16. Darunter, bei "Assignees" wähle dich selbst aus.
17. Bei "Labels" wähle "Allgemein".
18. Klicke auf "Projects" und wähle das einzige verfügbare mit dem Namen "Inhalt" (zum Zeitpunkt der Erstellung dieser Readme).
Das packt diese Request automatisch in die Aufgabenliste des Projekts.
19. Klicke auf den großen grünen Button "Create Pull Request". 
Nun ist die Anfrage eingegangen. Wenn mindestens 2 Leute sie sich angesehen und bestätigt (approved) haben, wird deine Änderung zum master hinzugefügt und offiziell.

13. Zurück im Programm: Klicke in der Programm-Befehlszeile auf "Branch -> Delete". 
Sollte eine Frage auftauchen: Auf gar keinen Fall den Haken setzen um auch den Branch online zu löschen, sonst wird das mit der Request problematisch. 
Online wird der Branch automatisch gelöscht, wenn er in den master gemerged wurde. 
"Delete"


-> Bevor du einen Branch löscht, solltest du dir sicher sein, dass du fertig mit der Bearbeitung bist. 
Bevor du ihn löscht, kannst du auch ein weiteres Mal Dateien ändern, committen, pushen und dann eine Pull Request stellen. Sooft du möchtest. 
Aber wenn du ihn einmal gelöscht hast, dann musst du ihn entweder von online neu runterladen oder warten, bis deine Änderungen dem Master hinzugefügt wurden, um dann einen neuen Branch zu öffnen und weiter zu arbeiten!


Super, du hast jetzt erfolgreich deinen Namen hinzugefügt!


Während deiner Arbeit am Projekt solltest du am Besten jedes Mal, wenn du aufhörst, deine Commits pushen. 
Damit ist ab dann jeder, der mit dir zusammen im gleichen Branch arbeitet auf dem aktuellen Stand. 
Beziehungsweise solltest du unerwartet länger ausfallen als gedacht, hast du zumindest alles was du getan hast online gestellt und jemand anderes kann daran anknüpfen. 
Bevor du nicht gepusht hast, ist es nicht online!


## Falscher Branch!?!?!
Hast du versehentlich mit deiner Arbeit im falschen Branch begonnen (zB im Master), so ist das unkompliziert SOLANGE NOCH KEIN COMMIT ERFOLGTE. 
In dem Fall bitte uns ansprechen.
Ansonsten kannst du einfach einen neuen Branch erstellen und wirst dann danach gefragt, ob du die bisherigen Änderungen mitnehmen oder auf dem Master/falschen Branch belassen möchtest.

Auf dem Master kannst du übrigens auch nicht pushen. Also nichts von deinen Änderungen online stellen. 


## Viel Spaß beim kreativen Arbeiten!
