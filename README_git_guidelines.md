# Git Guidelines

## Pullen

Mit Pullen bezeichnet man das Kopieren eines remote-Repositorys (also der online Version des Projekt-Ordners) auf den eigenen Rechner.
Änderungen, die am remote-Repository gemacht werden, werden nicht automatisch auch bei euch durchgeführt. Dafür müsst ihr erneut pullen.
Ihr könnt immer nur einen Branch des Repository (also eine Version des Projekt-Ordners) pullen (s.unten).

## Branches

Ein Branch stellt immer eine Version eines git-Repositorys dar.
Dabei können beliebig viele Branches gleichzeitig in einem Repository existieren. 
Ein neuer Branch ist erst einmal eine Kopie eines bereits bestehenden Branches.
Wenn der neue Branch bearbeitet wird, bleibt der alte jedoch unberührt.
Der default-Branch nennt sich "master" und darf nicht angefasst werden. Von diesem werden normalerweise die Kopien erstellt.
Es gibt lokale und remote Branches. Es kann also sein, dass ein Branch nur bei euch lokal existiert, aber nicht online. Oder umgekehrt.

Die Namen von Branches werden grundsätzlich in der Form "thema/abschnitt" geschrieben.
Mögliche Themen wären dabei "charakter", "quest", "religion", "welt" etc. (Wenn ihr euch unsicher seid ob ihr den Begriff verwendet könnt: Fragt nach!)
Ein Beispiel Branch wäre: "charakter/herbertDerSchmied" oder "religion/religionsgebäude".

## Commits

Gemachte Änderungen in einem lokalen git-Repository werden immer zu sogenannten Commits zusammen gefasst.
Wann alle gemachten Änderungen commitet werden entscheidet der Autor, es sollte aber immer am Ende eines logischen Abschnittes auch ein Commit gemacht werden.

Die Commitnachrichten, mit denen die Commits versehen werden,werden grundsätzlich der Übersicht halber in der Form "AKTION: [was habe ich getan]" geschrieben.
Aktionen sind dabei immer in der Befehlsform zu benutzen.
Mögliche Aktionen sind "FÜGE HINZU", "ENTFERNE" und "UPDATE".
Ein Beispiel Commit wäre: "ENTFERNE: Kapitel 1" oder "FÜGE HINZU: Sagen & Legenden".

## Pushen

Wenn man gemachte Commits veröffentlichen (also online stellen) möchte tut man dies über einen Push. Der Push lädt die gemachten Commits im aktuellen Branch ins remote-Repository hoch.

## Pull Requests

Um die gemachten Änderungen innerhalb eines gepushten Branches dem Ursprungsbranch (normalerweise dem master) hinzuzufügen muss ein Pull Request erstellt werden.
Damit wird beim jeweiligen Administrator angefragt, ob die gemachten Änderungen in Ordnung sind. Wenn dieser dies bestätigt (approved) kann der Branch dem Ursprungsbranch wieder hinzugefügt werden (gemerged werden).
Damit sind die Änderungen im master angekommen und somit vollendet.

All diese Aktionen bilden einen Kreis, der für jede Komponente wiederholt wird.
