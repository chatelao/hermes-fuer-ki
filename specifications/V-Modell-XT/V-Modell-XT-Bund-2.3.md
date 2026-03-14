V-Modell XT Bund

Das Referenzmodell für Systementwicklungsprojekte in der Bundesverwaltung
Version: 2.3

Herausgeber

Kontakt

Version

Autoren

Copyright

Das V-Modell XT Bund wird vom Informationstechnikzentrum Bund im Auftrag
des Beauftragten der Bundesregierung für die Informationstechnik
herausgegeben.

Informationstechnikzentrum Bund
V-Modell-XT-Team
E-Mail: v-modell-xt@itzbund.de

2.3

Das V-Modell XT Bund 2.3 wurde auf Basis des V-Modell XT 2.3 durch die
4Soft GmbH in Zusammenarbeit mit dem Informationstechnikzentrum Bund
erarbeitet.

Das V-Modell®XT Bund ist urheberrechtlich geschützt (© 2019 V-Modell-XT-
Bund-Autoren und andere) und ist unter der Apache License Version 2.0
freigegeben:
Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License. You may obtain a copy of the
License at http://www.apache.org/licenses/LICENSE-2.0. Unless required by
applicable law or agreed to in writing, software distributed under the License is
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
OF ANY KIND, either express or implied. See the License for the specific
language governing permissions and limitations under the License.
Von dieser Regelung ausgenommen ist die Titelseite der V-Modell-
Dokumentation. Diese ist unter einem "Creative Commons Namensnennung-
Weitergabe unter gleichen Bedingungen 3.0 Deutschland"-Lizenzvertrag
lizenziert. Um die Lizenz anzusehen, gehen Sie bitte zu
http://creativecommons.org/licenses/by-sa/3.0/de/ oder schicken Sie einen Brief
an Creative Commons, 171 Second Street, Suite 300, San Francisco, California
94105, USA.
Der Scrum Guide©2017 von Ken Schwaber and Jeff Sutherland unterliegt
der"Attribution Share-Alike"-Lizenz der Creative Commons, einsehbar unter
http://creativecommons.org/licenses/by-sa/4.0/legalcode und zusammenfassend
beschrieben unter http://creativecommons.org/licenses/by-sa/4.0/.
The Scrum Guide©2017 von Ken Schwaber and Jeff Sutherland is offered for
license under the Attribution Share-Alike license of Creative Commons,
accessible at http://creativecommons.org/licenses/by-sa/4.0/legalcode and also
described in summary form at http://creativecommons.org/licenses/by-sa/4.0/.

3

 4
 4
 4
 5
 5
 7
 8
 27
 55
 55
 188
 194
 198
 198
 215
 220
 224
 226
 226
 238
 242
 244
 246
 246
 249
 255
 273
 275
 275
 301
 311
 318
 324
 324
 341
 343

Inhaltsverzeichnis
A Einstieg in das V-Modell XT Bund

A.1 Ziele und Vorteile
A.2 Zielgruppen
A.3 V-Modell XT Bund im Überblick
A.4 Anwendungsbereich und Abgrenzung

B Konzepte und Inhalte des V-Modell XT Bund

B.1 Grundkonzepte
B.2 Inhalte des V-Modell XT Bund

C Referenz Produkte

C.1 Produkte
C.2 Produktabhängigkeiten
C.3 Produktindex
D Referenz Rollen

D.1 Projektteamrollen
D.2 Projektrollen
D.3 Organisationsrollen
D.4 Rollenindex
E Referenz Abläufe

E.1 Entscheidungspunkte
E.2 Projektdurchführungsstrategien
E.3 Ablaufbausteine
E.4 Ablaufindex
F Referenz Tailoring

F.1 Projekttypen und Projekttypvarianten
F.2 Projektmerkmale
F.3 Vorgehensbausteine
F.4 Tailoringindex
G Referenz Arbeitshilfen

G.1 Methoden und Werkzeuge
G.2 Produktvorlagen
G.3 V-Modell XT Projektassistent
G.4 Arbeitshilfenindex

H Anhang

H.1 Glossar
H.2 Abkürzungen
H.3 Literaturverzeichnis

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland














































































































4

 Einstieg in das V-Modell XT Bund

A Einstieg in das V-Modell XT Bund

Das   V-Modell   XT   ist   ein   Vorgehensmodell   zum   Planen   und   Durchführen   von   Systementwicklungs-
Projekten. Das V-Modell XT Bund (im Text kurz: "V-Modell") ist eine Anpassung des V-Modell XT an die
Bedürfnisse der Bundesverwaltung.

A.1 Ziele und Vorteile
Die Beteiligten eines Systementwicklungs-Projekts benötigen ein einheitliches und konsistentes Bild des
gemeinsamen Vorgehens, um das Projekt zum Erfolg führen zu können. Die Anwendung des V-Modells
gewährleistet dies und unterstützt zudem folgende Ziele:

➢ Kommunikation verbessern: Die Projektbeteiligten verfügen anhand detaillierter Beschreibungen
der Bestandteile des V-Modells und klarer Begriffsdefinitionen über ein gemeinsames Vokabular und
ein gemeinsames Verständnis des Vorgehens. So werden Reibungsverluste zwischen Auftraggeber
und Auftragnehmer, aber auch innerhalb von Projektteams reduziert.

➢ Projektrisiken   minimieren:   Durch   die   Vorgabe   von   Ergebnissen,   verantwortlichen   Rollen,
standardisierten Vorgehensweisen und Entscheidungspunkten im Projekt erhöht das V-Modell die
Projekttransparenz   und   verbessert   die   Planbarkeit   von   Projekten.   Planungsabweichungen   und
Risiken werden so frühzeitig erkannt.

➢ Qualität   sicherstellen:   Durch   die   Beschreibung   der   erwarteten   Inhalte   und   die   frühzeitige
Überprüfung   von   Ergebnissen   unterstützt   das   V-Modell   die   Projektmitarbeiter,   Ergebnisse
vollständig und in der gewünschten Qualität zu liefern. Qualitätsbewusstsein von Anfang an zahlt
sich mit Blick auf das gesamte Projekt und den gesamten Systemlebenszyklus aus.

➢ Bundesstandards   einhalten:   In   Systementwicklungsprojekten   des   Bundes   müssen   bestimmte
Standards   beachtet   werden,   insbesondere  WiBe  und  UfAB.   Jeder   Standard   fokussiert   einen
bestimmten Aspekt und gibt dazu detaillierte Vorgaben. Das V-Modell integriert die Standards und
stellt sie im Zusammenhang dar.

➢ Controlling-Anforderungen   erfüllen:   Die   Anwendung   des   V-Modells   entspricht   den  IuK-
Mindestanforderungen-2011  der   Rechnungshöfe   des   Bundes   und   der   Länder   in   den   Bereichen
Projektmanagement, Softwareentwicklung und Test- und Freigabeverfahren.

➢ Informationssicherheit   verbessern:  Das   V-Modell   integriert   zentrale   Aspekte   von
Informationssicherheits-Normen   wie   dem   IT-Grundschutz   in   die   Abläufe   der   Projektarbeit.
Auftraggeber   und   Auftragnehmer   werden   in   die   Pflicht   genommen,   Anforderungen   an
Informationssicherheit und Datenschutz einzubringen, entsprechende Risiken zu identifizieren und
geeignete Maßnahmen zu deren Verringerung oder Vermeidung festzulegen. Das V-Modell fordert zu
verschiedenen   Entscheidungspunkten   entsprechende   Festlegungen   und   unterstützt   dies   durch
praxisnahe Vorlagen, Checklisten und Mustertexte.

A.2 Zielgruppen
Das   V-Modell   ist   ein   Angebot   des  BfIT  an   alle   Bundesbehörden,   die   Systementwicklungs-Projekte
durchführen. Es beschreibt Projektabläufe bei Bundesbehörden als Auftraggeber und bei der Entwicklung
innerhalb einer Bundesbehörde (Inhouse-Entwicklung). Das V-Modell wendet sich an alle Projektbeteiligten,
insbesondere an Projektleiter, QS-Verantwortliche und Projektmitarbeiter.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

A.3 V-Modell XT Bund im Überblick

5

A.3 V-Modell XT Bund im Überblick
Das V-Modell ist ein Produkt-zentriertes Vorgehensmodell; die Projektergebnisse stehen also im Mittelpunkt.
Es definiert die Struktur und die Inhalte dieser Ergebnisse und beschreibt, wie die einzelnen Ergebnisse
aufeinander   aufbauen   und   voneinander   abhängen.   Ein   Rollenmodell   kapselt   Kompetenzen   von   und
Anforderungen an Projektbeteiligte und bestimmt ihre Verantwortung oder Mitwirkung bei der Erstellung
der Projektergebnisse. Das V-Modell gibt eine Reihe von Entscheidungspunkten (Meilensteinen) vor, denen
Projektergebnisse zugeordnet sind. Es fordert an diesen Entscheidungspunkten eine Fortschrittskontrolle und
eine Entscheidung über den weiteren Projektverlauf.

Abbildung 1: V-Modell im Überblick

Das Entwicklungsvorgehen (gelb-blaues "V" in Abbildung 1) ist eingebettet in ein Managementmodell zur
Steuerung   des   Projekts.   Neben   dem   eigentlichen   Projektmanagement   enthält   es   Vorgaben   zur
Qualitätssicherung, zum Umgang mit Problemen und Änderungen im Projektverlauf und zur Vorhaltung von
Projektergebnissen   (Konfigurations-Management).   Das   V-Modell   ist   dabei   auf   ein   iteratives   Vorgehen
ausgelegt, bei dem der Entwicklungszyklus mehrmals durchlaufen wird. Dadurch können technische Risiken
frühzeitig erkannt und die Anwenderzufriedenheit durch zeitnahe Reaktionen verbessert werden.

Das V-Modell unterscheidet zwischen einem behördeninternen Projekt und der Beauftragung eines externen
IT-Dienstleisters   bzw.   IT-Dienstleisters   des   Bundes.   Behördeninterne   Projekt   werden   innerhalb   eines  V-
Modell-Projekts durchgeführt. Bei der Beauftragung eines IT-Dienstleisters erfolgt eine Aufteilung in zwei
getrennte  Projekte  (eines   auf   der  Auftraggeber-   und eines  auf  der  Auftragnehmerseite).  Hierbei   legt  der
Auftraggeber (AG) die Anforderungen fest und prüft die Ergebnisse, die der Auftragnehmer (AN) entwickelt.
Das V-Modell regelt das Zusammenspiel der beiden Projekte in der AG/AN-Schnittstelle. Behördeninterne
Projekte benötigen diese Regelungen nicht und kommen daher mit einem schlankeren Satz an V-Modell-
Bestandteilen aus.

Das V-Modell kann zu Beginn eines Projekts an die konkrete Projektsituation angepasst werden (Tailoring).
Mit dem V-Modell-XT-Projektassistenten können ein Projekt-spezifisches Vorgehensmodell samt Vorlagen
für die erwarteten Ergebnisse erzeugt und ein erster grober Projektplan erarbeitet werden.

A.4 Anwendungsbereich und Abgrenzung
Das V-Modell ist auf die Planung und (Weiter-)Entwicklung von IT-Systemen ausgerichtet, umfasst aber
auch die Konzeption betrieblicher Aufgaben und die anfängliche Koordinierung der verantwortlichen Stellen
für die Pflege und Weiterentwicklung. Die weitere Organisation und Durchführung dieser Aufgaben wird
vom V-Modell nicht abgedeckt.

Das V-Modell XT Bund beschränkt sich gegenüber dem V-Modell XT auf die für Bundesbehörden relevante
Durchführung   von  Auftraggeber-seitigen   Projekten   und   Eigenentwicklungen   von   Softwaresystemen.   Es
überlässt   die   Durchführung   reiner  Auftragnehmer-Projekte   dem   allgemeinen   V-Modell   XT   und   seinen
Varianten wie dem V-Modell XT ITZBund, einer Spezialisierung für den IT-Dienstleister des Bundes. Die
Entwicklung von Hardware (Elektronik, Mechanik, eingebettete Systeme) wird vom V-Modell XT Bund
ebenfalls nicht abgedeckt.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

6

 Einstieg in das V-Modell XT Bund

Agile  Vorgehensweisen   wie   Scrum  oder   Kanban   können   je   nach   Projektkontext   gut   mit   dem  V-Modell
kombiniert werden und insbesondere dabei helfen, den "Sockel des Vs" auszugestalten. Eine detaillierte
Diskussion und konkrete Vorschläge finden sich beispielsweise in SKB14 und BIT13 .

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

B Konzepte und Inhalte des V-Modell XT Bund

7

B Konzepte und Inhalte des V-Modell XT
Bund

Der Lieferumfang des V-Modells besteht aus Dokumentationen, Produktvorlagen und einem Werkzeug:

➢ Dokumentationen:  Die  im Lieferumfang  enthaltene  Prozessdokumentation umfasst  alle  Elemente
des   V-Modells.   Die  Projektdokumentation   enthält   den   für   ein   konkretes   Projekt   relevanten
Ausschnitt   aus   der  Prozessdokumentation,   beispielsweise   den   Projektablauf,   zu   erstellende
Ergebnisse und dafür nötige Rollen. Sie wird durch das Tailoring aus dem Lieferumfang erzeugt.

➢ Produktvorlagen

 :   Für   die   während   des   Projekts   zu   erstellenden   Ergebnisse   (Produkte)   werden

Vorlagen angeboten.

➢ Werkzeug:   Der  V-Modell   XT   Projektassistent  unterstützt   die  Anpassung   des   V-Modells   an   ein

konkretes Projekt.

Die Dokumentationen sind wie folgt gegliedert:

➢ Der  Einstieg   in   das   V-Modell   XT   Bund  (nur   Prozessdokumentation)   beschreibt   die   Ziele   und
Adressaten   des   V-Modells,   bietet   einen   Überblick   über   dessen   Prinzipien,   erläutert   seinen
Anwendungsbereich und zeigt die Grenzen seiner Anwendung auf.

➢ Der  Einstieg in das projektspezifische V-Modell  (nur Projektdokumentation) stellt die gewählten

Tailoring-Einstellungen dar, die zum Projekt-spezifischen Vorgehensmodell geführt haben.

➢ Die  Konzepte   und Inhalte  des  V-Modell   XT  Bund  enthalten Definitionen  wesentlicher  Begriffe,
Erklärungen   grundlegender   Konzepte   und   eine   Beschreibung   des   Projekt-Vorgehens   und   des
Zusammenspiels verschiedener V-Modell-Projekte.

➢ Die  Referenz   Produkte  beschreibt   die  Produkte  und   Themen   des   V-Modells   sowie   deren

Zusammenhänge über Produktabhängigkeit

 en   .

➢ Die Referenz Rollen beschreibt die Rolle

 n   des V-Modells und deren Verantwortung oder Mitwirkung
bei der Erstellung von Produkten. Die Rollen sind nach Organisations-, Projektteam- und sonstigen
Projekt-Rollen kategorisiert.

➢ Die Referenz Abläufe beschreibt die im V-Modell vorgesehenen Projektdurchführungsstrategie

 n   und

Entscheidungspunkt

 e  .

➢ Die Referenz Tailoring (nur Prozessdokumentation) beschreibt die Projekttyp

 n
 en   , Projekttypvariante
 e  , mit denen das V-Modell auf ein bestimmtes Projekt zugeschnitten werden

und  Projektmerkmal
kann (Anwendungsprofil).

➢ Die Referenz Arbeitshilfen enthält Methodenreferenzen und Werkzeugreferenzen sowie Hinweise zu

den Produktvorlagen.

➢ Der Anhang enthält ein Glossar, ein Abkürzungsverzeichnis und Literaturangaben.

Die ersten beiden Kapitel (Einstieg, Konzepte und Inhalte) sollten sie gelesen haben, um das V-Modell in
Projekten   erfolgreich   anwenden   zu   können.   Die   Referenzen   dienen   zusammen   mit   dem  Anhang  als
Nachschlagewerk während der Projektdurchführung.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland









8

 Konzepte und Inhalte des V-Modell XT Bund

B.1 Grundkonzepte

Abbildung 2: Vorgehensmodellinhalte und Tailoring

Wie  Abbildung   2  zeigt,   stehen  Produkte  im   Mittelpunkt   des   V-Modells.   Produkte   sind  Artefakte   wie
Dokumente, Software oder auch Pläne, die in einem Projekt erzeugt oder (als externe Produkte) im Projekt
verwendet   werden.   Produkte   können  in Themen   aufgeteilt   sein  und  sind  zur   besseren Auffindbarkeit   in
Disziplinen gruppiert.

Jedem Produkt ist genau eine Rolle zugeordnet, deren Inhaber für die Erstellung des Produkts verantwortlich
ist. Weitere Rollen können an der Erstellung des Produkts mitwirken. Rollen strukturieren die Aufgaben und
Befugnisse im Rahmen eines Projekts und werden mit Mitarbeitern besetzt. Die Projektmitarbeiter werden
bei   der   Erstellung   von   Produkten   durch  Arbeitshilfen  wie   Produktvorlagen,   Werkzeug-   und
Methodenreferenzen unterstützt.

Ein   Projekt   durchläuft   verschiedene  Entscheidungspunkt
 e    (Meilensteine).   Zu   jedem   Entscheidungspunkt
müssen bestimmte Produkte fertig gestellt sein, anhand deren Qualität über die weitere Projektdurchführung
entschieden wird. Die Reihenfolge der Entscheidungspunkte wird von einer  Projektdurchführungsstrategie
festgelegt. Sie ist ein Ergebnis des  Tailorings, bei dem über den  Projekttyp, seine  Projekttypvariante  und
 e   die passenden Inhalte des V-Modells bestimmt werden.
spezifische Projektmerkmal

B.1.1 Produktmodell
Produkte sind die im Projekt zu erarbeitenden Ergebnisse und Zwischenergebnisse, gruppiert in Disziplinen.
Ist ein Produkt als initial gekennzeichnet, muss es in jedem Projekt genau einmal vorhanden sein. Im Projekt
verwendete Artefakte, die außerhalb des Projekts erstellt wurden, sind externe Produkte, deren Struktur und
inhaltliche Anforderungen allerdings vom V-Modell vorgegeben sind. Produkte können initial und extern
sein.

Produkte können in Themen untergliedert werden, strukturell oder inhaltlich voneinander abhängen oder von
anderen   Produkten   erzeugt   werden.   Die   nachfolgenden   Abschnitte   beschreiben   die   verschiedenen
Zusammenhänge zwischen Produkten, deren Strukturierung und Prüfung sowie den Inhalt und Aufbau der
Produkte-Referenz.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland



B.1 Grundkonzepte

9

B.1.1.1 Produkttypen und Produktexemplare

Jedes Produkt ist von einem bestimmten Typ. Ein  Produkttyp  gibt den inhaltlichen Rahmen vor, der von
einem  Produktexemplar  umgesetzt wird. Je nach Produkttyp werden ein oder mehrere Produktexemplare
angefertigt.  Abbildung   3  zeigt   beispielhaft   den  Produkttyp  Projektstatusbericht  und   die   dazu   erstellten
Produktexemplar

 e   für Mai, Juni und Juli.

Abbildung 3: Zusammenhang von Produkttyp und Produktexemplaren

B.1.1.2 Produktstrukturierung

Das V-Modell gibt für manche Produkte eine Untergliederung in weitere Produkte vor.

Die  Systemarchitektur  beschreibt   eine   hierarchische   Struktur   bestehend   aus   Segmenten,   Einheiten   und
Modulen.   Der  Aufbau   ist   durch   strukturelle   Produktabhängigkeiten   definiert   und   wird   in   der   Disziplin
Systemelemente beschrieben.

Für die  System
 e    können jeweils beliebig viele logistische Unterstützungsdokumentationen erstellt werden.
Diese   umfassen  jeweils   eine   inhaltlich  zusammengehörende   Menge   von  Dokumentationen   zur   Nutzung,
Ausbildung und logistischen Aspekten. Die Disziplinen  Systementwurf  und  Systemelemente  beschreiben
dazu die Details.

B.1.1.3 Erzeugende Produktabhängigkeiten

Produktexemplare   können   Projektrichtlinien   und   -bedingungen   enthalten   und   so   die   Erstellung   anderer
Produktexemplare   vorgeben.
  Dadurch   "erzeugt"   ein   Produktexemplar   weitere   (abhängige)
Produktexemplare. Zwischen dem erzeugenden Produktexemplar und den abhängigen Produktexemplaren
besteht eine erzeugende Produktabhängigkeit. Jede erzeugende Produktabhängigkeit ist genau einem Thema
des erzeugenden Produktexemplars zugeordnet. Innerhalb dieses Themas muss festgelegt werden, ob und
ggf.   wie   viele   Exemplare   des   abhängigen   Produkts   im   Projekt   erstellt   werden.   Der   Verzicht   auf   die
Erstellung abhängiger Produkte ist zu begründen.

Initiale Produkte sind stets erzeugende Produkte. Das initiale Projekthandbuch erzeugt unter anderem die
Risikoliste   (Thema:  Organisation   und   Vorgaben   zum   Risikomanagement)   und   die   Änderungsstatusliste
(Thema: Organisation und Vorgaben zum Problem- und Änderungsmanagement).

B.1.1.4 Produktprüfung und inhaltliche Produktabhängigkeiten

Das   V-Modell   unterstützt   die   Anwender   durch   die   Konzepte   zu   Produktprüfungen   und   inhaltlichen
Produktabhängigkeiten dabei, die Qualität erstellter Produktexemplar

 e   zu erhöhen.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland




10

 Konzepte und Inhalte des V-Modell XT Bund

Zwischen Produktexemplaren können inhaltliche Zusammenhänge bestehen. Diese werden durch inhaltliche
Produktabhängigkeiten beschrieben. Änderungen an einem Produktexemplar können dadurch Änderungen
an inhaltlich abhängigen Produktexemplaren verursachen. Bei der Qualitätssicherung ist daher nicht nur das
vorliegende Produkt selbst, sondern auch seine Konsistenz zu inhaltlich abhängigen Produkten zu prüfen.

Vorgaben   zur   Prüfung   werden   im   Produkt  QS-Handbuch  und   im   Implementierungs,-   Integrations-   und
Prüfkonzept   festgehalten   (siehe   auch   Disziplin  Qualitätssicherung).   Das   V-Modell   sieht   zwei  Arten   der
Prüfung   von   Produktexemplaren   vor:   die   Eigenprüfung   und   die   Prüfung   durch   eine   unabhängige
Qualitätssicherung.   Jedes   Produktexemplar   hat   einen   der   Zustände  in   Bearbeitung,  vorgelegt  und  fertig
gestellt.

Abbildung 4: Produktzustandsmodell

Ein Produktexemplar in Bearbeitung sollte stets einer Eigenprüfung unterzogen werden. Ist zusätzlich eine
unabhängige Qualitätsprüfung durch einen Prüfer notwendig, so wechselt der Zustand auf  vorgelegt. Ein
Produktexemplar   gilt   in   diesem   Fall   als  fertig   gestellt,   wenn   sowohl   eine   Eigenprüfung   als   auch   eine
notwendige unabhängige Prüfung erfolgreich gewesen sind. Ist keine unabhängige Prüfung gefordert, so
wechselt der Zustand direkt auf fertig gestellt. Bei Änderungen am Produktexemplar wechselt der Zustand
zurück zu in Bearbeitung.

In der Referenz Produkte werden zu jedem Produkt die inhaltlichen Produktabhängigkeiten aufgeführt und
referenziert. Eine inhaltliche Produktabhängigkeit besteht aus zwei Gruppen mit jeweils mindestens einem
Produkt. Jedes Produkt einer Gruppe ist inhaltlich abhängig zu jedem Produkt der anderen Gruppe. Die
innerhalb einer Gruppe enthaltenen Produkte stehen nicht in Abhängigkeit zueinander.

B.1.1.5 Inhalt und Aufbau der Referenz Produkte

Die Referenz Produkte ist das Nachschlagewerk für die Produkte des V-Modells und ihre Abhängigkeiten.

Im Kapitel Produkte werden die Produkttyp
 en    zusammengefasst aufgeführt.
Die   Beschreibung   eines   Produkttyps   enthält   seinen   Zweck,   seine   Themen   sowie   tabellarisch   seine
Abhängigkeiten und Beziehungen zu Aktivitäten, Rollen und anderen Produkttypen.

 en    des V-Modells nach Disziplin

Das   Kapitel   Produktabhängigkeiten   listet   alle   inhaltlichen   Produktabhängigkeiten   nach   Themen.   Der
Produktindex führt die Produkte in alphabetischer Reihenfolge auf.

Die  Prozessdokumentation enthält alle Produkttypen des V-Modells, die  Projektdokumentation nur den für
das Projekt relevanten Teil.

B.1.2 Rollenmodell
Rolle
Personen. Rollen sind verantwortlich für die Erstellung von Produkte

 n   beschreiben die Akteure eines Projekts unabhängig von bestimmten Organisationen, Projekten oder

 n   oder wirken daran mit.

Eine   Rolle   hat   einen  Namen   und  eine   Menge   von Aufgaben  und  Befugnissen.   Ein  Fähigkeitsprofil   mit
Kriterien und Rahmenbedingungen hilft bei der Suche nach Personen, die zur Besetzung der Rolle geeignet
sind.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland





B.1 Grundkonzepte

11

Der  Projektleiter  besetzt   die   wichtigsten   Rollen   bei   der   Projektinitialisierung   und   dokumentiert   die
Zuordnung im Projekthandbuch. Er dokumentiert dort auch spätere Neu- oder Umbesetzungen von Rollen.

Eine  Rolle  kann grundsätzlich  durch mehrere  Personen besetzt  werden,  und  eine  Person  kann in einem
Projekt   mehrere   Rollen   einnehmen.   Ausnahmen   sind   die   singuläre   Rolle   des   Projektleiters   und
Interessenkonflikte   zwischen   Rollen,   die   eine   gleichzeitige   Besetzung   mit   derselben   Person   verhindern.
Solche Besetzungshinweise runden die jeweilige Rollenbeschreibung ab.

Alle   Rollen-   und   Funktionsbezeichnungen   beziehen   sich   auf  Angehörige   beiderlei   Geschlechts,   werden
jedoch der besseren Lesbarkeit halber im generischen Maskulin formuliert.

B.1.2.1 Projektteamrollen, Projektrollen und Organisationsrollen

Das V-Modell teilt Rolle

 n   in Projektteamrollen, Projektrollen und Organisationsrollen ein.

Abbildung 5: Rollenmodell im V-Modell

Projektteamrollen   arbeiten   inhaltlich   am   Projekt   mit   und   bestehen   zur   Projektlaufzeit.   Sie   übernehmen
Verantwortung für Produkte oder wirken bei deren Erstellung mit. Der Projektleiter ist eine Projektteamrolle
und den anderen Projektteamrollen gegenüber weisungsbefugt.

Projektrollen werden außerhalb des Projekts, aber für das Projekt besetzt. Sie wirken entweder mit ihrem
Fachwissen an der Erstellung von Produkten mit  oder  entscheiden über  den Projektfortschritt.  Beispiele
dafür sind die Anwender, die Verfahrensverantwortlichen und der Lenkungsausschuss. Der Projektleiter hat
den Projektrollen gegenüber keine Weisungsbefugnis.

Organisationsrollen   bestehen   in   der   Organisation   unabhängig   von   Projekten.   Sie   haben   über   ihre
Regelungskompetenz   Einfluss   auf   das   Projekt.   Das   V-Modell   beschreibt   die   Mitwirkung   von
Organisationsrollen,  die  wie  die  Personalvertretung  oder  der  Qualitätsmanager  in  den  meisten  Behörden
anzutreffen sind.

B.1.2.2 Besetzung, Mitwirkung und Verantwortung von Rollen

Für jedes  Produkt  gibt es genau eine verantwortliche  Rolle  und eine bestimmte Anzahl von mitwirkenden
Rollen. Verantwortung für ein Produkt zu übernehmen bedeutet,

➢ die Erstellung des Produkts im geplanten Qualitäts-, Termin- und Kostenrahmen sicherzustellen,

➢ erstellte oder geänderte Produkte an das Konfigurationsmanagement (KM) zu übergeben und

➢ die mitwirkenden Rollen zu koordinieren.

Konkrete Arbeiten an einem Produkt können delegiert werden, nicht aber die Verantwortung für das Produkt.

Mitwirkende Rollen tragen zur Erarbeitung von Produkten bei oder sind an der Prüfung und Freigabe von
Produkten beteiligt.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


12

 Konzepte und Inhalte des V-Modell XT Bund

B.1.2.3 Inhalt und Aufbau der Referenz Rollen

Die  Referenz   Rollen  ist   das   Nachschlagewerk   für   die   Rollen   des  V-Modells,   unterteilt   in   die   Gruppen
Projektteam-,   Projekt-   und  Organisationsrollen  sowie   einen  alphabetischen   Index.   Die   Beschreibung   der
jeweiligen Rolle wird ergänzt um eine Liste der  Produkte, an denen die  Rolle  mitwirkt oder für die sie
verantwortlich ist.

Die  Prozessdokumentation enthält alle Rollen des V-Modells, die  Projektdokumentation nur den für das
Projekt relevanten Teil.

B.1.3 Ablaufplanung und Entscheidungspunkte
Das Produktmodell des V-Modells legt die Ergebnisse fest, die in einem Projekt erarbeitet werden. Die im
Tailoring gewählte Projektdurchführungsstrategie bestimmt die Reihenfolge der Entscheidungspunkte des
Projekts   und   damit   Zeitpunkte   für   die   Erstellung   von   Produkten.   Der   Projektablauf   kann   über
Ablaufvarianten,   Parallelisierungen   und   Synchronisationen   angepasst   werden.   Die   Details   werden
nachfolgend erläutert.

B.1.3.1 Entscheidungspunkte

Entscheidungspunkte   sind   Qualitätsmesspunkte   (engl.   Quality   Gates),   zu   denen   anhand   vorzulegender
Produkte   der   Projektfortschritt   geprüft   und  über   die   Fortführung  des   Projekts   entschieden  wird.   Die   im
Tailoring   festgelegte
 Projektdurchführungsstrategie  bestimmt   die   für   ein   Projekt   relevanten
Entscheidungspunkte.

Abbildung 6: Entscheidungspunkte des V-Modells

Die   weiß   dargestellten   Entscheidungspunkte   sind   in   jeder   Projektdurchführungsstrategie   enthalten;   die
hellorangen beinhalten vertragliche Aspekte und deren Kontrolle, während die dunkelorangen die Aspekte
der Spezifikation, Umsetzung, Prüfung und Abnahme eines Systems enthalten.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

B.1 Grundkonzepte

13

Abbildung 7: Vorstellung des Projektstands durch den Projektleiter am Entscheidungspunkt

Zum Entscheidungspunkt berichtet der Projektleiter dem Lenkungsausschuss im Rahmen einer Besprechung,
per E-Mail oder in sonstiger abgestimmter Weise über den Projektfortschritt. Er stellt dabei sicher, dass alle
dem Entscheidungspunkt zugeordneten Produkte im Zustand fertig gestellt vorliegen und unterbreitet einen
Vorschlag (oder auch alternative Vorschläge) für das weitere Vorgehen.

trifft

 Lenkungsausschuss

Der
  vorgelegten   Produkte   eine   dokumentierte
Projektfortschrittsentscheidung.  Eine  positive  Entscheidung  gibt  das  Budget  und die  Ressourcen  für  den
nächsten Projektabschnitt frei und formuliert dafür ggf. Auflagen. Der Entscheidungspunkt ist damit erreicht.
Eine   negative   Entscheidung   legt   fest,   ob   der   Entscheidungspunkt   nach   Überarbeitung   der   Produkte
wiederholt oder das Projekt neu aufgesetzt oder abgebrochen wird.

  anhand   der

B.1.3.2 Projektdurchführungsstrategien

Für eine zuverlässige Planung und Steuerung eines Projekts muss ein geordneter Projektablauf entwickelt
 n    zur Verfügung, die je nach  Projekttyp
werden. Hierfür stellt das V-Modell  Projektdurchführungsstrategie
und  Projekttypvariante Ablaufregeln für die Reihenfolge der  Entscheidungspunkt
 e    vorgeben. Die gewählte
Projektdurchführungsstrategie  definiert   somit   auch   die   Reihenfolge   der   zu   erstellenden  Produkte  und
durchzuführenden Aktivität

 en   .

Jedes Projekt beginnt mit den Entscheidungspunkten  Projekt genehmigt  und  Projekt initialisiert  und endet
mit dem Entscheidungspunkt Projekt abgeschlossen. Dazwischen kann der Projektleiter die Reihenfolge der
Entscheidungspunkt
 e    im   Rahmen   der  Projektdurchführungsstrategie  selbst   bestimmen,   solange   sie   die
Ablaufregeln einhält. Außerdem kann der Projektleiter zwischen Entscheidungspunkten beliebige weitere
Meilensteine einplanen.

Abbildung 8: Einfache Projektdurchführungsstrategie

Abbildung 8  zeigt beispielhaft eine einfache, schematische  Projektdurchführungsstrategie. Ein Projekt, das
dieser Strategie folgt, plant zunächst einen Entscheidungspunkt A, danach einen Entscheidungspunkt B, um
vor Projektschluss einen Entscheidungspunkt C zu erreichen. Nach dem Erreichen des Entscheidungspunkts
B   kann  dieser   beliebig  oft   erneut   eingeplant   werden,   bevor   mit   den Arbeiten  zu  Entscheidungspunkt   C
begonnen wird.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland





14

 Konzepte und Inhalte des V-Modell XT Bund

B.1.3.3 Von der Projektdurchführungsstrategie zum Projektdurchführungsplan

  und   Abfolge   der

Nach   der   projektspezifischen   Anpassung   des   V-Modells   (Tailoring)   steht   die   zu   verwendende
Projektdurchführungsstrategie  fest, die vom Projektleiter im Projektdurchführungsplan  mit einer konkreten
Anzahl
  Der
Projektdurchführungsplan kann mit dem V-Modell XT Projektassistenten erstellt und anschließend zu einem
detaillierteren Projektplan ausgearbeitet werden. Der Projektdurchführungsplan wird vom Projektleiter zum
Entscheidungspunkt  Projekt initialisiert  erstellt, zu jedem Entscheidungspunkt  Iteration geplant  aktualisiert
und im Projekthandbuch festgehalten.

  Terminen   ausgestaltet

 Entscheidungspunkt

  wird.

samt

 e

Abbildung 9: Beispiel eines Projektdurchführungsplans

Abbildung 9  zeigt den Projektdurchführungsplan eines beispielhaften Auftraggeber-Projekts mit konkreten
Entscheidungspunkten und Terminen. Der Projektleiter hat hier zwei Iterationen vorgesehen: in der ersten
soll   ein   Prototyp   geliefert   werden   und   in   der   zweiten   das   fertige   Gesamtsystem.   Da   beide   Iterationen
gemeinsam beauftragt werden, wird der Entscheidungspunkt Beauftragung erteilt nur einmal durchlaufen.

Bei Anwendung einer agilen  Entwicklungsmethode  kommt  die hier dargestellte iterative Vorgehensweise
nicht zum Tragen. In diesem Fall erfolgt die Steuerung des (Unter-)Auftragnehmers auf Basis von   Sprint
 s
anstelle der Iterationen. Der Entscheidungspunkt Iteration geplant entfällt.

B.1.3.4 Ablaufvarianten durch Ablaufbausteine

Jede  Projektdurchführungsstrategie  besteht   aus   Ablaufbausteinen,   die   jeweils   einen   Teil   der
Entscheidungspunkte samt deren Reihenfolge vorgeben. Manche Ablaufbausteine gibt es in verschiedenen
Varianten. Beispielsweise kann bei jeder Planung einer Iteration zwischen prototypischer, inkrementeller und
komponentenbasierter Systementwicklung gewählt werden. In einer frühen Iteration könnte so zunächst ein
Prototyp  erstellt  werden,  der  in folgenden Iterationen inkrementell  ausgebaut wird.  Durch diese  Ablauf-
Varianten kann der Projektleiter die Planung an die Bedürfnisse des Projekts anpassen.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland



B.1 Grundkonzepte

15

Abbildung 10: Projektdurchführungsstrategie mit dem Ablaufbaustein Unterauftrag

Abbildung  10  zeigt   oben  den  Ausschnitt   (Ablaufbaustein)   "Inkrementelle   Systementwicklung"   aus   einer
Projektdurchführungsstrategie.  Darin  sind  zwei   schwarz   dargestellte  Platzhalter  "Unterauftrag"  enthalten.
Diese stehen für  den gleichnamigen unten dargestellten Ablaufbaustein,  in den von oben verzweigt und
später wieder zurückgekehrt wird. Dadurch kann der Auftragnehmer bei Bedarf Unteraufträge erteilen und
übernimmt   dafür   die   Rolle   eines   Auftraggebers   gegenüber   dem   Unterauftragnehmer.   Die
Entscheidungspunkte des Unterauftrags werden dann wie die entsprechenden Entscheidungspunkte in der
Projektdurchführungsstrategie AG-Projekt mit einem Auftragnehmer durchgeführt.

B.1.3.5 Parallelisierung und Synchronisation des Projektablaufs

Die Abbildungen der Projektdurchführungsstrategie
den Projektfluss durch die  Entscheidungspunkt
erläutert.

 n   im gleichnamigen Kapitel der Referenz Abläufe zeigen
 e  . Die Semantik der Abbildungselemente wird nachfolgend

Abbildung 11
hingearbeitet.

 :   Nach Erreichen von Entscheidungspunkt A wird auf das Erreichen von Entscheidungspunkt B

Abbildung 11: Projektfluss (1): Einfache Folge

Abbildung   12
Entscheidungspunkt B oder auf das Erreichen von Entscheidungspunkt C hingearbeitet werden.

 :    Nach   Erreichen   von   Entscheidungspunkt   A   kann  entweder  auf   das   Erreichen   von

Abbildung 12: Projektfluss (2): Verzweigung

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland





16

 Konzepte und Inhalte des V-Modell XT Bund

Abbildung 13
Entwicklungsstränge auf (S = Split). Dabei gibt es

 :    Nach Erreichen von Entscheidungspunkt A teilt sich der Projektablauf in mehrere parallele

Abbildung 13: Projektfluss (3): Parallelisierung

➢ genau einen Strang, der das Erreichen von Entscheidungspunkt B zum Ziel hat,

➢ beliebig viele Stränge, die das Erreichen von Entscheidungspunkt C zum Ziel haben und

➢ mindestens einen Strang, der das Erreichen von Entscheidungspunkt D zum Ziel hat.

Abbildung   14
Entwicklungsstränge zusammengeführt (J = Join). Die zusammenzuführenden Stränge umfassen

 :    Durch   das   Erreichen   von   Entscheidungspunkt   D   werden   mehrere   parallele

Abbildung 14: Projektfluss (4): Synchronisierung

➢ genau einen Strang, in dem Entscheidungspunkt A erreicht wurde,

➢ beliebig viele Stränge, in denen Entscheidungspunkt B erreicht wurde und

➢ mindestens einen Strang, in dem Entscheidungspunkt C erreicht wurde.

B.1.3.6 Inhalt und Aufbau der Referenz Abläufe

Die Referenz Abläufe enthält in der Prozessdokumentation folgende Inhalte:

Im Kapitel Entscheidungspunkte werden alle im V-Modell definierten Entscheidungspunkte beschrieben. Zu
jedem   Entscheidungspunkt   wird   aufgeführt,   auf   Basis   welcher   Produkte   die   zugehörige
Projektfortschrittsentscheidung getroffen wird und welche Rollen für diese Produkte verantwortlich sind.

 n    enthält entsprechende Einträge je  Projekttypvariante, in denen
Das Kapitel  Projektdurchführungsstrategie
die   Entscheidungspunkte   und   der   Projektfluss   dargestellt   und   die   relevanten  Ablaufbausteine   aufgeführt
werden.

Im   Kapitel
Entwicklungsstrategien, Unterauftrag) erläutert.

 Ablaufbausteine  werden   alle   im   V-Modell   wählbaren   Ablaufbausteine   (Abnahmen,

Der  Ablaufindex  listet alle im V-Modell enthaltenen  Entscheidungspunkt
und Entwicklungsstrategien (Ablaufbausteine) auf.

 e  ,  Projektdurchführungsstrategie

 n

Die   Projektdokumentation   enthält   nur   die   für   das   Projekt   relevanten   Bestandteile:   Das   Kapitel
Projektdurchführungsstrategie  beschreibt   die   im  Tailoring  ausgewählte   Variante.   Die   Kapitel
Entscheidungspunkte, Ablaufbausteine und Ablaufindex enthalten die für das Projekt relevanten Einträge.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland






B.1 Grundkonzepte

17

B.1.4 Projektkonstellation und Tailoring
Systementwicklungsprojekte   werden   in   verschiedenen   Organisationen   unterschiedlich   gehandhabt   und
können   sich   selbst   innerhalb   einer   Organisation   in   ihren   Merkmalen   wesentlich   unterscheiden.   Die
Anpassbarkeit   eines   Vorgehensmodells   an   die   jeweilige   Projektsituation   ist   daher   eine   wichtige
Voraussetzung für den Projekterfolg.

Das V-Modell unterstützt die Anpassung an unterschiedliche Projekt-Charakteristika durch das  Tailoring.
Das   Tailoring   umfasst   die   Auswahl   von  Projekttyp
 n    und   die   weitere
Charakterisierung   des   Projekts   anhand   von  Projektmerkmal
 en   .   Das   Ergebnis   ist   ein   an   das   Projekt
angepasstes Produkt- und Rollenmodell sowie eine optimale Projektdurchführungsstrategie.

 en     und  Projekttypvariante

Die folgenden Abschnitte beschreiben, wie durch das Tailoring die relevanten Produkte, Rolle
für ein Systementwicklungsprojekt zur Verfügung gestellt werden.

 n   und Abläufe

B.1.4.1 Projektkonstellationen und Projekttypen

Das   V-Modell   XT   Bund   unterstützt   zwei   Projektkonstellationen,   die   durch   folgende  Projekttypen
charakterisiert werden:

➢ Das

 Systementwicklungsprojekt   (AG)  befasst   sich   mit   V-Modell-Projekten   auf   der
Auftraggeberseite. Bei ihnen muss im Projektverlauf ein Auftragnehmer bestimmt werden. Für die
Beauftragung eines externen IT-Dienstleisters wird zu diesem Zweck eine Ausschreibung erstellt und
eines der eingegangenen Angebote ausgewählt. Die Beauftragung eines IT-Dienstleisters des Bundes
erfolgt ohne Ausschreibungs- und Vergabeverfahren auf Basis einer Angebotsaufforderung.

Der  Auftragnehmer   ist   für   die   Systementwicklung   zuständig   und   liefert   dem  Auftraggeber   ein
System,   welches   dieser   abnehmen   muss.   Der   Auftragnehmer   führt   seinerseits   das   Projekt   als
Systementwicklungsprojekt   (AN)   nach   dem   allgemeinen   V-Modell   XT   bzw.   einer
organisationsspezifischen Anpassung des Standards durch.

➢ Das  Systementwicklungsprojekt   (AG/AN)  befasst   sich   mit   V-Modell-Projekten,   die   keine
(vertragliche)   Trennung   der   Auftraggeber-   und   Auftragnehmerseite   in   zwei   separate   Projekte
erfordern,   sondern   als   Eigenentwicklung   innerhalb   einer   Behörde   durchgeführt   werden.
Ausschreibungs- und Vertragswesen sowie die formale Angebotserstellung entfallen hierbei ebenso
wie eine doppelte Projektorganisation.

Abbildung 15: Schematische Darstellung der Projekttypen Systementwicklung (AG) und Systementwicklung (AN)

Abbildung   15  zeigt   das   Zusammenspiel   der  Projekttyp
 en     Systementwicklungsprojekt   (AG)  und
Systementwicklungsprojekt   (AN).   Beide   enthalten   dieselben   Managementmechanismen   (weiß),   die
allerdings   jeweils   spezifisch   ausgestaltet   und   durchgeführt   werden.   Der  Auftragnehmer   führt   nach   den
Vorgaben des Auftraggebers (orange) die Systementwicklung (blau) durch. Über eine AG/AN-Schnittstelle
tauschen Auftraggeber und Auftragnehmer relevante Produkte wie etwa die Lieferung aus.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland






18

 Konzepte und Inhalte des V-Modell XT Bund

Abbildung 16: Schematische Darstellung des Projekttyps Systementwicklungsprojekt (AG)/(AN)

zeigt

Abbildung   16
  demgegenüber   eine   deutliche   Vereinfachung   für   den   Projekttyp
Systementwicklungsprojekt (AG/AN), bei dem die Anforderungsfestlegung, die Projektabwicklung und die
Entwicklung   innerhalb   einer   Organisation   erfolgen.  Weil   in   einem   solchen   Projekt   kein   außenstehender
Auftragnehmer in Erscheinung tritt, entfällt die AG/AN-Schnittstelle. Die Rolle des Auftraggebers und des
Auftragnehmers   werden   dabei   Organisations-intern   eingenommen,   zum   Beispiel   durch   verschiedene
Abteilungen.

B.1.4.2 Projekttypvarianten und Projektmerkmale

Nach der Unterscheidung in  Projekttyp
 en     wird das Projekt durch Projekttypvarianten und davon abhängig
durch Projektmerkmale weiter charakterisiert. Die Auswahl des Projekttyps, der Projekttypvariante und der
Projektmerkmale bildet das Anwendungsprofil des Projekts.

Das   V-Modell   bietet   zu   jedem   Projekttypen   zwei  Projekttypvariante
 n    an.  Auftraggeberprojekte   werden
entweder a) mit einem oder b) mit mehreren Auftragnehmern durchgeführt. Bei mehreren Auftragnehmern
wird die Systementwicklung auf verschiedene Teilprojekte aufgeteilt. AG/AN-Projekte wiederum werden
nach   a)   der   (Weiter-)Entwicklung   oder   Migration   oder   b)   der   Wartung   und   Pflege   von   Systemen
unterschieden. Während bei a) neue Funktionalität im Vordergrund steht, geht es bei b) um die Umsetzung
von Änderungsanforderungen.

Projektmerkmal
 e    charakterisieren  Eigenschaften  eines  Projekts,   beispielsweise   ob ein Altsystem  migriert
oder ob Fertigprodukte eingesetzt werden sollen. Die Auswahl von Projekttyp und -variante bestimmt die
Menge möglicher Projektmerkmale und deren Werte. Projektmerkmale und mögliche Werte werden in der
Referenz Tailoring erläutert.

B.1.4.3 Modularisierung durch Bausteine

Das   V-Modell   ist   modular   aufgebaut.   Neben   den   bereits   beschriebenen  Ablaufvarianten   durch
Ablaufbausteine stehen Vorgehensbausteine zur Verfügung, die passend zum Projekt ausgewählt werden.

 e    fassen  Produkte,   Themen   und  Aktivität

Vorgehensbaustein
 en     eines   Teilprozesses   zusammen.   Die
Vorgehensbausteine  Projektmanagement,  Qualitätssicherung,  Konfigurationsmanagement  sowie  Problem-
und Änderungsmanagement bilden den V-Modell-Kern, der in jedem Projekt enthalten ist. Dieser Kern wird
im   V-Modell   XT   Bund   stets   um   den   Vorgehensbaustein  Wirtschaftlichkeitsbetrachtung  erweitert.   Alle
anderen   Vorgehensbausteine   werden   abhängig   vom   Ergebnis   des  Tailoring
 s    (Anwendungsprofil)
hinzugefügt.

 n    zu Produkten (vgl. Kapitel  Rollenmodell) werden mit der Auswahl von
Durch die Zuordnung von  Rolle
Vorgehensbaustein
 en     automatisch auch die Rollen ausgewählt, die für die Projektdurchführung notwendig
sind. Und auch die Produkte selbst werden angepasst, indem ihre Themen auf die im Projekt benötigten
Inhalte eingegrenzt werden. Beispielsweise enthält das Produkt  Projekthandbuch  das Thema  Organisation
und Vorgaben zur Systemerstellung nur, wenn der Vorgehensbaustein Systemerstellung ausgewählt wurde, es
sich also um ein AG/AN-Projekt handelt.

Die Vorgehensbausteine werden in der Referenz Tailoring beschrieben.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland









B.1 Grundkonzepte

19

B.1.4.4 Inhalt und Aufbau der Referenz Tailoring

Die Referenz Tailoring besteht aus folgenden Kapiteln:

Im   Kapitel  Projekttypen   und   Projekttypvarianten  werden   die   Projekttypen   charakterisiert.   Zu   jedem
Projekttyp   wird   aufgelistet,   welche   Vorgehensbausteine   und   Projektmerkmale   er   mitbringt.   Außerdem
werden   seine  Projekttypvariante
 n    mit   der   jeweiligen  Projektdurchführungsstrategie  und   den
hinzukommenden Projektmerkmalen, Vorgehens- und Ablaufbausteinen beschrieben.

Das Kapitel  Projektmerkmal
 e    beschreibt alle im V-Modell vorkommenden Projektmerkmale. Neben einem
Erläuterungstext   werden   die   Werte   aufgelistet,   die   ein   Projektmerkmal   annehmen   kann,   und   welche
Bedeutung der jeweilige Wert hat.

Das   Kapitel  Vorgehensbausteine  enthält   zu   jedem   Vorgehensbaustein   analog   zu  Abbildung   17  eine
Darstellung   seiner  Produkte  (Rechtecke   mit   abgerundeten   Ecken)   und  Aktivität
 en     (Rechtecke),   die   in
Disziplin
 en    (graue Rechtecke) zusammengefasst sind. Durchgezogene Linien zeigen, durch welche Aktivität
ein Produkt erstellt wird und welche Rolle dafür verantwortlich ist. Im Oval gesetzte Kürzel zeigen, ob ein
Produkt initial ("I") zu erstellen ist oder dem Projekt von extern ("E") zur Verfügung gestellt wird.

Abbildung 17: Überblicksgrafik für Disziplinen in Vorgehensbausteinen

Zu jedem Vorgehensbaustein ist außerdem eine Tabelle enthalten mit

➢ Themen, die zu Produkten anderer Vorgehensbausteine hinzugefügt werden,

➢ Rollen, die an Produkten dieses Vorgehensbaustein

 s   mitwirken sowie

➢ Projekttypen, -varianten und Projektmerkmalswerten, die den Vorgehensbaustein bedingen.

Der Tailoringindex listet die Tailoring-relevanten Modellelemente auf.

Die Projektdokumentation enthält in den o.g. Themen jeweils nur die für das Projekt relevanten Einträge.

B.1.5 Arbeitshilfen

B.1.5.1 Aktivitäten

Eine Aktivität im V-Modell benennt die Tätigkeit, die zur Erstellung eines Produkt
 s   ausgeführt werden muss.
Mit Ausnahme externer Produkte sind alle im V-Modell enthaltenen Produkte mit einer Aktivität verknüpft.
Die   Aktivitäten   dienen   der   Herleitung   des   Projektplans.   Ein   mit   dem   Projektassistenten   generierter
Meilensteinplan umfasst alle Aktivitäten, die für die Erstellung der an den Entscheidungspunkt
 en    geforderten
Produkte notwendig sind.

B.1.5.2 Methoden- und Werkzeugreferenzen

Das   V-Modell   enthält   für   einige   Produkte   Verweise   auf   Methoden   (z.B.  Anforderungsanalyse)   und
Werkzeuge   (z.B.  Anforderungsmanagement).   Die   aufgeführten  Referenzen  haben   sich  als   Best-Practices
erwiesen und sollten bei der Erstellung der Produkte berücksichtigt werden. Einen verbindlichen Einsatz der
aufgeführten Referenzen definiert das V-Modell nicht.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland








20

 Konzepte und Inhalte des V-Modell XT Bund

Die Methodenreferenz

 en    und Werkzeugreferenz

 en    sind im Arbeitshilfenindex enthalten.

B.1.5.3 Produktvorlagen

Eine Produktvorlage ist ein Dokument, das die Erstellung eines Produktexemplars für einen bestimmten
Produkttyp erleichtert, indem sie die in der Referenz Produkte zu einem konkreten Produkttyp geforderten
Inhalte   umsetzt.   Produktvorlagen   haben   eine   geeignete   Struktur,   enthalten   Metadaten   wie   Produktname,
 n    sowie Produkt- und Themenbeschreibungen. Dadurch wird sichergestellt,
Disziplin  und beteiligte  Rolle
dass  Produktexemplar
 e    – auch projektübergreifend – bezüglich des Layouts einheitlich gestaltet sind und
Projektmitarbeiter sich auf die Ausgestaltung der projektspezifischen Inhalte konzentrieren können.

Die Produktvorlagen sind im Arbeitshilfenindex enthalten.

B.1.5.4 Der V-Modell XT Projektassistent

 V-Modell   XT   Projektassistent  unterstützt   das  Tailoring  zunächst   durch   eine   schrittweise
Der
Charakterisierung   des   Projekts   (Anwendungsprofil).   Anschließend   können   die   Projektdokumentation,
Projekt-spezifische Produktvorlagen und ein initialer Projektplan generiert werden. Der Projektplan enthält
die für das Projekt relevanten Entscheidungspunkte (Meilensteine) sowie die  Aktivität
 en     und Ressourcen
 n  ), um die notwendigen Produkte zu erstellen. Der vom Projektassistenten erstellte
(verantwortliche  Rolle
initiale Projektplan muss vom Projektleiter noch weiter ausgestaltet werden. Eine detaillierte Anleitung zum
Umgang mit dem Projektassistenten findet sich im Kapitel V-Modell XT Projektassistent.

B.1.5.5 Überblicksbilder

In   den   nachfolgenden   Unterkapiteln   sind  Abbildungen   zu   finden,   die   sich   besonders   in   Schulungen   als
hilfreiche Überblicksbilder erwiesen haben.

B.1.5.5.1

Zuordnung der Produkte zu den einzelnen Entscheidungspunkten nach Projekttyp

 en     Systementwicklungsprojekt   (AG)  und
Abbildung   18  und  Abbildung   19  zeigen   für   die  Projekttyp
 en     zugeordnet   sind.
Systementwicklungsprojekt   (AG/AN),   welche  Produkte  welchen  Entscheidungspunkt
Die   Darstellung   des  AG-Projekts   basiert   auf   der   Beauftragung   eines   externen   IT-Dienstleisters   mit   der
Durchführung eines klassischen Softwareentwicklungsprojekts. Bei der Beauftragung eines IT-Dienstleisters
des   Bundes   und/oder   der   Durchführung   eines   agilen   Softwareentwicklungsprojekts   variieren   die
Bezeichnungen einzelner Entscheidungspunkte sowie die zugeordneten Produkte.

Die Abbildungen stellen die jeweilige Produktmenge dar, die durch das Tailoring zumeist wieder reduziert
wird. Die Produkte  Projektfortschrittsentscheidung,  Projektplan,  Projektstatusbericht  und  QS-Bericht  sind
bei   fast   jedem  Entscheidungspunkt  vorzulegen.   Ausnahmen   hiervon   sind   der   Projektstart
(Entscheidungspunkt Projekt genehmigt) und das Projektende (Entscheidungspunkt Projekt abgeschlossen).

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland









B.1 Grundkonzepte

21

Abbildung 18: Überblick über Entscheidungspunkte und spezifische Produkte aus Sicht eines AG

Abbildung 19: Überblick über Entscheidungspunkte und spezifische Produkte aus Sicht eines AG/AN

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

22

 Konzepte und Inhalte des V-Modell XT Bund

B.1.5.6 Inhalt und Aufbau der Referenz Arbeitshilfen

Die Referenz Arbeitshilfen besteht aus den folgenden Kapiteln:

Das Kapitel Methoden und Werkzeuge beschreibt Best Practices bei der Erstellung von Produkten, verweist
auf die jeweiligen Produkte und nennt weiterführende Literatur.

Das   Kapitel  Produktvorlagen  erläutert   deren  Zweck,  Verfügbarkeit   und  Bezugsmöglichkeiten,   beschreibt
 en   .
Inhalt und Aufbau der generierten Produktvorlagen und zeigt sie in einer Übersicht, sortiert nach Disziplin

Das   Kapitel  V-Modell   XT   Projektassistent  erklärt   die   Nutzung   dieses   Werkzeugs,   insbesondere   die
Durchführung des Tailorings, der Meilensteinplanung und der Vorlagengenerierung.

Der Arbeitshilfenindex listet die Arbeitshilfen des V-Modells auf.

B.1.6 Änderungen gegenüber dem V-Modell XT
Die grundlegenden Aspekte des Projektvorgehens im V-Modell XT Bund entsprechen denen des V-Modell
XT   und   sind   an   derselben   Stelle   der   Dokumentation   (Inhalte   des   V-Modell   XT   Bund)   enthalten.   Die
nachfolgend im Überblick beschriebenen Spezifika der Bundesverwaltung sind dort integriert.

B.1.6.1 Projekt-Vorlauf

Ein V-Modell-Projekt beginnt mit dem Erreichen des Entscheidungspunkts Projekt genehmigt. Erst danach
übernehmen  Projektleiter,  Projekteigner  und  Lenkungsausschuss  die   Verantwortung   für   das   Projekt.
Allerdings muss schon vor dem Projektbeginn eine Entscheidungsgrundlage vorliegen, auf deren Basis das
Projekt in Gang gesetzt wird.

Die Abbildung 20 zeigt die Produkte, die als Entscheidungsgrundlage für den Projektstart dienen:

Abbildung 20: Rollen und Produkte im Projekt-Vorlauf

➢ Der  Projektauftrag  schafft   den   Rahmen   für   die   Projektdurchführung.   Er   definiert   die   Ziele,   den
Zeitrahmen   und   das   Budget   und   benennt   den   Projektleiter,   den   Projektmanager   und   den
Lenkungsausschuss.

➢ Die   optionale  Projektvorstudie  beschreibt   die   dem   Projekt   zu   Grunde   liegende   Systemidee,
begründet   die   Notwendigkeit   einer   Systementwicklung   und   klärt   deren   Machbarkeit.   Die
Projektvorstudie kann eine Beschreibung der zu unterstützenden Geschäftsprozesse und auch eine
Marktsichtung von Fertigprodukten enthalten.

➢ Die  WiBe   (Vorkalkulation)  ist   gemäß   der   Bundeshaushaltsordnung   für   alle   finanzwirksamen
Maßnahmen   verpflichtend   durchzuführen.   Sie   bestätigt   die   Notwendigkeit   des   Projekts   aus
strategischen oder wirtschaftlichen Gründen und beschreibt die Kosten (Projekt- und Folgekosten)
des Systems.

➢ Die  Checkliste Informationssicherheit  enthält Aussagen zum Projektinhalt, denen zugestimmt oder
widersprochen werden kann. Auf Grundlage der Checkliste wird entschieden, ob im Projekt Aspekte
der Informationssicherheit und/oder des Datenschutzes zu berücksichtigen sind.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


B.1 Grundkonzepte

23

Abbildung 20 zeigt außerdem die am Vorlauf eines Projekts regelmäßig beteiligten Rollen der Organisation
(Behörde):

➢ Ein Fachverantwortlicher benötigt das System, um seinen fachlichen Auftrag zu erfüllen.

➢ Ein Projektauftraggeber budgetiert das Vorhaben und erteilt den Auftrag für das Projekt.

➢ Ein Betriebsbeauftragter kennt das gesamte Serviceportfolio der Behörde. Er sorgt für die Integration
des Vorhabens in die Systemlandschaft, legt technische Rahmenbedingungen fest und wirkt an der
Vorkalkulation mit.

➢ Die  Multi-Projektkoordination  ist verantwortlich für das operative Multi-Projektmanagement. Sie
koordiniert   die   Ressourcenverteilung   zwischen   den   einzelnen   Projekten   und   unterstützt   das
Projektcontrolling.

➢ Die Personalvertretung wirkt bei der Genehmigung und der Zieldefinition von Projekten mit.

B.1.6.2 UfAB

Soll die Systemerstellung an einen externen IT-Dienstleister als Auftragnehmer vergeben werden, erfolgt die
Durchführung der externen Vergabe gemäß der jeweils gültigen  UfAB  (Unterlage für Ausschreibung und
Bewertung von IT-Leistungen). Die UfAB unterteilt den Ablauf einer Beschaffung in die Phasen

➢ Planung einer Beschaffung

➢ Design einer Beschaffung

➢ Durchführung eines Vergabeverfahrens

und definiert für jede dieser Phasen einzelne Prozessschritte.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

24

 Konzepte und Inhalte des V-Modell XT Bund

Abbildung 21: UfAB-Schritte und Entscheidungspunkte

Abbildung   21  zeigt   die   Einordnung   der   Phasen   und   Prozessschritte   der   UfAB   in   den   Ablauf   der
Entscheidungspunkte des V-Modells. Die Einordnung gilt gleichermaßen für alle in der UfAB genannten
Verfahrensarten. Abhängig von der Verfahrensart ergeben sich jedoch individuelle Besonderheiten bei der
Durchführung  des  Vergabeverfahrens.   Die   Details   sind   in  der   UfAB   beschrieben.   Die   nach  den  UfAB-
Vorgaben   zu   erstellenden   Produkte   des   V-Modells   sind   in   den   Disziplinen  Ausschreibungswesen
(Vergabeakte) und Vertragswesen gruppiert. Deren Beschreibung geht auf die jeweiligen Vorgaben der UfAB
ein.

B.1.6.3 Zusammenarbeit mit der IT-Organisation

Das   V-Modell   definiert   die   Zusammenarbeit   des   Projekts   mit   der   umgebenden   IT-Organisation   und
insbesondere mit dem IT-Betrieb. Dadurch berücksichtigt das Projekt frühzeitig Aspekte, die für den späteren
Systembetrieb in der Linienorganisation notwendig sind.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

B.1 Grundkonzepte

25

Abbildung 22: Einbeziehung der IT-Organisation bei der Anforderungsermittlung

Wie  Abbildung   22  zeigt,   müssen   bereits   bei   der   Projektdefinition   und   der   Anforderungsfestlegung
Regelungen der IT-Organisation berücksichtigt werden. Diese werden aus den behördenweit geltenden, im
V-Modell nicht enthaltenen Produkten Informationssicherheit-, Datenschutz- und Betriebskonzept abgeleitet
und im Projekt als Vorgaben

➢ zur Informationssicherheit

➢ zum Datenschutz

➢ zum IT-Betrieb

erfasst.   Umgekehrt   können   durch   das   neue  System  Änderungen   an   den   zuvor   genannten   Konzepten
notwendig werden, die mit der IT-Organisation abgestimmt und ggf. von dieser umgesetzt werden müssen.

Der weitere Projektablauf und die Form der Qualitätssicherung sollten mit der IT-Organisation dahingehend
abgestimmt   werden,   dass   das   zu   entwickelnde   System   den   o.g.   Vorgaben   entspricht   und   möglichst
reibungslos in den IT-Betrieb überführt werden kann. Diese Vorgaben werden im Projekthandbuch und im
QS-Handbuch notiert und sind im weiteren Projektverlauf die Basis für den Vertrag mit dem Auftragnehmer.
Auf diese Weise ist sichergestellt, dass das vom Auftragnehmer entwickelte  System  im Einklang mit den
Regelungen und Konzepten der IT-Organisation steht und schließlich auch eingesetzt werden kann.

Abbildung 23: Regelung des weiteren Vorgehens noch im Projekt

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

26

 Konzepte und Inhalte des V-Modell XT Bund

Auch die organisatorischen Aspekte des späteren Systembetriebs müssen noch vor dem Projektende geregelt
sein. Der  Projektleiter  muss folglich dafür sorgen, dass das Verhältnis der drei Verfahrensverantwortlichen
(Fachseite, IT-Betrieb und Weiterentwicklung) untereinander und gegenüber dem Anwender definiert ist. Die
getroffenen   Regelungen   müssen   mit   dem   IT-Betrieb   abgestimmt   werden.   Sie   sollten   in
Leistungsvereinbarungen (siehe Produkt Leistungsvereinbarung (SLA/OLA/UC)) dokumentiert werden.

B.1.6.4 Projekt-Ende

Abbildung 24: Abnahme und betriebliche Freigabe eines Systems

Um das  vom Auftragnehmer   entwickelte  System  abzunehmen und in  Betrieb  zu bringen,  muss  es  zwei
"Hürden" überwinden, wie Abbildung 24 zeigt:

1. Das  System  muss den vertraglichen Vereinbarungen entsprechen. Dazu muss der Auftraggeber die

Lieferung (von AN) prüfen und eine Abnahmeerklärung ausstellen.

2. Das System muss den Anforderungen des IT-Betriebs entsprechen, der dies durch eine Betriebliche
Freigabeerklärung bestätigt. Für die betriebliche Freigabe werden die Vorgaben zum IT-Betrieb und
die ggf. vom Auftragnehmer erstellten Erweiterungen geprüft. Sofern vom Auftraggeber  Vorgaben
zur Informationssicherheit  und/oder zum Datenschutz definiert wurden, sind auch diese (inkl. der
jeweiligen Erweiterungen) für die Prüfung relevant.

Die  Abnahmeerklärung  und die  Betriebliche Freigabeerklärung  sind formal voneinander unabhängig. Die
Umsetzung betrieblicher Anforderungen sollte daher stets ein Vertragsbestandteil sein und deren Prüfung
(Prüfspezifikation   Inbetriebnahme)   in   die  Abnahmespezifikation  integriert   werden.   Dadurch   wird   die
Prüfung   betrieblicher   Anforderungen   zu   einem   Teil   des   Abnahmeprozesses.   Die   Entscheidungspunkte
Abnahme   erklärt  und  Systembetrieb   freigegeben  können   dann   zu   einem   Meilenstein   zusammengelegt
werden.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

B.1 Grundkonzepte

27

Abbildung 25: Beteiligte Rollen am Projektabschluss

Der   Projektleiter   schließt   das   Projekt   mit   dem  Projektabschlussbericht  ab   und   übergibt   ihn   dem
Lenkungsausschuss.

B.2 Inhalte des V-Modell XT Bund
Dieses Kapitel gibt einen Überblick über die Inhalte des V-Modells, die auf dessen zuvor beschriebenen
Grundkonzepten,   gleichsam   seiner   Grammatik,   aufbauen.   Es   ist   nach   Disziplinen   gegliedert,   die   in   die
Bereiche Management, Entwicklung und AG/AN-Schnittstelle eingeteilt sind.

Abbildung 26: Überblick über die Disziplinen im V-Modell

Die  Abbildung   26  zeigt   alle  Disziplin
 en     des   V-Modells   samt   ihrer   Bereichszuordnung.   Die   Position
innerhalb der Grafik ist lediglich der Optik geschuldet und nicht als zeitliche Einordnung der Disziplin zu
verstehen.   Beispielsweise   sind  Qualitätssicherung  und  Berichtswesen   im  ganzen  Projektverlauf   relevant,
nicht erst am Projektende.

B.2.1 Management
Das V-Modell ist ein Vorgehensmodell für Entwicklungsprojekte. Der Projektleiter führt das Projektteam und
verantwortet   insbesondere   die   Projektplanung   und   das   Risikomanagement.   Der  Projekteigner  trägt   die
Gesamtverantwortung für das Projekt, ist der erste Ansprechpartner des Projektleiters bei Problemen und
Mitglied im Lenkungsausschuss, dem obersten Entscheidungsgremium eines Projekts.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


28

 Konzepte und Inhalte des V-Modell XT Bund

Abbildung 27: Symmetrische Projektorganisation im V-Modell für Auftraggeber und Auftragnehmer

 Abbildung   27

Wie
  haben   Auftraggeber   und   Auftragnehmer   prinzipiell   dieselbe
Projektorganisationsstruktur.   Je   nach   Projektkonstellation   kann   es   sinnvoll   sein,   einen   gemeinsamen
Lenkungsausschuss einzurichten, der die jeweiligen Lenkungsausschüsse auf beiden Seiten ersetzt.

zeigt,

Abbildung 28: Ablauf eines V-Modell-Projekts aus der Management-Sicht

Die  Abbildung 28  zeigt den zeitlichen Ablauf eines Projekts aus der Management-Sicht. Jedes V-Modell-
Projekt beginnt mit einer Projektinitialisierung, in der die Projektziele fixiert und die Projektorganisation
eingerichtet   werden.   In   der   Projektdurchführung   werden   die   Entscheidungspunkte   der   gewählten
Projektdurchführungsstrategie   iterativ   durchlaufen.   In   jeder  Iteration  werden   die   nächsten   Schritte   zur
Umsetzung   des  Vorhabens   eingeplant,   die  Vorgaben   in  Projekt-   und   QS-Handbuch  ggf.   aktualisiert   und
aufgetretene   Probleme   und   Änderungen   berücksichtigt.   Jedes   V-Modell-Projekt   endet   mit   dem
Entscheidungspunkt  Projekt   abgeschlossen,   zu   dem   ein  Projektabschlussbericht  präsentiert   und   die
Projektorganisation wieder aufgelöst wird.

B.2.1.1 Anbahnung und Organisation

Die Disziplin Anbahnung und Organisation enthält alle für die Einrichtung und Organisation eines Projekts
notwendigen   Produkte.  Ausgangspunkt   sind   die   im  Projekt-Vorlauf  erstellten   Produkte  Projektvorstudie,
WiBe (Vorkalkulation) und Projektauftrag. Der Projektauftraggeber budgetiert auf dieser Basis das Vorhaben
und genehmigt den Projektauftrag (die erste Projektfortschrittsentscheidung des Projekts).

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

B.2 Inhalte des V-Modell XT Bund

29

Abbildung 29: Disziplin Anbahnung und Organisation

Mit genehmigtem Projektauftrag wird die Projektorganisation ins Leben gerufen. Der Projektleiter erstellt
eine   erste   Version   des  Projekthandbuch
 s    mit   den   Projektzielen,   "Spielregeln"   (z.B.   Jour   fixes   und
Berichtswege),   einer   ersten   Planung   sowie   der   Rollenbesetzung.   Dort   benennt   er   mindestens   den   QS-
Verantwortlichen   und   den   KM-Verantwortlichen,   die   wiederum   eine   erste   Version   des  QS-Handbuch
 s
ausarbeiten und die  Produktbibliothek  einrichten. Nach Abschluss dieser Arbeiten werden die Ergebnisse
(Produkte) dem Projektmanager zum Entscheidungspunkt  Projekt initialisiert  vorgelegt. Mit dem Projekt-
Kick-off beginnt dann die Durchführungsphase.

Verantwortliche und
Produkte

Projektauftraggeber:
Projektauftrag, Projektvorstudie
Projekteigner:
Checkliste Informationssicherheit
Projektleiter:
Informationssicherheits-Navigator, Projekthandbuch

B.2.1.2 Planung und Steuerung

Die Disziplin Planung und Steuerung enthält die für das Projektmanagement notwendigen Produkte. Die
Basis ist die jeweils letzte Projektfortschrittsentscheidung zusammen mit den darin enthaltenen Planvorgaben
und Rahmenbedingungen. Der Projektleiter arbeitet die Vorgaben in den Projektplan als zentralem Produkt
der Disziplin ein und berücksichtigt dabei Schätzung

 en    und Fortschreibungen der WiBe.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland




30

 Konzepte und Inhalte des V-Modell XT Bund

Abbildung 30: Disziplin Planung und Steuerung

Der Projektplan umfasst neben dem klassischen  Projektstrukturplan  auch weitere "Sichten", wie etwa den
Produktstrukturplan oder den Termin- und Ablaufplan. Der Projektplan sollte immer realistisch und erfüllbar
sein und muss mindestens vor jedem Entscheidungspunkt aktualisiert werden.

Das Projektteam wird über die  Aufgabenliste  gesteuert, die den Projektplan weiter verfeinert. Vor jedem
Entscheidungspunkt   verfasst   der   Projektleiter   einen  Projektstatusbericht  (Berichtswesen)   für   den
Lenkungsausschuss  und berichtet darin über den aktuellen Projektstand und die Planung für den nächsten
Projektabschnitt.
in   der
  Die
Projektfortschrittsentscheidung dokumentiert.

  Entscheidungen   des

  Lenkungsausschusses

  werden

Verantwortliche und
Produkte

Projektauftraggeber:
WiBe (Vorkalkulation)
Projekteigner:
Projektfortschrittsentscheidung
Projektleiter:
Aufgabenliste, Projektplan, Schätzung, WiBe (Fortschreibung)

B.2.1.3 Risikomanagement

Risikomanagement bedeutet, mit den Projektrisiken geordnet und strukturiert umzugehen: Es gilt, Risiken zu
erkennen,   darauf   hinzuwirken,   dass   sie   nicht   eintreten   oder   sich   gezielt   auf   das   Eintreten   von   Risiken
vorzubereiten.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

B.2 Inhalte des V-Modell XT Bund

31

Abbildung 31: Disziplin Risikomanagement

Die Disziplin Risikomanagement enthält die  Risikoliste  als zentrales, vom Projektleiter  geführtes Produkt.
Organisation und Vorgaben zum Risikomanagement werden im Projekthandbuch beschrieben; hierzu zählen
beispielsweise   die   Definition   von   Risikostufen   oder   die   Zeitpunkte   für   die   Identifizierung   oder
Neubewertung von Risiken. Der Projektleiter trägt die Verantwortung für das Risikomanagement und das
Führen der Risikoliste. Er kann jedoch nicht alle Risiken selbst erkennen und sollte das Thema daher fest im
Projektteam verankern, sodass er über neu erkannte Risiken umgehend informiert wird. Es empfiehlt sich,
Projektrisiken   als   festen  Agendapunkt   in   den   Jour   fixes   zu   behandeln.   Das   operative   Management   von
Risiken   kann   bei   großen   Projekten   an   einen  Risikomanager  delegiert   werden;   die  Verantwortung   bleibt
allerdings beim Projektleiter.

Die  Projektstatusbericht
 e    enthalten   eine   Zusammenfassung   der   aktuellen   Projektrisiken,   sodass   sich   das
Management einen schnellen Überblick über das Risikopotential des Projekts verschaffen kann. In einer
Projektfortschrittsentscheidung kann festgelegt werden, wie mit bestimmten Risiken umzugehen ist.

Verantwortliche und
Produkte

Projektleiter:
Risikoliste

B.2.1.4 Problem- und Änderungsmanagement

In   jedem   Projekt   tauchen   Probleme   und   Änderungswünsche   auf,   mit   denen   geordnet   und   strukturiert
umgegangen werden muss. Die Disziplin Problem- und Änderungsmanagement enthält alle Produkte, die für
einen Änderungsprozess notwendig sind.

Abbildung 32: Disziplin Problem- und Änderungsmanagement

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


32

 Konzepte und Inhalte des V-Modell XT Bund

Der Startpunkt ist die Problemmeldung / der Änderungsantrag. Gemeldet / beantragt werden kann sowohl
aus dem Projektumfeld (1a) als auch aus dem Projekt heraus (1b). Ein Änderungsverantwortlicher erfasst die
Problemmeldung / den Änderungsantrag in der  Änderungsstatusliste  und organisiert die Bewertung nach
Relevanz,   Machbarkeit,   Dringlichkeit   und   sonstiger   Kriterien.   Die   Änderungssteuerungsgruppe   trifft   auf
dieser   Basis   eine  Änderungsentscheidung,   beispielsweise   die   Annahme   des   Änderungsantrags   samt
Umsetzung   in   der   nächsten   Iteration.   Durch   die   Änderungsentscheidung   können   Konsequenzen   wie
Planänderungen oder Vertragsanpassungen entstehen.

Die Details des Vorgehens und die Verantwortlichkeiten werden im Projekthandbuch im Kapitel Organisation
und Vorgaben zum Problem- und Änderungsmanagement festgelegt.

Verantwortliche und
Produkte

Änderungssteuerungsgruppe (Change Control Board):
Änderungsentscheidung
Änderungsverantwortlicher:
Änderungsstatusliste, Problem-/Änderungsbewertung,
Problemmeldung/Änderungsantrag

B.2.1.5 Konfigurationsmanagement

Das   Konfigurationsmanagement   sorgt   dafür,   dass   alle   im   Projekt   erstellten   Ergebnisse   nachvollziehbar
abgelegt und gesichert werden. Das zentrale Produkt ist die Produktbibliothek, die alle im Projekt erstellten
Produktexemplare in sämtlichen Produktversionen vorhält (siehe Produkttypen und Produktexemplare).

Abbildung 33: Disziplin Konfigurationsmanagement

Die   Produktbibliothek   sollte   durch   geeignete   Werkzeuge   realisiert   werden,   beispielsweise   durch   ein
Dokumentenmanagement- und/oder ein Versionsverwaltungssystem. Verantwortlich für deren Einrichtung
und die Organisation der Ablagestruktur ist der KM-Verantwortliche, der zudem nach den Vorgaben des
Projekthandbuch
 s    und   mindestens   zu   jedem   Entscheidungspunkt   eine  Produktkonfiguration  (Baseline)
erstellt.   Eine   Produktkonfiguration   dokumentiert   den   Projektstand   zu   einem   Zeitpunkt   und   enthält   die
aktuellen (und untereinander  konsistenten!) Produktversionen in einer  Weise,  dass  darauf im Bedarfsfall
zurückgegriffen werden kann.

Verantwortliche und
Produkte

Informationssicherheitsbeauftragter:
Informationssicherheits-Managementsystem
KM-Verantwortlicher:
Produktbibliothek, Produktkonfiguration

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


B.2 Inhalte des V-Modell XT Bund

B.2.1.6 Qualitätssicherung

33

In der Disziplin Qualitätssicherung werden die Qualitätsziele des Projekts definiert und qualitätssichernde
Maßnahmen   geplant   und   durchgeführt.   Konstruktive   QS-Maßnahmen   definieren   Vorgaben   für   die
Produkterstellung zur Erreichung der Qualitätsziele. Analytische QS-Maßnahmen prüfen, ob die Vorgaben
eingehalten und die Qualitätsziele erreicht wurden.

Der QS-Verantwortliche definiert im  QS-Handbuch  die Qualitätsziele und die QS-Maßnahmen sowie die
 e  , mit denen er die Qualität im Projekt darstellt. Dort regelt er auch,
Inhalte der regelmäßigen  QS-Bericht
unter   welchen   Umständen   ein   außerplanmäßiger   QS-Bericht   geschrieben   wird.   Der   QS-Verantwortliche
wirkt über die QS-Planung am Projektplan mit und führt bei Bedarf eine Nachweisakte, in der er Protokolle
nachzuweisender Prüfungen (z.B. von externen Prüfstellen wie dem TÜV gefordert) sammelt.

Abbildung 34: Disziplin Qualitätssicherung

Das QS-Handbuch kann für bestimmte Produkte eine unabhängige Qualitätssicherung fordern. Unabhängig
bedeutet hierbei, dass der Prüfer nicht der Ersteller des Produkts ist. Der Prüfer prüft das Produkt anhand
einer   Prüfspezifikation  und  notiert   die   Ergebnisse   in  einem  Prüfprotokoll.   Systemelemente   können  (und
sollten) mit einer regressionsfähigen Prüfprozedur (z.B. Unit-Tests) geprüft werden.

Verantwortliche und
Produkte

Betriebsverantwortlicher:
Prüfprotokoll Inbetriebnahme, Prüfspezifikation Inbetriebnahme
Prüfer:
Abnahmeprotokoll, Abnahmespezifikation, Prüfprotokoll, Prüfprotokoll
Systemelement, Prüfprozedur Systemelement, Prüfspezifikation,
Prüfspezifikation Systemelement
QS-Verantwortlicher:
Nachweisakte, QS-Handbuch

B.2.1.7 Messung und Analyse

Die Disziplin Messung und Analyse beschreibt die Definition und Nutzung von Kennzahlen (Metriken) und
Messdaten.   Der   Einsatz   von   Kennzahlen   liefert   sowohl   quantitative   als   auch   qualitative  Aussagen   zu
verschiedenen Fragestellungen im Projekt, die sich aus den Projektzielen ableiten (Goal-Question-Metric).
Kennzahlen   sind   damit   die   Grundlage   für   effektives   und   objektives   Projektcontrolling   und   bilden   ein
wichtiges Instrument zur Steuerung von Projekten. Darüber hinaus dienen Kennzahlen zum Aufbau von
Erfahrungswissen in einer Organisation, das beispielsweise die Planung in anderen Projekten erleichtert,
oder zur Informationsgewinnung über die Güte von Teilprozessen, um systematische Fehler zu erkennen.
Nicht zur Zielsetzung von Kennzahlen gehören die Kontrolle oder Leistungsbewertung einzelner Mitarbeiter.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


34

 Konzepte und Inhalte des V-Modell XT Bund

Abbildung 35: Disziplin Messung und Analyse

Verantwortlich für die Messung und Analyse im Projekt ist der  Projektleiter. Idealerweise kann er die im
Projekt   verwendeten   Kennzahlen   aus   einem   organisationsweiten   Metrikkatalog   auswählen   und   im
Projekthandbuch  um projektspezifische Details wie z.B. Erhebungszeitpunkte oder Grenzwerte ergänzen.
Der Projektleiter ist auch für die Erhebung der Messdaten verantwortlich, wobei diese in der Praxis entweder
vom Projektteam manuell erfasst oder automatisiert gesammelt werden.

In regelmäßigen Abständen werden auf Basis der Messdaten die relevanten Kennzahlen berechnet und als
Kennzahlenauswertung  dokumentiert. Diese erläutert auch, wie die Kennzahlen zu interpretieren sind. Die
Kennzahlenauswertungen   sind   die   Grundlage   für   das   Berichtswesen   und   dienen   als   Eingabe   für   die
Erfahrungsdatenbasis der Organisation.

Verantwortliche und
Produkte

Projektleiter:
Kennzahlenauswertung, Messdaten

B.2.1.8 Berichtswesen

Die Disziplin Berichtswesen enthält alle Produkte, die zur Kommunikation innerhalb des Projekts und mit
dem Projektumfeld dienen. Ausgestaltet und konkretisiert wird die Disziplin im Projekthandbuch, welches
Vorgaben   für  Berichtswesen   und   Kommunikationswege  definiert.   Beispielsweise   kann   dort   festgelegt
werden,   dass   zu   jeder   Besprechung   ein   Protokoll   erstellt   wird   und   in   welcher   Form   solche
 e    die Ergebnisse, Beschlüsse und Arbeitsaufträge dokumentieren. Der  Projektleiter
Besprechungsdokument
trägt die Verantwortung dafür, dass die Vorgaben des Projekthandbuchs umgesetzt werden und im Beispiel
jede   Besprechung   protokolliert   wird.   Er   kann   die   entsprechenden   Tätigkeiten   (im   Beispiel   das
Protokollieren) delegieren.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


B.2 Inhalte des V-Modell XT Bund

35

Abbildung 36: Disziplin Berichtswesen (Projektdurchführung)

Das zentrale Produkt im Berichtswesen ist der vom Projektleiter zu jedem Entscheidungspunkt vorzulegende
Projektstatusbericht.   In   ihm   finden   sich   die   aktuellen   Projektergebnisse   und   entscheidungsrelevante
Informationen   aus   der  Risikoliste,   dem  Projektplan,   der  Änderungsstatusliste  und   anderen   Produkten   in
aufbereiteter Form. Auf dieser Grundlage kann sich der Lenkungsausschuss einen schnellen Überblick über
den Stand des Projekts verschaffen und eine qualifizierte Projektfortschrittsentscheidung treffen.

Der QS-Verantwortliche erstellt den QS-Bericht, dessen Zusammenfassung als Qualitätsbewertung in den
Projektstatusbericht einfließt.

Abbildung 37: Disziplin Berichtswesen (Projektabschluss)

Zum Projektabschluss schreibt der Projektleiter einen  Projektabschlussbericht. Inhaltlich entspricht er dem
Projektstatusbericht bis auf die "vorausblickenden" Themen, die nicht enthalten sind. Stattdessen führt er
Projekterfahrungen ("Lessons learned") auf, die der Projektleiter ggf. aus dem Projekttagebuch übernehmen
kann.   In   AG-Projekten   fließt   der   Projektabschlussbericht   des   Auftragnehmers   in   den   eigenen
Projektstatusbericht   ein.   Die   Adressaten   des   Projektabschlussberichts   sind   im   Kapitel  Projekt-Ende
beschrieben.   Innerhalb   einer   "lernenden   Organisation"   sollte   der   Bericht   auch   dem   Verwalter   der
Erfahrungsdatenbasis   zugehen,   der   die   Projekterfahrungen  in  die   Erfahrungsdatenbasis   einpflegt   und   sie
damit Folgeprojekten verfügbar macht.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

36

 Konzepte und Inhalte des V-Modell XT Bund

Verantwortliche und
Produkte

Projektleiter:
Besprechungsdokument, Projektabschlussbericht, Projektabschlussbericht (von
AN), Projektstatusbericht, Projektstatusbericht (von AN), Projekttagebuch
QS-Verantwortlicher:
QS-Bericht

B.2.2 Entwicklung
Das V-Modell ist ein Vorgehensmodell für  Systementwicklungsprojekte. Es unterscheidet zwischen einem
Gesamtsystem und einem System:

➢ Das  Gesamtsystem  im   V-Modell   entspricht   dem   Systembegriff   der   ISO/IEC   12207:   Es   ist   „ein
einheitliches Ganzes, das aus einem oder mehreren Prozessen, Hardware, Software, Einrichtungen
und   Personen   besteht,   das   die   Fähigkeit   besitzt,   vorgegebene   Forderungen   oder   Ziele   zu
befriedigen.“ (siehe Abbildung 38 rechts).

➢ Unter   einem  System  wird   im  V-Modell   XT  Bund   ein   einheitliches   Ganzes   verstanden,   das   aus
Software   und   der   zur  Ausführung   notwendigen   beigestellten   Hardware   besteht.   (Die   Hardware-
Entwicklung wird vom V-Modell XT Bund im Gegensatz zum V-Modell XT nicht unterstützt.)

Abbildung 38: System und Gesamtsystem in Entwicklung und Betrieb

Aus der Entwicklungssicht reduziert sich das Gesamtsystem auf ein zu entwickelndes System und beliebig
viele zu erstellende Logistische Unterstützungsdokumentationen. Darüber hinaus kann das Gesamtsystem
beliebig viele weitere, unterstützende Systeme enthalten, die beispielsweise zum Betrieb oder zum Test des
 e    bestehen   aus   Systemelementen,   die  Logistische
"eigentlichen"   Systems   benötigt   werden.
Unterstützungsdokumentation  besteht   aus   Logistikelementen.  Alle   Systemelemente   und   Logistikelemente
sind als Produkte im V-Modell definiert; das Gesamtsystem selbst ist kein Produkt.

 System

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


B.2 Inhalte des V-Modell XT Bund

37

Abbildung 39: Strukturelle Produktabhängigkeiten und Produktumfänge der einzelnen Systemelemente

Ein  System besteht  aus  Segmenten,  Einheiten,   Komponenten  und Modulen,  die  hierarchisch strukturiert
werden. Im Kontext jedes Systemelements kann eine Menge von Entwicklungsdokumentationen existieren,
die als Produktumfang des Systemelements bezeichnet werden. Beispielsweise muss sich im Produktumfang
jeder SW-Einheit genau eine entsprechende SW-Architektur befinden. Die Definition der Systemstruktur und
die Ausgestaltung der dazugehörigen Produktumfänge  erfolgen im Rahmen des Systementwurfs und der
Systemspezifikation. Ein derart zerlegtes System erleichtert die Schätzung der Aufwände und Kosten für die
Erstellung seiner Bestandteile.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

38

 Konzepte und Inhalte des V-Modell XT Bund

Das in der Abbildung 40 dargestellte V-förmige Vorgehen fußt auf vier Prinzipien:

Abbildung 40: V-Modell-Entwicklungsprozess im Überblick

➢ Spezifikation und Zerlegung: Auf dem absteigenden Ast des „Vs“ wird das Gesamtsystem bis auf die
Modulebene dekomponiert und dabei immer feiner spezifiziert. Der Auftraggeber legt im Lastenheft
(Anforderungen) fest, was das System leisten soll. Im Pflichtenheft (Gesamtsystementwurf) definiert
der  Auftragnehmer,   wie   er   die  Anforderungen   umsetzt.   Dazu   erstellt   er   eine  Systemarchitektur,
Systemspezifikation
 en     und   ein   Konzept   für   die   Implementierung,   Integration   und   Prüfung   des
Systems (IIPK System). Im letzten Dekompositionsschritt bestimmt er die SW-Einheiten und die
jeweiligen SW-Architektur

 en   , IIPKs SW und SW-Spezifikation

 en   .

➢ Realisierung   und   Integration:  Auf   dem   aufsteigenden   Ast   des   „Vs“   werden   die   System-   und
Logistikelemente   implementiert   und/oder   beschafft   und   zum   (Gesamt-)System   integriert.   Auf
unterster   Ebene   werden   zunächst   die  SW-Einheit
 en
zusammengefasst und anschließend mit den Externen Einheiten zum System integriert. Abschließend
werden (auf Gesamtsystemebene) Lieferung

 en     realisiert.   Diese   werden   zu  Segment

 en    zusammengestellt und ausgeliefert.

➢ Verifikation   und   Validierung:  Auf   jeder   (waagrechten)  Abstraktionsstufe   finden   Prüfschritte   zur
Verifikation und Validierung statt. Hier wird überprüft, ob die Systemelemente ihrer Spezifikation
entsprechen und ob Sie das benötigte Verhalten zeigen. Die Prüfspezifikationen (absteigender Ast)
leiten   sich   aus   den   Anforderungen,   Spezifikationen   und   Architekturen   ab.   Die   Prüfprotokolle
(aufsteigender   Ast)   beschreiben   das   Prüfergebnis   eines   konkreten   Prüfobjekts,   also   eines
Systemelements, eines Logistikelements oder einer Lieferung.

➢ Iterationen und Inkremente:  Das „V“ wird in der Regel mehrfach in  Iteration

 en     durchlaufen. Die
Systemfunktionalität   wächst   dabei   stetig   (inkrementelles   Vorgehen),   bis   schließlich   alle
Anforderungen erfüllt werden. Dabei erlaubt das V-Modell unterschiedliche Reihenfolgen für den
„V-Durchlauf“: Während die Inkrementelle Systementwicklung dem Weg des „V“s unmittelbar folgt
(I1-I8),   durchläuft   die   Prototypische   Entwicklungsstrategie   die   Entscheidungspunkte   in   anderer
Reihenfolge   (P1-P8).   Darüber   hinaus   sind   in   beiden   Strategien   Iterationen   auf   feineren
Abstraktionsebenen möglich.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland








B.2 Inhalte des V-Modell XT Bund

B.2.2.1 Systemelemente

39

Die   Disziplin   Systemelemente   beinhaltet   alle   Bestandteile   eines   Systems,   die   im   Rahmen   der
Systemerstellung zu entwickeln, ggf. zu beschaffen und zu integrieren sind. Jedes Produkt der Disziplin wird
verallgemeinernd als Systemelement bezeichnet.

Abbildung 41: Disziplin Systemelemente (Beispielhafte Systemstruktur)

Die Bausteine der Systemstruktur werden durch strukturelle Produktabhängigkeiten modelliert: Ein System
besteht aus Einheiten, die zu Segment
 en    gruppiert werden können. Ein Segment kann selbst aus Segmenten
bestehen. Das im Beispiel gezeigte System besteht beispielsweise aus 5 Einheiten, wovon 4 im Segment
Webserver gruppiert sind. Für den Zusammenbau des Systems aus den Einheiten ist der  Systemintegrator
verantwortlich, der dafür den Integrationsbauplan aus dem Implementierungs-, Integrations- und Prüfkonzept
System verwendet.

Einheiten unterscheiden sich in SW-Einheiten und externe Einheiten. SW-Einheiten sind Systemelemente,
die rein aus Software (SW) bestehen und im Projekt durch  SW-Entwickler  entwickelt werden. Eine SW-
Einheit besteht aus SW-Modul

 en    und kann durch SW-Komponente

 n   hierarchisch gegliedert werden.

Externe Einheiten sind Systemelemente, die aus Hard- und/oder Software bestehen und nicht im Rahmen des
Projekts entwickelt werden. Dies kann folgende Gründe haben:

➢ Das Systemelement wird (z.B. aus früheren Projekten) wiederverwendet.

➢ Das Systemelement ist ein am Markt verfügbares Fertigprodukt.

➢ Das Systemelement wird durch den Auftraggeber beigestellt.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland




40

 Konzepte und Inhalte des V-Modell XT Bund

➢ Das Systemelement wird im Rahmen eines Unterauftrags entwickelt. Dies gilt nicht für Hardware,

da Hardware generell nicht im Rahmen von V-Modell XT Bund-Projekten entwickelt wird.

Gleiches gilt für Externe SW-Module. In reinen Integrationsprojekten besteht das System ausschließlich aus
externen Einheiten, eine Entwicklung von SW findet nicht statt. Für die Beschaffung von externen Einheiten
ist der Systemintegrator verantwortlich.

Verantwortliche und
Produkte

SW-Entwickler:
Externes SW-Modul, SW-Einheit, SW-Komponente, SW-Modul
Systemintegrator:
Externe Einheit, Segment, System

B.2.2.2 Systemanalyse

Die   Disziplin  Systemanalyse   umfasst   alle   Produkte,   die   dafür   vorgesehen  sind,   die   Eigenschaften   eines
Systems  oder  einzelner  Systemelemente  zu  untersuchen und zu dokumentieren.  Dabei  kann sich das  zu
untersuchende System(element) bereits im Einsatz befinden, auf dem Markt angeboten werden oder noch in
der Entwicklung oder in den Köpfen der Anwender sein.

Abbildung 42: Disziplin Systemanalyse (AG-Seite)

Der Anforderungsanalytiker (AG) ermittelt die gewünschten Eigenschaften eines zu entwickelnden Systems
z.B. durch Anwenderbefragungen und Workshops und dokumentiert diese als  Lastenheft (Anforderungen).
Er bewertet die Anforderungen in der  Anforderungsbewertung, z.B. hinsichtlich ihrer Machbarkeit, ihrer
Finanzierbarkeit oder der Notwendigkeit.

Auf der AG-Seite kann der Projektleiter eine Marktsichtung für Fertigprodukte erstellen (lassen), um diese in
die   Anforderungen   oder   die   Anforderungsbewertung   einfließen   zu   lassen.   Eine   Marktsichtung   kann
beispielsweise dazu dienen, die Anforderungen so zu definieren, dass sie den Einsatz von Fertigprodukten
nicht   ausschließen.   Bei   der   Anforderungsbewertung   kann   sie   dabei   helfen,   die   Machbarkeit   und
Finanzierbarkeit von Anforderungen besser abzuschätzen.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

B.2 Inhalte des V-Modell XT Bund

41

Abbildung 43: Disziplin Systemanalyse (AN-Seite)

Auch in einem AG/AN-Projekt kann der Projektleiter eine Marktsichtung für Fertigprodukte durchführen, in
der er beispielsweise den Funktionsumfang von Schnittstellen sowie Preise und Lizenzen von potentiell im
System einsetzbaren Systemelementen aufführt und damit eine Make-or-Buy-Entscheidung vorbereitet.

Der Ergonomieverantwortliche untersucht die Interaktion der Anwender mit dem zu entwickelnden System.
Die   Untersuchung   kann   dabei   rein   auf   der   Systemvision   des  Auftraggebers,   aber   auch   auf   Basis   von
Systemprototypen   durchgeführt   werden.   Seine   Ergebnisse   fasst   er   in   der  Anwenderaufgabenanalyse
zusammen.

Der  Systemarchitekt  analysiert   ein   bestehendes   Altsystem   im   Rahmen   der  Altsystemanalyse  und
dokumentiert hier beispielsweise die verwendete Architektur, Schnittstellen und Datenstrukturen. Er greift
dabei   –   sofern   vorhanden   –   auf   bestehende   Systemdokumentationen   zurück   oder   spricht   direkt   mit
Anwendern, Betreuern und Entwicklern des Altsystems.

Auch ein System, das sich gerade in der Entwicklung befindet, kann zum Analysegegenstand werden. Die
Grundlage   der  Analyse   sind   hier   Spezifikations-   und   Entwurfsdokumente   sowie   Systemprototypen.   Die
Personalvertretung   kann   das   entstehende   System   beispielsweise   hinsichtlich   der  Auswirkungen   auf   den
Arbeitslauf oder potentieller Möglichkeiten zur Leistungsüberwachung untersuchen.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

42

 Konzepte und Inhalte des V-Modell XT Bund

Verantwortliche und
Produkte

Anforderungsanalytiker (AG):
Anforderungsbewertung, Bewertung Lastenheft Gesamtprojekt, Lastenheft
(Anforderungen), Lastenheft Gesamtprojekt
Datenschutzverantwortlicher:
Vorgaben zum Datenschutz
Ergonomieverantwortlicher:
Anwenderaufgabenanalyse
Fachverantwortlicher:
Checkliste für das Interview zur Schutzbedarfsfeststellung,
Schutzbedarfsfeststellung
Informationssicherheitsverantwortlicher:
Vorgaben zur Informationssicherheit
Projektleiter:
Make-or-Buy-Entscheidung, Marktsichtung für Fertigprodukte
Systemarchitekt:
Altsystemanalyse

B.2.2.3 Systementwurf

Einstiegspunkt   für   den   Systementwurf   ist   das  Pflichtenheft   (Gesamtsystementwurf),   das   vom
Anforderungsanalytiker (AN) verantwortet wird. Das Produkt beschreibt, was das Gesamtsystem letztendlich
leisten   wird.   Dabei   werden   die   funktionalen   und   nichtfunktionalen  Anforderungen   aus   dem   Lastenheft
übernommen und in Vorbereitung auf die Systementwicklung detailliert. Die Anforderungsverfolgung zum
Lastenheft zeigt auf, wie sich die Anforderungen in Lasten- und Pflichtenheft aufeinander abbilden. Der
Gesamtsystementwurf   definiert   auch   die   Gesamtsystemarchitektur   und   identifiziert   damit   die   zu
entwickelnden Systeme und den Umfang der logistischen Unterstützung.

Abbildung 44: Disziplin Systementwurf (Gesamtsystementwurf)

Die   übrigen   Produkte   der   Disziplin   Systementwurf   beschreiben   den   prinzipiellen   Aufbau   und   die
querschnittlichen   Eigenschaften   der   zuvor   im   Pflichtenheft   identifizierten   Systeme   ohne   dabei   auf   die
Funktionsweise   einzelner   Systemelemente   im   Detail   einzugehen.   Dies   ist   dann   Inhalt   der   Disziplin
Systemspezifikation, die eng mit dem Systementwurf verbunden ist.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

B.2 Inhalte des V-Modell XT Bund

43

Abbildung 45: Disziplin Systementwurf

Hauptverantwortlich für den Systementwurf sind die Architekten mit den von ihnen erstellten Architekturen
und Implementierungs-, Integrations- und Prüfkonzepten (IIPKs). Bei den Rollen und Produkten existieren
jeweils spezifische Ausprägungen für das System (z.B.  Systemarchitekt) und die SW-Einheiten (z.B.  SW-
Architektur). Obwohl sich Unterschiede in den Details und unterschiedliche Verantwortlichkeiten ergeben,
sind die Architektur-Produkte alle gleich aufgebaut, sodass sich ein einheitliches Entwurfsprinzip ergibt.

Auf   Systemebene   erstellt   der   Systemarchitekt   zum   Entscheidungspunkt
 System   entworfen  die
Systemarchitektur und das zugehörige IIPK. Die Systemarchitektur enthält die Dekomposition des Systems
und das IIPK den Integrationsbauplan: Beide Themen enthalten eine Zerlegung des Systems bis hinunter auf
die Ebene von Einheiten. Während die Architektur sich tendenziell eher auf Typebene bewegt, definiert der
Integrationsbauplan konkrete Exemplare der einzelnen Systemelemente.

Auf der Ebene von SW-Einheiten setzt sich das gezeigte Entwurfsprinzip analog fort. Eine Ausnahme von
dem Prinzip bilden Datenbanken: Werden Datenbanken in der System- oder SW-Architektur identifiziert, so
beschreibt der SW-Architekt Datenmodell und Konfiguration der Datenbank in einem Datenbankentwurf und
nicht innerhalb der Architektur.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

44

 Konzepte und Inhalte des V-Modell XT Bund

Verantwortliche und
Produkte

Anforderungsanalytiker (AN):
Pflichtenheft (Gesamtsystementwurf)
Datenschutzverantwortlicher:
Erweiterung der Vorgaben zum Datenschutz
Ergonomieverantwortlicher:
Mensch-Maschine-Schnittstelle (Styleguide)
Informationssicherheitsverantwortlicher:
Erweiterung der Vorgaben zur Informationssicherheit, Sicherheitskonzeption
SW-Architekt:
Datenbankentwurf, Implementierungs-, Integrations- und Prüfkonzept SW, SW-
Architektur
Systemarchitekt:
Implementierungs-, Integrations- und Prüfkonzept System, Migrationskonzept,
Systemarchitektur

B.2.2.4 Systemspezifikation

Die   Produkte   der   Disziplin   Systemspezifikation  beschreiben   die  Anforderungen   und   die   Funktionsweise
einzelner   Systemelemente   und   der   logistischen   Unterstützung.   Hauptbestandteil   der   Disziplin   sind   die
Spezifikationen, die hier als Oberbegriff für Systemspezifikationen, SW-Spezifikationen und „Externe(s)-...-
Spezifikationen“ verwendet werden. Eine Spezifikation gibt einen Überblick über das Systemelement und
beschreibt   dessen   funktionale   Anforderungen   (Schnittstellenbeschreibung)   und   nichtfunktionale
Anforderungen, jeweils als Black-Box-Sicht. System- und SW-Spezifikationen beschreiben außerdem die
interne Schnittstellenrealisierung sowie die Verfeinerung der nichtfunktionalen Anforderungen (Glass-Box-
Sicht/White-Box-Sicht). Nachfolgend sind die Prinzipien und Inhalte der Disziplin anhand einer SW-Einheit
beschrieben.   Für   die   Beschreibung   der  SW-Einheit  und   der   zugehörigen   SW-Elemente   werden  SW-
Spezifikation
 en     und   bei   Bedarf   Externe-SW-Modul-Spezifikation   verwendet.   Die   Prinzipien   lassen   sich
analog auf Systeme übertragen.

Abbildung 46: Disziplin Systemspezifikation (Abdeckungsbereich einzelner SW-Spezifikationen)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


B.2 Inhalte des V-Modell XT Bund

45

Das aus der Disziplin Systementwurf stammende Produktexemplar SW-Architektur für die Webanwendung
benennt die für die Webanwendung zu spezifizierenden Systemelemente, im Beispiel also diejenigen  SW-
Komponente
 e  , für die eine eigenständige Spezifikation erstellt werden soll (SWK2, SWK3
und SWM2). Das V-Modell gibt nicht vor, dass für jedes Systemelement eine eigene Spezifikation erstellt
werden muss.

 n   und SW-Modul

Ein   Spezifikationsdokument   beschreibt   die   Funktionsweise   eines   Systemelements   bis   „hinunter“   zur
nächsten   Spezifikationsebene:   Im   Beispiel   würde   also   die   SW-Spezifikation   Webanwendung   die
Funktionsweise der SW-Einheit bis zur Schnittstelle der SW-Komponenten SWK2 und SWK3 beschreiben.
Die vollständige Schnittstelle und die Spezifikation der beiden SW-Komponenten finden sich dann in der
SW-Spezifikation SWK2/SWK3. Prinzipiell ist es also möglich, dass für eine SW-Einheit nur eine einzige
SW-Spezifikation   erstellt   wird,   die   das   gesamte   Systemelement   bis   hinunter   zur   Modulebene   abdeckt;
welcher Detaillierungsgrad sinnvoll ist, muss individuell festgestellt werden.

Verantwortliche und
Produkte

SW-Architekt:
Externes-SW-Modul-Spezifikation, SW-Spezifikation
Systemarchitekt:
Externe-Einheit-Spezifikation, Systemspezifikation

B.2.2.5 Logistikelemente

Die   Disziplin   Logistikelemente   beinhaltet   die   vom   Technischen   Autor   erstellte   Dokumentation   zur
Unterstützung   der
 Logistische
Unterstützungsdokumentation, die Ausbildungsunterlagen und eine Nutzungsdokumentation enthalten kann.

  Oberstes   „Containerprodukt“

  Systemnutzung.

  die

ist

Bei   Entwicklungsprojekten   können   bereits   im  Pflichtenheft   (Gesamtsystementwurf)  Anforderungen
bezüglich der Nutzungsdokumentation und der notwendigen Ausbildungsunterlagen erfasst werden.

Abbildung 47: Disziplin Logistikelemente

Verantwortliche und
Produkte

Technischer Autor:
Ausbildungsunterlagen, Logistische Unterstützungsdokumentation,
Nutzungsdokumentation

B.2.2.6 Softwareentwicklung nach Scrum (AG)

Bei der Softwareentwicklung nach Scrum werden die Anforderungen an das System nicht zu Projektbeginn,
sondern im  Projektverlauf   auf   Grundlage   regelmäßiger  Zwischenergebnisse  festgelegt.   Der  Auftraggeber
erstellt   hierfür   zunächst   ein  Anforderungskonzept,   welches   eine   grobe   Leistungsbeschreibung   des
gewünschten Systems enthält. Dieses bildet die Grundlage für die Ausschreibung bzw. die Auftragsvergabe
an einen IT-Dienstleister des Bundes.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland



46

 Konzepte und Inhalte des V-Modell XT Bund

Abbildung 48: Disziplin Softwareentwicklung nach Scrum (AG)

Die anschließende Entwicklung des Systems erfolgt in kurzen, aufeinanderfolgenden Zyklen (Sprints) mit
einer   Dauer   von   jeweils   maximal   4   Wochen.   Vor   Beginn   des   ersten   Sprints   wird   auf   Basis   des
Anforderungskonzept
 s    das  Product Backlog  erstellt. Dieses enthält eine nach Priorität geordnete Liste der
umzusetzenden Anforderungen in Form von User Stories und Epics und wird während des gesamten Projekts
verfeinert   und   fortgeschrieben.   Verantwortlich   für   das  Product   Backlog  ist   der  Product   Owner,   ein
Mitarbeiter   des   Auftraggebers,   der   im   Projekt   des   Auftragnehmers   mitwirkt   und   die   Interessen   des
Auftraggebers vertritt. Zu diesem Zweck arbeitet der Product Owner direkt mit dem Scrum Master und dem
Entwicklungsteam   zusammen.   Zu   Beginn   jedes   Sprints   werden   die   am   höchsten   priorisierten   Backlog-
Einträge durch das Entwicklungsteam zur Bearbeitung im Sprint ausgewählt.

Nach Abschluss eines Sprints wird das darin erstellte Ergebnis als Inkrement an den Auftraggeber geliefert.
Ein Inkrement bildet einen lauffähigen Teil des Systems und kann in den IT-Betrieb überführt werden.

Verantwortliche und
Produkte

Product Owner:
Anforderungskonzept, Inkrement (von AN), Product Backlog

B.2.2.7 IT-Organisation und Betrieb

Der IT-Betrieb, der das zu entwickelnde System nach dessen Fertigstellung betreibt, ist frühzeitig in das
Projekt einzubinden. Die Disziplin IT-Organisation und Betrieb enthält alle Produkte, die zur Abstimmung
mit   der   IT-Organisation   und   dem   Betrieb   erforderlich   sind.  Abbildung   49  zeigt   zunächst   die   für   den
Auftraggeber relevanten Umfänge.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


B.2 Inhalte des V-Modell XT Bund

47

Abbildung 49: Disziplin IT-Organisation und Betrieb im AG-Projekt

Im Projekthandbuch des Auftraggebers wird die Zusammenarbeit mit dem IT-Betrieb geregelt. Hierzu gehört
die Beschreibung, auf Basis welcher Produkte geprüft wird, ob das entwickelte System den betrieblichen
Anforderungen genügt und unter welchen Voraussetzungen die  Betriebliche Freigabeerklärung erteilt wird.
Die   betrieblichen  Anforderungen   müssen   vom   Betriebsverantwortlichen   in   Form   der  Vorgaben   zum   IT-
Betrieb dokumentiert und dem Auftragnehmer als Teil der Vergabeunterlagen (Ausschreibung) bereitgestellt
werden.   Hierbei   kann   der   Auftraggeber   die   durch   dessen   Organisation   vorgegebenen   Lösungsräume
(Alternativen) für den Auftragnehmer einschränken. Bei der Beauftragung eines IT-Dienstleisters des Bundes
werden   diesem   die  Vorgaben   zum   IT-Betrieb  als   Bestandteil   der  Angebotsaufforderung  (anstelle   der
Ausschreibung) übermittelt.

In der  Leistungsvereinbarung (SLA/OLA/UC)  wird der Betrieb des Systems und die Qualität des Betriebs
  Der   Projektleiter   erstellt   das   Produkt   zusammen   mit   den
nach   Projektende   definiert.
Verfahrensverantwortlichen   (Fachseite,   IT-Betrieb,   Weiterentwicklung)   und   den  Anwender
 n  .   Die
Aushandlung erfolgt bereits im Projekt, wobei die Anforderungen an das System früh berücksichtigt werden
sollen.   Spätestens   zum   Entscheidungspunkt  Projekt   abgeschlossen  muss   die  Leistungsvereinbarung
(SLA/OLA/UC) fertig gestellt sein.

Die bei der Durchführung eines AG/AN-Projekts für die Auftragnehmer-Seite relevanten Umfänge sind in
Abbildung 50 dargestellt.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


48

 Konzepte und Inhalte des V-Modell XT Bund

Abbildung 50: Disziplin IT-Organisation und Betrieb im AG/AN-Projekt

Im Rahmen des Gesamtsystementwurfs überträgt der Auftragnehmer die Anforderungen aus dem Lastenheft
in   das   Pflichtenheft   und   beschreibt   deren   technische   Umsetzung.   Basierend   auf   der   gewählten   Lösung
entscheidet   der   Betriebsverantwortliche,   ob   auf   Ebene   des   Gesamtsystems   Erweiterungen   der   vom
Auftraggeber erstellten Vorgaben zum IT-Betrieb erforderlich sind. Notwendige Erweiterungen müssen mit
dem Auftraggeber abgestimmt werden und führen häufig zu Vertragszusätzen. Das beschriebene Vorgehen
setzt sich analog beim Grobentwurf (System-Ebene) und Feinentwurf (Einheiten-Ebene) fort.

Verantwortliche und
Produkte

Betriebsverantwortlicher:
Betriebliche Freigabeerklärung, Erweiterung der Vorgaben zum IT-Betrieb,
Vorgaben zum IT-Betrieb
Projektleiter:
Leistungsvereinbarung (SLA/OLA/UC)

B.2.2.8 Informationssicherheit und Datenschutz

Das   Ziel   der   Informationssicherheit   (Security)   ist   es,   den   Schutz   der   Vertraulichkeit,   Integrität,
Nichtabstreitbarkeit   und   Verfügbarkeit   von   Informationen   zu   gewährleisten.   Der   Datenschutz   (Privacy)
regelt die Umsetzung der datenschutzrechtlichen Vorgaben für den Umgang mit personenbezogenen Daten.
Die   Querschnittsdisziplin   Informationssicherheit   und   Datenschutz   erstreckt   sich   über   viele   andere
Disziplinen und betrifft sowohl AG- als auch AG/AN-Projekte.  Abbildung 51  zeigt zunächst die für den
Auftraggeber relevanten Umfänge im V-Modell.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

B.2 Inhalte des V-Modell XT Bund

49

Abbildung 51: Disziplin Informationssicherheit und Datenschutz im AG-Projekt

Bereits im Vorlauf eines Projekts muss geprüft werden, ob darin Aspekte der Informationssicherheit oder des
Datenschutzes   zu   berücksichtigen   sind.   Dafür   stellt   das   V-Modell   die  Checkliste   Informationssicherheit
bereit, die mit wenigen einfachen Kriterien eine Klärung herbeiführt. Der Auftraggeber nutzt das Ergebnis im
Tailoring  zur   Bestimmung  des   entsprechenden Projektmerkmals.  Bei  Relevanz  sind  im  Projekthandbuch
Vorgaben zur Informationssicherheit und zum Datenschutz aufzuführen, bspw. anzuwendende Methoden und
im   Projekthandbuch   müssen   der   Aufbau   des   organisationsweiten
Standards.
 s    (ISMS)   und   dessen   ggf.   notwendige,   projektspezifische
Informationssicherheits-Managementsystem
Erweiterungen beschrieben werden.

  Ebenfalls

In vielen Behörden existieren organisationsweit geltende Informationssicherheits- und Datenschutzkonzepte,
welche   bei   der   (Weiter-)Entwicklung   von   IT-Systemen   zu   berücksichtigen   sind.   Die   für   das   Projekt
relevanten   Auszüge   müssen   in   Form   der  Vorgaben   zur   Informationssicherheit  bzw.  Vorgaben   zum
Datenschutz  dokumentiert   und   dem   Auftragnehmer   als   Teil   der  Vergabeunterlagen   (Ausschreibung)
bereitgestellt   werden.   Hierbei   kann   der   Auftraggeber   die   durch   dessen   Organisation   vorgegebenen
Lösungsräume   (Alternativen)   für   den   Auftragnehmer   einschränken.   Zusätzlich   erstellt   der
Fachverantwortliche   des   zu   entwickelnden   IT-Systems   eine  Schutzbedarfsfeststellung,   die   ebenfalls   dem
Auftragnehmer zur Verfügung gestellt wird. Bei der Beauftragung eines IT-Dienstleisters des Bundes werden
diesem die zuvor genannten Produkte als Bestandteil der Angebotsaufforderung (anstelle der Ausschreibung)
übermittelt.

Die bei der Durchführung eines AG/AN-Projekts für die Auftragnehmer-Seite relevanten Umfänge sind in
Abbildung 52 dargestellt.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


50

 Konzepte und Inhalte des V-Modell XT Bund

Abbildung 52: Disziplin Informationssicherheit und Datenschutz im AG/AN-Projekt

Im Rahmen des Gesamtsystementwurfs überträgt der Auftragnehmer die Anforderungen aus dem Lastenheft
in   das   Pflichtenheft   und   beschreibt   deren   technische   Umsetzung.   Basierend   auf   der   gewählten   Lösung
entscheidet der Informationssicherheits- bzw. Datenschutzverantwortliche, ob auf Ebene des Gesamtsystems
eine  Sicherheitskonzeption  sowie   Erweiterungen   der   vom   Auftraggeber   erstellten   Vorgaben   zur
Informationssicherheit und zum Datenschutz erforderlich sind. Notwendige Erweiterungen müssen mit dem
Auftraggeber abgestimmt werden. Das beschriebene Vorgehen setzt sich analog beim Grobentwurf (System-
Ebene) und Feinentwurf (Einheiten-Ebene) fort.

B.2.3 AG/AN-Schnittstelle
Behörden   können   Dritte   mit   der   Erstellung   eines   Systems   beauftragen.   Hierbei   wird   zwischen   der
Beauftragung eines externen Dienstleisters und der eines IT-Dienstleisters des Bundes unterschieden (siehe
Projektmerkmal  Auftragnehmer). In beiden Fällen werden zwei getrennte V-Modell-Projekte durchgeführt:
ein Systementwicklungsprojekt (AG) in der Behörde als Auftraggeber und ein Systementwicklungsprojekt
(AN) beim Auftragnehmer. Das V-Modell regelt das Zusammenspiel der beiden Projekte in der AG/AN-
Schnittstelle, die Entscheidungspunkt

 e   und auszutauschende Produkte umfasst.

Bei   der   Beauftragung   eines   externen   Dienstleisters   richtet   sich   das  V-Modell   nach   der   UfAB.   Für   den
Auftraggeber  sind in  diesem Fall  die  Produkte  der  Disziplinen  Ausschreibungswesen  (Vergabeakte)  und
Vertragswesen relevant. Als Gegenstück hält das V-Modell XT auf Seiten des Auftragnehmers Produkte in
der Disziplin Angebots- und Vertragswesen vor. Die Disziplinen Berichtswesen und Lieferung und Abnahme
enthalten die für beide Seiten relevanten Schnittstellenprodukte für die Projektlaufzeit und das Projektende.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


B.2 Inhalte des V-Modell XT Bund

51

Wird   die   Systementwicklung   durch   einen   IT-Dienstleister   des   Bundes   erbracht,   entfallen   das
Ausschreibungs- und Vergabeverfahren und die  für den Auftraggeber  genannten Disziplinen.  Stattdessen
kommen die Produkte der Disziplin Angebots- und Auftragswesen zur Anwendung. Der Auftragnehmer (IT-
Dienstleister des Bundes) erhält anstelle einer Ausschreibung eine Angebotsaufforderung und erstellt auf
deren Basis ein Angebot. Mit der Annahme des Angebots durch den Auftraggeber wird das Angebot zum
Auftrag   und   bildet   die   Grundlage   für   die   Zusammenarbeit.   Im   V-Modell   XT   ist   dieser   Prozess   nicht
abgebildet. Der Auftragnehmer benötigt daher eine organisationsspezifische Anpassung des Standards.

Abbildung 53  sowie die nachstehende Beschreibung verdeutlichen den auf Basis einer Ausschreibung und
Angebotswertung erfolgten Vertragsschluss zwischen einem Auftraggeber und einem externen Dienstleister.
Die   im   Projektverlauf   (nach   Vertragsschluss)   über   die  AG/AN-Schnittstelle   auszutauschenden   Produkte
gelten gleichermaßen für die Zusammenarbeit mit einem IT-Dienstleister des Bundes.

Abbildung 53: AG/AN-Schnittstelle im Überblick

Im   AG-Projekt   werden   zunächst   die  Vergabeunterlagen   (Ausschreibung)  erarbeitet.   Sie   enthalten   die
Leistungsbeschreibung   sowie   das   geschuldete   Leistungssoll   des   Auftragnehmers   in   Form   eines
Kriterienkatalogs.

 s    und des  QS-Handbuch

Auf Basis der Ausschreibung erstellt der potenzielle Auftragnehmer ein Angebot. Das Angebot spiegelt die
Leistungsbeschreibung   wider   und   enthält   bereits   Inhalte   des   Pflichtenhefts   und   -   sofern   gefordert   -   des
Projekthandbuch
 s    des Auftragnehmers. Da das  Angebot (von AN)  Grundlage des
Vertrag
ist,   enthält   es   auch   rechtliche   und   kommerzielle   Vereinbarungen,   die   bereits   in   den
 s
Vergabeunterlagen (Ausschreibung) vorgegeben sein können. Durch den Zuschlag auf ein Angebot schließt
der Auftraggeber mit dem Auftragnehmer einen Vertrag über die Systemerstellung. Er kann im Verlauf des
Projektes um Vertragszusätze ergänzt werden.

Während   der   Projektlaufzeit   informiert   der   Auftragnehmer   den   Auftraggeber   in   Form   von
Projektstatusbericht
 en     über die erzielten Projektergebnisse, Planungsabweichungen, aktuellen Risiken und
über die Planung für den nächsten Berichtszeitraum.  Zur  Abstimmung übergreifender  Themen zwischen
Auftraggeber und Auftragnehmer  sollte der Auftraggeber sowohl im  Lenkungsausschuss  als auch in der
Änderungssteuerungsgruppe (Change Control Board) des Auftragnehmers vertreten sein.

Das AN-Projekt übergibt Zwischen- und Endprodukte in Form von Lieferungen. Mit der Abnahmeerklärung
nimmt   das   AG-Projekt   eine  Lieferung   (von   AN)  ab   oder   fordert   Nachbesserungen   ein.   Eine
Abnahmeerklärung ist meist die Grundlage vereinbarter Zahlungen an den Auftragnehmer.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland





52

 Konzepte und Inhalte des V-Modell XT Bund

B.2.3.1 Ausschreibungswesen (Vergabeakte)

In   der   Disziplin  Ausschreibungswesen   (Vergabeakte)  sind   alle   Produkte   zusammengefasst,   die   für   eine
externe  Auftragsvergabe   im   Rahmen   eines   IT-Entwicklungsprojekts   relevant   sind.   Die   Verwaltung   der
Verträge wird in der Disziplin Vertragswesen dargestellt.

Ausschreibungen der öffentlichen Auftraggeber unterliegen bestimmten gesetzlichen Bestimmungen. Hierbei
sind insbesondere GWB, VgV, UVgO, VOL/A und VOB zu nennen. Ein Leitfaden zur Durchführung einer
Ausschreibung findet sich in der jeweils aktuellen UfAB (Unterlage für Ausschreibungen von IT-Leistungen,
aktuell in der Version 2018). Die Inhalte dieser Disziplin wurden in Anlehnung an die UfAB erstellt.

Für   die   Vorbereitung   einer   Beschaffung   (Planungsphase)   ist   zunächst   eine  Beschaffungskonzeption  zu
erstellen.   Hierin   sind   sowohl   die   vergaberechtlichen,   aber   auch   die   technischen   Anforderungen
zusammenzutragen und für eine Veröffentlichung vorzubereiten. Anschließend erfolgt in der Designphase die
Erstellung   eines   produktneutralen   und   funktionalen  Kriterienkatalog
 s    und   der   Bewertungsmatrizen   zur
Wertung   der  Angebote.   Zusätzlich   sind  Anforderungen   an   die   Eignung   der   potenziellen   Bewerber   zu
definieren. Anschließend erfolgt in der dritten Phase die Durchführung des Vergabeverfahrens durch den
Ausschreibungs-   und   Vertragsverantwortlichen.   Sie   endet   nach   Abschluss   von   Prüfung,   Wertung   und
Zuschlagserteilung mit Abschluss des Vergabeverfahrens.

Verantwortliche und
Produkte

Abbildung 54: Disziplin Ausschreibungswesen (Vergabeakte)

Ausschreibungs- und Vertragsverantwortlicher:
Beschaffungskonzeption, Eignungsbewertungsmatrix, Kriterienkatalog,
Leistungsbewertungsmatrix, Verfahrensdokumentation, Vergabeunterlagen
(Ausschreibung), Vergabevermerk
Vergabestelle:
Angebot (von AN)

B.2.3.2 Vertragswesen

Diese   Disziplin   fasst   alle   Produkte   und  Aktivitäten   zusammen,   die   beim   Vertragsschluss   zu   einem   IT-
Entwicklungsprojekt relevant sind.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


B.2 Inhalte des V-Modell XT Bund

53

Nachdem die Rolle  Ausschreibungs- und Vertragsverantwortlicher  im Vergabeverfahren einen geeigneten
Auftragnehmer   ausgewählt   hat,   schließt   der  Auftraggeber   mit   ihm   einen  Vertrag.   Der  Vertrag  ist   die
rechtliche Grundlage für die Erbringung der Leistungen von Auftragnehmer und Auftraggeber und regelt die
Zusammenarbeit zwischen den beiden Parteien. Im Verlauf eines Projekts können Änderungen am Vertrag,
beispielsweise bezüglich des Leistungsumfangs, der Kosten und der Termine, durch einen  Vertragszusatz
vereinbart werden.

Abbildung 55: Disziplin Vertragswesen

In der  Vertragsübersicht  werden sämtliche das Projekt betreffenden Verträge zusammenfassend aufgeführt.
Zu jedem Vertrag sind der aktuelle Status und die zu erbringenden Leistungen und Liefertermine, aber auch
die   im   Fall   nicht   erbrachter   Leistungen   zu   zahlenden   Vertragsstrafen   sowie   die   im   Projektverlauf
vorgenommenen Vertragsanpassungen (Vertragszusätze) zu dokumentieren.

Verantwortliche und
Produkte

Ausschreibungs- und Vertragsverantwortlicher:
Vertrag, Vertragsübersicht, Vertragszusatz

B.2.3.3 Angebots- und Auftragswesen

Die   Disziplin   Angebots-   und   Auftragswesen   enthält   alle   Produkte,   die   zur   Beauftragung   eines   IT-
Dienstleisters des Bundes benötigt werden. Der Auftraggeber erstellt zunächst eine  Angebotsaufforderung
und übermittelt diese gemeinsam mit dem Lastenheft (Anforderungen) an einen IT-Dienstleister des Bundes
(Auftragnehmer).   Auf   Basis   der  Anforderungen   unterbreitet   der  Auftragnehmer   dem   Auftraggeber   ein
Angebot für die Entwicklung des Systems. Mit der Annahme des Angebots durch den Auftraggeber wird das
Angebot zum Auftrag und bildet die Grundlage für die Zusammenarbeit.

Abbildung 56: Disziplin Angebots- und Auftragswesen

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

54

 Konzepte und Inhalte des V-Modell XT Bund

Verantwortliche und
Produkte

Ausschreibungs- und Vertragsverantwortlicher:
Änderungsvereinbarung (Change Request), Angebotsaufforderung, Auftrag

B.2.3.4 Lieferung und Abnahme

Die Disziplin Lieferung und Abnahme regelt die Überbringung der zugesicherten Liefergegenstände sowie
deren rechtliche Abnahme. Zum Entscheidungspunkt Lieferung durchgeführt sendet der Auftragnehmer die
(vertraglich)   vereinbarte  Lieferung  an   den   Auftraggeber.   In   einem   Inhouse-Projekt   (Projekttyp
Systementwicklungsprojekt (AG/AN)) erfolgt die Lieferung entsprechend an den internen Auftraggeber (z.B.
die   Fachabteilung).   Eine   Lieferung   umfasst   eine   Menge   von   zusammengehörigen   und   konsistenten
Systemelementen und Dokumenten.

Der Auftraggeber entscheidet auf Basis eines Prüfprotokolls, ob die Lieferung (von AN) die Anforderungen
erfüllt.   Das   V-Modell   sieht   vor,   dass   Lieferungen   nur   nach   einem   kompletten   Durchlauf   durch   den
Entwicklungszyklus abgenommen werden; eine Abnahme von reinen Dokumenten, ohne dass deren Validität
durch ein System oder einen Prototypen nachgewiesen wurde, ist nicht gewünscht. Für jede Lieferung wird
eine  Abnahmeerklärung  von   Auftraggeber   und   Auftragnehmer   unterzeichnet.   Für   die   Erstellung   der
Abnahmeerklärung ist der Projekteigner des Auftraggebers verantwortlich, da im Rahmen der Abnahme oft
auch Vereinbarungen hinsichtlich Zahlungsterminen und zu erfolgenden Nachbesserungen getroffen werden,
die vertraglichen Charakter besitzen. Der Auftragnehmer erkennt mit seiner Unterschrift die ggf. geforderten
Nachbesserungen an.

Abbildung 57: Disziplin Lieferung und Abnahme

Am Beginn jeder Iteration kann erneut der Entscheidungspunkt Beauftragung erteilt eingeplant werden, um
an dieser Stelle einen Vertragszusatz abzuschließen. Ein Vertragszusatz kann bereits im Vertrag vorgesehen
sein, beispielsweise als Option auf ein zusätzliches Leistungspaket. Vertragszusätze können aber auch das
Ergebnis von Problemen und Änderungswünschen sein, die während einer vorangegangenen Iteration oder
im Rahmen der Qualitätssicherung der Lieferung (von AN) erkannt wurden. Typische Beispiele hierfür sind
Anforderungsänderungen beim Auftraggeber oder technische/terminliche Probleme beim Auftragnehmer.

Verantwortliche und
Produkte

Projekteigner:
Abnahmeerklärung
Projektleiter:
Lieferung, Lieferung (von AN)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C Referenz Produkte

55

C Referenz Produkte

Hinweise zum Aufbau siehe Inhalt und Aufbau der Referenz Produkte.

C.1 Produkte

C.1.1 Anbahnung und Organisation

C.1.1.1 Projektvorstudie

Eine   Projektvorstudie   dokumentiert   die   Voruntersuchungen,   die   vor   der   Genehmigung   des   eigentlichen
Projekts durchgeführt werden. Je nachdem, wie umfangreich ein Projekt ist, kann die Projektvorstudie selbst
im Rahmen eines Vorprojekt

 s   erstellt werden.

Sie   beschreibt   das   eigentliche   Problem,   die   Rahmenbedingungen   sowie   die   unterschiedlichen
Lösungsoptionen.   Die   unterschiedlichen   Optionen   werden   hinsichtlich   ihrer   Machbarkeit   bewertet;
schließlich enthält die Projektvorstudie den Ansatz zur Lösung des eingangs geschilderten Problems - da die
Lösung   in   der   Regel   in   der   Durchführung   eines   Projekts   besteht,   wird   darin   auch   der   Projektumfang
skizziert.

Verantwortlich

Projektauftraggeber

Mitwirkend

Aktivität

Methoden

Multi-Projektkoordination

Projektvorstudie erstellen

Anforderungsanalyse, Bewertungsverfahren, Geschäftsprozessmodellierung,
Prototyping, Systemanalyse

Vorlagen

Projektvorstudie(.odt|.doc)

Inhaltlich abhängig

Berücksichtigung der Projektvorstudie:
Projekthandbuch, Projektauftrag
Projektvorstudie, Projektauftrag und Anforderungen:
Lastenheft Gesamtprojekt, Lastenheft (Anforderungen)

Entscheidungsrelevant
bei

Projekt genehmigt

Sonstiges

Extern

C.1.1.1.1 Problemstellung

In diesem Thema ist die Problemstellung detailliert darzustellen. Sie kann auf einer Ist-Analyse basieren und
hat   zum   Ziel,   den   Handlungsbedarf   klar   darzustellen.   In   der  Analyse   der   Problemstellung   sind   neben
fachlichen   Fragen   auch   organisatorische   Fragen   wie   ineffizienter   Personaleinsatz,   hohe   Hardware-   oder
Betriebskosten zu berücksichtigen.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


56

 Referenz Produkte

C.1.1.1.2 Bestehende Rahmenbedingungen

In   diesem   Thema   sind   alle   Rahmenbedingungen   darzustellen,   die   bei   einer   Umsetzung   im   Projekt   zu
berücksichtigen   sind.   Dabei   kann   es   sich   insbesondere   um   personelle,   organisatorische,   rechtliche   und
technische   Rahmenbedingungen   handeln.   Die   Rahmenbedingungen   sind   so   darzustellen,   dass   eine
Erarbeitung von Lösungsalternativen und die Erstellung einer Machbarkeitsanalyse möglich ist.

C.1.1.1.3

Lösungsalternativen

Dieses   Thema   dokumentiert   alle   untersuchten   Lösungsoptionen   für   das   gestellte   Problem.   Jeder
Lösungsvorschlag   ist   individuell   und   so   detailliert   darzustellen,   dass   eine   anschließende,   objektive
Bewertung möglich ist.

C.1.1.1.4 Machbarkeitsanalyse

Auf   Basis   der   Inhalte   der   Themen  Bestehende   Rahmenbedingungen  und  Lösungsalternativen  analysiert
dieses Thema die Machbarkeit. Dabei sind folgende Kriterien zu berücksichtigen:

➢ organisatorische (bzgl. Personalressourcen und Zeit),

➢ wirtschaftliche,

➢ technische und

➢ rechtliche Machbarkeit.

Bei   der   Bewertung   der   Machbarkeit,   bzw.   der   Umsetzbarkeit,   sind   alle   oben   genannten   Kriterien
gleichermaßen   zu   berücksichtigen.   Die   Nachweisfindung   kann   z.B.   auch   über   die   Erstellung   von
Demonstratoren oder Prototypen erfolgen, die eine Bewertung der Kriterien erleichtern.

In diesem Thema ist die Machbarkeit für jede der zuvor benannten Lösungsalternativen zu dokumentieren.
Dabei   wird   hier   gleichzeitig   festgehalten,   ob   eine   Lösungsoption   während   der   Überprüfung   verworfen
wurde. In diesem Fall ist dies hier zu begründen.

Auf   Basis   der   Ergebnisse   der  Analyse   enthält   dieses   Thema   auch   eine   Priorisierung   der   untersuchten
Lösungsalternativen.

C.1.1.1.5

Lösungsvorschlag und Projektumfang

In diesem abschließenden Thema wird der bevorzugte oder zu wählende Lösungsansatz beschrieben. Da die
Lösung meist in der Durchführung eines Projekts besteht, werden die Projekteckdaten (wichtigste Ziele,
ungefähres Budget, Enddatum, Organisation) beschrieben. Diese grobe Skizze ist dann die Basis für die
Ausarbeitung des Projektauftrag

 s  .

C.1.1.2 Checkliste Informationssicherheit

Die Checkliste Informationssicherheit dient im Rahmen der Projektvorbereitung zur Entscheidungsfindung,
ob im Projekt Aspekte der Informationssicherheit und des Datenschutzes zu berücksichtigen sind. Zu diesem
Zweck enthält die Checkliste einige wenige Aussagen, denen jeweils zugestimmt oder widersprochen werden
kann.   Sofern   mindestens   eine   der   Aussagen   auf   das   Projekt   zutrifft,   sollte   beim   Tailoring   das   die
Informationssicherheit und den Datenschutz betreffende Projektmerkmal gesetzt werden.

Verantwortlich

Projekteigner

Vorlagen

Checkliste Informationssicherheit (Externe Kopiervorlage)

Entscheidungsrelevant
bei

Projekt genehmigt

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


C.1 Produkte

57

Sonstiges

Extern, Keine Produktvorlage

C.1.1.3 Projektauftrag

Der Projektauftrag ist das zentrale Produkt zur Genehmigung eines Projekts und in diesem Sinne für jedes
Projekt   zu  erstellen.   Durch  ihn  wird  das   Projekt   durch  den  Projektauftraggeber  formal   eingerichtet,   der
Projektauftrag definiert, was im Projekt getan werden soll, wer beteiligt ist und wie vorgegangen werden
soll.   Dazu   legt   der   Projektauftrag   bereits   die   grobe   Projektorganisation   fest,   besetzt   die   zentralen
Projektrollen und skizziert den Projektplan, soweit es zu Projektbeginn schon möglich und sinnvoll ist. Er
beschreibt außerdem, warum das Projekt nützlich und wirtschaftlich ist und zählt mögliche Risiken sowie
Chancen auf, die den Projektverlauf negativ oder positiv beeinflussen können.

Verantwortlich

Projektauftraggeber

Mitwirkend

Vorlagen

Inhaltlich abhängig

Multi-Projektkoordination, Personalvertretung

Projektauftrag(.odt|.doc)

Berücksichtigung der Projektvorstudie:
Projektvorstudie
Projektvorstudie, Projektauftrag und Anforderungen:
Lastenheft Gesamtprojekt, Lastenheft (Anforderungen)

Entscheidungsrelevant
bei

Projekt genehmigt

Sonstiges

Initial, Extern

C.1.1.3.1 Projektcharta

Die Projektcharta ist ein Management Summary des Projektauftrags und stellt das Projekt überblicksartig auf
maximal einer Seite dar. Die Projektcharta sollte Führungskräfte in die Lage versetzen, sich ein Bild des
Projekts zu machen, ohne den Projektauftrag im Detail studieren zu müssen.

C.1.1.3.2 Projektmotivation und Projektziele

Dieses  Thema   beantwortet,   warum  das   Projekt   durchgeführt   wird  und  welche   Ziele   im  Projekt   erreicht
werden   sollen.   Wurde   eine  Projektvorstudie  durchgeführt,   so   können   Motivation   und   Ziele   aus   dieser
abgeleitet   bzw.   übernommen   werden.   Im   Projektverlauf   werden   die   Inhalte   dieses   Themas   ins
Projekthandbuch übernommen und dort gepflegt.

Als   Motivation   für   ein   Projekt   kommen   beispielsweise   politische   Entscheidungen   (z.B.
Gesetzesänderungen),   wirtschaftliche   Betrachtungen   (z.B.   Reduzierung   des   Bearbeitungsaufwands)   oder
technische Erfordernisse (z.B. Ablösung eines Altsystems) in Betracht. Die Projektmotivation soll also den
Sinn   der   Projektdurchführung   vermitteln.   Die   Projektziele   sollten   nach   dem  SMART-Prinzip   spezifisch,
messbar, akzeptiert, realisierbar  und terminierbar formuliert sein. Ggf. können auch Nicht-Ziele  benannt
werden, um das Projekt abzugrenzen.

C.1.1.3.3 Stakeholder-Übersicht und Rahmenbedingungen

Dieses   Thema   beschreibt   das   Projektumfeld,   das   im   Projekt   berücksichtigt   werden   muss.   Dazu   zählen
insbesondere die Projektstakeholder, also alle relevanten Personen(kreise), die ein Interesse an dem Gelingen
bzw. Scheitern des Projekts haben. Diese werden bereits hier überblicksartig dargestellt und im Laufe des
Projekts genau analysiert. Aber auch unveränderliche (oder schwer veränderliche) Rahmenbedingungen wie

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

58

 Referenz Produkte

zu   beachtende   Gesetze   und   Vorschriften,   bestehende   Haushaltspläne,   die   Einbettung   in   ein
organisationsweites   Berichtswesen   oder   technische   Vorgaben   sind   hier   als   Rahmenbedingungen   zu
benennen.

C.1.1.3.4

Lösungsansatz und Vorgehensmodell

Der Lösungsansatz des Projekts (engl. Project Approach) beschreibt die prinzipielle Herangehensweise, die
im   Projekt   verfolgt   wird.   Hier   werden   so   grundsätzliche   Projekt-Designentscheidungen   getroffen,
beispielsweise "Soll ein Fertigprodukt eingekauft werden?", "Sollen wir die Entwicklung ausschreiben?"
oder "Entwickeln wir selbst?". Auch die Vorgehensweise (z.B. iterativ-inkrementelles Vorgehen) und das
Vorgehensmodell (z.B. V-Modell XT Bund) werden hier bestimmt. Damit sind die hier definierten Inhalte
Basis für das Tailoring des Projekts, das im Projekthandbuch als Projektspezifisches V-Modell festgehalten
wird.   Auch   Systemvorstellungen   (fachlich   oder   technisch)   können   bereits   hier   im   Rahmen   des
Projektauftrags  definiert  werden,  sofern  sie  sich nicht  sowieso  aus  den Zielen und Rahmenbedingungen
ergeben.

C.1.1.3.5 Projektorganisation und Projektplan

Dieses Thema gibt einen groben Überblick über die Organisation des Projekts. Bereits hier sollte festgelegt
werden, wie sich die Projektorganisation zur Linienorganisation verhält (z.B. reine Projektorganisation oder
Matrix-Organisation) und wie die zentralen Rollen  Projekteigner  und  Projektleiter  besetzt sind. Ggf. kann
hier auch bereits die Zusammensetzung des Lenkungsausschuss
 es    bestimmt werden. Bei größeren Projekten
kann hier bereits die Definition von Teilprojekten erfolgen.

Außerdem enthält das Thema den aktuellen (eher groben) Planungsstand, der im Projekt in den Projektplan
übernommen und dort weiter detailliert und gepflegt wird. Prinzipiell können alle Themen des Projektplans
bereits   hier   umrissen   werden,   beispielsweise   wichtige   Meilensteine   (Termin-   und  Ablaufplan),   geplante
Arbeitspakete   (Projektstrukturplan),   verfügbare   Ressourcen   (Ressourcen-   und   Organisationsplan)   oder
geplante Budgets (Budget- und Kostenplan).

C.1.1.3.6 Kosten-Nutzen-Analyse

Dieses Thema beschreibt, welcher Nutzen durch die Projektdurchführung erzielt werden kann bzw. warum
das Projekt wirtschaftlich ist, sich also "rechnet"; im Englischen wird häufig der Begriff   Business Case
verwendet.   Das  Thema   identifiziert   insbesondere   Kosten-   und   Nutzentreiber:   Dabei   handelt   es   sich   um
Projekteigenschaften oder Projektergebnisse, die entweder Kosten verursachen oder Nutzen herbeiführen.
Auch   die  Verbindung  zwischen  den  Projektstakeholdern  und  den  Kosten-   und  Nutzentreibern  (Wer   will
welchen Nutzen erzielen? Welche Interessen können Kosten verursachen?). Das Thema ist eng verwandt mit
der WiBe (Vorkalkulation) und kann die dort gewonnenen Erkenntnisse ggf. zusammenfassend darstellen.

C.1.1.3.7 Chancen und Risiken

Ausgangspunkt   für   den   Projektauftrag   und   die   Projektplanung   ist   der   erwartete   bzw.   wahrscheinliche
Projektverlauf.   Chancen   und   Risiken   beschreiben   darin   nicht   berücksichtigte   glückliche   Umstände   und
ungünstige   Ereignisse,   die   diesen   Verlauf   positiv   bzw.   negativ   beeinflussen   können.   Sie   müssen   im
Projektverlauf   ständig   beobachtet   werden,   um   die   negativen   Auswirkungen   zu   vermeiden
(Risikomanagement) oder die möglichen positiven Auswirkungen auch tatsächlich "mitzunehmen".

Typische Risiken sind beispielsweise Gesetzesänderungen und damit verbundene Anforderungsänderungen
im Projektverlauf oder der Wegfall wichtiger Ressourcen. Eine typische Chance ist, dass im Rahmen des
Projekts ein bestehendes Problem "nebenbei" gelöst wird, dass gemäß den Projektzielen nicht Bestandteil
des   Projekts   ist.   Beim   Bau   eines   Großflughafens   könnte   beispielsweise   durch   geschickte   Bahn-
Trassenführung erreicht werden, dass weitere Ortschaften eine dringend benötigte Anbindung erhalten. Bei
der Entwicklung eines IT-Systems könnte ggf. nebenbei ein "Blueprint" für weitere Systeme entstehen.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


C.1 Produkte

59

C.1.1.4 Informationssicherheits-Navigator

Der  Informationssicherheits-Navigator  gibt einen Überblick der im V-Modell XT enthaltenen Regelungen
zur   Gewährleistung   der   Informationssicherheit.   Er   greift   die   verschiedenen   Aspekte   der
Informationssicherheit auf, beschreibt deren Bedeutung und verweist auf die entsprechenden Vorgaben im V-
Modell XT.

Das Dokument enthält Regelungen für den Auftraggeber und den Auftragnehmer und sollte zu Projektbeginn
von allen Projektbeteiligten gelesen werden. Auf Basis des Informationssicherheits-Navigators können die
im Projekt benötigten Ressourcen und Aufwände zur Gewährleistung der Informationssicherheit abgeschätzt
und im Projektplan berücksichtigt werden.

Verantwortlich

Projektleiter

Vorlagen

Sonstiges

Informationssicherheits-Navigator (Externe Kopiervorlage)

Extern, Keine Produktvorlage

C.1.1.5 Projekthandbuch

Das   V-Modell   ist   ein   generischer   Vorgehensstandard,   der   für   ein   konkretes   Projekt   angepasst   und
konkretisiert werden muss. Das Projekthandbuch legt die für Management und Entwicklung notwendigen
Anpassungen und Ausgestaltungen fest. Somit  dokumentiert es Art und Umfang der Anwendung des V-
Modells im Projekt und ist Informationsquelle und Richtlinie für alle Projektbeteiligten.

Das   Projekthandbuch   beinhaltet   eine   Kurzbeschreibung   des   Projekts,   die   Beschreibung   des   Tailoring-
Ergebnisses, den grundlegenden Projektdurchführungsplan, die notwendige und vereinbarte Unterstützung
des Auftraggebers sowie Organisation und Vorgaben für die Planung und Durchführung des Projekts und die
anstehenden Entwicklungsaufgaben. Der Projektleiter muss dieses zentrale Produkt in Abstimmung mit den
Schlüsselpersonen des Projekts erarbeiten.

Dabei   werden   im   Projekthandbuch   auch   insbesondere   Häufigkeit   und   Notwendigkeit   der   Erzeugung
weiterführender Produkte, die für die Planung und Durchführung des Projekts, für das Ausschreibungs- und
Vertragswesen   sowie   für   die   Prozessverbesserung   notwendig   sind,   festgelegt,   zum   Beispiel
Projektstatusbericht

 n  , Verträge und Bewertungen von Vorgehensmodellen.

 e  , Risikoliste

Verantwortlich

Projektleiter

Mitwirkend

Aktivität

Werkzeuge

Vorlagen

Inhaltlich abhängig

KM-Verantwortlicher, Projekteigner, Systemarchitekt,
Informationssicherheitsverantwortlicher, Datenschutzverantwortlicher,
Betriebsverantwortlicher, Personalvertretung

Projekthandbuch erstellen

Tailoring/Projektinitialisierung, V-Modell XT Projektassistent

Projekthandbuch(.odt|.doc)

Berücksichtigung der Projektvorstudie:
Projektvorstudie
Vorgaben für den Auftragnehmer:
Vergabeunterlagen (Ausschreibung)

Entscheidungsrelevant
bei

Projekt initialisiert, Iteration geplant, Gesamtprojekt aufgeteilt

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland



60

 Referenz Produkte

Sonstiges

Initial

C.1.1.5.1 Projektüberblick, Projektziele und Erfolgsfaktoren

Das Projekthandbuch ist eine unverzichtbare Informationsquelle und Richtlinie für alle Projektbeteiligten. In
diesem Thema wird kurz, prägnant und möglichst plastisch das gemeinsame Projektleitbild dargestellt.

C.1.1.5.2

Teilprojekte

Auf   der   Basis   einer  Skizze   des   Lebenszyklus   und   der   Gesamtsystemarchitektur,   den  Funktionale
Anforderungen  und   den  Nicht-Funktionale  Anforderungen  des   Gesamtprojektes   werden   die  Teilprojekte
festgelegt. Die Festlegung der Teilprojekte enthält die Anzahl der Teilprojekte, eine Kurzbeschreibung der
Teilprojekte, die wichtigsten Teilprojekt-Entscheidungspunkte, die Zuordnung der funktionalen und nicht-
funktionalen   Anforderungen   zu   den   Teilprojekten   und   die   Abdeckung   der   Elemente   der
Gesamtsystemarchitektur durch die Teilprojekte.

Dabei wird auch ein Teilprojekt Integration festgelegt, das die Ergebnisse aller anderen Teilprojekte zum
Gesamtprojekt integriert.

Das Teilprojekt Integration beschreibt die Reihenfolge der zu integrierenden Teilprojekte, die besonderen
Verfahren oder Methoden zur Integration der Teilprojektergebnisse, die Termine, Aufwände, Verantwortliche
und Ressourcen.

C.1.1.5.3 Projektspezifisches V-Modell

Das V-Modell ist ein generisches Vorgehensmodell. Die projektspezifische Anpassung - das so genannte
Tailoring  -   wird   in   diesem   Thema   dokumentiert.   Das   dabei   zu   erstellende  Anwendungsprofil,   der
resultierende  Projekttyp, die zu verwendenden und zusätzlich ausgewählten  Vorgehensbaustein
 e    sowie die
 n    sind dabei festzuhalten. Im Rahmen dieses Themas können
ausgewählten  Projektdurchführungsstrategie
auch die Umstände und Konsequenzen von bereits vorhersehbarem,  dynamischem Tailoring festgehalten
werden. Alle diese Festlegungen sind entsprechend den Vorgaben des V-Modells zu begründen (siehe dazu
auch Kapitel Projektkonstellation und Tailoring).

C.1.1.5.4 Abweichungen vom V-Modell

Sämtliche   Abweichungen   von   den   Vorgaben   des   V-Modells,   wie   Streichungen   einzelner  Produkte,
Aktivitäten und Abweichung vom Tailoring-Verfahren, müssen unter Angabe von Gründen dokumentiert
werden. Die Änderungen sind in diesem Thema aufzuführen.

C.1.1.5.5 Projektdurchführungsplan

 en    Vorgaben zur groben Strukturierung
Das V-Modell macht durch die Festlegung von Entscheidungspunkt
des Projekts. Dieses Thema enthält die planerische Ausgestaltung dieser Entscheidungspunkt
 e   in Form eines
Projektdurchführungsplans. Hierbei sind zumindest der Projektanfang, das Projektende und alle wichtigen
Entscheidungspunkte während des Projekts einzuplanen. Es muss dokumentiert werden, welche Produkte für
das   Herbeiführen   einer  Projektfortschrittsentscheidung,   also   dem   Erreichen   eines   Entscheidungspunktes
erforderlich sind.

Darüber hinaus können noch weitere projektspezifische Meilensteine festgelegt werden, soweit diese für alle
Projektbeteiligten relevant sind. Meilensteine, die nur projektintern relevant sind, werden im Projektplan
dokumentiert.

Erzeugt

Bestätigung eines Entscheidungspunkts:
Projektfortschrittsentscheidung

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland





C.1 Produkte

61

C.1.1.5.6 Organisation und Vorgaben zum Risikomanagement

Damit die Einschätzungen der Risiken innerhalb des Projekts nach denselben Maßstäben erfolgen, wird das
im V-Modell bereits vorgesehene Risikomanagement in diesem Thema ausgestaltet und konkretisiert. Dabei
ist die generelle Entscheidung zu treffen, ob neben Risiken auch Chancen betrachtet werden sollen. Für
Chancen wird das gleiche Verfahren wie für Risiken angewendet, deshalb wird im Folgenden nicht mehr
zwischen den Begriffen Chance und Risiko unterschieden.

Hier erfolgt die Festlegung, wann und nach welchen Kriterien Risiken in einer  Risikoliste  dokumentiert
werden.   Zusätzlich   muss   definiert   werden,   mit   welchen   Methoden,   Richtlinien   und   Standards   und   mit
welchen Werkzeugen das Risikomanagement durchzuführen ist.

Dabei sind im Einzelnen die folgenden Punkte festzulegen:

➢ Risikoklasse

 n   zur Einstufung von Risiken

➢ Kriterien zur Risikoakzeptanz

➢ Eskalationsstufen   basierend   auf   den   definierten   Risikoklassen,   entsprechend   den   Vorgaben   des

Themas Organisation und Vorgaben zum Projektmanagement

➢ Verfahren für die Dokumentation der identifizierten Risiken und der geplanten Maßnahmen

➢ Zeitpunkte und Vorgehen bei der Risikoidentifizierung

➢ Zeitpunkte für die Neubewertung von Risiken

➢ Zeitpunkte und Verfahren für die Planung und Durchführung von Gegenmaßnahmen

Erzeugt

Führung einer Risikoliste:
Risikoliste

C.1.1.5.7 Organisation und Vorgaben zur Vergabe von Entwicklungsleistungen

In   diesem   Thema   ist   der   Vergabeprozess   bis   hin   zur   Beauftragung   eines   externen   IT-Dienstleiters
(Auftragnehmer) zu dokumentieren. Es muss festgelegt werden, welche Produkte dabei relevant sind und
nach welchen Regelungen und Vorgaben diese erstellt werden. Neben einem Prozess zur Vorbereitung und
Veröffentlichung der Ausschreibung ist festzuhalten, wie die Bewertung der eingegangenen Angebote und
letztlich die Zuschlagserteilung erfolgen.

Erzeugt

Dokumentation des Vergabeverfahrens:
Verfahrensdokumentation, Vergabevermerk
Veröffentlichung der Ausschreibung:
Beschaffungskonzeption, Eignungsbewertungsmatrix, Kriterienkatalog,
Leistungsbewertungsmatrix, Vergabeunterlagen (Ausschreibung)
Zuschlagserteilung auf ein Angebot:
Vertrag, Vertragsübersicht

C.1.1.5.8 Organisation und Vorgaben zum Problem- und Änderungsmanagement

In   diesem   Thema   wird   das   im   V-Modell   bereits   vorgesehene   Problem-   und   Änderungsmanagement
ausgestaltet   und   konkretisiert.   Es   erfolgt   die   Festlegung,   ob,   wann   und   welche   Problemmeldungen   und
Änderungsanträge   erstellt   werden   müssen,   nach   welchen   Methoden,   Richtlinien   und   Standards   diese   zu
bearbeiten sind und mit welchen Werkzeugen sie weiterverarbeitet werden.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


62

 Referenz Produkte

Dies   beinhaltet   beispielsweise   die   Definition   der   vorgesehenen   Status   von   Problemmeldungen   und
Änderungsanträgen   (erstellt,   genehmigt   und   abgelehnt)   die   Besetzung   der  Änderungssteuerungsgruppe
(Change   Control   Board)  sowie   das   Konfliktmanagement   und   die   Eskalationsstrategie.   Dabei   kann   es
erforderlich   sein,   mehrere   Änderungsverantwortliche   und   Änderungssteuerungsgruppen   (Change   Control
Boards) mit unterschiedlicher Entscheidungskompetenz und Zusammensetzung einzurichten.

Bei unterschiedlichen Auffassungen in einer Änderungssteuerungsgruppe (Change Control Board) werden
Eskalationsstufen definiert. Beispielsweise kann eine mit größerer Entscheidungskompetenz ausgestattete
Änderungssteuerungsgruppe   (Change   Control   Board)   oder   ein  Lenkungsausschuss  als   Eskalationsinstanz
festgelegt werden.

Erzeugt

Umgang mit Änderungen:
Problem-/Änderungsbewertung, Problemmeldung/Änderungsantrag,
Änderungsentscheidung, Änderungsstatusliste

C.1.1.5.9 Organisation und Vorgaben zur Beauftragung eines IT-Dienstleisters des Bundes

In diesem Thema ist das Vorgehen zur Beauftragung eines IT-Dienstleisters des Bundes (Auftragnehmer) zu
dokumentieren.   Es   muss   festgelegt   werden,   welche   Produkte   dabei   relevant   sind   und   nach   welchen
Regelungen und Vorgaben diese erstellt werden.

Erzeugt

Abschluss von Änderungsvereinbarungen:
Änderungsvereinbarung (Change Request)
Aufforderung zur Abgabe eines Angebots:
Angebotsaufforderung
Erteilung des Auftrags:
Auftrag

C.1.1.5.10 Organisation und Vorgaben zum Konfigurationsmanagement

In diesem Thema wird das im V-Modell bereits vorgesehene Konfigurationsmanagement ausgestaltet und
 e    wann   nach   welchen   Methoden,
konkretisiert.   Es   erfolgt   die   Festlegung,   welche  Produktexemplar
Richtlinien und Standards vom Konfigurationsmanagement zu verwalten sind, sowie wann und in welchen
Abständen  Produktkonfiguration
 en     und   Releases   zu   erstellen   sind.   Zu   Anzahl   und   Umfang   der
Produktkonfigurationen   sind   mindestens   die   Vorgaben   zum   Konfigurationsmanagement   (siehe   auch
Produktmodell) einzuhalten.

Alle Produkte, die im Rahmen eines V-Modell Projektes erstellt werden, werden entsprechend den Vorgaben
im   Projekthandbuch   in   die  Produktbibliothek  eingestellt   und   verwaltet.   Hierzu   muss   festgelegt   werden,
welche Dateiablagestruktur und Namenskonventionen in der Produktbibliothek einzuhalten sind, wie die
Produkte   im   Konfigurationsmanagement   eindeutig   zu   bezeichnen   sind,   wie   die   Fortschreibung   von
Versionen   und   Releases   erfolgt   und   welche   Produktzustände   ein   Produktexemplar   aus   Sicht   des
Konfigurationsmanagements   durchläuft.   Die   Produktzustände   müssen   mindestens   die   im   Kapitel
Produktprüfung und inhaltliche Produktabhängigkeiten definierten Zustände umfassen.

Neben der Verwaltung der Produktbibliothek ist im Rahmen dieses Themas ein Konzept zur Datensicherung
und Archivierung der Exemplare in der Produktbibliothek zu erstellen. Es werden die Verantwortlichkeiten,
Termine und Verfahren zur Datensicherung festgelegt, sowie Konzepte zur Archivierung und Aufbewahrung
der Daten über längere Zeiträume erstellt.

Das   Konfigurationsmanagement   liefert   zudem   einen   Beitrag   zum  Projektstatusbericht,   welcher   zur
Fortschrittskontrolle der Produktexemplare und Produktkonfigurationen dient. Es ist festzulegen, wann, in
welcher Form und an welche Personen eine KM-Auswertung zu übergeben ist.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland



C.1 Produkte

63

Ferner wird in diesem Kapitel beschrieben, wie Eintragungen in das  Änderungs- und Prüfverzeichnis  von
Produkten vorzunehmen sind, d.h. z.B. Häufigkeit von Einträgen und welche Einträge bei der Bearbeitung
vorgenommen werden und unter welchen Bedingungen.

Erzeugt

Sicherung der Produktbibliothek:
Produktkonfiguration

C.1.1.5.11 Organisation und Vorgaben zum Projektmanagement

In diesem Thema werden die Vorgaben des V-Modells zum Projektmanagement angepasst und konkretisiert.
Es werden alle internen und externen Projektbeteiligten aufgeführt. Die verantwortlichen Ansprechpartner
sind   dabei   namentlich   zu   benennen.   Darüber   hinaus   werden   die   Schlüsselrollen   des   V-Modells,   wie
Projektleiter,  QS-Verantwortlicher  und  Systemarchitekt,   mit   Personen   besetzt   und   deren  Aufgaben   und
Verantwortlichkeiten entsprechend den V-Modell-Vorgaben ausgestaltet.

Die grundlegende Organisation und Durchführung der Zusammenarbeit zwischen allen Projektbeteiligten
wird  definiert.   Dabei   werden   beispielsweise   Besprechungen,   das  Vorgehen  für  Abstimmungsrunden,   das
Konfliktmanagement,   die   Eskalationsstrategie,   die   Bedingungen   für   die   Durchführung   eines   formalen
Entscheidungsprozesses   festgelegt   und   dokumentiert.   Zusätzlich   werden   Schwellenwerte   definiert,   deren
Überschreitung zur Einleitung von Steuerungsmaßnahmen führt. Ein Beispiel dafür ist die Überschreitung
von Sollwerten für die Planung um mehr als 15%. Organisationsweite Vorgaben müssen dabei berücksichtigt
werden.

Für   die   im   Rahmen   des   Projektmanagements   zu   erstellenden   V-Modell-Produkte,   wie   Projektplan,
Aufgabenliste  und  Projekttagebuch,  wird festgelegt,  ob  und  wann  diese  zu  erstellen  sind,  nach welchen
Methoden, Richtlinien und Standards diese  Produkte  auszuarbeiten sind und mit welchen Werkzeugen sie
bearbeitet werden (siehe dazu auch Abschnitt Erzeugende Produktabhängigkeiten).

Projektorganigramm

Das   Projektorganigramm   verbildlicht   die   aufbauorganisatorische   Projektstruktur,   beispielsweise   die
Untergliederung eines Projekts in Teilprojekte bzw. die Zusammensetzung des Projekts aus einzelnen Teams.
Dabei   sollte   auch   die  Auftraggeber/Auftragnehmer-Konstellation   beachtet   werden.  Außerdem   sollte   das
Projektorganigramm   die   Beziehungen   der   Führungs-   und   Managementrollen   (beispielsweise
Lenkungsausschuss, Projekteigner, Projektleiter, Projektmanagementbüro) aufzeigen.

In   großen   Projekten   enthält   es   die   Aufteilung   des   Gesamtprojekts   in   Verantwortungsbereiche   und
Teilprojekte  (einschließlich Aufgabenabgrenzung zwischen den Teilprojekten)  und dokumentiert,  wer für
welche   Teile   verantwortlich   ist.   Ggf.   kann   für   einzelne   Rollen   auch   deren   konkrete   Besetzung   im
Projektorganigramm dargestellt werden.

Die   im   Projektorganigramm   dokumentierte   Struktur   ist   unabhängig   von   den  Aufbauorganisationen   der
beteiligten   Behörden   oder   Unternehmen.   Die   Aufteilung   auf   Verantwortungsbereiche   und   Teilprojekte
orientiert   sich   an   Projektinhalten,   die   in   der   Definition   des   Projektumfangs   und   letztendlich   im
Projektstrukturplan  beschrieben   sind   und   ist   Basis   für   den  Ressourcen-   und   Organisationsplan  .   Das
Projektorganigramm   bleibt   im   Projektverlauf   meist   relativ   stabil,   kann   aber   jederzeit   an   aktuelle
Entwicklungen angepasst werden.

Rollenbeschreibungen

Die   Rollenbeschreibungen   machen   deutlich,   welche   Projektrolle   welche  Aufgaben   wahrnimmt,   welche
Kompetenzen   ihr   zugeordnet   sind   und   welche   Verantwortung   sie   im   Projektkontext   hat.   Die
Rollenbeschreibungen   stellen   sicher,   dass   alle   benötigten  Aufgaben   wahrgenommen   werden   und   keine
Aufgaben   doppelt   oder   mit   unklarer   Verantwortung   vergeben   werden.   Entspricht   das   Rollenmodell   des
Projekts dem Rollenmodell im V-Modell, so reichen hier meist Verweise auf die V-Modell-Dokumentation.
Weicht das Rollenmodell im Projekt vom V-Modell-Rollenmodell ab, so sollte zumindest versucht werden,
eine entsprechende Zuordnung zu finden.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

64

 Referenz Produkte

Projektmitarbeiter und Rollenbesetzung

Im Projekthandbuch werden alle Projektmitarbeiter nebst ihren Kontaktdaten aufgelistet. Außerdem wird für
jeden Mitarbeiter festgelegt, welche Rollen er im Projekt einnimmt oder einnehmen kann und in welchen
Teilprojekten oder Teams er eingesetzt wird.

Erzeugt

Ermittlung des Projektstatus:
Projektabschlussbericht, Projektstatusbericht
Erstellung von Schätzungen:
Schätzung
Erstellung von Wirtschaftlichkeitsbetrachtungen:
WiBe (Fortschreibung)
Erteilung von Arbeitsaufträgen:
Aufgabenliste
Führung eines Projektagebuchs:
Projekttagebuch
Protokollierung von Besprechungen:
Besprechungsdokument

C.1.1.5.12 Organisation und Vorgaben zum Projektcontrolling

In diesem Thema wird das im V-Modell bereits vorgesehene Vorgehen zum Projektcontrolling ausgestaltet
und konkretisiert. Hierfür werden die Projektziele, die durch Projektkennzahlen verfolgt werden sollen, die
Kennzahlen selbst und die dazugehörigen Messdatentypen zusammengestellt. Die Projektkennzahlen werden
dabei   den  Projektzielen  zugeordnet.   Damit   ist   eine   quantitative   oder   qualitative  Verfolgung  dieser   Ziele
möglich.

Abschließend   erfolgt   die   Festlegung,   ob,   wann,   welche   und   durch   wen  Messdaten  zu   erfassen   und
Kennzahlenauswertungen   zu   erstellen   sind.   Zusätzlich   muss   definiert   werden,   mit   welchen   Methoden,
Richtlinien   und   Standards   und   mit   welchen   Werkzeugen   dabei   vorgegangen   werden   soll.   Dabei   ist
insbesondere die projektspezifische Ablagestruktur der Messdaten festzulegen.

Erzeugt

Ermittlung von Projektkennzahlen:
Kennzahlenauswertung, Messdaten

C.1.1.5.13 Organisation und Vorgaben zu Informationssicherheit und Datenschutz

In diesem Thema wird das Vorgehen in den Bereichen Informationssicherheit und Datenschutz ausgestaltet
und konkretisiert. Die Ausgangslage ist eine Auflistung der für das Projekt relevanten Standards, Normen
und Richtlinien sowie eine Erklärung zum geplanten Betriebsort und den Regionen, in denen das System
genutzt werden darf. Aus letzteren leiten sich die rechtlichen Vorgaben her.

Hier finden sich in jedem Projekt Verweise auf organisationsweite Regelungen und Arbeitshilfen.

In   Projekten   eines   Auftraggebers   finden   sich   zusätzlich   Aussagen   darüber,   wie   Vorgaben   an   die
Informationssicherheit und an den Datenschutz erstellt und an die Auftragnehmer übermittelt werden. Diese
finden   sich   in   den   zugehörigen   Produkten  Vorgaben   zur   Informationssicherheit  und  Vorgaben   zum
Datenschutz.

Zudem wird festgelegt, welche sicherheitsrelevanten Produkte im Projekt zu welchem Zeitpunkt von wem
erstellt werden und welche Methodik und welche Werkzeuge hier jeweils zum Einsatz kommen sollen. Das
in   diesem   Zusammenhang   die   Schnittstellen   zu   den   Rollen
Thema   präzisiert
Informationssicherheitsbeauftragter und Datenschutzbeauftragter.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


C.1 Produkte

65

Für beide Bereiche ist es wichtig, die Beteiligten zu sensibilisieren und für die Fälle, in denen ihre Mitarbeit
erforderlich ist (z.B. Eskalation bei einem Sicherheitsvorfall), Handlungsanweisungen zu kommunizieren.
Beides wird in diesem Thema konzipiert und als einzelne Maßnahmen abgebildet.

Erzeugt

Festlegung der Vorgaben zum Datenschutz:
Vorgaben zum Datenschutz
Festlegung der Vorgaben zur Informationssicherheit:
Vorgaben zur Informationssicherheit

C.1.1.5.14 Organisation und Vorgaben zum Informationssicherheits-Managementsystem

In diesem Thema wird geregelt, wie die im Projekthandbuch festgelegten elektronischen Werkzeuge für die
Projektarbeit   in   das  Informationssicherheits-Managementsystem  (ISMS)   der   Organisation   eingebunden
werden   und   welche   Vorgaben   aus   dem   ISMS   für   den   Einsatz   der   Werkzeuge   zu   beachten   sind.
Beispielsweise kann festgelegt werden, dass E-Mails nur verschlüsselt an im System hinterlegte Empfänger
übertragen werden dürfen.

C.1.1.5.15 Organisation und Vorgaben zum Anforderungsmanagement

Dieses Thema beschreibt die im Rahmen des Anforderungsmanagements anzuwendenden Verfahren. Dies
beinhaltet Festlegungen zu folgenden Bereichen zu treffen:

➢ Ermittlung von Anforderungen

➢ Dokumentation von Anforderungen

➢ Identifikation von Anforderungen

➢ Stakeholder

Insbesondere   sind   auch   die   Verantwortlichen   für   die   Produkte   (insb.   das   Produkt
 Lastenheft
(Anforderungen)) der Anforderungserhebung zu benennen, sowohl für die Durchführung im Projekt als auch
für die Betriebsphase. Zu berücksichtigen sind bei den Festlegungen auch, ob und welche Werkzeuge für die
Anforderungserhebung zu  verwenden  sind,  wie  die  Statuskontrolle  der  Anforderungen  erfolgen  soll  und
welche   Metriken   dafür   zu   verwenden   sind.   Eine   angemessene   Regelung   dafür   ist   insbesondere   für   die
Erstellung des Produkts Anforderungsbewertung erforderlich, dessen Erstellung ebenfalls hier zu regeln ist.
Abschließend ist hier zu dokumentieren, wie die Anforderungserhebung in das Berichtswesen eingebunden
werden soll.

Es lassen sich drei Arten von Anforderungen unterscheiden:

➢ Funktionale Anforderungen

  definieren die jeweilige Funktion, die von einem System zur Verfügung

gestellt werden muss und vom Benutzer erwartet wird.

➢ Nicht-Funktionale   Anforderungen

   definieren   die   Qualitätsmerkmale   für   ein   System   und   seine

Funktionalität, zu denen in der Regel auch Anforderungen aus dem Bereich des IT-Betriebs zählen.

➢ Randbedingungen   leiten   sich   aus   Rahmenbedingungen   (z.B.   organisatorische   und   technische
Vorgaben)   ab.   Sie   sind   in   der   Regel   projektextern   und   schränken   die   Art   und   Weise   der
Systemrealisierung ein bzw. geben konkrete Vorgaben für diese.

Für  jede dieser  Anforderungsarten sind hier  Festlegungen zu den oben aufgeführten Punkten zu treffen.
Darüber hinaus ist auch die frühzeitige Einbindung des Betriebs zu regeln, um die spätere Inbetriebnahme
des Systems zu erleichtern.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland



66

Ermittlung von Anforderungen

 Referenz Produkte

Eine Anforderung im Allgemeinen stellt eine Bedingung oder Fähigkeit dar, die von einem Benutzer zur
Problemlösung oder Zielerreichung benötigt wird und die ein (Teil-)System erfüllen oder besitzen muss, um
bestimmte   Vorgaben   (z.B.   Normen,   Spezifikationen)   zu   erfüllen.   Außerdem   ist   die   Anforderung   die
Dokumentation dieser Bedingung bzw. Fähigkeit.

Zur Ermittlung von Anforderungen können verschiedene Techniken zum Einsatz kommen, wie z.B.:

➢ Kreativitätstechniken (z.B. Brainstorming, Mind-Mapping etc.) für die Sammlung erster Ideen

➢ Beobachtungstechniken (z.B. Feldbeobachtung) zur Ableitung von Details für die Anforderungen

abzuleiten und für das Erkennen impliziter Anforderungen

➢ Befragungstechniken (z.B. Fragebogen, Interview) zur Erfragung von Anforderungen in beliebigem

Detaillierungsgrad

➢ Vergangenheitsorientierte Techniken (z.B. Analyse bestehender Lösungen) zur Wiederverwendung
der   bei   früheren  Systementwicklungen   bereits   gemachten  Erfahrungen   und  zur   Überprüfung,   ob
tatsächlich alle Anforderungen ermittelt wurden

Der Einsatz der Techniken, die für die Anforderungsfestlegung verwendet werden ist hier zu dokumentieren.

Dokumentation von Anforderungen

Funktionale Anforderungen können sowohl natürlichsprachlich als auch modellbasiert erfasst werden. Nicht-
Funktionale Anforderungen  werden dabei ausschließlich in Textform dokumentiert. Anforderungen sollen
stets so beschrieben sein, dass ihre Erfüllung prüfbar und entscheidbar ist. Bei einer textuellen Beschreibung
ist daher auf hinreichende Präzision zu achten. Bei der modellbasierten Dokumentation von Anforderungen
sind insbesondere die Perspektiven zu berücksichtigen, die zur Dokumentation verwendet werden, da sie
einen Einfluss auf die Art der Interpretation der Anforderungen haben. Folgende Perspektiven sind dabei
üblich:

➢ Strukturperspektive: Mit ihr lassen sich z.B. Abhängigkeitsbeziehungen im Systemkontext abbilden.
Hierfür   können   z.B.   UML-Klassendiagramme   oder   Entity-Relationship-Diagramme   verwendet
werden.

➢ Funktionsperspektive: Sie ist die Darstellungsform zur Erläuterung der Informations- / Datenflüsse.
D.h., welche Informationen / Daten bekommt das System als Input, wie verarbeitet das System diese
und   welche   Informationen   /   Daten   liefert   das   System   als   Output.   Hierfür   können   z.B.   UML-
Aktivitätsdiagramme oder Datenflussdiagramme verwendet werden.

➢ Verhaltensperspektive: Mit ihr lässt sich beschreiben, wie ein System auf Ereignisse reagiert und was
die   Bedingungen   für   einen   Zustandswechsel   des   Systems   sind.   Hierfür   können   z.B.   UML-
Zustandsdiagramme oder Statecharts verwendet werden.

Die Festlegungen, wie in einem Projekt Anforderung erfasst werden, welche technischen und methodischen
Hilfsmittel für die Dokumentation Verwendung finden ist hier zu dokumentieren.

Identifikation von Anforderungen

Anforderungen   müssen   eindeutig   identifizierbar   sein,   um   eine   verlässliche  Anforderungsverfolgung   zu
ermöglichen. In diesem Thema sind daher die Festlegungen zu dokumentieren, wie die Identifikation, z.B.
durch Nummerierung, im Projekt erfolgen soll.

Stakeholder

In diesem Thema sind alle an der Anforderungserhebung beteiligten Personen (Stakeholder) zu benennen.
Dies   umfasst   nicht   nur   den  Anforderungsanalytiker   (AG)  sondern   auch   weitere   Personen,   wie   z.B.
Anwender, die ein Interesse am IT-System haben. Insbesondere die Ansprechpartner des IT-Betriebs sind hier
einzubinden.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

67

C.1.1.5.16 Organisation und Vorgaben zum IT-Betrieb

Hier   wird   beschrieben,   wie   der   vorgesehene   Betreiber   des   zu   entwickelnden   Systems   in   das   Projekt
eingebunden wird. Insbesondere sollte die Mitarbeit des IT-Betriebs bei der Anforderungsfestlegung und der
Qualitätssicherung geregelt werden.

Die Anforderungen des IT-Betriebs fließen als Vorgaben zum IT-Betrieb in das Lastenheft ein oder werden
dort referenziert. Zur Überprüfung, ob die Anforderungen des IT-Betriebs korrekt und vollständig umgesetzt
wurden, wird eine Prüfspezifikation Inbetriebnahme erstellt. Im Fall einer erfolgreichen Überprüfung erteilt
der IT-Betrieb die Betriebliche Freigabeerklärung.

Erzeugt

Abschluss von Leistungsvereinbarungen:
Leistungsvereinbarung (SLA/OLA/UC)
Festlegung der Vorgaben zum IT-Betrieb:
Vorgaben zum IT-Betrieb
Herbeiführung der betrieblichen Freigabe:
Betriebliche Freigabeerklärung, Prüfprotokoll Inbetriebnahme, Prüfspezifikation
Inbetriebnahme

C.1.1.5.17 Organisation und Vorgaben zur Systemerstellung

In diesem Thema wird das im V-Modell bereits vorgesehene Vorgehen zur Systemerstellung ausgestaltet und
konkretisiert. Es erfolgt die Festlegung, wann und welche Produkte für die Systemerstellung zu verwenden
sind,   nach   welchen   Methoden,   Richtlinien   und   Standards   diese   zu   erstellen   sind   und   mit   welchen
Werkzeugen sie zu bearbeiten sind.

Dies   beinhaltet
Entwicklungsumgebung, Technologien sowie Konfliktmanagement und Eskalationsstrategie.

  die   Festlegung   der   anzuwendenden   Entwicklungsmethoden,

  zumindest

Die   Reports   der   Werkzeuge   passen   im   Normalfall   nicht   zur   Struktur   der   V-Modell   XT   Produkte.   Die
Modellierung in den Werkzeugen müssen inhaltlich die Produktmuster abdecken.

C.1.1.5.18 Vorgaben für das Projekthandbuch der Auftragnehmer

In diesem Thema kann der Auftraggeber die unterschiedlichsten Vorgaben für die Planung und Durchführung
des   Projektes   beim   Auftragnehmer   festlegen.   Sie   werden   hier   dokumentiert   und   dann   in   alle
Ausschreibungen übernommen und gegebenenfalls angepasst. Die Vorgaben können beispielsweise den zu
verwendenden Entwicklungsprozess, das Tailoring, die zu verwendende Infrastruktur und das Vorgehen bzgl.
der Sicherheit umfassen.

C.1.1.5.19 Berichtswesen und Kommunikationswege

In den vorhergehenden Themen wurden die Organisation und Vorgaben für die unterschiedlichen Aufgaben
der Planung und Durchführung von Projekten festgelegt. In diesem Thema wird ein Überblick über das dabei
festgelegte   Berichtswesen   und   die   Kommunikationswege   dargestellt.   Dies   beinhaltet   beispielsweise   die
getroffenen Festlegungen, wer wann welche Informationen in welcher Form an wen zu liefern hat.

Das Thema beschreibt sowohl die projektinterne als auch die projektexterne Kommunikation. Die Ziele des
Kommunikationsmanagements werden dabei in der Zielgruppenübersicht definiert, die Umsetzung wird im
Kommunikationsplan beschrieben.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

68

Zielgruppenübersicht

 Referenz Produkte

Die Zielgruppenübersicht beschreibt, welche Personen und Personenkreise welche Informationen über das
Projekt   erhalten  müssen,   sollen   oder   möchten.   Kommunikationszielgruppen   sind  oft   deckungsgleich  mit
Projektstakeholdern,   und   umfassen   beispielsweise   die   Projektmitarbeiter,   Lenkungsausschuss,   Leitung,
Anwender,   aber   auch   Öffentlichkeit   oder   Medien.   Ziel   des   Kommunikationsmanagements   ist   es,   das
Informationsbedürfnis der einzelnen Zielgruppen durch geeignete Maßnahmen zu bedienen.

Kommunikationsplan

 wie

Der   Kommunikationsplan   beschreibt,
definierten
Informationsbedürfnisse   der   Kommunikationszielgruppen   befriedigt   werden   sollen.   Er   legt   fest,   welche
Information   (z.B.   Projektfortschritt),   wann   (z.B.   jeweils   zum   Monatsende)   in   welcher   Form   und   über
welches Medium (z.B. schriftlicher Projektstatusbericht via E-Mail) an welche Kommunikationszielgruppe
(z.B.   Lenkungsausschuss   und   Leitung)   kommuniziert   wird   und   wer   dafür   verantwortlich   ist   (z.B.
Projektleiter). Auch die projektinterne Kommunikation wird hier geplant und organisiert, beispielsweise dass
alle Besprechungen protokolliert werden und an wen das Protokoll im Anschluss verteilt wird.

 Zielgruppenübersicht

in   der

die

C.1.2 Planung und Steuerung

C.1.2.1 Projektfortschrittsentscheidung

Die  Projektdurchführungsstrategie  definieren   den   Rahmen   für   die   Projektdurchführung.   Sie   legen   die
 e    fest. Auf Grundlage der vorzulegenden
Reihenfolge der im Projekt zu erreichenden  Entscheidungspunkt
Produktexemplar
 e    wird   in   jedem  Entscheidungspunkt  über   das   Erreichen   der   anstehenden
Projektfortschrittsstufe entschieden und das Ergebnis in der Projektfortschrittsentscheidung festgehalten.

Dabei   werden   der   Projektfortschritt   bewertet,   die   inhaltliche   und   zeitliche   Planung   für   den   nächsten
Planungsabschnitt abgestimmt  und die hierfür notwendigen Ressourcen freigegeben sowie Vorgaben und
Randbedingungen des weiteren Projekts definiert. Der dabei betrachtete Planungsabschnitt muss mindestens
den nächsten Projektabschnitt umfassen.

 es     getroffen,   so   dass   alle
Die   Projektfortschrittsentscheidung   wird   im   Rahmen   des  Lenkungsausschuss
Entscheidungsträger entsprechend dazu beitragen können. Verantwortlich für die Entscheidung ist aber der
Projekteigner. Nur er kann über die Freigabe von Planung und Ressourcen entscheiden.

Für   jeden   im   Projekt   anstehenden   Entscheidungspunkt   wird   eine   eigene   Projektfortschrittsentscheidung
getroffen. Die erste Projektfortschrittsentscheidung im Rahmen des Entscheidungspunktes Projekt genehmigt
repräsentiert die Beauftragung des Projektes durch das übergeordnete Management.

Verantwortlich

Projekteigner

Mitwirkend

Aktivität

Vorlagen

Erzeugt durch

Lenkungsausschuss, Projektleiter, Multi-Projektkoordination

Projektfortschrittsentscheidung herbeiführen

Projektfortschrittsentscheidung(.odt|.doc)

Anbahnung und Organisation:
Projekthandbuch (Projektdurchführungsplan)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland




C.1 Produkte

Entscheidungsrelevant
bei

69

Projekt initialisiert, Anforderungen festgelegt, Produktvision entworfen,
Ausschreibung freigegeben, Angebotsaufforderung erstellt, Beauftragung erteilt,
Iteration geplant, Gesamtsystem entworfen, System entworfen, Einheit(en)
entworfen, Einheit(en) realisiert, System integriert, Lieferung durchgeführt,
Projektfortschritt überprüft, Abnahme erklärt, Abnahme durchgeführt,
Systembetrieb freigegeben, Gesamtprojekt aufgeteilt, Gesamtprojektfortschritt
überprüft, Projekt abgeschlossen

Sonstiges

Extern

C.1.2.1.1 Bewertung

Die Bewertung dient dazu festzustellen, ob das Projekt alle notwendigen Ergebnisse  fertig gestellt hat, um
die Aufgaben des nächsten Projektabschnitt
 s   erfolgreich anzugehen. Grundlage hierfür sind die im Rahmen
des Entscheidungspunkt

 en    Produkte.

 es    vorgelegt

C.1.2.1.2 Entscheidungsvorlage und getroffene Entscheidung

Muss   auf   Basis   der  Organisation   und   Vorgaben   zum   Projektmanagement  eine   formale   Entscheidung
durchgeführt   werden,   sind   in   diesem   Thema   alle   für   die   Entscheidung   notwendigen   Informationen
zusammengestellt. Es beschreibt damit die

➢ Priorisierten Kriterien zur Bewertung alternativer Lösungen

➢ Alternativen Lösungen

➢ Ausgewählte Bewertungsmethodik

➢ Bewertung der alternativen Lösungen

➢ Empfohlene Lösung

➢ Dokumentation der Entscheidung

C.1.2.1.3

Inhaltliche und zeitliche Planung

Die  Projektfortschrittsentscheidung  dokumentiert   den   mit   dem  Projekteigner  und  Lenkungsausschuss
abgestimmten Rahmen für den nächsten Planungsabschnitt, der mindestens den nächsten  Projektabschnitt
beinhaltet.   Hierbei   wird   die   vereinbarte   inhaltliche   und   zeitliche   Planung   für   diesen   Planungsabschnitt
festgehalten. Diese umfasst eine zusammenfassende Darstellung der gegebenenfalls angepassten Eckdaten
des Projektauftrags, Projekthandbuchs,  QS-Handbuch
 s    und Projektplans hinsichtlich des geplanten Grades
der Produktfertigstellung, sowie die Termin-, Qualitäts-, Aufwands- und Kostenziele.

C.1.2.1.4 Ressourcenplanung

Die   Ressourcenplanung   umfasst   die   vereinbarte   und   vom  Projekteigner  und   dem  Lenkungsausschuss
zugesicherte   Bereitstellung   von   Ressourcen   für   den   anstehenden   Planungsabschnitt,   zum   Beispiel
qualifiziertes Personal, Material und Finanzmittel.

C.1.2.1.5 Vorgaben und Rahmenbedingungen

In diesem Thema werden die mit dem Projekteigner und dem Lenkungsausschuss vereinbarten Vorgaben und
Rahmenbedingungen   zusammenfassend   dokumentiert.
  Sie   umfassen   die   im   Rahmen   der
Projektfortschrittsentscheidung  veränderten   Eckdaten   der   inhaltlichen   und   zeitlichen   Planung   sowie   der
Ressourcenplanung.   Darüber   hinaus   werden   hier   auch   weitere   Vorgaben   und   Rahmenbedingungen

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland





70

 Referenz Produkte

festgehalten, die der Projekteigner und der Lenkungsausschuss dem Projekt mit auf den Weg gegeben haben,
zum Beispiel einzuhaltende Standards und Richtlinien und notwendige Kooperationen mit Einrichtungen und
Personen außerhalb des Projektes.

C.1.2.2 Projektplan

Planung   ist   die   gedankliche   Vorwegnahme   von   Handlungen,   die   geeignet   erscheinen,   um   ein   Ziel   zu
erreichen. Ein Plan ist die bei der Planung entstehende Dokumentation der Gedanken.

Für   die   gesicherte   und   geordnete   Durchführung   eines   Projekts   ist   ein   solider   Projektplan   zwingend
erforderlich. Der Projektplan beschreibt die gewählte Vorgehensweise des Projekts und legt detailliert fest,
was wann und von wem zu tun ist. Der Projektplan ist damit die Basis für die Kontrolle und Steuerung des
Projektes. Der  Projektleiter  ist für ihn verantwortlich. Die Erstellung und Bearbeitung des Projektplanes
erfolgt aber in Abstimmung mit allen Projektbeteiligten.

Der   Projektplan   umfasst   in   der   Regel   eine   Menge   von   einzelnen   Teilplänen   oder   Plansichten,   die   im
Folgenden als Themen dargestellt sind und sich in der Praxis auf unterschiedliche Dokumente oder Dateien
verteilen können. Je nach Projektart und Projektgröße können einzelne Sichten mehr oder weniger wichtig
sein. Wenn im V-Modell von Projektplan gesprochen wird, ist die Gesamtheit dieser Plansichten gemeint.

Verantwortlich

Projektleiter

Mitwirkend

Aktivität

Methoden

Werkzeuge

Vorlagen

Inhaltlich abhängig

Entscheidungsrelevant
bei

KM-Verantwortlicher, Projekteigner, QS-Verantwortlicher, Systemarchitekt

Projekt planen

Projektplanung und -steuerung

Projektplanung, Tailoring/Projektinitialisierung, V-Modell XT Projektassistent

Projektplan(.odt|.doc)

Planung der Prüfung von Systemelementen:
Implementierungs-, Integrations- und Prüfkonzept System, Implementierungs-,
Integrations- und Prüfkonzept SW

Projekt initialisiert, Anforderungen festgelegt, Produktvision entworfen,
Ausschreibung freigegeben, Angebotsaufforderung erstellt, Beauftragung erteilt,
Iteration geplant, Gesamtsystem entworfen, System entworfen, Einheit(en)
entworfen, Einheit(en) realisiert, System integriert, Lieferung durchgeführt,
Projektfortschritt überprüft, Abnahme erklärt, Abnahme durchgeführt,
Systembetrieb freigegeben, Gesamtprojekt aufgeteilt, Gesamtprojektfortschritt
überprüft

Sonstiges

Initial

C.1.2.2.1 Projektstrukturplan

Der   Projektstrukturplan   (engl.   Work   Breakdown   Structure)   ist   die   vollständige,   hierarchische   und
überlappungsfreie Gliederung des Projekts in Planungssegmente. "Planungssegment" ist dabei ein abstrakter
Begriff, der das gesamte Projekt, Teilprojekte, (Unter-)Arbeitspakete oder auch Einzelaufgaben umfasst.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

71

Jedes   Planungssegment   im   Projektstrukturplan   kann   aus   weiteren,   nachgeordneten   Planungssegmenten
bestehen.  Die  Planungssegmente  bilden damit  einen "Projekt-Baum",   in dessen Wurzel  sich das  Projekt
selbst befindet und der sich immer weiter "verästelt". Wird ein Planungssegment allerdings in nachgeordnete
Planungssegmente aufgeteilt, so muss diese Aufteilung vollständig und überlappungsfrei erfolgen (100%-
Regel).

Der   Projektstrukturplan   enthält   für   jedes   Planungssegment   den   Verantwortlichen   und   ggf.   weitere
Basisdaten, beispielsweise Start, Ende, Aufwand, Kosten und wichtigste Ergebnisse. Der Projektstrukturplan
enthält nicht die zeitlichen und logischen Abhängigkeiten zwischen den einzelnen Arbeitspaketen.

C.1.2.2.2 Produktstrukturplan

Der Produktstrukturplan (engl. Product Breakdown Structure) beschreibt die Ergebnisse des Projekts, die
Ergebnisstruktur   und   die   Abhängigkeiten,   beispielsweise   den   Aufbau   eines   Systems   aus   Segmenten,
Einheiten,  Komponenten und Modulen und ist  damit  verwandt  mit  der  Systemarchitektur  und der darin
beschriebenen Dekomposition des Systems. Aber auch wichtige Dokumente wie das Projekthandbuch oder
die Systemspezifikation sollten als Ergebnisse im Produktstrukturplan auftauchen. Das V-Modell hilft bei der
 en   , sowie durch die
Erstellung eines Produktstrukturplans durch die Einordnung von Produkten in Disziplin
Definition von strukturellen, inhaltlichen und erzeugenden Produktabhängigkeit
 en   . Der Produktstrukturplan
kann   außerdem   die   Zuordnung   der   Ergebnisse   zu   den   einzelnen   Plansegmenten/Arbeitspaketen   des
Projektstrukturplans enthalten.

Beispiel: "Das System X besteht aus der SW-Einheit Server und der SW-Einheit Client. Der Server wird in
AP 1 erstellt, der Client in AP 2, die Integration zum System erfolgt im AP 3."

C.1.2.2.3

Termin- und Ablaufplan

Der Termin- und Ablaufplan beschreibt den zeitlichen Ablauf eines Projekts. Typischerweise wird er in Form
eines   Gantt-Diagramms   dargestellt,   das   Vorgänge,   Sammelvorgänge,   Vorgangsfolgen   und   Meilensteine
enthält. Der Termin- und Ablaufplan enthält die zeitliche Abfolge von Arbeitspaketen und Aufgaben und
berücksichtigt   dabei   fachliche,   technische   und   organisatorische  Abhängigkeiten.   Dauer   und  Termine   der
Vorgänge ergeben sich aus dem geschätzten Aufwand und der Kapazität der verfügbaren Ressourcen. Aus
dem Termin- und Ablaufplan lässt sich somit der kritische Pfad eines Projekts ableiten.

Auf   oberster  Abstraktionsebene   zeigt   der  Termin-   und  Ablaufplan   den   Projektablauf   mit   den   wichtigen
Projektphasen   und   Meilensteinen   und   beinhaltet   damit   den  Projektdurchführungsplan  aus   dem
Projekthandbuch,   der   sich   wiederum   aus   der   beim   Tailoring   gewählten  Projektdurchführungsstrategie
ableitet.   In   der   Detailansicht   veranschaulicht   der   Termin-   und   Ablaufplan   die   konkrete   Terminierung
einzelner Aufgaben und Arbeitspakete.

C.1.2.2.4 Ressourcen- und Organisationsplan

Der Ressourcen- und Organisationplan beschreibt, welche Ressourcen in welchem Umfang benötigt werden
(Aufwandsplan), welche Ressourcen dem Projekt zur Verfügung stehen (Mitarbeiterverfügbarkeitsplan), und
wie diese Ressourcen in den Plansegmenten/Arbeitspaketen eingesetzt werden (Mitarbeitereinsatzplan).

Aufwandsplan

Der Aufwandsplan zeigt für jedes Plansegment (z.B. Arbeitspaket) auf, welche Aufwände in diesem anfallen;
ggf. können diese Aufwände rollenspezifisch und/oder zeitspezifisch ermittelt werden, beispielsweise "AP 3
benötigt im Mai 20 PT SW-Architekt und im Juni 50 PT SW-Entwickler".

Mitarbeiterverfügbarkeitsplan

Der   Mitarbeiterverfügbarkeitsplan   zeigt   auf,   welche   Mitarbeiter   zu   welchem   Anteil   und   in   welchem
Zeitraum für das Projekt zur Verfügung stehen, beispielsweise "Frau Müller ist im Mai zu 70% für das
Projekt verfügbar".

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland



72

Mitarbeitereinsatzplan

 Referenz Produkte

Der Mitarbeitereinsatzplan beschreibt, welcher Mitarbeiter in welcher Rolle und in welchem Zeitraum in den
einzelnen Plansegmenten eingesetzt wird,  beispielsweise "Frau Müller arbeitet  im Mai  zu 50% als SW-
Architektin im AP 1 und zu 20% als Prüferin im AP 2".

C.1.2.2.5 Budget- und Kostenplan

Der Budget- und Kostenplan zeigt das für das Projekt verfügbare Budget sowie die geplanten Kosten bzw.
Ausgaben.   Budget   und   geplante   Kosten   werden   dabei   für   die   einzelnen   Arbeitspakete   des
Projektstrukturplans ausgewiesen. Betrachtet werden der in Geldwert umgerechnete Aufwand sowie weitere
im Projekt anfallende externe (bzw. haushaltswirksame) Kosten, beispielsweise für Lizenzen, Hardware oder
Reisen, aber auch interne (bzw. nicht haushaltswirksame) Kosten wie z.B. Kosten für Fortbildungen. Der
initiale Budget- und Kostenplan dient als Basis für Soll-Ist-Vergleiche in Bezug auf die Kosten. Notwendige
Änderungen im Budget- und Kostenplan werden im Projektverlauf dokumentiert.

C.1.2.2.6 QS-Plan

Der   QS-Plan   legt   die  Aufgaben,   Verantwortlichkeiten   und   die   erforderlichen   Ressourcen,   zum   Beispiel
Personen und Arbeitsmittel, fest, um Prüfungen im Projekt durchzuführen. Geprüft werden können dabei
Ergebnisse   wie   Dokumente   oder   Systemelemente   und   Prozesse,   beispielsweise   immer   wiederkehrende
Aufgaben.

Prüfplan Dokumente

Der Prüfplan Dokumente enthält alle entsprechenden Dokumenten-Prüfungsaktivitäten mit den zugehörigen
Informationen, wie Prüfspezifikation erstellen und Prüfprotokoll erstellen.

Integrations- und Prüfplan Systemelemente

Der   Integrations-   und   Prüfplan   Systemelemente   enthält   alle   entsprechenden   systemelementspezifischen
Integrations- und Prüfungsaktivitäten mit den zugehörigen Informationen, zum Beispiel System integrieren
und Systemelement prüfen.

Prüfplan Prozesse

Der   Prüfplan   Prozesse   enthält   alle   entsprechenden   Prozess-Prüfungsaktivitäten   mit   den   zugehörigen
Informationen, wie Prüfspezifikation erstellen und Prüfprotokoll erstellen.

C.1.2.2.7 Ausbildungsplan

Im Ausbildungsplan sind rollen- und projektspezifische Schulungen und Weiterbildungen zur Qualifizierung
der Projektmitarbeiter einzuplanen. Die hierfür einzuplanenden Aktivitäten sind nicht Bestandteil des V-
Modells. Sie müssen projektspezifisch festgelegt werden.

C.1.2.3 Aufgabenliste

Eine Aufgabenliste (auch: To-do-Liste, Liste offener Punkte, Action-Item-Liste) hält fest, welche Aufgaben
im Projekt anstehen, bis wann sie erledigt sein müssen und wer sie verantwortet. Die Einträge ergeben sich
in   der   Regel   aus  Besprechungsdokumenten,   beispielsweise   im   Nachgang   der   Projekt-Jour-fixes;   die
Statusverfolgung geschieht meist ebenfalls im Rahmen der Besprechungen. Sie liegt in der Regel in der
Verantwortung des Projektleiters. Ob und wie eine Aufgabenliste geführt wird, ist im Projekthandbuch unter
Organisation und Vorgaben zum Projektmanagement beschrieben.

Verantwortlich

Projektleiter

Aktivität

Arbeitsauftragsliste erstellen

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

Vorlagen

Erzeugt durch

Aufgabenliste (Externe Kopiervorlage)

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zum Projektmanagement)

73

Sonstiges

Keine Produktvorlage

C.1.2.4 Schätzung

Für eine gesicherte Planung und Durchführung von Projekten sind verlässliche  Schätzung unerlässlich. Im
Rahmen  einer   Schätzung  wird  der   Umfang  des   Schätzobjektes  und  der   damit   verbundene  Aufwand  mit
einem   gewissen   Unsicherheitsfaktor   nachvollziehbar   und   methodisch   untermauert,   abgeschätzt   und
dokumentiert.

Im Rahmen der Schätzung werden beispielsweise die Schätzobjekte, deren Beschreibung, die Schätzwerte,
die   Schätzannahmen  und  die   eingesetzte   Schätzmethodik  dokumentiert.  Typische   Schätzobjekte   sind  bei
einer
 Umfangschätzung  zu   erstellende   Spezifikationen   oder   Systemelemente   sowie   bei   einer
Aufwandsschätzung durchzuführende Arbeitspaket

 e  .

Für   die   Schätzung   ist   der  Projektleiter  verantwortlich.   Zur   Erstellung   der   Schätzung   greift   er   auf   die
notwendigen Projektbeteiligten und gegebenenfalls auf weitere zusätzliche Experten zurück.

Auf Basis der Schätzungen wird die Projektplanung erstellt. Im Zuge der Projektdurchführung ergeben sich
neue   Fakten,   und   Schätzparameter   konkretisieren   sich.   Dementsprechend   werden   dann   neue,   präzisere
Schätzungen   durchgeführt.   Die   Anzahl   und   Häufigkeit   der   zu   erstellenden   Schätzungen   wird   im
Projekthandbuch festgelegt.

Verantwortlich

Projektleiter

Aktivität

Methoden

Werkzeuge

Vorlagen

Erzeugt durch

Schätzung durchführen

Schätzmodelle

Projektplanung

Schätzung(.odt|.doc)

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zum Projektmanagement)

C.1.2.4.1 Umfangschätzung

In diesem Thema wird der Umfang des Schätzobjektes abgeschätzt. Der abzuschätzende Umfang kann dabei
durch die Funktionalität des Systems, beispielsweise Art und Anzahl von Anwendungsfällen, Function Points
oder   Object   Points,   oder   die   zu   erstellenden   Ergebnisse,   wie   die   Art   und   Anzahl   der   Klassen   oder
Programmzeilen, bestimmt werden. Die für eine Schätzung verwendeten Schätzeinheiten müssen eindeutig
definiert sein.

Darüber hinaus liefern Schätzungen wichtige Informationen für die Projektsteuerung, für Fehlervorhersagen
und   für   die  Abschätzung   der  Auslegung   von   Zielsystemen,   zum   Beispiel   Rechner,   Rechnernetze   und
Busstrukturen.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


74

C.1.2.4.2 Aufwandsschätzung

 Referenz Produkte

In der Aufwandsschätzung wird auf der Basis des abgeschätzten Umfangs ein Schätzwert für den Aufwand
ermittelt, beispielsweise in Personenmonaten oder -tagen. Es geht um den Nettoaufwand; Urlaub, Krankheit
und anderer, nicht projektrelevanter Aufwand wird nicht berücksichtigt. Der Aufwand für die übergreifenden
Projektarbeiten, wie Konfigurationsmanagement und Projektmanagement, muss mit abgeschätzt werden.

Neben dem Umfang sind auch Einflussfaktoren wie die Erfahrung der Projektbeteiligten, die Stabilität der
Anforderungen oder der Wiederverwendungsgrad des Schätzobjektes mit einem Aufschlag oder Abzug an
Aufwand zu berücksichtigen.

C.1.2.5 WiBe (Vorkalkulation)

Eine erste Wirtschaftlichkeitsbetrachtung (WiBe) ist als Vorkalkulation bereits im Projekt-Vorlauf  jedes V-
Modell-Projekts zu erstellen. In der Vorkalkulation werden folgende Aspekte berücksichtigt:

➢ Ausgangslage und Handlungsbedarf

➢ Ziele und Erfolgskriterien

➢ Alternativen und Lösungsmöglichkeiten

➢ Einmalige und laufende Kosten / Nutzen (WiBe KW)

➢ Qualitativ-strategische Wirkungen (WiBe Q)

➢ Externe Effekte (WiBe E, einschl. Dringlichkeit)

Diese  Aspekte   werden   anhand   der   zum   Projekt   passenden   Kriterien   der   WiBe-Module   KW,   Q   und   E
bewertet. Abschließend wird die Wirtschaftlichkeit der Maßnahme anhand des Kapitalwerts und der Werte
für WiBe Q und E insgesamt ermittelt.

Verantwortlich

Projektauftraggeber

Mitwirkend

Aktivität

Werkzeuge

Inhaltlich abhängig

Betriebsbeauftragter, Fachverantwortlicher, Multi-Projektkoordination

WiBe (Vorkalkulation) erstellen

WiBe-Kalkulator

Fortschreibung der WiBe:
WiBe (Fortschreibung)

Entscheidungsrelevant
bei

Projekt genehmigt

Sonstiges

Extern, Keine Produktvorlage

C.1.2.6 WiBe (Fortschreibung)

Die WiBe (Fortschreibung) ist eine Folgeversion der WiBe (Vorkalkulation). Die WiBe muss beim Vorliegen
des   Lastenhefts   fortgeschrieben   werden.   Sie   aktualisiert   die   Vorkalkulation   anhand   der   nun   im   Detail
vorliegenden Anforderungen und ggf. neuer Erkenntnisse. Sonstige Fortschreibungen der WiBe während der
Projektlaufzeit liegen im Ermessen des Projektleiters.

Verantwortlich

Projektleiter

Mitwirkend

Anforderungsanalytiker (AG)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

Aktivität

Werkzeuge

Erzeugt durch

Inhaltlich abhängig

75

WiBe fortschreiben

WiBe-Kalkulator

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zum Projektmanagement)

Berücksichtigung der WiBe im Projektabschlussbericht:
Projektabschlussbericht
Berücksichtigung der WiBe in den Anforderungen:
Lastenheft (Anforderungen)
Fortschreibung der WiBe:
WiBe (Vorkalkulation)

Entscheidungsrelevant
bei

Anforderungen festgelegt, Produktvision entworfen

Sonstiges

Keine Produktvorlage

C.1.3 Risikomanagement

C.1.3.1 Risikoliste

Ziel   des   Risikomanagements   ist   es,   mögliche   Risiken   im  Projekt   frühzeitig   zu   erkennen   und   auf   diese
Risiken proaktiv zu reagieren, bevor sie zu einem Problem für das Projekt werden. In der  Risikoliste werden
die identifizierten Risiken verwaltet und die geplanten Gegenmaßnahmen festgehalten.

Für   die   Risikoliste   ist   der  Projektleiter  verantwortlich.   Zur   Bearbeitung   greift   er   auf   die   notwendigen
Projektbeteiligten und gegebenenfalls auf weitere zusätzliche Experten zurück. Die erkannten Risiken und
die zugehörigen Gegenmaßnahmen fließen dann wieder in die Projektplanung ein.

Verantwortlich

Projektleiter

Mitwirkend

Aktivität

Vorlagen

Erzeugt durch

QS-Verantwortlicher

Risiken managen

Risikoliste(.odt|.doc), Risikoliste (Externe Kopiervorlage)

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zum Risikomanagement)

C.1.3.1.1

Identifizierte Risiken

In diesem Thema werden alle identifizierten Risiken mit den im Projekthandbuch geforderten Informationen,
wie Status des Risikos und Risikoklasse, aufgelistet.

C.1.3.1.2 Maßnahmenplan

Den   identifizierten   Risiken   werden   die   Maßnahmen,   die   als   Reaktion   auf   das   Risiko   geplant   sind,
gegenübergestellt. Für jede Maßnahme sind die im Projekthandbuch geforderten Informationen (wie Art der
Maßnahmen, Ereignis, das zur Einleitung der Maßnahme führt, und Verantwortlicher für die Durchführung
der Maßnahmen) festzuhalten.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

76

C.1.3.1.3 Risikomatrix

 Referenz Produkte

Die Risikomatrix gibt einen Überblick über die in der Risikoliste erfassten Risiken und kann deshalb auch
als Übersicht für das Thema Aktuelle Risiken und Risikomaßnahmen im Projektstatusbericht dienen. Häufig
ist sie als tatsächliche Matrix mit den Dimensionen Eintrittswahrscheinlichkeit und Schaden realisiert.

C.1.4 Problem- und Änderungsmanagement

C.1.4.1 Problemmeldung/Änderungsantrag

Problemmeldung  und  Änderungsantrag  sind  der   dokumentierte  Wunsch  nach  Behebung  eines   Problems,
Durchführung einer Änderung oder Einführung einer Verbesserung. Auslöser von Problemmeldungen und
Änderungsanträgen können unterschiedlicher Natur sein, zum Beispiel Änderungen von Anforderungen oder
Fehler im System.

Jeder Projektbeteiligte, zum Beispiel SW-Entwickler oder Anwender, kann eine Problemmeldung oder einen
Änderungsantrag erstellen. Problemmeldung und Änderungsantrag können als  externes Produkt  auch von
außerhalb des Projekts eingehen. Wann Problemmeldungen und Änderungsanträge erstellt werden müssen,
um eine Änderung einzusteuern und durchzusetzen, ist im Projekthandbuch geregelt.

Verantwortlich

Änderungsverantwortlicher

Aktivität

Werkzeuge

Vorlagen

Erzeugt durch

Problemmeldung/Änderungsantrag erstellen

Fehler-/Änderungsmanagement

ProblemmeldungÄnderungsantrag(.odt|.doc)

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zum Problem- und
Änderungsmanagement)

Sonstiges

Extern

C.1.4.1.1

Identifikation und Einordnung

In diesem Thema werden das identifizierte Problem und der Änderungswunsch näher beschrieben. Dabei
sind   alle   Informationen   (wie   eindeutige   Identifikation   des   Problemgegenstandes,   Antragsteller   und
Dringlichkeit)   die   notwendig   sind,   um   das   Problem   zu   reproduzieren   beziehungsweise   den
Änderungswunsch nachzuvollziehen, zu dokumentieren. Jeder Änderungswunsch ist zu kategorisieren und
einzuordnen, zum Beispiel bezüglich seiner Änderungsart, Änderungspriorität und Fertigstellung.

C.1.4.1.2 Chancen-/Problembeschreibung

Ausgehend   von   der   Beschreibung   des   Ist-Zustandes   im   vorhergehenden   Thema   wird   in   der
Chancen-/Problembeschreibung
technische   Probleme,
Ressourcenknappheit und organisatorische Konflikte, dargelegt. In der Begründung kann auch auf Chancen
und Nutzen der gewünschten Änderung sowie auf den möglichen Schaden durch eine Nicht-Durchführung
der Änderungen hingewiesen werden.

der   Änderungsgrund,

  zum   Beispiel

Bezieht sich der Antrag auf eine Abweichung des Systemverhaltens von den vorgegebenen Anforderungen
oder auf die Änderung einer Anforderung, so ist diese Anforderung anzugeben.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


C.1 Produkte

C.1.4.1.3

Lösungsvorschlag

77

Falls   der  Antragsteller   konkrete   Vorstellungen   von   der   Umsetzung   des   Soll-Zustandes   hat,   sind   diese
darzustellen. Dabei sollten auch die Auswirkungen der Umsetzungen mit dargestellt werden.

C.1.4.2 Problem-/Änderungsbewertung

Die  Problem-/Änderungsbewertung  beinhaltet   die  Analyse   eines   oder   mehrerer   Problemmeldungen   und
Änderungsanträge.   Die   Bewertung   muss   alle   notwendigen   Informationen,   wie   Problemanalyse,
Lösungsvorschlag und Auswirkungen, beinhalten, damit die  Änderungssteuerungsgruppe (Change Control
Board) auf dieser Basis über die Problemmeldungen und Änderungsanträge entscheiden kann.

Verantwortlich

Änderungsverantwortlicher

Mitwirkend

Aktivität

Werkzeuge

Vorlagen

Erzeugt durch

KM-Verantwortlicher, QS-Verantwortlicher, SW-Architekt, Systemarchitekt

Problemmeldung/Änderungsantrag bewerten

Fehler-/Änderungsmanagement

Problem-Änderungsbewertung(.odt|.doc)

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zum Problem- und
Änderungsmanagement)

C.1.4.2.1 Chancen-/Problemanalyse

In der Problemanalyse muss die Ursache der betrachteten Probleme beziehungsweise der Änderungswünsche
erforscht und dargestellt werden. Die sich dabei ergebenden Chancen sind entsprechend darzustellen und
einzuordnen.

C.1.4.2.2

Lösungsvorschläge und Auswirkungen

Alle   sinnvollen   Lösungsvorschläge   zur   Behebung   der   Probleme   beziehungsweise   zur   Umsetzung   der
Änderungen sind mit den notwendigen Informationen, zum Beispiel Aufwand, Auswirkungen sowie Vor-
und Nachteile, darzustellen.

C.1.4.2.3 Empfehlung

Die   zuvor   dargestellten  Lösungsvorschläge   werden  bewertet   und  die   geeignetste   Lösung   mit   möglichen
Varianten im Sinne einer Empfehlung festgelegt und begründet.

C.1.4.3 Änderungsentscheidung

In   der  Änderungsentscheidung  wird   die   Entscheidung   der  Änderungssteuerungsgruppe   (Change   Control
Board) bezüglich einer oder mehrerer Problem-/Änderungsbewertung
 en    dokumentiert. Erforderlich ist dabei
eine aussagekräftige Begründung dafür, nach welchen Kriterien die Entscheidung zu Stande gekommen ist.
Die Änderungsentscheidung enthält auch den Beschluss, wie diese Entscheidung umgesetzt werden soll.

Verantwortlich

Mitwirkend

Änderungssteuerungsgruppe (Change Control Board)

KM-Verantwortlicher, Änderungsverantwortlicher, QS-Verantwortlicher, SW-
Architekt, Systemarchitekt

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


78

Aktivität

Werkzeuge

Vorlagen

Erzeugt durch

 Referenz Produkte

Änderungen beschließen

Fehler-/Änderungsmanagement

Änderungsentscheidung(.odt|.doc)

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zum Problem- und
Änderungsmanagement)

C.1.4.3.1 Entscheidungskriterien

Kriterien wie entstehende Kosten, zeitliche Verzögerung und Eignung der Lösung werden dargestellt und
begründet.

C.1.4.3.2 Entscheidung und Begründung

Die   Entscheidungen   hinsichtlich   der   zur   Entscheidung   anstehenden  Problem-/Änderungsbewertung
 en
werden   dokumentiert   und   begründet.   Dabei   ist   darzustellen,   wie   eine   Entscheidung   im   Rahmen   des
laufenden Projektgeschehens einzusteuern und umzusetzen ist. Die Auswirkungen, zum Beispiel bezüglich
Zeit, Budget und Ressourcen, werden so dokumentiert, dass sie vom  Projektmanagement  für die weitere
Planung   berücksichtigt   werden   können.   Aufgrund   einer   getroffenen   Änderungsentscheidung   können
Anpassungen   am   bestehenden   Vertrag   notwendig   werden.   Diese   sind   in   einem   Vertragszusatz   zu
dokumentieren.

Erzeugt

Erstellung eines Vertragszusatzes:
Vertragszusatz

C.1.4.4 Änderungsstatusliste

Die  Änderungsstatusliste  enthält entsprechend den Vorgaben des Projekthandbuchs alle Informationen, die
zur Verwaltung und Verfolgung eingegangener Problemmeldungen und Änderungsanträge notwendig sind
(zum   Beispiel   Identifikation   und   Status   der   Problemmeldungen   und   Änderungsanträge,   zuständige
Änderungsverantwortliche   sowie   eine   Referenz   auf   die  Problem-/Änderungsbewertung  und   die
Änderungsentscheidung).

Verantwortlich

Änderungsverantwortlicher

Aktivität

Werkzeuge

Vorlagen

Erzeugt durch

Änderungsstatusliste führen

Fehler-/Änderungsmanagement

Änderungsstatusliste(.odt|.doc), Änderungsstatusliste (Externe Kopiervorlage)

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zum Problem- und
Änderungsmanagement)

Inhaltlich abhängig

Inhalte im Projektstatusbericht:
Projektstatusbericht

Entscheidungsrelevant
bei

Iteration geplant

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


C.1 Produkte

79

C.1.5 Konfigurationsmanagement

C.1.5.1 Produktbibliothek

Die  Produktbibliothek  umfasst   alle  Produktexemplar
 en   ,   die   im   Laufe   eines
Projekts   erstellt   werden.   Dies   sind   mindestens   die   Produktexemplare,   die   durch   die   Produktstruktur
vorgegeben sind. Dementsprechend kann sie als die zentrale Projektdatenbank verstanden werden. Sie wird
in der Regel durch ein KM-Werkzeug verwaltet.

 e    und   deren  Produktversion

In der Produktbibliothek werden alle Produktexemplare entsprechend den Vorgaben im Projekthandbuch
verwaltet.   Ein   Produktexemplar   im   Sinne   des  V-Modells   kann   ein   Dokument   sein,   ein   HW-   oder  SW-
Element, einzeln oder in möglicher Kombination.

Die Festlegung, welche Produktexemplar
zum Beispiel physikalische HW-Element
Identifikator der Produktexemplar

 e   nicht körperlich in der Produktbibliothek verwaltet werden, wie
 e  , erfolgt im Projekthandbuch. In diesem Fall muss zumindest ein

 e   in der Produktbibliothek verwaltet werden.

Über die im Projekthandbuch  festgeschriebene Identifikationssystematik, zum Beispiel Dateiablagestruktur
und   Namenskonventionen,   erfolgt   die   Initialisierung,   Identifikation   und   Referenzierung   aller   in   der
Produktbibliothek verwalteten  Produkte. Beim Einrichten und bei der Aufbewahrung der Produkte in der
Produktbibliothek sind zudem die im Projekthandbuch festgelegten Zugriffsrechte einzurichten, zu verwalten
und zu überwachen.

Verantwortlich

KM-Verantwortlicher

Mitwirkend

Aktivität

Werkzeuge

Entscheidungsrelevant
bei

Projektleiter

Produktbibliothek einrichten und pflegen

KM-Werkzeug

Projekt initialisiert

Sonstiges

Initial, Keine Produktvorlage

C.1.5.2 Produktkonfiguration

Eine  Produktkonfiguration  ist eine Menge von  Produktversion
besteht darin, die Konfigurationseinheiten und deren strukturellen Zusammenhang zu definieren.

 en   , eine so genannte Baseline. Ihre Aufgabe

Produktkonfigurationen   werden   entsprechend   den   Vorgaben   des  Projekthandbuch
 s    und   gemäß   dem
Projektplan   erstellt.   Dabei   muss   zumindest   für   jeden  Entscheidungspunkt  und   jeden   projektinternen
Meilenstein   eine   Produktkonfiguration   erstellt   werden.   Wie   jedes  Produktexemplar  wird   auch   die
Produktkonfiguration selbst in der Produktbibliothek verwaltet.

In einer Produktkonfiguration müssen dabei die im Entscheidungspunkt beziehungsweise im projektinternen
Meilenstein vorgegebenen Produkte in der im Projekthandbuch und im Projektplan geplanten Produktversion
enthalten   sein.   Darüber   hinaus   sind   mindestens   alle  Produktversion
 en     mit   aufzunehmen,   zu   denen   es
 en    gibt. Weitere Produktversion
Produktabhängigkeit

 en    können beliebig mit aufgenommen werden.

Verantwortlich

KM-Verantwortlicher

Aktivität

Werkzeuge

Produktkonfiguration verwalten

KM-Werkzeug

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland











80

Erzeugt durch

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zum Konfigurationsmanagement)

 Referenz Produkte

Sonstiges

Keine Produktvorlage

C.1.5.3 Informationssicherheits-Managementsystem

Organisationen,   die   IT-Systeme   entwickeln,   nutzen   oder   betreiben,   sollten   ein  Informationssicherheits-
Managementsystem (ISMS) einführen und etablieren. Verantwortlich für das ISMS einer Organisation ist der
Informationssicherheitsbeauftragte. Er legt unter anderem den Einsatzbereich des ISMS in der Organisation
fest und kann für Systementwicklungsprojekte bestimmen, dass darin verwendete Werkzeuge in das ISMS
einzubinden sind.

Das Informationssicherheits-Managementsystem muss zum Entscheidungspunkt  Projekt initialisiert  die im
Projekt relevanten Aspekte und Werkzeuge abdecken. Die Details werden im Projekthandbuch im Thema
Organisation und Vorgaben zum Informationssicherheits-Managementsystem festgelegt.

Verantwortlich

Informationssicherheitsbeauftragter

Entscheidungsrelevant
bei

Projekt initialisiert

Sonstiges

Extern, Keine Produktvorlage

C.1.6 Qualitätssicherung

C.1.6.1 QS-Handbuch

Das   V-Modell   ist   ein   generischer   Vorgehensstandard,   der   für   ein   konkretes   Projekt   angepasst   und
konkretisiert werden muss. Das QS-Handbuch legt die für die Qualitätssicherung notwendigen Anpassungen
und Ausgestaltungen fest. Somit dokumentiert es Art und Umfang der Anwendung des V-Modells im Projekt
und ist Informationsquelle und Richtlinie für alle Projektbeteiligten.

Das  QS-Handbuch  beinhaltet eine Kurzbeschreibung der Qualitätsziele im Projekt, die Festlegung der zu
prüfenden  Produkte  und Prozesse, die Organisation und Vorgaben für die Planung und Durchführung der
Qualitätssicherung im Projekt sowie die Vorgaben für die Qualitätssicherung von externen Zulieferungen.
Der   QS-Verantwortliche   muss   dieses   zentrale   Produkt   in  Abstimmung   mit   den   Schlüsselpersonen   des
Projekts erarbeiten.

Dabei   werden   im   QS-Handbuch   insbesondere   auch   Häufigkeit   und   Notwendigkeit   der   Erzeugung
weiterführender Produkte, die für die Qualitätssicherung im Projekt notwendig sind, festgelegt, zum Beispiel
QS-Bericht

 e  , Nachweisakte und Prüfprotokolle.

Verantwortlich

QS-Verantwortlicher

Mitwirkend

Aktivität

Vorlagen

Projektleiter, Qualitätsmanager

QS-Handbuch erstellen

QS-Handbuch(.odt|.doc)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


C.1 Produkte

Inhaltlich abhängig

81

Vorgaben des QS-Handbuchs zu Fertigprodukten:
Prüfspezifikation Systemelement
Vorgaben für den Auftragnehmer:
Vergabeunterlagen (Ausschreibung)
Vorgaben zur Prüfung der Systemelemente:
Implementierungs-, Integrations- und Prüfkonzept System, Implementierungs-,
Integrations- und Prüfkonzept SW

Entscheidungsrelevant
bei

Projekt initialisiert, Iteration geplant, Gesamtprojekt aufgeteilt

Sonstiges

Initial

C.1.6.1.1 Qualitätsziele und -anforderungen

In   diesem   Thema   werden   die  Anforderungen   an   die   Qualitätssicherung   und   die   damit   verfolgten   Ziele
definiert,   zum   Beispiel   eine   geforderte   Prüfüberdeckung   oder   formale   Spezifikationstechniken.   Die
Qualitätsziele und -anforderungen  an den Entwicklungsgegenstand selbst werden hier nicht festgelegt, sie
werden   bereits   mit   dem  Lastenheft   (Anforderungen)  fixiert.   Steht   ein   organisationsspezifisches
Qualitätsmanagementhandbuch   zur   Verfügung,   so   sind   die   dort   festgelegten   Ziele   und   Anforderungen
projektspezifisch auszugestalten.

C.1.6.1.2

Zu prüfende Produkte

In diesem Thema sind die durch eine eigenständige Qualitätssicherung zu prüfenden  Produkte festzulegen.
Die   Auswahl   ist   entsprechend   zu   begründen.   Für   diese   Produkte   müssen   dann   die   entsprechenden
Prüfspezifikationen   und   Prüfprotokolle   erstellt   werden.   Die   Festlegung,   welche   Systemelemente   geprüft
werden, wird in den zugrunde liegenden Implementierungs-, Integrations- und Prüfkonzepten dokumentiert.

Erzeugt

Prüfung von Dokumenten:
Prüfprotokoll, Prüfspezifikation
Prüfung von Produktkonfigurationen:
Prüfprotokoll, Prüfspezifikation

C.1.6.1.3

Zu prüfende Prozesse

In diesem Thema sind die durch eine unabhängige Qualitätssicherung zu prüfenden Prozesse festzulegen.
Die Auswahl ist entsprechend zu begründen. Dabei sind auch die der Prüfung zugrunde liegenden Standards
oder   Richtlinien   zu   nennen.   Für   alle   zu   prüfenden   Prozesse   müssen   dann   die   entsprechenden
Prüfspezifikationen und Prüfprotokolle erstellt werden.

Darüber   hinaus   kann   die   Prüfung   weiterer   Prozesse   durch   aktuelle   Ereignisse   im   Projekt   oder   im
Projektumfeld erforderlich werden, wie z. B. eine überdurchschnittliche Abweichung der Soll- von der Ist-
Planung.

Erzeugt

Prüfung von Prozessen:
Prüfprotokoll, Prüfspezifikation

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

82

 Referenz Produkte

C.1.6.1.4 Organisation und Vorgaben zur Qualitätssicherung im Projekt

In diesem Thema werden die Vorgaben des V-Modells zur Qualitätssicherung von Produkten bzw. Prozessen
im Projekt angepasst und konkretisiert. Es erfolgt die Festlegung, ob, wann und welche QS-Produkte für die
Qualitätssicherung im Projekt zu verwenden sind, nach welchen Methoden, Richtlinien und Standards diese
zu erstellen sind und mit welchen Werkzeugen sie zu bearbeiten sind.

Abgeleitet   aus   den  Qualitätszielen  sind  die   Organisation  der   Qualitätssicherung  und  ihre   Befugnisse   im
Projekt festzulegen. Die konstruktiven und analytischen QS-Maßnahmen werden dargestellt.

Zu   den   konstruktiven   Maßnahmen   zählen   z.B.   defensives   Programmieren,   das   Vier-Augen-Prinzip,
typprüfende Sprachen, Standards, Vorgehensmodelle, Checklisten und Richtlinien. Zu den analytischen QS-
Maßnahmen gehören alle Prüfmaßnahmen für Dokumente (z.B. Reviews), Tests von Systemelementen und
Prozessprüfungen.

Für   Fertigprodukte   (z.B.   Beistellungen   oder   Softwarebibliotheken)   ist   festzulegen,   wie   diese   für   einen
Einsatz   im   Projekt   qualitätsgesichert   werden.   Dies   umfasst   etwa   die   verpflichtende   Erstellung   einer
Prüfspezifikation.   Die   zur   Qualitätssicherung   von   Fertigprodukten   einzusetzenden   Prüfverfahren   und
notwendigen   Prüfschritte   werden   im   Thema  Vorgaben   für   die   Prüfspezifikation   von   Fertigprodukten
beschrieben.

Im Rahmen der Qualitätslenkung ist zu beschreiben, wie entstehende Qualitätsprobleme behandelt, verfolgt
und durch korrektive Maßnahmen gelöst werden sollen. Weiter ist festzulegen, für welche Problemarten ein
außerplanmäßiger QS-Bericht erstellt werden muss.

Falls   Unterauftragnehmer   beauftragt   werden   sollen,   ist   darzustellen,   welche   Qualitätsvorgaben   für   diese
gelten sollen.

Erzeugt

Führung einer Nachweisakte:
Nachweisakte
Zusammenfassende Beurteilung der Produktqualität:
QS-Bericht

C.1.6.1.5 Organisation und Vorgaben zur Qualitätssicherung der Auslieferung

In   diesem   Thema   werden   die   Vorgaben   zur   Qualitätssicherung   der  Auslieferung   konkretisiert.   Für   jede
Lieferung wird vom Auftraggeber eine Abnahmeprüfung durchgeführt.

Daher   muss   der   Auftragnehmer   sicherstellen,   dass   seine   Lieferung   den   Vorgaben   des   Auftraggebers
entspricht. Die Vorgaben sind mittels der Prüfspezifikation Systemelement nachvollziehbar. Sie enthält unter
anderem eine Aufzählung der Prüffälle der Abnahme, mit welchen die Abdeckung der Anforderungen des
Lastenheftes nachweisbar ist.

Die Ergebnisse werden im Prüfprotokoll Systemelement festgehalten.

C.1.6.1.6 Vorgaben für die Prüfspezifikation von Fertigprodukten

Wie   alle   Systemelemente   können   und   sollen   auch   Fertigprodukte   geprüft   werden.   Hierfür   wird   eine
entsprechende Prüfspezifikation Systemelement erstellt. Um gerade bei Fertigprodukten einen einheitlichen
Standard der Qualitätssicherung zu erreichen, werden in diesem Thema Vorgaben für die Prüfspezifikationen
von   Fertigprodukten   festgelegt.   Diese   Vorgaben   sind   dann   in   die   zugehörige   Prüfspezifikation
Systemelement zu übernehmen. Die Vorgaben können beispielsweise Anforderungen bezüglich Umfang und
Qualität der Dokumentation, des Herstellers und der Verwendungsprüfung beinhalten.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

83

C.1.6.1.7 Vorgaben für das QS-Handbuch der Auftragnehmer

Der  Auftraggeber  kann die  unterschiedlichsten Vorgaben für  die  Qualitätssicherung beim Auftragnehmer
festlegen.   Sie   werden   hier   dokumentiert   und   in   alle  Ausschreibungen   übernommen   und   gegebenenfalls
angepasst. Diese Vorgaben können beispielsweise den Umfang der Produkt- und Prozessprüfung und über
die Anwendung des V-Modells hinausgehende anzuwendende konstruktive Qualitätssicherungsmaßnahmen
umfassen.

C.1.6.2 Prüfspezifikation

Eine Prüfspezifikation dient dem Prüfer als Vorgabe und Anleitung bei der Durchführung der Prüfung. In der
 s  ,   für   jede   zu   prüfende   Produktversion
Regel   wird,   entsprechend   den   Vorgaben   des  QS-Handbuch
beziehungsweise für jedes zu prüfende Prozessexemplar eine spezifische Prüfspezifikation erstellt. Für jede
Prüfung wird somit eine eigene Prüfspezifikation erstellt.

Verantwortlich

Prüfer

Aktivität

Methoden

Vorlagen

Erzeugt durch

Prüfspezifikation erstellen

Review

Prüfspezifikation(.odt|.doc)

Qualitätssicherung:
QS-Handbuch (Zu prüfende Produkte; Zu prüfende Prozesse)
Systementwurf:
Pflichtenheft (Gesamtsystementwurf) (Abnahmekriterien und Vorgehen zur
Ausgangsprüfung)

Entscheidungsrelevant
bei

Gesamtsystem entworfen

C.1.6.2.1 Prüfobjekt

Es   ist   die   eindeutig   definierte   identifizierbare   Version   des   Prüfobjektes   festzulegen,   auf   die   sich   die
Prüfspezifikation beziehungsweise das Prüfprotokoll bezieht.

C.1.6.2.2 Prüfkriterien

In   den   Prüfkriterien   wird   die   Prüfmethode   (beispielsweise   Review,   Inspektion   und   Interviews),   der
Abdeckungsgrad   (zum   Beispiel   Stichprobenprüfung   und   vollständige   Prüfung)   sowie   die   formalen   und
inhaltlichen   Prüfkriterien   (wie   inhaltliche   Korrektheit,   Einhaltung   der   Projektstandards,   Gestaltung,
Rechtschreibung)   beschrieben.   Zu   den  Prüfkriterien   gehören   auch   die   Bedingungen   für   das   erfolgreiche
beziehungsweise nicht erfolgreiche Ende der Prüfung.

C.1.6.3 Prüfprotokoll

Das   Prüfprotokoll   enthält   die   vom  Prüfer  verfassten Aufzeichnungen  über   den Verlauf   der   Prüfung,   die
Gegenüberstellung   von   Ist-   und   Soll-Ergebnissen,   sowie   die   Analyse   der   identifizierten   Ist-/Soll-
Abweichungen und entsprechende Lösungsvorschläge. Dabei ist darauf zu achten, dass das Prüfergebnis
reproduziert werden kann.

Anzahl   und   Häufigkeit   der   Durchführung   von   Prüfungen   und   damit   der   Erstellung   der   zugehörigen
Prüfprotokolle   entsprechen   den  Vorgaben  im  QS-Handbuch  und  in   den   zugehörigen  Implementierungs-,
Integrations- und Prüfkonzepten.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


84

 Referenz Produkte

Verantwortlich

Prüfer

Aktivität

Methoden

Vorlagen

Erzeugt durch

Prüfprotokoll erstellen

Prozessanalyse, Review

Prüfprotokoll(.odt|.doc)

Qualitätssicherung:
QS-Handbuch (Zu prüfende Produkte; Zu prüfende Prozesse)
Systementwurf:
Pflichtenheft (Gesamtsystementwurf) (Abnahmekriterien und Vorgehen zur
Ausgangsprüfung)

Inhaltlich abhängig

Prüfprotokolle im QS-Bericht:
QS-Bericht

Entscheidungsrelevant
bei

Lieferung durchgeführt

C.1.6.3.1 Prüfobjekt

Es   ist   die   eindeutig   definierte   identifizierbare   Version   des   Prüfobjektes   festzulegen,   auf   die   sich   die
Prüfspezifikation beziehungsweise das Prüfprotokoll bezieht.

C.1.6.3.2 Prüfergebnisse

In diesem Thema werden der Verlauf der Prüfung und die dabei ermittelten Ist-Ergebnisse der Prüfung, zum
Beispiel  Systemausgaben,  identifizierte  Fehler  in  Dokumenten  und  Defizite  in  der  Prozessdurchführung,
dokumentiert und den Soll-Ergebnissen der Prüfspezifikation gegenübergestellt. Dabei ist insbesondere auch
zu dokumentieren, wie das beschriebene Prüfergebnis reproduziert werden kann.

C.1.6.3.3 Ergebnisanalyse und Korrekturvorschläge

In der Ergebnisanalyse werden die beobachteten Abweichungen zwischen den Ist-Ergebnissen und den Soll-
Ergebnissen inhaltlich und ursächlich analysiert. Konnte die Ursache identifiziert werden, so sollten bereits
Korrekturvorschläge   mit   dokumentiert   werden,   soweit   es   sie   gibt.   Zeigt   sich   aus   den  Prüfresultaten   ein
bestimmter Trend im Auftreten gleichartiger Mängel, so ist dies festzuhalten und entsprechende Maßnahmen
vorzuschlagen. Diese Informationen fließen in den QS-Bericht ein.

Entsprechend den Vorgaben im  Projekthandbuch kann  ein Prüfresultat  oder  Korrekturvorschlag  zu  einer
Problemmeldung bzw. einem Änderungsantrag führen.

C.1.6.4 Prüfspezifikation Systemelement

Die Prüfspezifikation dient dem  Prüfer  als Vorgabe und Anleitung bei der Durchführung der Prüfung und
orientiert sich an den Vorgaben im dazugehörigen Implementierungs-, Integrations- und Prüfkonzept. In der
Prüfspezifikation werden die Prüffälle und die Prüfumgebung definiert sowie eine Zuordnung der Prüffälle
zu den Anforderungen vorgenommen. Hierbei sollte jede an das Systemelement gestellte funktionale und
nicht-funktionale   Anforderung   und   alle   das   Systemelement   betreffenden   Maßnahmen   der
Sicherheitskonzeption  durch   mindestens   einen   Prüffall   abgedeckt   werden.   Die   Abdeckung   der
Anforderungen durch die Prüffälle kann beispielsweise in Form einer Abdeckungsmatrix erfolgen.

Weiterhin werden Schutzvorkehrungen beschrieben, die während der Prüfung einzuhalten sind. Mit Hilfe der
Prüfspezifikation muss entschieden werden können, ob die Prüfung erfolgreich war oder nicht.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

Verantwortlich

Prüfer

85

Mitwirkend

Aktivität

Methoden

Vorlagen

Erzeugt durch

Ergonomieverantwortlicher, SW-Architekt, Systemarchitekt, Systemintegrator

Prüfspezifikation Systemelement erstellen

Test

Prüfspezifikation Systemelement(.odt|.doc)

Systementwurf:
Implementierungs-, Integrations- und Prüfkonzept SW (Zu prüfenden SW-
Elemente), Implementierungs-, Integrations- und Prüfkonzept System (Zu
prüfende Systemelemente), Pflichtenheft (Gesamtsystementwurf)
(Abnahmekriterien und Vorgehen zur Ausgangsprüfung)

Inhaltlich abhängig

Vorgaben des QS-Handbuchs zu Fertigprodukten:
QS-Handbuch

Entscheidungsrelevant
bei

C.1.6.4.1 Prüfobjekt

Gesamtsystem entworfen, System entworfen, Einheit(en) entworfen

Es   ist   die   eindeutig   definierte   identifizierbare   Version   des   Prüfobjektes   festzulegen,   auf   die   sich   die
Prüfspezifikation beziehungsweise das Prüfprotokoll bezieht.

C.1.6.4.2 Prüfstrategie

Die Prüfstrategie beschreibt, wie die Anforderungen an das Prüfobjekt durch eine geeignete Struktur von
Prüffällen in der notwendigen und geforderten Prüfungstiefe abgeprüft werden können. Dabei werden die
verwendeten   Prüfmethoden,
  und
Nachweismethoden, wie zum Beispiel Test, Nachweis und Demonstrator, festgelegt.

  wie   zum   Beispiel   Funktionsprüfung   und   Stressprüfung,

Die   anzuwendende   Prüfstrategie   wird   aus   dem   entsprechenden   Implementierungs-,   Integrations-   und
Prüfkonzept abgeleitet und gegebenenfalls angemessen verfeinert.

C.1.6.4.3 Prüffälle

Basierend auf der Konzeption der Prüfstrategie erfolgt in diesem Thema eine Beschreibung der einzelnen
Prüffälle   mit   den   hierfür   notwendigen   Informationen   wie   Startzustand   des   Systems,   Prüfablauf   und
erwarteter Endzustand des Systems.

Besonders   zu   berücksichtigen   sind   der   Abdeckungsgrad   der   Prüffälle   sowie   die   Endekriterien.   Der
Abdeckungsgrad  legt   fest,   wie   detailliert   zu  prüfen  ist.   Die   Endekriterien  benennen  Bedingungen,   unter
denen die Prüfung erfolgreich abgeschlossen ist.

C.1.6.4.4 Prüfumgebung

Die   allgemeine   Prüfumgebung   wird   bereits   in   den   zugehörigen   Implementierungs-,   Integrations-   und
Prüfkonzepten beschrieben. In diesem Thema werden notwendige Ausgestaltungen und Erweiterungen der
allgemeinen   Prüfumgebung   oder   speziell   notwendige   Prüfumgebungen   für   das   konkrete   Prüfobjekt
beschrieben,   wie   zum  Beispiel   ein   Drehtisch   mit   Echtzeitbildsimulation   für   einen   Flugkörper   oder   eine
Autoteststrecke mit einem entsprechenden Fahrparcours.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

86

C.1.6.4.5 Prüffallzuordnung

 Referenz Produkte

Die   aus   den  Anforderungen   abgeleiteten   Prüffälle   werden   den  Anforderungen   zugeordnet.   Das   erfolgt
beispielsweise   mithilfe   einer   Abdeckungsmatrix.   Hier   soll   sichtbar   werden,   ob   der   gewünschte
Abdeckungsgrad   und   die   Prüfqualität   gegeben   sind,   besonders   in   Bezug   auf   die   vorher   festgelegte
Prüfstrategie.

C.1.6.5 Prüfprozedur Systemelement

Die  Prüfprozedur Systemelement  ist eine regressionsfähige Beschreibung der Durchführung der Prüffälle
gemäß den Vorgaben der Prüfspezifikation. Sie ist eine Arbeitsanleitung, die exakte Anweisungen für jeden
einzelnen Prüffall enthält und einzelne Schritte der Prüfung definiert.

Sie   kann   sowohl   ein   Drehbuch   sein,   das   manuell   abgearbeitet   wird,   oder   eine   maschinenverarbeitbare
Ablaufanweisung, die von einer Prüfumgebung automatisiert ausgeführt wird.

Verantwortlich

Prüfer

Mitwirkend

Aktivität

Vorlagen

Erzeugt durch

Systemintegrator

Prüfprozedur Systemelement realisieren

Prüfprozedur Systemelement(.odt|.doc)

Systementwurf:
Implementierungs-, Integrations- und Prüfkonzept SW (Zu prüfenden SW-
Elemente), Implementierungs-, Integrations- und Prüfkonzept System (Zu
prüfende Systemelemente), Pflichtenheft (Gesamtsystementwurf)
(Abnahmekriterien und Vorgehen zur Ausgangsprüfung)

C.1.6.6 Prüfprotokoll Systemelement

Das   Prüfprotokoll   enthält   die   vom  Prüfer  verfassten Aufzeichnungen  über   den Verlauf   der   Prüfung,   die
Gegenüberstellung   von   Ist-   und   Soll-Ergebnissen,   sowie   die   Analyse   der   identifizierten   Ist-/Soll-
Abweichungen und entsprechende Lösungsvorschläge. Dabei ist darauf zu achten, dass das Prüfergebnis
reproduziert werden kann.

Anzahl   und   Häufigkeit   der   Durchführung   von   Prüfungen   und   damit   der   Erstellung   der   zugehörigen
Prüfprotokolle   entsprechen   den  Vorgaben  im  QS-Handbuch  und  in   den   zugehörigen  Implementierungs-,
Integrations- und Prüfkonzepten.

Verantwortlich

Prüfer

Mitwirkend

Aktivität

Methoden

Vorlagen

Erzeugt durch

SW-Entwickler, Systemintegrator

Systemelement prüfen

Simulation, Test

Prüfprotokoll Systemelement(.odt|.doc)

Systementwurf:
Implementierungs-, Integrations- und Prüfkonzept SW (Zu prüfenden SW-
Elemente), Implementierungs-, Integrations- und Prüfkonzept System (Zu
prüfende Systemelemente), Pflichtenheft (Gesamtsystementwurf)
(Abnahmekriterien und Vorgehen zur Ausgangsprüfung)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

Inhaltlich abhängig

Entscheidungsrelevant
bei

C.1.6.6.1 Prüfobjekt

87

Prüfprotokolle im QS-Bericht:
QS-Bericht
Prüfprotokolle in der Nachweisakte:
Nachweisakte

Einheit(en) realisiert, System integriert, Lieferung durchgeführt

Es   ist   die   eindeutig   definierte   identifizierbare   Version   des   Prüfobjektes   festzulegen,   auf   die   sich   die
Prüfspezifikation beziehungsweise das Prüfprotokoll bezieht.

C.1.6.6.2 Prüfergebnisse

In diesem Thema werden der Verlauf der Prüfung und die dabei ermittelten Ist-Ergebnisse der Prüfung, zum
Beispiel  Systemausgaben,  identifizierte  Fehler  in  Dokumenten  und  Defizite  in  der  Prozessdurchführung,
dokumentiert und den Soll-Ergebnissen der Prüfspezifikation gegenübergestellt. Dabei ist insbesondere auch
zu dokumentieren, wie das beschriebene Prüfergebnis reproduziert werden kann.

C.1.6.6.3 Ergebnisanalyse und Korrekturvorschläge

In der Ergebnisanalyse werden die beobachteten Abweichungen zwischen den Ist-Ergebnissen und den Soll-
Ergebnissen inhaltlich und ursächlich analysiert. Konnte die Ursache identifiziert werden, so sollten bereits
Korrekturvorschläge   mit   dokumentiert   werden,   soweit   es   sie   gibt.   Zeigt   sich   aus   den  Prüfresultaten   ein
bestimmter Trend im Auftreten gleichartiger Mängel, so ist dies festzuhalten und entsprechende Maßnahmen
vorzuschlagen. Diese Informationen fließen in den QS-Bericht ein.

Entsprechend den Vorgaben im  Projekthandbuch kann  ein Prüfresultat  oder  Korrekturvorschlag  zu  einer
Problemmeldung bzw. einem Änderungsantrag führen.

C.1.6.7 Abnahmespezifikation

Für   jede  Lieferung  muss   eine  Abnahmeprüfung   durchgeführt   werden.   Die  Abnahmespezifikation  ist   die
Grundlage für diese Abnahmeprüfung. In ihr werden alle zur Abnahme notwendigen Prüffälle und - falls die
Lieferung auch Dokumente enthält - auch die notwendigen Prüfkriterien definiert.

Sie enthält die Spezifikation der Eingangskontrolle einschließlich der Überprüfung der Sollkonfiguration.
Die Sollkonfiguration wird entweder vom Auftraggeber vorgeschrieben oder ist in der Lieferung enthalten,
zum   Beispiel   in   den   Release   Notes.   Darüber   hinaus   enthält   die  Abnahmespezifikation  alle   zur
Abnahmeprüfung notwendigen Prüffälle sowie die Prüfumgebung. Sie wird aus den im Vertrag und in den
Vertragszusätzen   enthaltenen   Anforderungen   -   und   nur   aus   diesen   -   erstellt.   Die   Abdeckung   dieser
Anforderungen an die Lieferung durch die Prüffälle und Prüfkriterien ist zu dokumentieren, beispielsweise in
Form einer Abdeckungsmatrix.

Verantwortlich

Prüfer

Mitwirkend

Aktivität

Vorlagen

Informationssicherheitsverantwortlicher, Datenschutzverantwortlicher,
Betriebsverantwortlicher

Abnahmespezifikation erstellen

Abnahmespezifikation(.odt|.doc)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

88

Erzeugt durch

 Referenz Produkte

Systemanalyse:
Lastenheft (Anforderungen) (Abnahmekriterien), Lastenheft Gesamtprojekt
(Abnahmekriterien)
Systemspezifikation:
Externe-Einheit-Spezifikation (Abnahmekriterien und Vorgehen zur
Abnahmeprüfung), Externes-SW-Modul-Spezifikation (Abnahmekriterien und
Vorgehen zur Abnahmeprüfung)

Entscheidungsrelevant
bei

Beauftragung erteilt

C.1.6.7.1 Prüfobjekt

Es   ist   die   eindeutig   definierte   identifizierbare   Version   des   Prüfobjektes   festzulegen,   auf   die   sich   die
Prüfspezifikation beziehungsweise das Prüfprotokoll bezieht.

C.1.6.7.2 Prüfstrategie

Die Prüfstrategie beschreibt, wie die Anforderungen an das Prüfobjekt durch eine geeignete Struktur von
Prüffällen in der notwendigen und geforderten Prüfungstiefe abgeprüft werden können. Dabei werden die
verwendeten   Prüfmethoden,
  und
Nachweismethoden, wie zum Beispiel Test, Nachweis und Demonstrator, festgelegt.

  wie   zum   Beispiel   Funktionsprüfung   und   Stressprüfung,

Die   anzuwendende   Prüfstrategie   wird   aus   dem   entsprechenden   Implementierungs-,   Integrations-   und
Prüfkonzept abgeleitet und gegebenenfalls angemessen verfeinert.

C.1.6.7.3 Prüffälle

Basierend auf der Konzeption der Prüfstrategie erfolgt in diesem Thema eine Beschreibung der einzelnen
Prüffälle   mit   den   hierfür   notwendigen   Informationen   wie   Startzustand   des   Systems,   Prüfablauf   und
erwarteter Endzustand des Systems.

Besonders   zu   berücksichtigen   sind   der   Abdeckungsgrad   der   Prüffälle   sowie   die   Endekriterien.   Der
Abdeckungsgrad  legt   fest,   wie   detailliert   zu  prüfen  ist.   Die   Endekriterien  benennen  Bedingungen,   unter
denen die Prüfung erfolgreich abgeschlossen ist.

C.1.6.7.4 Prüfkriterien

In   den   Prüfkriterien   wird   die   Prüfmethode   (beispielsweise   Review,   Inspektion   und   Interviews),   der
Abdeckungsgrad   (zum   Beispiel   Stichprobenprüfung   und   vollständige   Prüfung)   sowie   die   formalen   und
inhaltlichen   Prüfkriterien   (wie   inhaltliche   Korrektheit,   Einhaltung   der   Projektstandards,   Gestaltung,
Rechtschreibung)   beschrieben.   Zu   den  Prüfkriterien   gehören   auch   die   Bedingungen   für   das   erfolgreiche
beziehungsweise nicht erfolgreiche Ende der Prüfung.

C.1.6.7.5 Prüfumgebung

Die   allgemeine   Prüfumgebung   wird   bereits   in   den   zugehörigen   Implementierungs-,   Integrations-   und
Prüfkonzepten beschrieben. In diesem Thema werden notwendige Ausgestaltungen und Erweiterungen der
allgemeinen   Prüfumgebung   oder   speziell   notwendige   Prüfumgebungen   für   das   konkrete   Prüfobjekt
beschrieben,   wie   zum  Beispiel   ein   Drehtisch   mit   Echtzeitbildsimulation   für   einen   Flugkörper   oder   eine
Autoteststrecke mit einem entsprechenden Fahrparcours.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

C.1.6.7.6 Prüffallzuordnung

89

Die   aus   den  Anforderungen   abgeleiteten   Prüffälle   werden   den  Anforderungen   zugeordnet.   Das   erfolgt
beispielsweise   mithilfe   einer   Abdeckungsmatrix.   Hier   soll   sichtbar   werden,   ob   der   gewünschte
Abdeckungsgrad   und   die   Prüfqualität   gegeben   sind,   besonders   in   Bezug   auf   die   vorher   festgelegte
Prüfstrategie.

C.1.6.8 Abnahmeprotokoll

Das Abnahmeprotokoll enthält die vom Prüfer verfassten Aufzeichnungen über den Verlauf der Prüfung, die
Gegenüberstellung   von   Ist-   und   Soll-Ergebnissen,   sowie   die   Analyse   der   identifizierten   Ist-/Soll-
Abweichungen und entsprechende Lösungsvorschläge. Dabei ist darauf zu achten, dass das Prüfergebnis
reproduziert werden kann.

Verantwortlich

Prüfer

Mitwirkend

Aktivität

Vorlagen

Erzeugt durch

Anwender, Systemintegrator, Informationssicherheitsverantwortlicher,
Datenschutzverantwortlicher, Betriebsverantwortlicher

Lieferung prüfen

Abnahmeprotokoll(.odt|.doc)

Systemanalyse:
Lastenheft (Anforderungen) (Abnahmekriterien), Lastenheft Gesamtprojekt
(Abnahmekriterien)
Systemspezifikation:
Externe-Einheit-Spezifikation (Abnahmekriterien und Vorgehen zur
Abnahmeprüfung), Externes-SW-Modul-Spezifikation (Abnahmekriterien und
Vorgehen zur Abnahmeprüfung)

Inhaltlich abhängig

Prüfprotokolle im QS-Bericht:
QS-Bericht

Entscheidungsrelevant
bei

Abnahme erklärt

C.1.6.8.1 Prüfobjekt

Es   ist   die   eindeutig   definierte   identifizierbare   Version   des   Prüfobjektes   festzulegen,   auf   die   sich   die
Prüfspezifikation beziehungsweise das Prüfprotokoll bezieht.

C.1.6.8.2 Prüfergebnisse

In diesem Thema werden der Verlauf der Prüfung und die dabei ermittelten Ist-Ergebnisse der Prüfung, zum
Beispiel  Systemausgaben,  identifizierte  Fehler  in  Dokumenten  und  Defizite  in  der  Prozessdurchführung,
dokumentiert und den Soll-Ergebnissen der Prüfspezifikation gegenübergestellt. Dabei ist insbesondere auch
zu dokumentieren, wie das beschriebene Prüfergebnis reproduziert werden kann.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

90

 Referenz Produkte

C.1.6.8.3 Ergebnisanalyse und Korrekturvorschläge

In der Ergebnisanalyse werden die beobachteten Abweichungen zwischen den Ist-Ergebnissen und den Soll-
Ergebnissen inhaltlich und ursächlich analysiert. Konnte die Ursache identifiziert werden, so sollten bereits
Korrekturvorschläge   mit   dokumentiert   werden,   soweit   es   sie   gibt.   Zeigt   sich   aus   den  Prüfresultaten   ein
bestimmter Trend im Auftreten gleichartiger Mängel, so ist dies festzuhalten und entsprechende Maßnahmen
vorzuschlagen. Diese Informationen fließen in den QS-Bericht ein.

Entsprechend den Vorgaben im  Projekthandbuch kann  ein Prüfresultat  oder  Korrekturvorschlag  zu  einer
Problemmeldung bzw. einem Änderungsantrag führen.

C.1.6.9 Prüfspezifikation Inbetriebnahme

Die  Prüfspezifikation Inbetriebnahme  enthält alle Prüfkriterien sowie die anzuwendende Prüfstrategie zur
Überprüfung,   ob   ein   geliefertes   (Teil-)System   die  Vorgaben   zum   IT-Betrieb  erfüllt   und   in   den   Betrieb
überführt werden kann. Bei erfolgreicher Prüfung kann die Betriebliche Freigabeerklärung erstellt werden.

Verantwortlich

Betriebsverantwortlicher

Vorlagen

Erzeugt durch

Prüfspezifikation Inbetriebnahme(.odt|.doc)

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zum IT-Betrieb)

Sonstiges

Extern

C.1.6.9.1 Prüfobjekte

In   diesem   Thema   sind   alle   Prüfobjekte   aufzuführen,   die   einer   Prüfung   unterzogen   werden.   Für   jedes
Prüfobjekt ist die Version anzugeben, auf die sich die Prüfspezifikation bezieht.

C.1.6.9.2 Prüfstrategie

Die Prüfstrategie beschreibt, wie die Umsetzung der in den Vorgaben zum IT-Betrieb und in deren ggf. vom
Auftragnehmer   erstellten   Erweiterungen   enthaltenen   Anforderungen   durch   geeignete   Prüffälle   geprüft
werden   (vgl.   ISO/IEC/IEEE   29119   Software   Testing).   Dabei   werden   die   verwendeten   Prüf-   (z.B.
Funktionsprüfung, Lasttest) und Nachweismethoden (z.B. Test, Demonstrator) und deren Abdeckungsgrad
(Prüftiefe, Prüfvarianten) festgelegt. Außerdem wird hier bestimmt, unter welchen Bedingungen die Prüfung
insgesamt als erfolgreich gewertet wird (Erfolgskriterien).

In Projekten, in denen der Auftraggeber Anforderungen an die Informationssicherheit oder den Datenschutz
definiert hat, muss für eine Inbetriebnahme auch deren Umsetzung abgesichert werden. Die entsprechenden
Prüffälle leiten sich aus den Vorgaben zur Informationssicherheit, den Vorgaben zum Datenschutz und deren
ggf. vom Auftragnehmer erstellten Erweiterungen ab.

C.1.6.9.3 Prüffälle

Basierend auf der Prüfstrategie werden in diesem Thema die einzelnen Prüffälle beschrieben mit den hierfür
notwendigen   Informationen   wie   Startzustand   des   Systems,   Prüfablauf   und   erwartetem   Endzustand   des
Systems.   Die   Prüffälle   entsprechen   in   ihrer   Prüftiefe   und   ihren   Varianten   dem   Abdeckungsgrad   der
Prüfstrategie.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

C.1.6.9.4 Prüfumgebung

91

Für   die   Inbetriebnahme-Prüfung   ist   meist   eine   spezielle   Prüfumgebung   notwendig,   die   der   späteren
Produktivumgebung   möglichst   ähnlich   ist.   Dieses   Thema   beschreibt,   welche   Eigenschaften   die
Prüfumgebung aufweisen muss und wie sie ggf. aufzusetzen ist.

C.1.6.9.5 Prüffallzuordnung

Die  Prüffälle  werden den Anforderungen zugeordnet, deren Umsetzung sie prüfen sollen, beispielsweise
mithilfe einer Abdeckungsmatrix. Hierbei muss erkennbar werden, ob der in der  Prüfstrategie  festgelegte
Abdeckungsgrad erreicht wird.

C.1.6.9.6 Prüfkriterien für die Systemdokumentation

Zusammen   mit   dem   (Teil-)System   wird   auch   die   dazugehörige   technische   Systemdokumentation
(Architekturen,   Spezifikationen,   Implementierungs-,   Integrations-   und   Prüfkonzepte)   geliefert,   bei
informationssicherheits- und datenschutzkritischen Systemen auch die Sicherheitskonzeption. Dieses Thema
definiert die Prüfkriterien für die entsprechenden Dokumente aus Sicht des Betriebs.

C.1.6.9.7 Prüfkriterien für die Erweiterung der Vorgaben zum IT-Betrieb

Während der Systementwicklung erforderliche Änderungen und Erweiterungen an den vom Auftraggeber
festgelegten Vorgaben zum IT-Betrieb werden vom Auftragnehmer in den Erweiterungen der Vorgaben zum
IT-Betrieb beschrieben. Dieses Thema definiert die Prüfkriterien für das entsprechende Dokument aus Sicht
des Betriebs.

C.1.6.9.8 Prüfkriterien für die Erweiterung der Vorgaben zur Informationssicherheit

Während der Systementwicklung erforderliche Änderungen und Erweiterungen an den vom Auftraggeber
festgelegten  Vorgaben   zur   Informationssicherheit  werden   vom Auftragnehmer   in   den   Erweiterungen   der
Vorgaben   zur   Informationssicherheit   beschrieben.   Dieses   Thema   definiert   die   Prüfkriterien   für   das
entsprechende Dokument aus Sicht des Betriebs.

C.1.6.9.9 Prüfkriterien für die Erweiterung der Vorgaben zum Datenschutz

Während der Systementwicklung erforderliche Änderungen und Erweiterungen an den vom Auftraggeber
festgelegten  Vorgaben zum Datenschutz  werden vom Auftragnehmer in den Erweiterungen der Vorgaben
zum Datenschutz beschrieben. Dieses Thema definiert die Prüfkriterien für das entsprechende Dokument aus
Sicht des Betriebs.

C.1.6.10 Prüfprotokoll Inbetriebnahme

Das  Prüfprotokoll Inbetriebnahme  enthält den dokumentierten Prüfungsablauf und die Prüfungsergebnisse
für die in der Prüfspezifikation Inbetriebnahme definierten Prüfobjekte.

Verantwortlich

Betriebsverantwortlicher

Vorlagen

Erzeugt durch

Prüfprotokoll Inbetriebnahme(.odt|.doc)

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zum IT-Betrieb)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

92

Inhaltlich abhängig

 Referenz Produkte

Prüfprotokolle im QS-Bericht:
QS-Bericht
Relevanz des Prüfprotokolls Inbetriebnahme für die Betriebliche
Freigabeerklärung:
Betriebliche Freigabeerklärung

Sonstiges

Extern

C.1.6.10.1 Prüfobjekte

In   diesem   Thema   sind   alle   Prüfobjekte   aufzuführen,   die   einer   Prüfung   unterzogen   wurden.   Für   jedes
Prüfobjekt ist die Version anzugeben, auf die sich das Prüfprotokoll bezieht.

C.1.6.10.2 Prüfergebnisse

In diesem Thema werden der Verlauf der Prüfung und die dabei ermittelten Ist-Ergebnisse der Prüfung, zum
Beispiel Systemausgaben oder identifizierte Fehler in Dokumenten dokumentiert und den Soll-Ergebnissen
der   Prüfspezifikation   gegenübergestellt.   Hierbei   ist   festzuhalten,   wie   das   beschriebene   Prüfergebnis
reproduziert werden kann.

C.1.6.10.3 Ergebnisanalyse und Korrekturvorschläge

In   der   Ergebnisanalyse   werden   übereinstimmende   Soll-   und   Ist-Ergebnisse   als   Erfolg   gewertet   und
Abweichungen inhaltlich und ursächlich analysiert. Zu identifizierten Ursachen sollten Korrekturvorschläge
dokumentiert werden. Zeigt sich aus den Prüfresultaten ein bestimmter Trend im Auftreten gleichartiger
Mängel, so ist dies festzuhalten und entsprechende Maßnahmen vorzuschlagen. Diese Informationen fließen
in   den  QS-Bericht  ein.   Entsprechend   den   Vorgaben   im  Projekthandbuch  kann   ein   Prüfresultat   oder
Korrekturvorschlag zu einer Problemmeldung oder einem Änderungsantrag führen.

C.1.6.11 Nachweisakte

Die  Nachweisakte  listet   alle   Nachweise   auf,   die   im   Verlauf   des   Projekts   zu   erbringen   sind.   Es   wird
aufgeführt, dass und wie die Nachweise erbracht wurden.

Beispiele für derartige Nachweise sind: Prüfung des Systems nach einem Normtyp, etwa DIN, VDE und EN,
Nachweise   von   Prüfstellen,   wie   TÜV   und   DEKRA,   und   Nachweise   von   Genehmigungsbehörden,   wie
Luftfahrtbundesamt   und   Kraftfahrtbundesamt.   Das   Erstellen   und   Führen   der   Nachweisakte   erfolgt
entsprechend den Vorgaben des QS-Handbuch

 es   .

Im Übrigen können auch die Ergebnisse projektinterner Prüfungen in der Nachweisakte festgehalten werden,
wenn beispielsweise die Durchführung solcher Prüfungen im Vertrag oder Projektauftrag vereinbart ist und
demzufolge nachgewiesen werden muss.

Verantwortlich

QS-Verantwortlicher

Aktivität

Vorlagen

Erzeugt durch

Nachweisakte führen

Nachweisakte(.odt|.doc)

Qualitätssicherung:
QS-Handbuch (Organisation und Vorgaben zur Qualitätssicherung im Projekt)

Inhaltlich abhängig

Prüfprotokolle in der Nachweisakte:
Prüfprotokoll Systemelement

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


C.1 Produkte

93

C.1.6.11.1 Notwendigkeit und Zuordnung der Nachweise

In  diesem Thema   wird   aus   den Anforderungen   abgeleitet,   welche   Nachweise   notwendig  sind.   Diese   zu
erbringenden   Nachweise   werden,   soweit   möglich,   den   verfügbaren   Nachweisen   in   der  Nachweisakte
zugeordnet.

C.1.6.11.2 Auflistung der Nachweise

Dieses Thema enthält eine Übersicht der erbrachten Nachweise mit den notwendigen Informationen wie
Identifikation, Nachweismethode, Erbringer des Nachweises und Abweichungen.

C.1.7 Messung und Analyse

C.1.7.1 Messdaten

Die   Messdaten   stellen   das   explizite   Zahlenmaterial   dar,   das   notwendig   ist,   um   die   zugehörigen
Projektkennzahlen   zu   berechnen   und   Auswertungen   zu   erstellen.   In   diesem   Produkt   werden   alle   im
Projektverlauf zur Berechnung von Projektkennzahlen erfassten Daten gemeinsam verwaltet.

Im Projekthandbuch wird für alle Projektkennzahlen festgelegt, welche Messdatentypen, das heißt welche
Beschreibung und welcher Aufbau der zu erfassenden Daten, für ihre Berechnung notwendig sind. Für die
Ablage der Messdaten steht eine zentrale oder verteilte Ablagestruktur zur Verfügung, entsprechend den
Vorgaben des Projekthandbuchs.

Verantwortlich

Projektleiter

Aktivität

Erzeugt durch

Messdaten erfassen

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zum Projektcontrolling)

Sonstiges

Keine Produktvorlage

C.1.7.2 Kennzahlenauswertung

Kennzahlenauswertungen liefern quantitative und qualitative Aussagen, um Fragestellungen im Projekt zu
beantworten.   Eine   Kennzahlenauswertung   stellt   das   Ergebnis   und   die   möglichen   Interpretationen   der
Berechnung einer Metrik auf Basis der zur Verfügung stehenden Messdaten dar.

Dabei   können   auch   erste   Schlussfolgerungen   aus   den   Ergebnissen,   beispielsweise   Vorschläge   für
einzuleitende Maßnahmen, enthalten sein. Außerdem können Kennzahlenauswertungen auch zum Soll-Ist-
Abgleich im Rahmen der Projektsteuerung herangezogen werden.

Beispiele   für   Kennzahlenauswertungen   sind   Anzahl   der   Fehler   pro   Klasse,   Änderungsaufwand   pro
Dokument, Termintreue im Projekt, der Leistungsfortschritt oder die Kostenkontrolle über die Zeit.

Verantwortlich

Projektleiter

Aktivität

Vorlagen

Erzeugt durch

Kennzahlen berechnen und auswerten

Kennzahlenauswertung(.odt|.doc)

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zum Projektcontrolling)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

94

 Referenz Produkte

C.1.8 Berichtswesen

C.1.8.1 Besprechungsdokument

Unter dem Besprechungsdokument wird die Dokumentation der unterschiedlichen Arten von Besprechungen
(wie Jour fixe des Projekts, Entwurfsworkshops oder Anforderungserhebungsworkshops) zusammengefasst.
Dabei   wird   im   Vorfeld   eine   Einladung   verteilt   und   die   Besprechung   entsprechend   dokumentiert.
Verantwortlich ist hierbei der  Projektleiter  . Dies bezieht sich aber nicht auf die Erstellung des Produkts,
sondern   auf   seine   Verantwortung   dafür,   dass   Besprechungsdokumente   für   die   laut   Projekthandbuch   zu
dokumentierenden Besprechungen erstellt werden.

Verantwortlich

Projektleiter

Aktivität

Vorlagen

Erzeugt durch

C.1.8.1.1 Einladung

Besprechung durchführen

Besprechungsdokument(.odt|.doc)

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zum Projektmanagement)

Die Einladung enthält alle im Vorfeld notwendigen Informationen zur Durchführung der Besprechung wie
Termin, Ort, Ziel und Agenda der Besprechung.

C.1.8.1.2 Protokoll

Das Protokoll ist eine schriftliche Dokumentation des Verlaufs und der Resultate einer Besprechung. Dabei
sollten insbesondere Teilnehmer, Verteilerliste und die der Aufgabenliste hinzuzufügenden Einträge enthalten
sein. Das Protokoll ist nach Fertigstellung an alle Teilnehmer und sonstige Betroffene zu verteilen und von
diesen auf Richtigkeit zu prüfen.

C.1.8.2 Projekttagebuch

Das  Projekttagebuch  dient als projektinterne Informationsquelle über alle wichtigen Projektereignisse und
durchgeführten   Projektentscheidungen.   Damit   ist   der  Projektleiter  stets   in   der   Lage,   über   das   bisherige
Projektgeschehen - auch im Detail - Auskunft zu geben. Außerdem können die Projektmitglieder sowohl für
die restliche Projektlaufzeit als auch für Folgeprojekte die gemachten positiven wie negativen Erfahrungen
nutzen. Das Projekttagebuch wird laufend fortgeschrieben.

Verantwortlich

Projektleiter

Aktivität

Vorlagen

Erzeugt durch

Projekttagebuch führen

Projekttagebuch(.odt|.doc)

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zum Projektmanagement)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

C.1.8.2.1 Projekterfahrungen

95

Das   Thema   enthält   die   Dokumentation   aller  Projekterfahrungen,   die   positiv   wie   negativ   das   Projekt
beeinflusst haben, zum Beispiel die Projektausstattung, die Projektrisiken, das Einhalten von Vereinbarungen
und die Form und Effizienz von Besprechungen. Darüber hinaus gibt es einen Überblick über alle wichtigen
Projektereignisse und durchgeführten Projektentscheidungen.

C.1.8.2.2 Erfahrungen mit Fertigprodukten

In   diesem   Thema   werden   die   Erfahrungen   mit   externen   Zulieferern   dokumentiert.   Bei   der   zukünftigen
Auswahl von Zulieferern können diese Erfahrungen mit als Entscheidungsgrundlage dienen. Dabei sollte
sowohl die Beschreibung des Auftrags als auch die Bewertung des Zulieferers nach verschiedenen Kriterien
wie Zusammenarbeit, Qualität und Termintreue vorgenommen werden.

Diese Informationen werden an den Vergabestelle weitergeleitet, von diesem entsprechend verwaltet und bei
der Auswahl zukünftiger Zulieferer berücksichtigt.

C.1.8.3 Projektstatusbericht

Der Projektfortschritt muss regelmäßig überprüft werden, damit gegebenenfalls steuernd eingegriffen werden
kann. Der Projektstatusbericht ist das zentrale Dokument zur Beurteilung des Projektfortschritts. Er enthält
Aussagen   zum   aktuellen   Fertigungsstand,   zur   Stabilität   und   Qualität   der   Projektergebnisse,   zur
Risikoeinschätzung   und   zur  Abweichung   von   der   ursprünglichen   Planung.   Bei   Bedarf   wird   in   ihm   die
Planung aktualisiert.

Verantwortlich für den Projektstatusbericht ist der  Projektleiter. Er erstellt ihn in Zusammenarbeit mit den
anderen   Schlüsselrollen   des   Projekts.   Anzahl,   Häufigkeit   und   Verteiler   des   Projektstatusberichtes
entsprechen den Vorgaben des Projekthandbuchs. Der Projektstatusbericht wird sowohl zur projektinternen
als auch -externen Berichterstattung eingesetzt.

Verantwortlich

Projektleiter

Mitwirkend

Aktivität

Vorlagen

Erzeugt durch

Inhaltlich abhängig

Entscheidungsrelevant
bei

KM-Verantwortlicher, Änderungsverantwortlicher, QS-Verantwortlicher

Projektstatusbericht erstellen

Projektstatusbericht(.odt|.doc)

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zum Projektmanagement)

Berichte des Auftragnehmers im Projektstatusbericht:
Projektstatusbericht (von AN)
Inhalte im Projektstatusbericht:
QS-Bericht, Änderungsstatusliste

Projekt initialisiert, Anforderungen festgelegt, Produktvision entworfen,
Ausschreibung freigegeben, Angebotsaufforderung erstellt, Beauftragung erteilt,
Iteration geplant, Gesamtsystem entworfen, System entworfen, Einheit(en)
entworfen, Einheit(en) realisiert, System integriert, Lieferung durchgeführt,
Projektfortschritt überprüft, Abnahme erklärt, Abnahme durchgeführt,
Systembetrieb freigegeben, Gesamtprojekt aufgeteilt, Gesamtprojektfortschritt
überprüft

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

96

C.1.8.3.1 Managementübersicht

 Referenz Produkte

Stellt kurz und prägnant die aktuellen Kennzahlen zum Projektfortschritt dar und notwendige Maßnahmen
zur Steuerung des Projektes vor.

C.1.8.3.2 Projektergebnisse

Dieses   Thema   enthält   einen   Überblick   über   die   im   Berichtszeitraum   fertig   gestellten   Ergebnisse   und
durchgeführten Arbeiten. Konnten Ergebnisse nicht wie geplant fertig gestellt werden, so ist dies ebenfalls
hier   festzuhalten.   Die   im   Projekthandbuch   festgelegten   KM-Auswertungen   können   hierbei   eine
entsprechende Informationsquelle sein.

C.1.8.3.3 Problem- und Änderungsstatistik

In   diesem   Thema   wird   entsprechend   den   Vorgaben   des   Projekthandbuchs   die  Problem-   und
Änderungsstatistik  dargestellt,   zum   Beispiel   Anzahl   und   Umfang   der   Problemmeldungen   und
Änderungsanträge und die Anzahl der bereits fertig gestellten und wieder veränderten Produkte. Sowohl die
Änderungsstatusliste  als   auch   die   im   Projekthandbuch   festgelegten   KM-Auswertungen   können   hierbei
entsprechende Informationsquellen sein.

C.1.8.3.4 Qualitätsbewertung

Die Qualitätsbewertung beinhaltet eine Zusammenfassung des QS-Bericht

 es   .

C.1.8.3.5 Aktuelle Risiken und Risikomaßnahmen

Die   Bewertung   der   aktuellen   Risiken   und   die   notwendigen   anstehenden   und   bereits   eingeleiteten
Maßnahmen werden zusammenfassend dargestellt.

C.1.8.3.6 Sicherheitsrisiken

In   diesem   Thema   werden   die   zwischen   Auftraggeber   und   Auftragnehmer   abgestimmten   und   vom
Auftraggeber bestätigten Restrisiken der Sicherheitskonzeption dargestellt. Aus ihnen können Projektrisiken
abgeleitet   und   in   die   Projekt-Risikoliste  aufgenommen   werden   analog   dem   Vorgehen   bei   "normalen"
Projektrisiken.

C.1.8.3.7 Planungsabweichungen

Die  Abweichungen   zwischen   den   Soll-   und   Istwerten,   zum   Beispiel   hinsichtlich   Fertigstellungsgrades,
Terminsituation, Qualität und Kosten, werden dargestellt.

C.1.8.3.8 Planung für den nächsten Berichtszeitraum

Die Planung für den nächsten Berichtszeitraum, insbesondere auch die aufgrund der Planungsabweichungen
notwendigen Planungsänderungen werden zusammenfassend dargestellt. Darüber hinaus können hier auch
Entscheidungsvorlage   und   getroffene   Entscheidung
 en     für   die   Berichtsempfänger   vorgestellt   und   dann
entsprechend   verabschiedet   werden   (zum  Beispiel   eine   gravierende   Projektsteuerungsmaßnahme,   die   im
Rahmen einer Projektfortschrittsentscheidung beschlossen und eingeleitet werden muss).

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland



C.1 Produkte

C.1.8.3.9 Gesamtprojektfortschritt

97

Der  Gesamtprojektfortschritt  ist   eine   Verdichtung   der   wichtigsten   Projektfortschrittswerte   der   einzelnen
Teilprojekte für das Gesamtprojekt. Die Projektfortschrittswerte der Teilprojekte enthalten Aussagen zum
aktuellen Fertigungsstand, zur Stabilität und Qualität der Projektergebnisse, zur Risikoeinschätzung und zur
Abweichung von der ursprünglichen Planung.

Wichtig für die Darstellung des  Gesamtprojektfortschritt
Teilprojekte, zu dem aus Vergleichsgründen alle Projektfortschrittswerte ermittelt sein müssen.

 s    ist ein gemeinsamer Berichtszeitpunkt für alle

Ein   wichtiges   Ergebnis   ist   der   kritische   Pfad   des   Gesamtprojektes,   der   sich   aus   der  Aggregation   der
Projektfortschrittswerte aller Teilprojekte ergibt.

C.1.8.4 QS-Bericht

Die   Qualität   der   Ergebnisse   muss   regelmäßig   überprüft   werden,   damit   man   gegebenenfalls   steuernd
eingreifen kann. Der QS-Bericht ist das zentrale Dokument zur Beurteilung der Produktqualität. Er enthält
Aussagen   über   den   Umfang   der   durchgeführten   Prüfungen   und   deren   Ergebnisse,   eine   Bewertung
aufgetretener Qualitätsprobleme und Maßnahmen zu deren Behebung. Verantwortlich für den QS-Bericht ist
der QS-Verantwortliche. Er erstellt ihn in Zusammenarbeit mit den anderen Schlüsselrollen des Projekts.
 s  . Der  QS-
Anzahl, Häufigkeit und Verteiler des  QS-Bericht
Bericht wird sowohl zur projektinternen als auch -externen Berichterstattung eingesetzt.

 s    entsprechen den Vorgaben des  QS-Handbuch

Verantwortlich

QS-Verantwortlicher

Aktivität

Vorlagen

Erzeugt durch

Inhaltlich abhängig

Entscheidungsrelevant
bei

QS-Bericht erstellen

QS-Bericht(.odt|.doc)

Qualitätssicherung:
QS-Handbuch (Organisation und Vorgaben zur Qualitätssicherung im Projekt)

Inhalte im Projektstatusbericht:
Projektstatusbericht
Prüfprotokolle im QS-Bericht:
Prüfprotokoll, Prüfprotokoll Systemelement, Prüfprotokoll Inbetriebnahme,
Abnahmeprotokoll

Projekt initialisiert, Anforderungen festgelegt, Produktvision entworfen,
Ausschreibung freigegeben, Angebotsaufforderung erstellt, Beauftragung erteilt,
Iteration geplant, Gesamtsystem entworfen, System entworfen, Einheit(en)
entworfen, Einheit(en) realisiert, System integriert, Lieferung durchgeführt,
Projektfortschritt überprüft, Abnahme erklärt, Abnahme durchgeführt,
Gesamtprojekt aufgeteilt, Gesamtprojektfortschritt überprüft

C.1.8.4.1 Umfang der Prüfungen

Dieses Thema beinhaltet einen Überblick über den Umfang der im letzten Berichtszeitraum durchgeführten
Prüfungen.   Für   den   anstehenden   Berichtszeitraum   wird   angegeben,   welche   Prüfungen   vorgesehen   sind.
Sollten dabei Änderungen der ursprünglichen Projektplanung enthalten sein, ist dies zu dokumentieren und
zu begründen.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland




98

 Referenz Produkte

C.1.8.4.2 Status der einzelnen Prozesse

Dieses Thema stellt kurz und prägnant den Status der einzelnen Prozesse dar, spiegelt die Praxis an den vom
Management   gesetzten   Erwartungen,   identifiziert   Probleme   und   schlägt   notwendige  Maßnahmen   zur
Verbesserung dieser Probleme vor.

C.1.8.4.3 Qualitätsstand und -bewertung

Der   Qualitätsstand   des   Projekts   wird   durch  Art,   Umfang   und   Ergebnisse   der   durchgeführten   Prüfungen
festgestellt. Die Ergebnisse der durchgeführten Prüfungen werden soweit möglich zusammengefasst. Nicht
oder nur unzureichend durch Prüfungen abgedeckte Bereiche werden dokumentiert. Aufgetretene Probleme
oder Fehler und deren Ursachen werden dargestellt und in ihrer Kritikalität bewertet.

C.1.8.4.4 Maßnahmen zur Verbesserung

Hier werden die Maßnahmen zur Behebung der festgestellten Qualitätsprobleme beschrieben. Dabei sollten
auch   die   Auswirkungen   der   Durchführung   dieser   Maßnahmen   dargestellt   werden,   zum   Beispiel   der
notwendige  Aufwand   zur   Durchführung,   sich   ergebende   Verzögerungen   und   mögliche   Risiken   bei   der
Behebung.

C.1.8.5 Projektabschlussbericht

Am Ende eines Projekts sollten die erreichten Ergebnisse und die gewonnenen Erfahrungen dokumentiert
werden, so dass nachfolgende Projekte darauf aufbauen können. Der Projektabschlussbericht enthält deshalb
eine kurze Übersicht über die Motivation und Zielsetzung des Projekts, eine Überblicksbeschreibung der
erarbeiteten Projektergebnisse und deren Qualität sowie eine Kurzbeschreibung des Projektverlaufs und der
dabei gewonnenen Erfahrungen. Der Projektabschlussbericht dient zur Information aller Projektbeteiligten
und insbesondere auch der projektexternen Personen.

Verantwortlich

Projektleiter

Mitwirkend

Aktivität

Vorlagen

Erzeugt durch

Inhaltlich abhängig

KM-Verantwortlicher, QS-Verantwortlicher, Verfahrensverantwortlicher
(Fachseite), Verfahrensverantwortlicher (IT-Betrieb), Verfahrensverantwortlicher
(Weiterentwicklung)

Projekt abschließen

Projektabschlussbericht(.odt|.doc)

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zum Projektmanagement)

Berichte des Auftragnehmers im Projektabschlussbericht:
Projektabschlussbericht (von AN)
Berücksichtigung der WiBe im Projektabschlussbericht:
WiBe (Fortschreibung)

Entscheidungsrelevant
bei

Projekt abgeschlossen

C.1.8.5.1 Managementübersicht

Stellt kurz und prägnant die aktuellen Kennzahlen zum Projektfortschritt dar und notwendige Maßnahmen
zur Steuerung des Projektes vor.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

C.1.8.5.2 Ausgangslage und Ziele

99

Zusammenfassend wird die Ausgangssituation und Zielsetzung des Projekts dargestellt.

C.1.8.5.3 Projektergebnisse

Dieses   Thema   enthält   einen   Überblick   über   die   im   Berichtszeitraum   fertig   gestellten   Ergebnisse   und
durchgeführten Arbeiten. Konnten Ergebnisse nicht wie geplant fertig gestellt werden, so ist dies ebenfalls
hier   festzuhalten.   Die   im   Projekthandbuch   festgelegten   KM-Auswertungen   können   hierbei   eine
entsprechende Informationsquelle sein.

C.1.8.5.4 Qualitätsbewertung

Die Qualitätsbewertung beinhaltet eine Zusammenfassung des QS-Bericht

 es   .

C.1.8.5.5 Projektverlauf

Im Rahmen einer chronologischen Beschreibung des Projektverlaufs werden die wesentlichen Ergebnisse
und   Entscheidungen   dargestellt   und   bewertet.   Änderungen   der   Planung   im   Laufe   des   Projekts   sind
darzustellen sowie inhaltlich und ursächlich zu beschreiben. Dabei sind insbesondere die Projekterfahrungen
zu dokumentieren. Ein zusammenfassender Soll-/Ist-Vergleich zeigt quantitativ den Projektverlauf.

C.1.8.6 Projektstatusbericht (von AN)

 es    des Auftragnehmers im Projekt
Der Projektstatusbericht (von AN) ist eine Kopie des Projektstatusbericht
des   Auftraggebers.   Relevante   Informationen   sind   in   den   eigenen  Projektstatusbericht  im   Projekt   des
Auftraggebers zu übernehmen.

Verantwortlich

Projektleiter

Inhaltlich abhängig

Berichte des Auftragnehmers im Projektstatusbericht:
Projektstatusbericht

Entscheidungsrelevant
bei

Projektfortschritt überprüft, Gesamtprojektfortschritt überprüft

Sonstiges

Extern, Keine Produktvorlage

C.1.8.7 Projektabschlussbericht (von AN)

 s    des Auftragnehmers im
Der  Projektabschlussbericht (von AN)  ist eine Kopie des  Projektabschlussbericht
Projekt des Auftraggebers. Relevante Informationen sind in den eigenen Projektabschlussbericht im Projekt
des Auftraggebers zu übernehmen.

Verantwortlich

Projektleiter

Inhaltlich abhängig

Berichte des Auftragnehmers im Projektabschlussbericht:
Projektabschlussbericht

Entscheidungsrelevant
bei

Projekt abgeschlossen

Sonstiges

Extern, Keine Produktvorlage

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland




100

 Referenz Produkte

C.1.9 Systemelemente

C.1.9.1 System

Als System werden das im Rahmen eines Systementwicklungsprojekts zu realisierende Ergebnis sowie jedes
zur   Unterstützung   des   "eigentlichen"   Systems   benötigte   System   (z.B.   Sonderwerkzeuge,   Mess-   und
Prüfgeräte) bezeichnet.

Ein   System   kann   sich   aus   SW-   und  HW-Element
 en     (z.B.   Flugzeug,   Schiff,   Auto,   Computer)
zusammensetzen. Es kann sich aber auch um ein reines SW-System (z.B. Informationssystem), ein reines
HW-System, das sowohl aus elektronischen/elektrischen wie auch aus mechanischen Elementen besteht (z.B.
Gehäuse, Netzteil) oder ein eingebettetes System (z.B. frei programmierbares Gatter Array (FPGA)) handeln.

Je nach Systemtyp setzt sich das System auf der untersten Ebene aus HW-Einheiten und/oder SW-Einheit
 en
zusammen. Eingebettete Systeme umfassen sowohl HW- als auch SW-Einheiten. Die Einheiten werden zu
 en     und schließlich zum  System integriert. Die Systeme werden entsprechend des im Pflichtenheft
Segment
(Gesamtsystementwurf)  beschriebenen   Lieferumfangs   zu   einer  Lieferung  zusammengestellt   und   an   den
Auftraggeber ausgeliefert.

Verantwortlich

Systemintegrator

Aktivität

Besteht aus

Produktumfang

Zum System integrieren

Segment, Externe Einheit, SW-Einheit

Altsystemanalyse, Anwenderaufgabenanalyse, Datenbankentwurf, Erweiterung
der Vorgaben zum Datenschutz, Erweiterung der Vorgaben zum IT-Betrieb,
Erweiterung der Vorgaben zur Informationssicherheit, Implementierungs-,
Integrations- und Prüfkonzept System, Marktsichtung für Fertigprodukte,
Mensch-Maschine-Schnittstelle (Styleguide), Migrationskonzept, Prüfprotokoll
Systemelement, Prüfprozedur Systemelement, Prüfspezifikation Systemelement,
Sicherheitskonzeption, Systemarchitektur, Systemspezifikation

Erzeugt durch

Systementwurf:
Pflichtenheft (Gesamtsystementwurf) (Dekomposition des Gesamtsystems)

Entscheidungsrelevant
bei

System integriert

Sonstiges

Keine Produktvorlage

C.1.9.2 Segment

Ein Segment ist ein wesentlicher Teil eines System
dar. Es ist die Realisierung eines Teils des  System
unterteilt werden. Daneben können Segment
In der Regel besteht ein Segment aus HW-Einheiten und SW-Einheit
Segmente, reine HW-Segmente oder auch rein durch Externe Einheit

 s   und stellt eine Hierarchie-Ebene unterhalb des System
 s
 e
 e    können hierarchisch in weitere  Segment
 e   auch HW- und/oder SW- und/oder Externe Einheit beinhalten.
 en   , prinzipiell sind aber auch reine SW-
 en    gebildete Segment

 e   vorstellbar.

 s  .  Segment

Verantwortlich

Systemintegrator

Aktivität

Teil von

Zum Segment integrieren

System, Segment

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland













C.1 Produkte

Besteht aus

Produktumfang

101

Segment, Externe Einheit, SW-Einheit

Erweiterung der Vorgaben zum Datenschutz, Erweiterung der Vorgaben zum IT-
Betrieb, Erweiterung der Vorgaben zur Informationssicherheit, Prüfprotokoll
Systemelement, Prüfprozedur Systemelement, Prüfspezifikation Systemelement,
Sicherheitskonzeption, Systemspezifikation

Erzeugt durch

Systementwurf:
Systemarchitektur (Dekomposition des Systems)

Entscheidungsrelevant
bei

System integriert

Sonstiges

Keine Produktvorlage

C.1.9.3 Externe Einheit

Unter   dem   Produkt  Externe   Einheit  versteht   man   Systemelemente,   die   nicht   innerhalb   des   Projekts
entwickelt   werden.   Bei   einer   Externen  Einheit   kann  es   sich  um  ein  Fertigprodukt,   eine   Beistellung  des
Auftraggebers,   ein   im   Vorfeld   entwickeltes   System   oder   Segment,   welches   wiederverwendet   wird,   ein
Nachbarsystem oder das Ergebnis eines Unterauftrags handeln. Eine Externe Einheit kann sowohl HW- als
auch SW-Anteile umfassen.

Handelt es sich um ein Systemintegrationsprojekt, wird das System ausschließlich aus Externen Einheiten
integriert. Eine Externe Einheit ist beispielsweise eine Middlewaretechnologie, ein Datenbankserver oder ein
zugekaufter Prozessor.

Verantwortlich

Systemintegrator

Mitwirkend

Aktivität

Teil von

Produktumfang

Vergabestelle

Externe Einheit übernehmen

System, Segment

Erweiterung der Vorgaben zum Datenschutz, Erweiterung der Vorgaben zum IT-
Betrieb, Erweiterung der Vorgaben zur Informationssicherheit, Externe-Einheit-
Spezifikation, Make-or-Buy-Entscheidung, Marktsichtung für Fertigprodukte,
Prüfprotokoll Systemelement, Prüfprozedur Systemelement, Prüfspezifikation
Systemelement, Sicherheitskonzeption

Erzeugt durch

Systementwurf:
Systemarchitektur (Dekomposition des Systems)

Entscheidungsrelevant
bei

System integriert

Sonstiges

Extern, Keine Produktvorlage

C.1.9.4 SW-Einheit

Eine SW-Einheit ist das in der Hierarchie am weitesten oben stehende Systemelement, das ausschließlich aus
Software besteht. SW-Einheiten setzen sich hierarchisch aus SW-Komponente
 n   zusammen. Eine SW-Einheit
ist beispielsweise die Kundenverwaltung eines Informationssystems oder das Steuermodul eines Roboters.
Verantwortlich für die Integration der SW-Komponenten zur SW-Einheit ist der SW-Entwickler.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


102

 Referenz Produkte

Verantwortlich

SW-Entwickler

Aktivität

Teil von

Besteht aus

Produktumfang

Zur SW-Einheit integrieren

System, Segment

SW-Komponente, SW-Modul, Externes SW-Modul

Datenbankentwurf, Erweiterung der Vorgaben zum Datenschutz, Erweiterung der
Vorgaben zum IT-Betrieb, Erweiterung der Vorgaben zur Informationssicherheit,
Implementierungs-, Integrations- und Prüfkonzept SW, Prüfprotokoll
Systemelement, Prüfprozedur Systemelement, Prüfspezifikation Systemelement,
SW-Architektur, SW-Spezifikation, Sicherheitskonzeption

Erzeugt durch

Systementwurf:
Systemarchitektur (Dekomposition des Systems)

Entscheidungsrelevant
bei

Einheit(en) realisiert

Sonstiges

Keine Produktvorlage

C.1.9.5 SW-Komponente

Eine  SW-Komponente  ist Teil einer  SW-Einheit. SW-Komponenten können hierarchisch in weitere  SW-
Komponenten unterteilt werden. Auf unterster Ebene der Komponentenhierarchie stehen SW-Modul
 e  . Eine
SW-Komponente   ist   beispielsweise   die   Privatkundenverwaltung   der   Einheit   Kundenmanagementsystem.
Verantwortlich für die Integration der SW-Modul
 e   zur SW-Komponente sowie für die Integration von SW-
Komponenten zu weiteren SW-Komponenten ist der SW-Entwickler.

Verantwortlich

SW-Entwickler

Aktivität

Teil von

Besteht aus

Produktumfang

Zur SW-Komponente integrieren

SW-Einheit, SW-Komponente

SW-Komponente, SW-Modul, Externes SW-Modul

Erweiterung der Vorgaben zum Datenschutz, Erweiterung der Vorgaben zum IT-
Betrieb, Erweiterung der Vorgaben zur Informationssicherheit, Prüfprotokoll
Systemelement, Prüfprozedur Systemelement, Prüfspezifikation Systemelement,
SW-Spezifikation, Sicherheitskonzeption

Erzeugt durch

Systementwurf:
SW-Architektur (Dekomposition der SW-Einheit)

Entscheidungsrelevant
bei

Einheit(en) realisiert

Sonstiges

Keine Produktvorlage

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland



C.1 Produkte

C.1.9.6 SW-Modul

103

Ein SW-Modul findet sich auf der untersten Hierarchieebene der Systemelemente und wird im Gegensatz zu
 en     durch   ein   nicht   weiter   unterstrukturiertes   Stück   Programmcode   konkret
allen   anderen  SW-Element
realisiert. Ein SW-Modul ist Teil einer SW-Komponente. Es wird nicht weiter untergliedert. Ein SW-Modul
ist beispielsweise die Klasse "Privatkunde" einer Komponente "Kundenverwaltung". Verantwortlich für die
Realisierung eines SW-Moduls ist der SW-Entwickler.

Verantwortlich

SW-Entwickler

Aktivität

Teil von

Produktumfang

SW-Modul realisieren

SW-Einheit, SW-Komponente

Erweiterung der Vorgaben zum Datenschutz, Erweiterung der Vorgaben zum IT-
Betrieb, Erweiterung der Vorgaben zur Informationssicherheit, Prüfprotokoll
Systemelement, Prüfprozedur Systemelement, Prüfspezifikation Systemelement,
SW-Spezifikation, Sicherheitskonzeption

Erzeugt durch

Systementwurf:
SW-Architektur (Dekomposition der SW-Einheit)

Entscheidungsrelevant
bei

Einheit(en) realisiert

Sonstiges

Keine Produktvorlage

C.1.9.7 Externes SW-Modul

 n  ), die
Unter dem Produkt Externes SW-Modul versteht man Systemelemente (SW-Modul
nicht innerhalb des Projekts entwickelt werden. Ein Externes SW-Modul ist ein selbständig beschreibbares
Funktionselement. Dabei kann es sich um ein Fertigprodukt, eine Beistellung des Auftraggebers, eine im
Vorfeld entwickelte Komponente, die wiederverwendet wird, ein Nachbarsystem oder das Ergebnis eines
Unterauftrags handeln.

 e  , SW-Komponente

Verantwortlich

SW-Entwickler

Mitwirkend

Aktivität

Teil von

Produktumfang

Vergabestelle

Externes SW-Modul übernehmen

SW-Einheit, SW-Komponente

Erweiterung der Vorgaben zum Datenschutz, Erweiterung der Vorgaben zum IT-
Betrieb, Erweiterung der Vorgaben zur Informationssicherheit, Externes-SW-
Modul-Spezifikation, Make-or-Buy-Entscheidung, Marktsichtung für
Fertigprodukte, Prüfprotokoll Systemelement, Prüfprozedur Systemelement,
Prüfspezifikation Systemelement, Sicherheitskonzeption

Erzeugt durch

Systementwurf:
SW-Architektur (Dekomposition der SW-Einheit)

Entscheidungsrelevant
bei

Einheit(en) realisiert

Sonstiges

Extern, Keine Produktvorlage

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland




104

 Referenz Produkte

C.1.10 Systemanalyse

C.1.10.1 Lastenheft (Anforderungen)

Das Produkt Lastenheft (Anforderungen) enthält alle an das zu entwickelnde System verbindlich gestellten
Anforderungen, die vom Auftraggeber ermittelt und hier dokumentiert werden. Es ist Grundlage für die
Ausschreibung   und   Vertragsgestaltung   und   damit   wichtigste   Vorgabe   für   die   Angebotserstellung.   Das
Lastenheft ist Bestandteil des Produkts  Vertrag  zwischen Auftraggeber und Auftragnehmer. Mit den Teilen
dieses Produkts, die in den Vergabeunterlagen (Ausschreibung) enthalten sind, erhält der Auftragnehmer alle
notwendigen Informationen zur Entwicklung des geforderten Systems, die er dann im Produkt Pflichtenheft
(Gesamtsystementwurf) detailliert und ausgestaltet.

Kern des Lastenhefts sind die funktionalen und nicht-funktionalen Anforderungen an das zu entwickelnde
System und die ggf. erforderlichen unterstützenden Systeme sowie eine Skizze der Gesamtsystemarchitektur.
Zusätzlich   werden   die   zu   unterstützenden   Phasen   im   Lebenszyklus   des   Systems   identifiziert   und   als
logistische   Anforderungen   aufgenommen.   Ebenfalls   Teil   der   Anforderungen   ist   die   Festlegung   von
Lieferbedingungen und Abnahmekriterien.

Die funktionalen und nicht-funktionalen Anforderungen dienen nicht nur als Vorgaben für die Entwicklung,
sondern sind zusätzlich Grundlage der Anforderungsverfolgung und des Änderungsmanagements.

Die Anforderungen sollten so aufbereitet sein, dass die Verfolgbarkeit (Traceability) sowie ein geeignetes
Änderungsmanagement für den gesamten Lebenszyklus eines Systems möglich sind.

Für   die   Erstellung   des   Lastenhefts   sowie   für   dessen   Qualität   ist   der  Auftraggeber   verantwortlich.   Das
Lastenheft sollte im Allgemeinen keine technischen Lösungen vorgeben, um Architekten und Entwickler bei
der Suche nach optimalen technischen Lösungen nicht einzuschränken.

Verantwortlich

Mitwirkend

Aktivität

Methoden

Werkzeuge

Vorlagen

Anforderungsanalytiker (AG)

Anwender, Projektleiter, Projekteigner, Informationssicherheitsverantwortlicher,
Datenschutzverantwortlicher, Betriebsverantwortlicher, Fachverantwortlicher,
Verfahrensverantwortlicher (Fachseite), Geschäftsprozessmanager

Anforderungen festlegen

Anforderungsanalyse, Geschäftsprozessmodellierung, Modellierung funktionaler
Anforderungen (UML)

Anforderungsmanagement

Lastenheft (Anforderungen)(.odt|.doc), Lastenheft (ITZBund) (Externe
Kopiervorlage)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

Inhaltlich abhängig

105

Anforderungen als Bestandteil der Vergabeunterlagen (Ausschreibung):
Vergabeunterlagen (Ausschreibung)
Berücksichtigung der Informationssicherheit und des Datenschutzes bei der
Anforderungsfestlegung:
Schutzbedarfsfeststellung, Vorgaben zur Informationssicherheit, Vorgaben zum
Datenschutz
Berücksichtigung der WiBe in den Anforderungen:
WiBe (Fortschreibung)
Berücksichtigung des IT-Betriebs bei der Anforderungsfestlegung:
Vorgaben zum IT-Betrieb
Konsistenz von Lasten- und Pflichtenheft (ohne Vertrag):
Pflichtenheft (Gesamtsystementwurf)
Konsistenz von Teilprojekt-Anforderungen zum Lastenheft Gesamtprojekt:
Lastenheft Gesamtprojekt
Projektvorstudie, Projektauftrag und Anforderungen:
Projektvorstudie, Projektauftrag

Entscheidungsrelevant
bei

Anforderungen festgelegt

Sonstiges

Initial

C.1.10.1.1 Ausgangssituation und Zielsetzung

In diesem Thema werden die Ausgangssituation und der Anlass zur Durchführung des Projektes anschaulich
dargestellt.   Es   wird   beschrieben,   welche   Defizite   bzw.   Probleme   existierender   Systeme   oder   auch   der
aktuellen Situation zur Entscheidung geführt haben, das Projekt durchzuführen, und welche Vorteile durch
den Einsatz des neuen Systems erwartet werden.

Es werden zusätzlich alle relevanten Stakeholder des Projektes benannt. Außerdem werden die technische
und fachliche Einbettung des zu entwickelnden Systems in seine Umgebung sowie der organisatorische und
technische Rahmen skizziert.

Ausgangssituation

In diesem Abschnitt wird dargestellt, was der Anlass zur Durchführung des Projektes ist. Dazu gehört die
Darstellung des Problems, welches durch das Projekt beseitigt werden soll. In diesem Zusammenhang soll
auch darauf eingegangen werden, warum das Problem nicht mit bereits existierenden Systemen behoben
werden kann.

Des   Weiteren   wird   die  Auftragsgrundlage   für   das   neu   durchzuführende   Projekt   benannt.   Resultiert   der
Projektauftrag beispielsweise daraus, dass Gesetzesänderungen umzusetzen sind, dann sind diese Gesetze in
diesem Kapitel angeführt.

Zielsetzung

Im Rahmen der Zielsetzung werden die Vorteile aufgezeigt, die durch den Einsatz des neuen Systems zu
erwarten   sind.   Hierbei   wird   der  Systemname  angegeben,   eine   kurze   Beschreibung   des   Systems
vorgenommen sowie die Nutzer des Systems benannt.

Zudem wird in einem kurzen Abriss dargestellt, wie der Soll-Zustand zur Beseitigung des Problems, also das
System, zu gestalten ist.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

106

Abgrenzung des Systems

 Referenz Produkte

Mit   dem   Produkt  Lastenheft   (Anforderungen)  werden   die  Anforderungen   an   das   zu   erstellende   System
erfasst,   um   den   Weg   zur   Systemrealisierung   vorzubereiten.   Bei   der   Erhebung   der  Anforderungen   sind
Fachseite, IT-Seite und eventuell Betrieb beteiligt. Die Anforderungen des Fachbereichs (der Anwender) sind
überwiegend   fachlicher   Natur.  Aus   den   fachlichen   und   technischen  Anforderungen   kann   das   IT-System
abgeleitet werden (siehe auch Skizze des Lebenszyklus und der Gesamtsystemarchitektur).

Dieses   Thema   beschreibt   schwerpunktmäßig   die  Abgrenzung   des   zu   entwickelnden   Systems   zu   seinen
Nachbarsystemen. Dabei sind von der Fachseite insbesondere die bereits etablierten  Geschäftsprozesse  zu
berücksichtigen. Der IT-Betrieb steuert dazu die Informationen zu den bereits betriebenen Systemen bei. Auf
Basis dieser Informationen ist der Bedarf, der durch das neue System gedeckt werden soll, zu bestimmen und
gegenüber   bereits   existierenden   Lösungen   abzugrenzen.   Somit   dokumentiert   dieses   Thema   die
Kernaufgaben, die das neue System erfüllen soll.

Weiterhin ist in diesem Thema zu dokumentieren, in welchen Organisationskontext (z.B. Referat, Behörde)
das neue System eingebettet werden soll.

Betroffene Geschäftsprozesse

Im Thema Abgrenzung des Systems werden bereits die Geschäftsprozesse und Nachbarsysteme benannt. In
diesem   Thema   ist   eine   detaillierte   Analyse   der   identifizierten,   betroffenen   Geschäftsprozesse   zu
dokumentieren. Die Analyse dieser Geschäftsprozesse dient dem Erkennen, welche Prozessschritte durch das
zu   entwickelnde   System   zu   unterstützen   sind.   Dies   ist   eine   wichtige   Quelle   für   die   Ermittlung   der
funktionalen Anforderungen (Thema Funktionale Anforderungen).

Anforderungen werden nicht nur aus Geschäftsprozessen abgeleitet, sondern können auch dazu führen, dass
bereits   etablierte   Geschäftsprozesse   angepasst   werden   müssen.   Daher   sind   in   diesem   Thema   auch   die
Geschäftsprozesse   aufzuführen,   die   Abhängigkeiten   zu   den   (neu)   umzusetzenden   Geschäftsprozessen
aufweisen und daher ggf. angepasst werden müssen.

Somit enthält dieses Thema eine Liste von Geschäftsprozessen, die sich auch in  Abgrenzung des Systems
wiederfinden müssen. Die hier gelisteten betroffenen Geschäftsprozesse stellen eine Teilmenge der gelisteten
Geschäftsprozesse des Themas Abgrenzung des Systems dar.

Stakeholder

Es werden alle Personen und Organisationen benannt, die im Rahmen der Anforderungserhebung zu dem zu
entwickelnden System berücksichtigt werden sollten, weil sie gegebenenfalls einen direkten oder indirekten
Einfluss auf die Anforderungen haben.

Bei   den   Personen   kann   es   sich   um   konkrete   Personen   handeln   oder   auch   um   Rollen,   während   unter
Organisationen im Allgemeinen konkrete Referate oder Abteilungen gesehen werden.

Während   konkrete   namentlich   benannte   Personen   im  Projekthandbuch  erfasst   werden,   werden   hier   die
Funktionen bzw. Rollen sowie die Organisationen, die Stakeholder darstellen, aufgeführt.

Zu typischen Stakeholdern zählen beispielsweise

➢ Fachabteilung,

➢ Anwender des Systems,

➢ IT-Abteilungen,

➢ Architektur,

➢ Betrieb,

➢ Management usw.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

107

Als zusätzliche Information kann an dieser Stelle auch beschrieben werden, welches spezielle Wissen der
Stakeholder zur Thematik hat, in welcher Form der Stakeholder Einfluss auf das neue zu schaffende System
hat und auf welchen Bereich des Systems.

Für die Erfassung empfiehlt sich entweder eine einfache Aufzählungsliste oder für detaillierte Informationen
eine tabellarische Erfassung.

Organisatorischer und technischer Rahmen

Dieses   Thema   dokumentiert   erkennbare   und   vorgegebene   Rahmenbedingungen.   Zu   diesen
Rahmenbedingungen   zählen   beispielsweise   technische   Vorgaben   (z.B.   im   Rahmen   von  SAGA).   Des
Weiteren   können   die   organisatorische   Einbettung   (wie   ordnen   sich   die   betroffenen   Bereiche   in   das
Gesamtorganigramm ein) und speziell vorgegebene IT-Strategien der jeweiligen Behörde eine Rolle spielen.

Aus diesem vorgegebenen organisatorischen und technischen Rahmen lassen sich dann  Randbedingungen
ableiten. Randbedingungen sind nicht-funktionale Anforderungen, die bei der Erstellung des Systems  zu
beachten sind, auf die die Projektbeteiligten jedoch keinen Einfluss haben. Randbedingungen können sich
sowohl   auf   das   zu   realisierende   System   als   auch   auf   den   Entwicklungsprozess   beziehen.   Beispiele   für
Randbedingungen sind dann z.B. Entwicklungsmethoden oder Programmiersprachen, die dem Projekt von
extern vorgegeben werden.

C.1.10.1.2

Funktionale Anforderungen

Funktionale   Anforderungen   sind   die   zentralen   Vorgaben   für   die   Systementwicklung.   Sie   werden   im
Anschluss   durch   den  Auftragnehmer   in   das  Pflichtenheft   (Gesamtsystementwurf)  übernommen   und   bei
Bedarf konkretisiert. Sie beschreiben die Fähigkeiten eines Systems, die ein Anwender erwartet, um mit
Hilfe   des   Systems   ein   Problem   zu   lösen.   Die   Anforderungen   werden   aus   den   zu   unterstützenden
Geschäftsprozessen und den Ablaufbeschreibungen zur Nutzung des Systems abgeleitet.

Für die Beschreibung der funktionalen Anforderungen können verschiedene Darstellungsmittel, wie:

➢ Text (natürliche Sprache)

➢ Anwendungsfälle (Text, Tabelle)

➢ Modelle

verwendet werden. Welche Technik im Detail verwendet wird, ist im Thema Organisation und Vorgaben zum
Anforderungsmanagement im Projekthandbuch festzulegen.

Unabhängig von der gewählten Darstellungsform sind bei der Erfassung der funktionalen Anforderungen
immer die folgenden Aspekte zu berücksichtigen:

➢ Inhalt: Was wird gemacht?

➢ Akteur

 e  : Wer ist involviert/beteiligt?

➢ Daten: Welche Daten werden genutzt, benötigt etc.?

➢ Schnittstellen: Mit welchen (Nachbar-)Systemen interagiert das System? Welche Schnittstellen zu

Anwendern hat das System?

Die   Struktur   und   die   Tiefe   der   Erfassung   der   funktionalen   Anforderungen   ist   ebenfalls   im   Thema
Organisation und Vorgaben zum Anforderungsmanagement im Projekthandbuch festzulegen.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


108

 Referenz Produkte

C.1.10.1.3 Nicht-Funktionale Anforderungen

Im Gegensatz zu den funktionalen Anforderungen (Thema:  Funktionale Anforderungen), die beschreiben,
was  das   System  leisten  soll,   geben  die   nicht-funktionalen Anforderungen  an,  wie   gut  das   System  diese
Funktionen leisten soll. Nicht-funktionale Anforderungen beschreiben also Anforderungen an das System
und an das Projekt, die nicht-fachlicher Natur sind, jedoch entscheidend zur Anwendbarkeit des Systems
beitragen.

Die   in   den  Vorgaben   zur   Informationssicherheit,   zum   Datenschutz   und   zum   IT-Betrieb   enthaltenen
Regelungen beschreiben ebenfalls nicht-funktionale Anforderungen und müssen in diesem Thema aufgeführt
oder   referenziert   werden.   Gleichermaßen   hier   aufgeführt   oder   referenziert   werden   muss   die
Schutzbedarfsfeststellung, die zusammen mit den vorgenannten Vorgaben die Grundlage der zu erstellenden
Sicherheitskonzeption bildet.

Nicht-funktionale Anforderungen entstehen in der Regel parallel zu den funktionalen Anforderungen und
können diesen daher zugeordnet werden. Die nicht-funktionalen Anforderungen können die funktionalen
einschränken und sie konkreter beschreiben.

Nicht-funktionale Anforderungen können unterschiedlichster Art sein. Sie lassen sich generell unterscheiden
in Qualitätsanforderungen (Qualitätskriterien gemäß ISO 9126) und Randbedingungen (Anforderungen, die
nicht   an   das   System   direkt,   jedoch   an   die   Entwicklung   des   Systems   gestellt   werden).   Zur   einfachen
Strukturierung der Anforderungen werden diejenigen Anforderungen, die nicht eindeutig zu den funktionalen
Anforderungen gehören, den nicht-funktionalen Anforderungen zugeordnet.

Die Darstellung und Beschreibung erfolgt bei nicht-funktionalen Anforderungen überwiegend in Textform.
Die nicht-funktionalen Anforderungen sollten dabei messbar, prüfbar und entscheidbar formuliert sein. Für
die Messbarkeit müssen geeignete Metriken definiert werden.

Funktionalität

Nicht-funktionale Anforderungen im Bereich Funktionalität betreffen das Vorhandensein von Funktionen mit
festgelegten Eigenschaften. Beispiele hierfür sind Angaben zu Genauigkeiten von berechneten Werten oder
die Erfüllung von Normen oder gesetzlichen Vorschriften.

Zuverlässigkeit

Nicht-funktionale  Anforderungen   im   Bereich   Zuverlässigkeit   betreffen   die   Fähigkeit   des   Systems,   sein
Leistungsniveau unter festgelegten Bedingungen über einen festgelegten Zeitraum zu bewahren. Beispiele
hierfür sind Angaben zur Verfügbarkeit oder zur Wiederherstellbarkeit nach Ausfällen hinsichtlich Aufwand
und Zeit.

Benutzbarkeit

Nicht-funktionale Anforderungen im Bereich Benutzbarkeit betreffen alle Eigenschaften, die zur Benutzung
erforderlich   sind   bzw.   eine   ordnungsgemäßen   Benutzung   ermöglichen.   Dazu   gehören   Anforderungen
bezüglich Verständlichkeit, Erlernbarkeit und Bedienbarkeit des Systems.

Effizienz

Nicht-funktionale   Anforderungen   im   Bereich   Effizienz   betreffen   Performanceanforderungen   sowie
Anforderungen zum Verbrauchsverhalten beim Betrieb des Systems.

Änderbarkeit

Nicht-funktionale  Anforderungen   im   Bereich   Änderbarkeit   betreffen   den  Aufwand,   der   erforderlich   ist,
Änderungen an der Software vorzunehmen. Anlässe für Änderungen können Korrekturen, Verbesserungen
oder geänderte Anforderungen sein.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

Übertragbarkeit

109

Nicht-funktionale Anforderungen im Bereich Übertragbarkeit betreffen die Eignung des Systems, von einer
Umgebung in eine andere übertragen zu werden. Dabei kann es sich um eine organisatorische Umgebung,
eine andere Hardware- oder Softwareumgebung handeln.

Randbedingungen

Randbedingungen legen Bedingungen und Einschränkungen fest, unter denen das Projekt durchgeführt wird
und die für die Entwicklung des Systems zu beachten sind. Randbedingungen sind häufig eine direkte Folge
des vorgegebenen organisatorischen und technischen Rahmens (dieser ist im Thema  Organisatorischer und
technischer Rahmen vorgegeben). Beispiele für Randbedingungen sind

➢ Richtlinien,

➢ einzuhaltende Standards wie z.B. Referenzarchitekturen,

➢ Entwicklungsmethoden,

➢ technologische Vorgaben wie Hardware- oder Software-Plattformen und

➢ zwingend einzuhaltende Terminvorgaben.

C.1.10.1.4 Skizze des Lebenszyklus und der Gesamtsystemarchitektur

Für die Einordnung, Systematisierung, Kategorisierung und auch Priorisierung von Anforderungen ist ein
Koordinierungsrahmen hilfreich, um die Visualisierung der Anwenderanforderungen zu erleichtern. Diese
Aufgabe   kann   eine  Gesamtsystemarchitektur  leisten,   die   die   Sichtweise   des   Anwenders   und/oder   des
Betriebs repräsentiert. Sie ist ein  nicht verbindlicher  Vorschlag, der organisatorische, fachliche aber auch
technische Sichten darstellen kann.

Die Gesamtsystemarchitektur muss eine Verbindung zu den im Thema Abgrenzung des Systems benannten
Geschäftsprozessen, (Nachbar-)Systemen und im Weiteren zu den Anforderungen herstellen. Dieses dient
Thema dazu,

➢ Fakten   wie   z.B.   verbindlich   einzusetzende,   bereits   etablierte   Systeme   zu   benennen   (etwa   ein

konkretes Datenbankmanagementsystem).

➢ Vorstellungen   zu   artikulieren,   wie   die   Realisierung   und   die   Einbettung   des   zu   entwickelnden

Systems möglich ist (etwa Zugriff über mobile Rechner).

Festlegungen werden an dieser Stelle nur insofern getroffen, als dass sie Fakten betreffen, die die Entwickler
zwingend berücksichtigen müssen. Ansonsten dient dieses Thema dazu, Erwartungen an die Einbettung des
Systems hinsichtlich der fachlichen Funktion und der technischen Einbettung zu formulieren.

Zur   Darstellung   der   fachlichen   Architektur   eignen   sich   einfache   Grafiken.   Auch   eine   modellbasierte
Darstellung, z.B. mittels UML-Komponentendiagrammen, kann erfolgen.

Lebenszyklus

Der   Lebenszyklus   des   zu   entwickelnden   Systems   endet   nicht   mit   der   Erstellung   des   Produkts,   sondern
umfasst   auch   noch   die   Zeit   nach   der   Überführung   in   den   Wirkbetrieb,   in   der   Fehlerbehebungen,
Anpassungen   und   Erweiterungen   der   Funktionalität   vorgenommen   werden.   Der   Lebenszyklus   endet
schließlich mit der Ablösung des Systems durch ein Nachfolgeprodukt. Es wird daher dargelegt,

➢ wie die Weiterentwicklung des Systems nach dem Projekt weitergeht,

➢ wie Nutzung und Betrieb verlaufen,

➢ ob und welche Ausbaustufen des Systems geplant sind,

➢ wann und wie das System stillgelegt werden soll.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

110

 Referenz Produkte

Diese Punkte besitzen einen entscheidenden Einfluss auf die Entwicklung des Systems und insbesondere auf
die Erstellung der Systemarchitektur.

C.1.10.1.5 Anforderungsverfolgung zu den Anforderungen (Lastenheft Gesamtprojekt)

Im   Rahmen   der   Anforderungsverfolgung   zum  Lastenheft   Gesamtprojekt  wird   zusammenfassend   die
Zuordnung der funktionalen und nicht-funktionalen Anforderungen aus dem  Lastenheft Gesamtprojekt  zu
Anforderungen im Lastenheft dargestellt. Die bidirektionale Verfolgbarkeit muss dabei sichergestellt werden.
Die Darstellung kann beispielsweise anhand einer Matrix erfolgen.

C.1.10.1.6

Lieferumfang

Es   werden  alle   Gegenstände   und   Dienstleistungen   aufgelistet,   die   während  des   Projektverlaufs   oder   bei
Abschluss des Projektes vom Auftragnehmer an den Auftraggeber zu liefern sind. Jede Lieferung (von AN)
erfordert eine Abnahmeprüfung. Der Lieferumfang kann je nach Vereinbarung das zu entwickelnde System,
Teile   des   Systems,   ein   unterstützendes   System,   Teile   eines   unterstützenden   Systems,   Dokumente   und
vereinbarte Dienstleistungen enthalten.

C.1.10.1.7 Abnahmekriterien

Abnahmekriterien   legen   fest,   welche   Kriterien   die  Lieferung   (von  AN)  erfüllen   muss,   um   den   an   sie
gestellten Anforderungen zu entsprechen. Sie sollen prüfbar dargestellt werden. Abnahmekriterien beziehen
sich sowohl auf funktionale als auch auf nicht-funktionale Anforderungen.

In der Phase bis zur Auftragsvergabe können die Abnahmekriterien nur in einer allgemeinen Form, z.B. als
K.O.-Kriterien, angegeben werden. Die allgemeinen Abnahmekriterien sollten auch die Forderung nach einer
Erstellung von Abnahmekriterien durch den Auftragnehmer enthalten. Dabei sind der Aufbau und die Anzahl
der Abnahmekriterien durch den Auftraggeber zu skizzieren. Eine Strukturierung der Abnahmekriterien nach
ihren drei wesentlichen Bestandteilen

➢ Ausgangssituation,

➢ Aktion(en) und

➢ erwartetes Ergebnis

ist   anzustreben.   In   jedem   Fall   müssen   die   erwarteten   Ergebnisse   der  Abnahme   pro  Abnahmekriterium
festgelegt werden.

Die Abnahmekriterien sind Grundlage der Abnahmeprüfung und ggf. auch für die Prüfung zur betriebliche
Freigabe  und gehen  als  Anforderungen in  die  Abnahmespezifikation  sowie  ggf.  in  die  Prüfspezifikation
Inbetriebnahme ein.

Erzeugt

C.1.10.1.8 Glossar

Abnahme der Lieferungen:
Abnahmeerklärung
Prüfung der Lieferungen:
Abnahmeprotokoll, Abnahmespezifikation

Das Glossar ist eine Sammlung aller verwendeten Fachbegriffe und dient dazu, allen Projektbeteiligten ein
gemeinsames   Verständnis   zu   ermöglichen.   Damit   können   unterschiedliche   Interpretationen   und
Missverständnisse vermieden werden und das Verständnis der Anforderungen wird erhöht. Das Glossar ist
für alle Projektbeteiligten verbindlich.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

111

Es   empfiehlt   sich,   neben   der   Erläuterung   der   Begriffe   auch   mögliche  Abkürzungen   und   für   eventuelle
Rückfragen auch die Herkunft bzw. die Quelle der Erläuterung anzugeben.

C.1.10.2 Vorgaben zur Informationssicherheit

Das   Produkt  Vorgaben   zur   Informationssicherheit  ist   der   für   das   Projekt   relevante   Auszug   aus   den
allgemeinen Vorgaben der Organisation zur Gewährleistung der Informationssicherheit. Es legt fest, welche
Maßnahmen zur Informationssicherheit stets umgesetzt werden müssen, welche umgesetzt werden sollten
und welche nicht zulässig sind. Die  Vorgaben zur Informationssicherheit  schränken den Lösungsraum im
Projekt auf gewollte Maßnahmen ein und schließen ungewollte Lösungen aus.

Neben einem angemessenen Niveau an Informationssicherheitsmaßnahmen soll auch deren Interoperabilität
mit   anderen   Systemen   der   Organisation   sichergestellt   werden.   Daher   sollten   die  Vorgaben   zur
Informationssicherheit  auf   IT-Spezifikationen   wie   kryptografische   Verfahren,   Datenformate   und
Übertragungsprotokolle   nebst   Parametrisierungen   sowie   deren   Verwendung   in   IT-Systemen   beschränkt
werden.   Vorgaben   zu   Software-Produkten   oder   Bibliotheken   werden   in   den  Vorgaben   zum   IT-Betrieb
festgelegt.

Das   Produkt  Vorgaben   zur   Informationssicherheit  ist   für   alle   Projekte   mit   Anforderungen   an   die
Informationssicherheit zu erstellen.

Verantwortlich

Informationssicherheitsverantwortlicher

Mitwirkend

Aktivität

Vorlagen

Erzeugt durch

Datenschutzverantwortlicher, Informationssicherheitsbeauftragter

Vorgaben zur Informationssicherheit festlegen

Vorgaben zur Informationssicherheit(.odt|.doc)

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zu Informationssicherheit und
Datenschutz)

Inhaltlich abhängig

Berücksichtigung der Informationssicherheit und des Datenschutzes bei der
Anforderungsfestlegung:
Lastenheft (Anforderungen)

Entscheidungsrelevant
bei

Anforderungen festgelegt, Produktvision entworfen

C.1.10.2.1 Verbindlich einzuhaltende Vorgaben

Dieser Abschnitt beschreibt alle Informationssicherheitsmaßnahmen, die das zu entwickelnde System für
allgemeine   oder   bestimmte   Zwecke   umsetzen   muss.   Beispielsweise   kann   vorgegeben   werden,   dass   für
symmetrische Verschlüsselung AES mit  einer Schlüssellänge von mindestens 128 Bit verwendet werden
muss. Solche Vorgaben können auch eine Menge von Optionen festlegen, aus denen eine zu verwenden ist.

C.1.10.2.2 Ausschlüsse

Dieser  Abschnitt   beschreibt   Informationssicherheitsmaßnahmen   und   Parametrisierungen,   die   nicht,   nicht
mehr   oder   nur   eingeschränkt   dem   Stand   der   Technik   entsprechen   oder   aus   sonstigen   Gründen   vom
Auftraggeber verworfen wurden und daher nicht oder nur eingeschränkt verwendet werden dürfen.

Beispiele dafür sind der Ausschluss der gebrochenen kryptografischen Hash-Verfahren MD5 und SHA-1
oder eine Inkompatibilität zu bestehenden Spezifikationen.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

112

C.1.10.2.3 Empfehlungen

 Referenz Produkte

Dieser Abschnitt beschreibt Informationssicherheitsmaßnahmen, die zur Gewährleistung von Schutzzielen
für allgemeine oder bestimmte Zwecke des Systems ergriffen werden sollten. Beispielsweise kann festgelegt
werden,   dass   zur   Gewährleistung   der   Authentizität   einer   Webseite   und   der   Vertraulichkeit   der
Kommunikation mit dieser HTTPS verwendet werden sollte.

C.1.10.3 Vorgaben zum Datenschutz

Das   Produkt  Vorgaben   zum   Datenschutz  ist   der   für   das   Projekt   relevante  Auszug   aus   den   allgemeinen
Vorgaben der Organisation zur Gewährleistung des Datenschutzes.  Es legt  fest,  welche  Maßnahmen zur
Erreichung seiner Schutzziele stets umgesetzt werden müssen, welche umgesetzt werden sollten und welche
nicht   zulässig   sind.   Das   Produkt   umfasst   auch   an   den   Datenschutz   angelehnte,   etwa   durch   die
Personalvertretung der Organisation definierte Regelungen. Die  Vorgaben zum Datenschutz  schränken den
Lösungsraum in Projekten auf gewollte Maßnahmen ein und schließen ungewollte Lösungen aus.

Das Produkt Vorgaben zum Datenschutz ist für alle Projekte zu erstellen, in denen personenbezogene Daten
verarbeitet werden, und ist ein verbindlicher Bestandteil deren Anforderungen.

Verantwortlich

Datenschutzverantwortlicher

Mitwirkend

Aktivität

Vorlagen

Erzeugt durch

Datenschutzbeauftragter

Vorgaben zum Datenschutz festlegen

Vorgaben zum Datenschutz(.odt|.doc)

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zu Informationssicherheit und
Datenschutz)

Inhaltlich abhängig

Berücksichtigung der Informationssicherheit und des Datenschutzes bei der
Anforderungsfestlegung:
Lastenheft (Anforderungen)

Entscheidungsrelevant
bei

C.1.10.3.1 Vorgehen

Anforderungen festgelegt, Produktvision entworfen

Hier   werden   das   Vorgehen   zur   Gewährleistung   des   Datenschutzes   und   das   Zusammenwirken   der
nachfolgenden Aspekte   im  Überblick   dargestellt.   Dies   betrifft   auch   die   in   der   Organisation  angewandte
Methodik zur Festlegung der nachstehenden Vorgaben und Ausschlüsse.

C.1.10.3.2 Kategorisierung

Dieser Abschnitt definiert die Kategorien von Daten nach ihrem Schutzbedarf. Zu jeder Kategorie werden
die Kriterien zur Einordnung von Daten beschrieben.

Beispielsweise können die Schutzbedarfsabstufungen des Standard-Datenschutzmodells verwendet werden,
die wie in den BSI-Standards in "normal", "hoch" und "sehr hoch" unterteilt sind.

C.1.10.3.3 Verbindlich einzuhaltende Vorgaben

Dieser  Abschnitt beschreibt  alle technischen und organisatorischen Maßnahmen (TOMs), die im Projekt
umgesetzt werden müssen. Beispiele dafür sind:

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

113

➢ Alle zu verarbeitenden personenbezogenen Daten sind nach ihrem Schutzbedarf zu kategorisieren.
Die   Kategorisierung   ist   nachvollziehbar   und   zusammen   mit   Erhebungszweck,   Rechtsgrundlage,
erlaubter Verwendung und Speicherdauer zu dokumentieren.

➢ Personenbezogene Daten müssen bei der Übertragung verschlüsselt werden.

➢ Bei der Verschlüsselung von Daten der Kategorie "sehr hoch" müssen kryptografische Verfahren der
 Vorgaben   zur

  Details   sind   in   den

höchsten   Sicherheitsstufe   verwendet   werden.
Informationssicherheit geregelt.

➢ Die  Authentifizierung   von  Administrator-Konten   muss   per   Smartcard   erfolgen.   Für   alle   übrigen

Benutzerkonten ist ein softwarebasiertes Zertifikat zu verwenden.

➢ Jede   Modifikation   von   Daten   der   Kategorien   "hoch"   und   "sehr   hoch"   ist   mit   Angabe   des
Zeitstempels, der Kennung des Ändernden und dem bisherigen Wert des Datums zu protokollieren.

C.1.10.3.4 Ausschlüsse

Dieser  Abschnitt beschreibt  alle technischen und organisatorischen Maßnahmen (TOMs), die im Projekt
nicht oder nur eingeschränkt umgesetzt werden dürfen. Beispiele dafür sind:

➢ Es dürfen keine Daten vom System ausgewertet werden, die eine unmittelbare Leistungskontrolle bei

der Nutzung des Systems durch einzelne Personen erlauben.

➢ Biometrische   Daten   zur   eindeutigen   Identifizierung   einer   natürlichen   Person   dürfen   nur   mit
entsprechender   Rechtsgrundlage   oder   ausdrücklicher   Einwilligung   der   Betroffenen   verarbeitet
werden.

➢ Andere   als   die   zuvor   genannten   biometrischen   Daten   aus   den   besonderen   Kategorien

personenbezogener Daten nach Art.9 (1) DSGVO dürfen nicht verarbeitet werden.

➢ Webserver dürfen keine IP-Adressen der Client-Rechner protokollieren.

C.1.10.3.5 Empfehlungen

Dieser Abschnitt beschreibt geeignete technische und organisatorische Maßnahmen (TOMs), die im Projekt
umgesetzt werden sollten.

C.1.10.4 Checkliste für das Interview zur Schutzbedarfsfeststellung

Der   Schutzbedarf   des   zu entwickelnden Systems  ist   vom Fachverantwortlichen  in Abstimmung  mit  den
Fachexperten   der   betroffenen   Bereiche   festzulegen.   Hierfür   empfiehlt   sich   die   Durchführung   eines
gemeinsamen   Workshops   mit   allen   Beteiligten.
 Checkliste   für   das   Interview   zur
Schutzbedarfsfeststellung dient als Hilfsmittel für die Vorbereitung und Durchführung dieses Workshops. Sie
enthält eine schrittweise Anleitung mit Empfehlungen und Hinweisen.

  Die

Verantwortlich

Fachverantwortlicher

Vorlagen

Sonstiges

Checkliste für das Interview zur Schutzbedarfsfeststellung (Externe
Kopiervorlage)

Extern, Keine Produktvorlage

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

114

 Referenz Produkte

C.1.10.5 Schutzbedarfsfeststellung

Die Schutzbedarfsfeststellung leitet für die vom System verarbeiteten Daten und deren Datenflüsse an Hand
von Schadensszenarien ein Maß für den Aufwand ab, der zur Absicherung des Systems betrieben werden
muss.   Der   Schutzbedarf   eines   Systems   hat   wesentlichen   Einfluss   auf   die   Höhe   von   IT-Konzeptions-,
Anschaffungs- und Betriebskosten.

Verantwortlich

Fachverantwortlicher

Mitwirkend

Aktivität

Vorlagen

Inhaltlich abhängig

Informationssicherheitsverantwortlicher, Datenschutzverantwortlicher

Schutzbedarf feststellen

Schutzbedarfsfeststellung(.odt|.doc)

Berücksichtigung der Informationssicherheit und des Datenschutzes bei der
Anforderungsfestlegung:
Lastenheft (Anforderungen)

Entscheidungsrelevant
bei

Anforderungen festgelegt, Produktvision entworfen

Sonstiges

Initial

C.1.10.5.1 Schutzbedarfskategorien

In diesem Thema müssen die zur Bewertung des Schutzbedarfs anzuwendenden Kategorien festgelegt und
beschrieben   werden.   Im   Regelfall   wird   hier   auf   die   organisationsweite   Festlegung   der
Schutzbedarfskategorien verwiesen.

Der IT-Grundschutz definiert drei Kategorien, anhand derer der Schutzbedarf qualitativ bewertet werden
kann. Es wird empfohlen, diese Kategorien als Grundlage der Schutzbedarfsfeststellung heranzuziehen. So
ist in den Sicherheitskonzeption
 en    eine eindeutige Auswahl und Zuordnung der umzusetzenden Maßnahmen
anhand der Schutzbedarfskategorien möglich.

➢ normal: Die Schadensauswirkungen sind begrenzt und überschaubar.

➢ hoch: Die Schadensauswirkungen können beträchtlich sein.

➢ sehr hoch: Die Schadensauswirkungen können ein existentiell bedrohliches, katastrophales Ausmaß

erreichen.

C.1.10.5.2 Schadensszenarien

In diesem Thema werden die  Schutzbedarfskategorien  anhand von Schadensszenarien konkretisiert und an
die Gegebenheiten des Bedarfsträgers angepasst. Ziel ist es, die Kategorien quantifizierbar zu machen, um
auf dieser Grundlage den Schutzbedarf des Systems möglichst objektiv bewerten zu können.

Hierzu definiert der IT-Grundschutz folgende Schadensszenarien, anhand derer der Schutzbedarf hinsichtlich
Vertraulichkeit, Integrität und Verfügbarkeit bewertet werden kann:

➢ Verstöße gegen Gesetze, Vorschriften oder Verträge

➢ Beeinträchtigungen des informationellen Selbstbestimmungsrechts

➢ Beeinträchtigungen der persönlichen Unversehrtheit

➢ Beeinträchtigungen der Aufgabenerfüllung

➢ Negative Innen- oder Außenwirkung

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


C.1 Produkte

➢ Finanzielle Auswirkungen

115

Für   jedes   Schadensszenario   muss   definiert   werden,   unter   welchen   Bedingungen   es   welcher
Schutzbedarfskategorie   zugeordnet   ist.   Dabei   sind   alle   Kombinationen   aus   Schadensszenario   und
Schutzbedarfskategorie zu berücksichtigen.

C.1.10.5.3 Schutzbedarfsmatrix

Ausgehend   von   den  Schadensszenarien  kann   der   Schutzbedarf   des   Systems   mit   Hilfe   einer
Schutzbedarfsmatrix   ermittelt   werden.   Hierbei   empfiehlt   es   sich,   eine   Schutzbedarfsmatrix   für   die   vom
System verarbeiteten Daten und eine oder mehrere weitere für Datenflüsse zu erstellen.

Als Grundlage dient das fachliche Datenmodell des Systems, welches im Lastenheft (Thema   Funktionale
Anforderungen) beschrieben ist. Abhängig vom Datenmodell kann es sinnvoll sein, eine Unterscheidung der
Daten   in   (fachliche)   Datengruppen   vorzunehmen   und   diese   jeweils   in   einer   eigenständigen
Schutzbedarfsmatrix   zu   behandeln.  Als   Datengruppe   kann   eine   Entität   oder   die   Kombination   mehrerer
Entitäten   des   Modells   herangezogen   werden.   Für   eine   weiterführende   Unterscheidung   der   Datenflüsse
können   ebenfalls   fachliche   Aspekte   oder   die   Schnittstellen   (innerhalb   des   Systems   und   mit
Nachbarsystemen) als Basis dienen.

Für   "normalen"   Schutzbedarf   sind   die   Sicherheitsanforderungen   des   IT-Grundschutz-Kompendiums
umzusetzen.   Diese   bieten   bereits   ein   solides   Fundament   und   damit   ein   gutes   Niveau   der
Informationssicherheit und erläutern an vielen Stellen, wie ein höheres Sicherheitslevel erreichbar ist. Für
"hohen" und "sehr hohen" Schutzbedarf sind Mehraufwände durch die Umsetzung zusätzlicher Maßnahmen
sowie eine vertiefende sicherheitstechnische Betrachtung in Form von Risikoanalysen notwendig.

C.1.10.5.4 Gesamtbewertung

Hier   werden   die   Schutzbedarfsmatritzen   für   die   verarbeiteten   Daten   und   Datenflüsse   zusammenfassend
betrachtet. Für jedes Sicherheitsziel sollte eine konsolidierte Bewertung dokumentiert werden.

C.1.10.6 Anforderungsbewertung

Ziel der Anforderungsbewertung ist es, Erfassung und Erstellung der Anwenderanforderungen zu bewerten
und das mögliche Realisierungsrisiko des Auftraggebers so weit als möglich transparent und beherrschbar zu
gestalten. Somit hat der Auftraggeber bei Auftragsvergabe auf der Basis seiner Bewertungsmöglichkeiten
bereits   überprüft,   ob   die   Anwenderanforderungen   aus   seiner   Sicht   technisch   machbar,   finanzierbar,
wirtschaftlich und wichtig sind.

Bei   wirtschaftlich   fraglichen   Anforderungen   beziehungsweise   bei   kostenseitig   nicht   ausreichend
abschätzbaren Anforderungen kann der Auftraggeber hilfsweise auf eine Optionierung der Leistungen, das
heißt Einholung von optional anzubietenden Leistungen beziehungsweise Leistungspaketen, zurückgreifen,
um auf Basis tatsächlicher Kostenangaben eine Bewertung durchzuführen.

Das   Produkt  Anforderungsbewertung  dokumentiert   die   Bewertungsergebnisse  für   die   bis   dahin  erfassten
Anwenderanforderungen. Dabei ist die Anforderungsbewertung kaum durchführbar, wenn nicht bereits eine
Skizze des Lebenszyklus und der Gesamtsystemarchitektur oder eine konkrete Systemarchitektur vorliegen,
also bereits Lösungsansätze vorhanden sind. Hierzu kann eine  Evaluierung von Fertigprodukten  wertvolle
Beiträge leisten.

  Die
Die   Anforderungsbewertung   baut
Bewertungsergebnisse   der   Anforderungsbewertung   werden   in   das   Produkt  Lastenheft   (Anforderungen)
eingearbeitet.

  auf   vorher   festgelegten   Bewertungskriterien   auf.

Verantwortlich

Anforderungsanalytiker (AG)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

116

Mitwirkend

Aktivität

Methoden

Vorlagen

 Referenz Produkte

Anwender, Projektleiter, Projekteigner, Ausschreibungs- und
Vertragsverantwortlicher, Fachverantwortlicher, Verfahrensverantwortlicher
(Fachseite)

Anforderungsbewertung erstellen

Bewertungsverfahren, Vom Lastenheft zum Kriterienkatalog

Anforderungsbewertung(.odt|.doc)

Entscheidungsrelevant
bei

Anforderungen festgelegt

Sonstiges

Initial

C.1.10.6.1 Bewertungskriterien

In diesem Thema werden die Bewertungskriterien festgelegt, die bei der Anforderungsbewertung bzw. der
Bewertung des Produkts Lastenheft Gesamtprojekt zu berücksichtigen sind. Die Bewertungskriterien sollten
folgende Aspekte abdecken:

➢ die Plausibilität der definierten Anforderungen,

➢ die Beherrschbarkeit der Komplexität,

➢ die Prüfung der Möglichkeiten zum Einsatz von Fertigprodukten,

➢ die   Übereinstimmung   der

 Schutzbedarfsfeststellung  mit   den   Anforderungen   an   die

Informationssicherheit und den Datenschutz,

➢ die Auswirkungen auf die vorhandene IT-Infrastruktur,

➢ die Kostenschätzungen für einzelne Anforderungen,

➢ die Übereinstimmung mit gesetzlichen Verpflichtungen sowie

➢ die   Übereinstimmung   mit   Anforderungen   an   die   Regeltreue   (Compliance),   soweit   diese   über

gesetzliche Verpflichtungen hinausgehen.

Für   eine   Bewertung   der   wirtschaftlichen   Umsetzbarkeit   der   Anforderungen   sollte   eine
Wirtschaftlichkeitsbetrachtung des zu entwickelnden Systems durchgeführt werden, die unter anderem zu
beachtende laufende Kosten aufführen und Grenzwerte für Kosten von Maßnahmen festlegen sollte.

C.1.10.6.2 Bewertungsergebnisse

Zu   den   Ergebnissen   der  Anforderungsbewertung  gehört   insbesondere   eine   Gesamtbewertung   der
Anwenderanforderungen.   Sie   bewertet,   inwieweit   vorgegebene   Restriktionen,   die   entweder   vom
Haushalt/Budget, von Terminplänen oder von verfügbaren Ressourcen gesetzt werden, eingehalten werden
können beziehungsweise überschritten werden. Des Weiteren werden alle erfassten Anwenderanforderungen
geprüft und ihre Einstufung bewertet:

➢ Es werden die zurückgestellten Anwenderanforderungen und die Begründung der Zurückstellung

geprüft (zum Beispiel ist die Notwendigkeit nicht nachweisbar).

➢ Es werden die modifizierten Anwenderanforderungen und die Begründung der Modifikation geprüft

(zum Beispiel durch den wirtschaftlicheren Einsatz von Fertigprodukten).

➢ Es werden neu hinzugekommene Anwenderanforderungen hinsichtlich ihrer Notwenigkeit geprüft

(zum Beispiel sind wichtige nicht-funktionale Anwenderanforderungen nicht erfasst worden).

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

117

Zu den Bewertungsergebnissen gehören zusätzlich die Ergebnisse der Betrachtung der Wirtschaftlichkeit der
Anwenderanforderungen,   beispielsweise   Kosten-Nutzen-Abwägungen,   Aufzeigen   von   kostentreibenden
Anwenderanforderungen sowie die Finanzierbarkeit der Anwenderanforderungen.

C.1.10.7 Marktsichtung für Fertigprodukte

Soll im zu erstellenden System ein  Segment, eine SW-Einheit, ein SW-Modul oder eine SW-Komponente
durch ein Fertigprodukt realisiert werden, muss anhand der zu diesem Zeitpunkt zur Verfügung stehenden
Spezifikationen  ein geeignetes  Fertigprodukt  gefunden  werden.  Um einen Überblick über  die  am  Markt
verfügbaren   Fertigproduktkandidaten   zu   bekommen,   wird   eine   Marktsichtung   erstellt.   Ergebnis   der
Marktsichtung   ist   eine   Kandidatenliste   möglicher   Fertigprodukte.   Zu   jedem   Kandidaten   werden
Zusatzinformationen wie Produktblätter, Produktspezifikationen, Leistungsmerkmale und Preise erfasst.

Die   Marktsichtung   kann   sowohl   auf  Auftraggeber-   wie   auch   auf  Auftragnehmerseite   zu   verschiedenen
Zeitpunkten im Projektverlauf vorgenommen werden.

Wenn   schon  aus   dem  Projektauftrag  ersichtlich   oder   sogar   vorgeschrieben   wird,   dass   nach   Möglichkeit
Fertigprodukte   einzusetzen   sind,   kann   der   Auftraggeber   noch   vor   der   formalen   Festschreibung   des
Lastenhefts   eine   erste   grobe   Marktsichtung   auf   Basis   des  Projektauftrag  durchführen.   Die   bewerteten
Ergebnisse fliessen dann in das Lastenheft (Anforderungen) ein.

Die   Marktsichtung   kann   auch   (ggfs.   erneut)   zu   einem   späteren   Zeitpunkt   auf   Basis   des   Lastenhefts
durchgeführt werden, um zu untersuchen, ob und in welchem Umfang Entwicklungen notwendig sind oder
ob   ganz   oder   teilweise   das   System   durch   Fertigprodukte   realisiert   werden   kann.   Die   Ergebnisse   der
Marktsichtung sind wichtige Eingabewerte für die Anforderungsbewertung und liefern damit die Grundlage
für eine Entscheidung über den Einsatz von Fertigprodukten.

Der  Auftragnehmer   erstellt   zu   einem   frühen   Zeitpunkt   im  Systementwicklungsprozess   das  Pflichtenheft
(Gesamtsystementwurf). Dieses kann den Anstoß für eine gezielte Marktsichtung geeigneter Fertigprodukte
geben.   Sind   bereits  Externe   Einheit  in   der   Systemarchitektur   identifiziert,   liefert   die  Externe-Einheit-
Spezifikation  die   notwendigen   Informationen.   Werden   externe   Elemente   auf   SW-Ebene   in   Gestalt   von
Produkten des Typs Externes SW-Modul identifiziert, so sind diese in der Externes-SW-Modul-Spezifikation
definiert. Bei der Suche und Bewertung von Fertigprodukten orientiert man sich damit am  Pflichtenheft
(Gesamtsystementwurf), der Externe-Einheit-Spezifikation oder der Externes-SW-Modul-Spezifikation. Die
Marktsichtung ist Grundlage und Entscheidungshilfe für eine  Make-or-Buy-Entscheidung. Die Ergebnisse
der Marktsichtung fließen direkt in die Entscheidungsbewertung ein.

Verantwortlich

Projektleiter

Mitwirkend

Aktivität

Methoden

Vorlagen

Erzeugt durch

Anforderungsanalytiker (AG), Vergabestelle, Systemarchitekt, Systemintegrator

Marktsichtung für Fertigprodukte durchführen

Bewertungsverfahren

Marktsichtung für Fertigprodukte(.odt|.doc)

Systementwurf:
SW-Architektur (Dekomposition der SW-Einheit), Systemarchitektur
(Dekomposition des Systems)

Inhaltlich abhängig

Berücksichtigung der Marktsichtung:
Make-or-Buy-Entscheidung

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

118

 Referenz Produkte

C.1.10.8 Make-or-Buy-Entscheidung

In   einer  Make-or-Buy-Entscheidung  wird   der   Weg   hin   zur   Entscheidung,   ob   eine  Externe   Einheit,   ein
Externes HW-Modul  oder ein  Externes SW-Modul  als Fertigprodukt zugekauft, selbst entwickelt oder als
Unterauftrag vergeben wird, dokumentiert. Abhängig von den strategischen Vorgaben kann eine vorrangige
Untersuchung durchzuführen sein, ob die Wiederverwendung einer Komponente aus Eigenentwicklung oder
die Verwendung einer Open-Source-Komponente möglich ist.

Strategische und wirtschaftliche Aspekte werden untersucht. Eventuell wird eine Evaluierung potentieller
Fertigprodukte   durchgeführt.   Die   Ergebnisse   der  Analysen   und   der   Evaluierung   stützen   die   endgültige
Entscheidung. Das Ergebnis der Entscheidung wird in der Systemarchitektur dokumentiert.

Verantwortlich

Projektleiter

Mitwirkend

Aktivität

Methoden

Vorlagen

Erzeugt durch

Inhaltlich abhängig

Vergabestelle, Projekteigner, SW-Architekt, Systemarchitekt, Systemintegrator

Make-or-Buy-Entscheidung durchführen

Bewertungsverfahren

Make-or-Buy-Entscheidung(.odt|.doc)

Systementwurf:
SW-Architektur (Dekomposition der SW-Einheit), Systemarchitektur
(Dekomposition des Systems)

Berücksichtigung der Marktsichtung:
Marktsichtung für Fertigprodukte
Einfluss eines Fertigprodukts auf die Spezifikation externer Systemelemente:
Externe-Einheit-Spezifikation, Externes-SW-Modul-Spezifikation
Vorgaben im Gesamtsystementwurf bezüglich Fertigprodukten:
Pflichtenheft (Gesamtsystementwurf)

C.1.10.8.1 Strategische Analyse

Der Auftragnehmer hat im Rahmen der strategischen Ausrichtung seiner Organisation zu untersuchen, ob die
möglichen   Vorteile   des   Einsatzes   von   Fertigprodukten,   der   Wiederverwendung   von   Komponenten   aus
eigener Entwicklung, der Verwendung von Open Source-Komponenten oder einer Auftragsvergabe für sein
Projekt genutzt werden können. Dabei hat er insbesondere abzuwägen, ob die Verfügbarkeit und die Reife
der vorgefertigten Komponenten für die von ihm benötigten Funktionalitäten ausreichend und geeignet sind.

Für   alle   Arten   der   Beschaffung   ist   zu   prüfen,   ob   eine   spürbare   Kostenersparnis   gegenüber   einer
Eigenentwicklung sowohl in der Beschaffungs- als auch in der Nutzungs- und Wartungsphase erkennbar und
eine signifikante Verkürzung der Lieferzeiten zwischen Anforderungsfestlegung und Implementierung zu
erwarten ist.

Bei   Open   Source-Komponenten   ist   außerdem   zu   beachten,   dass   die   verschiedenen   Open   Source-
Communities Regeln für die Benutzung der Open Source-Komponenten haben.

Die   strategische  Analyse   hat   dabei   gegebenenfalls   unternehmensweite  Vorgaben   zu   beachten.   Relevante
Vorgaben können beispielsweise sein:

➢ Es   dürfen   keine  Aufträge   vergeben   werden,   bei   denen   Kernkompetenzen   preisgegeben   werden

müssen.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

119

➢ Der   Einsatz   von   konkreten   Fertigprodukten   ist   vorgeschrieben.   Eigenentwicklungen   müssen
besonders begründet werden. Gründe können höhere wirtschaftliche oder technische Risiken beim
Einsatz von Fertigprodukten sein.

➢ Der Einsatz von Fertigprodukten ist freigestellt. Es ist die wirtschaftlichste Lösung anzustreben.

➢ Es   müssen   eigene   Komponenten   wiederverwendet   werden,   z.B.   im   Zusammenhang   mit

Produktlinienengineering.

C.1.10.8.2 Wirtschaftliche Analyse

Die Wirtschaftlichkeit der Verwendung von Produkten vom Typ Externe Einheit, Externes HW-Modul oder
Externes SW-Modul ist möglichst durch eine Kosten-Nutzen-Analyse in quantitativer Form (Geldeinheiten)
nachzuweisen. Dies ist unabhängig davon, ob es sich um die Verwendung eines vorgefertigten Produkte oder
um das Ergebnis eines Entwicklungsauftrags handelt. Bei einem Nutzenüberhang über die Kosten ist die
Verwendung eines Externen Systemelements eindeutig als wirtschaftlich einzustufen. Eventuell kann auch
durch Reduzierung der Anforderungen an ein externes Systemelement eine zusätzliche Kosteneinsparung
erreicht werden (z.B. können bei 20% der Kosten 80% der Anforderungen erfüllt sein).

Der messbare Nutzen eines vorgefertigten Produktes kann beispielsweise in seiner sofortigen Verfügbarkeit
liegen. Zusätzlich ist ein geringerer Aufwand für Prüfung und Integration zu erwarten, da die Produkte in der
Regel am Markt oder bereits im eigenen Haus erprobt wurden.

Wie die Kostenvorteile sind jedoch auch die Kostennachteile zu berücksichtigen. Beispielsweise können
Kostenvorteile vollständig aufgezehrt werden, wenn bei Fertigprodukten oder Open Source-Komponenten
aufwändige  Anpassungen   notwendig   werden   oder   Implementierungsfehler,   Schnittstelleninkompatibilität
oder Plattforminkompatibilität zu bereinigen sind.

Sollte   der   Nutzen   sich   nicht   in   Geldeinheiten   ausdrücken   lassen,   so   können   qualitative   Nutzenaspekte
hinzugezogen  werden  (dazu  kann  im  öffentlichen  Bereich  die   IT-WiBe   verwendet   werden).   Qualitativer
Nutzen entsteht beispielsweise beim Einsatz von Standardkomponenten durch eine höhere Flexibilität und
leichtere Erweiterbarkeit. Bei Produkten, die bereits im Markt oder im Haus erprobt wurden, kann von einer
geringeren   Ausfallwahrscheinlichkeit   und   damit   einer   höheren   Verfügbarkeit   des   neuen   Produktes
ausgegangen werden.

Kommt der Einsatz von Fertigprodukten, einer Open Source-Komponente oder einer wiederverwendbaren
Komponente nicht in Frage, muss zwischen der Fremd- oder Eigenentwicklung entschieden werden. Dabei
spielen Aspekte wie ‚Time to Market’, eigene Ressourcenverfügbarkeit und der Kostenfaktor eine Rolle.

C.1.10.8.3 Evaluierung der Fertigprodukte

Das Thema  Evaluierung der Fertigprodukte  dokumentiert die Evaluierung möglicher Kandidaten für eine
Externe   Einheit,   ein  Externes   HW-Modul  oder   ein  Externes   SW-Modul.   Damit   wird   die   Grundlage   zur
Entscheidung für oder gegen ein Fertigprodukt im Allgemeinen oder auch für oder gegen ein bestimmtes
Fertigprodukt gelegt. Kommen aus strategischen Überlegungen auch Open Source-Komponenten in Frage,
werden diese ebenfalls betrachtet.

Anhand   der   Schnittstellen   und   nicht-funktionalen  Anforderungen   der  Externe-Einheit-Spezifikation,   der
Externes-HW-Modul-Spezifikation  oder   der  Externes-SW-Modul-Spezifikation  wird   eine   Kriterienliste
aufgestellt. Sie dient dazu, die Eignung der Kandidaten zu überprüfen. Entscheidungen fallen oft aufgrund
der Nichterfüllung von K.o.-Kriterien in Randbereichen, die anfangs nicht immer gegenwärtig sind. Aus
diesem Grund ist eine Bewertung der Erfüllungsgrade der konkreten und gewichteten Anforderungen, das
heißt eine klassische Nutzwertanalyse mit K.o.-Kriterien erforderlich. Eine Bewertung von Fertigprodukten
z.B.   anhand   starrer   Funktionskataloge   ist   sinnlos   und   führt   zu   falschen   Ergebnissen.   Die   einzelnen
Fertigprodukte werden anhand der Kriterienliste bewertet.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

120

 Referenz Produkte

Zu beachten ist, dass Fertigprodukte oft nicht die besonderen (z.B. militärischen) Anforderungen, die aus
Umwelteinflüssen   und   speziellen   Einsatzbedingungen   herrühren,   erfüllen.   Daher   werden   Anpassungen
(Härtung   beziehungsweise   Wrapping-Technologien)   der   Fertigprodukte   an   die   vorgegebenen
Einsatzbedingungen notwendig, das heißt bei der Verwendung von Fertigprodukten muss der Aufwand für
eventuell   neu   zu   entwickelnde   Anpassungs-SW   beziehungsweise   -HW   hinsichtlich   Kosten   und
Integrationsrisiko betrachtet werden. Ergebnis der Evaluierung ist eine Liste mit priorisierten Kandidaten.

C.1.10.8.4 Bewertung und Ergebnis

Wurden   die   verschiedenen  Analysen   und   gegebenenfalls   eine   Fertigproduktevaluierung   durchgeführt,   ist
anhand der Ergebnisse die Entscheidung zur Eigenentwicklung, zum Kauf, zur Wiederverwendung oder zur
Fremdvergabe zu treffen.

In   die   Entscheidung   fließen   zusätzliche   Bewertungskriterien   für   mögliche   Fertigproduktlieferanten   bzw.
Unterauftragnehmer  mit   ein,   wie   beispielsweise   Bonitätskriterien,   Leistungskriterien   und   vertragliche
Kriterien.   Ebenso   relevant   für   eine   Make-or-Buy-entscheidung   sind   Kriterien   wie   Marktstellung   eines
Unternehmens,   Erfahrungen   auf   dem   Fachgebiet,   Beteiligungen   an   Standardisierungen,   Vertragspolitik,
Preispolitik und verfügbare Wartungs-, Support- und Schulungsangebote.

Wurde eine Evaluierung von Fertigprodukten durchgeführt, ist die priorisierte Kandidatenliste ebenfalls als
Entscheidungsgrundlage   hinzuzuziehen.   Des   Weiteren   sind   mögliche   Risiken   zu   bewerten,   wie
beispielsweise   Integrationsrisiken,   Beherrschbarkeit   neuer   Technologien   oder   Anpassungsfähigkeit   und
Modularität des Fertigprodukts.

Anhand   der   oben   genannten   Kriterien   und   untersuchten   Risiken   wird   eine   Rangfolge   der  Alternativen
aufgestellt, die Entscheidung durchgeführt und das Ergebnis dokumentiert.

Sofern   das   betrachtete   Systemelement   im   Rahmen   einer   Fremdvergabe   erstellt   werden   soll,   muss
dokumentiert werden, wie sich der dazugehörige Vergabeprozess gestaltet.

Erzeugt

Aufforderung zur Abgabe eines Angebots (Unterauftrag):
Angebotsaufforderung
Dokumentation des Vergabeverfahrens (Unterauftrag):
Verfahrensdokumentation, Vergabevermerk
Erteilung des Auftrags (Unterauftrag):
Auftrag
Veröffentlichung der Ausschreibung (Unterauftrag):
Beschaffungskonzeption, Eignungsbewertungsmatrix, Kriterienkatalog,
Leistungsbewertungsmatrix, Vergabeunterlagen (Ausschreibung)
Zuschlagserteilung auf ein Angebot (Unterauftrag):
Vertrag, Vertragsübersicht

C.1.10.9 Anwenderaufgabenanalyse

Ziel der  Anwenderaufgabenanalyse  ist es, die Grundlagen für die Gestaltung eines aufgabenangemessenen
Systems   zu   erarbeiten.   Dazu   müssen   die   zu   unterstützenden   Aufgaben   der   Anwender   in   ihrem
Zusammenwirken mit der Arbeitsumgebung dargestellt werden.

Im Rahmen der Anwenderaufgabeanalyse werden Anwenderprofile, die zu unterstützenden Aufgaben sowie
System- und Umgebungsbedingungen identifiziert und beschrieben.

Verantwortlich

Mitwirkend

Ergonomieverantwortlicher

Anwender, Anforderungsanalytiker (AN), Technischer Autor

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

Aktivität

Vorlagen

Erzeugt durch

121

Anwenderaufgaben analysieren

Anwenderaufgabenanalyse(.odt|.doc)

Systementwurf:
Pflichtenheft (Gesamtsystementwurf) (Nicht-funktionale Anforderungen)

Inhaltlich abhängig

Konsistenz von Anwenderaufgabenanalyse und Gesamtsystementwurf:
Pflichtenheft (Gesamtsystementwurf)

C.1.10.9.1 Anwenderprofile

Das   Anwenderprofil   beschreibt   Eigenschaften   und   Vorkenntnisse   der   zukünftigen   Anwender   des   zu
entwickelnden   Systems.   Zur   Erstellung   eines   Anwenderprofils   werden   persönliche   Eigenschaften   der
Anwender   wie   Alter   oder   Geschlecht   sowie   berufliche   Eigenschaften   der   Anwender   wie   Erfahrung,
Benutzungshäufigkeit und Intensität berücksichtigt.

C.1.10.9.2 Physische Benutzungsumgebung

Die  Arbeitsumgebung   des   am   Dialogsystem   arbeitenden   Benutzers   wird   erfasst   und   dokumentiert.   Die
Ergebnisse beeinflussen die Gestaltung des Dialogsystems. Entscheidende Faktoren sind beispielsweise der
Standort   des   Systems,   wie   Büro,   Halle,   öffentlicher   Platz,   die   Einflüsse   durch   Lärm,   Geräusche,   Licht,
Schmutz, Klima und Schwingungen sowie sonstige Störungen von außen.

C.1.10.9.3 Anwenderaufgaben

Das   Thema   enthält   die   Aufgabenbeschreibung   der   Anwender   des   neuen   Systems.   Es   werden   alle
Arbeitsabläufe   mit   ihren   Eigenschaften,   die   für   die   Gestaltung   der   Benutzungsoberfläche   des   Systems
wichtig sind, dargestellt.

C.1.10.10 Altsystemanalyse

Ziel der  Altsystemanalyse  ist die Beschreibung des Ist-Zustandes eines Systems. Mit ihrer Hilfe wird ein
Verständnis für das Altsystem vermittelt und die Grundlage für die Weiterentwicklung beziehungsweise die
Migration von Systemteilen gelegt. In der Analyse werden Funktionalität, Ziele und Grobarchitektur des
Altsystems   beschrieben   sowie   die   Interaktionen   des   Systems   zu   seiner   Umgebung   identifiziert.   Als
Grundlage der Migration ist das aktuelle Datenmodell des Altsystems zu ermitteln sowie eine Einschätzung
der Datenqualität zu erstellen.

Verantwortlich für die Durchführung der Altsystemanalyse ist der Systemarchitekt. Zur Unterstützung sollten
ihm Experten des Altsystems sowie die Verantwortlichen der Nachbarsysteme zur Verfügung stehen.

Verantwortlich

Systemarchitekt

Aktivität

Vorlagen

Erzeugt durch

Altsystem analysieren

Altsystemanalyse(.odt|.doc)

Systementwurf:
Pflichtenheft (Gesamtsystementwurf) (Dekomposition des Gesamtsystems)

Inhaltlich abhängig

Einfluss der Altsystemanalyse auf die Systemerstellung:
Pflichtenheft (Gesamtsystementwurf)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

122

C.1.10.10.1 Systemüberblick

 Referenz Produkte

Im  Systemüberblick  werden die Grobarchitektur  des  Altsystems  und seine Einbettung in die  Umgebung
beschrieben. Ziele und Aufgaben des Systems sowie der Kontext, in dem das System eingesetzt wird, werden
angegeben.   Die   Systemkomponenten   werden   grob   beschrieben   und   die   verwendeten   Technologien
identifiziert.

Zusätzlich werden Datenbanken, auf denen das System arbeitet, sowie Plattform und Programmiersprache
angegeben. Nachbarsysteme, mit denen das System Daten und Nachrichten austauscht, werden identifiziert
und die Schnittstellen zum Altsystem analysiert und definiert.

Zum besseren Verständnis kann der Systemüberblick durch eine grafische Darstellung ergänzt werden, die
das System in seiner Umgebung sowie eine Schnittstellenübersicht zeigt. Der Systemüberblick ist Grundlage
für die Daten- und Schnittstellenanalyse.

C.1.10.10.2

Funktionsüberblick

Der Funktionsüberblick beschreibt Funktionalität und Geschäftsprozesse, die das Altsystem unterstützt. Ist
eine   Ablösung   des   Altsystems   geplant,   dient   der   Funktionsüberblick   als   ergänzende   Information   zur
Festlegung der Anforderungen. So kann sichergestellt werden, dass keine essentielle Funktionalität in den
Anforderungen an das Neusystem vergessen wurden.

C.1.10.10.3 Schnittstellen- und Abhängigkeitsanalyse

Altsysteme, insbesondere wenn es sich um Informationssysteme handelt, kommunizieren häufig mit einer
Vielzahl   von   Nachbarsystemen.   Die   Kommunikation   kann   auf   unterschiedlichste   Weise   ablaufen.   Im
einfachsten Fall handelt es sich um dateibasierte Kommunikation, das heißt eine Datei mit Daten in einem
vereinbarten   Format   wird   vom   sendenden   System   an   eine   vereinbarte   Stelle   gelegt   und   dort   vom
empfangenden System gelesen.

Eine weitere Möglichkeit zur Kommunikation ist das asynchrone Senden beziehungsweise Empfangen von
Nachrichten mit Hilfe von Messaging-Systemen. Bei sehr enger Koppelung der Systeme werden Daten im
Rahmen von synchronen Aufrufen zwischen den Systemen ausgetauscht.

Für jede dieser Kommunikationsformen ist ein Schnittstellenvertrag (Protokoll) zu erstellen, der im Detail
festlegt,   nach   welchen   Regeln   die   Kommunikation   zu   erfolgen   hat.   Die   Verträge   werden   mit   den
Verantwortlichen des jeweiligen Nachbarsystems verhandelt und dokumentiert.

Die  Abläufe   im   System   legen   fest,   in   welcher   Reihenfolge   die   Schnittstellen   zu   bedienen   sind.   Damit
bestehen   inhärente   Abhängigkeiten   der   Schnittstellen   untereinander.   Diese   Abhängigkeiten   müssen
identifiziert und ebenfalls dokumentiert werden.

C.1.10.10.4 Datenmodell

Das Datenmodell des Altsystems beschreibt, wie die Datenhaltung im Altsystem realisiert wurde. Beteiligte
Datenbanken   werden   identifiziert,   die   jeweiligen   Datenbankschemata   eruiert   und   die   Ergebnisse   im
Zusammenhang   dokumentiert.   Die   Dokumentation   erfolgt   analog   zum   physikalischen   Datenmodell   des
Datenbankentwurf

 s   eines Neusystems.

Neben der Datenstruktur ist die Datenqualität zu ermitteln. Anhand von Stichproben sowie Datenabzügen
wird festgestellt, in welchem Ausmaß ungültige Datensätze in den Datenbanken des Altsystems vorliegen
und inwieweit sich diese Datensätze störend auf die Abläufe auswirken.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


C.1 Produkte

123

C.1.10.11 Lastenheft Gesamtprojekt

Das Produkt  Lastenheft Gesamtprojekt  enthält alle an das zu entwickelnde System verbindlich gestellten
Anforderungen,   die   das   Gesamtprojekt   vollständig   und   konsistent   beschreiben.   Es   ist   Basis   für   die
Aufteilung in Teilprojekte.

Alle relevanten Anforderungen an das System werden vom Auftraggeber ermittelt und dokumentiert. Kern
des Lastenhefts Gesamtprojekt sind die funktionalen und nicht-funktionalen Anforderungen an das System,
sowie eine Skizze des Gesamtsystementwurfs. Der Entwurf berücksichtigt die zukünftige Umgebung und
Infrastruktur, in der das System später betrieben wird, und gibt Richtlinien für Technologieentscheidungen.
Die   Skizze   der   Gesamtsystemarchitektur   ist   die   bestimmende   Grundlage   für   die   Aufteilung   des
Gesamtprojektes in Teilprojekte.

Zusätzlich   werden   die   zu   unterstützenden   Phasen   im   Lebenszyklus   des   Systems   identifiziert   und   als
logistische   Anforderungen   aufgenommen.   Ebenfalls   Teil   der   Anforderungen   ist   die   Festlegung   von
Lieferbedingungen und Abnahmekriterien.

Die funktionalen und nicht-funktionalen Anforderungen dienen nicht nur als Vorgaben für die Entwicklung,
sondern   sind   zusätzlich   Grundlage   der   Anforderungsverfolgung   und   des   Änderungsmanagements.   Die
Anforderungen   sollten   so   aufbereitet   sein,   dass   die   Verfolgbarkeit   (Traceability)   sowie   ein   geeignetes
Änderungsmanagement für den gesamten Lebenszyklus eines Systems möglich sind.

Für die Erstellung des Lastenhefts Gesamtprojektes sowie für dessen Qualität ist der Auftraggeber alleine
verantwortlich.   Bei   Bedarf   kann   er   Dritte   mit   der   Erstellung   beauftragen.   Das   Lastenheft   sollte   im
Allgemeinen keine technischen Lösungen vorgeben, um Architekten und Entwickler bei der Suche nach
optimalen technischen Lösungen nicht einzuschränken.

Verantwortlich

Mitwirkend

Aktivität

Vorlagen

Inhaltlich abhängig

Anforderungsanalytiker (AG)

Anwender, Projektleiter, Projekteigner, Informationssicherheitsverantwortlicher,
Datenschutzverantwortlicher, Betriebsverantwortlicher, Fachverantwortlicher

Lastenheft Gesamtprojekt erstellen

Lastenheft Gesamtprojekt(.odt|.doc)

Konsistenz von Teilprojekt-Anforderungen zum Lastenheft Gesamtprojekt:
Lastenheft (Anforderungen)
Projektvorstudie, Projektauftrag und Anforderungen:
Projektvorstudie, Projektauftrag

Entscheidungsrelevant
bei

Gesamtprojekt aufgeteilt

Sonstiges

Initial

C.1.10.11.1 Ausgangssituation und Zielsetzung

In diesem Thema werden die Ausgangssituation und der Anlass zur Durchführung des Projektes anschaulich
dargestellt.   Es   wird   beschrieben,   welche   Defizite   bzw.   Probleme   existierender   Systeme   oder   auch   der
aktuellen Situation zur Entscheidung geführt haben, das Projekt durchzuführen, und welche Vorteile durch
den Einsatz des neuen Systems erwartet werden.

Es werden zusätzlich alle relevanten Stakeholder des Projektes benannt. Außerdem werden die technische
und fachliche Einbettung des zu entwickelnden Systems in seine Umgebung sowie der organisatorische und
technische Rahmen skizziert.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

124

Ausgangssituation

 Referenz Produkte

In diesem Abschnitt wird dargestellt, was der Anlass zur Durchführung des Projektes ist. Dazu gehört die
Darstellung des Problems, welches durch das Projekt beseitigt werden soll. In diesem Zusammenhang soll
auch darauf eingegangen werden, warum das Problem nicht mit bereits existierenden Systemen behoben
werden kann.

Des   Weiteren   wird   die  Auftragsgrundlage   für   das   neu   durchzuführende   Projekt   benannt.   Resultiert   der
Projektauftrag beispielsweise daraus, dass Gesetzesänderungen umzusetzen sind, dann sind diese Gesetze in
diesem Kapitel angeführt.

Zielsetzung

Im Rahmen der Zielsetzung werden die Vorteile aufgezeigt, die durch den Einsatz des neuen Systems zu
erwarten   sind.   Hierbei   wird   der  Systemname  angegeben,   eine   kurze   Beschreibung   des   Systems
vorgenommen sowie die Nutzer des Systems benannt.

Zudem wird in einem kurzen Abriss dargestellt, wie der Soll-Zustand zur Beseitigung des Problems, also das
System, zu gestalten ist.

Abgrenzung des Systems

Mit   dem   Produkt  Lastenheft   (Anforderungen)  werden   die  Anforderungen   an   das   zu   erstellende   System
erfasst,   um   den   Weg   zur   Systemrealisierung   vorzubereiten.   Bei   der   Erhebung   der  Anforderungen   sind
Fachseite, IT-Seite und eventuell Betrieb beteiligt. Die Anforderungen des Fachbereichs (der Anwender) sind
überwiegend   fachlicher   Natur.  Aus   den   fachlichen   und   technischen  Anforderungen   kann   das   IT-System
abgeleitet werden (siehe auch Skizze des Lebenszyklus und der Gesamtsystemarchitektur).

Dieses   Thema   beschreibt   schwerpunktmäßig   die  Abgrenzung   des   zu   entwickelnden   Systems   zu   seinen
Nachbarsystemen. Dabei sind von der Fachseite insbesondere die bereits etablierten  Geschäftsprozesse  zu
berücksichtigen. Der IT-Betrieb steuert dazu die Informationen zu den bereits betriebenen Systemen bei. Auf
Basis dieser Informationen ist der Bedarf, der durch das neue System gedeckt werden soll, zu bestimmen und
gegenüber   bereits   existierenden   Lösungen   abzugrenzen.   Somit   dokumentiert   dieses   Thema   die
Kernaufgaben, die das neue System erfüllen soll.

Weiterhin ist in diesem Thema zu dokumentieren, in welchen Organisationskontext (z.B. Referat, Behörde)
das neue System eingebettet werden soll.

Betroffene Geschäftsprozesse

Im Thema Abgrenzung des Systems werden bereits die Geschäftsprozesse und Nachbarsysteme benannt. In
diesem   Thema   ist   eine   detaillierte   Analyse   der   identifizierten,   betroffenen   Geschäftsprozesse   zu
dokumentieren. Die Analyse dieser Geschäftsprozesse dient dem Erkennen, welche Prozessschritte durch das
zu   entwickelnde   System   zu   unterstützen   sind.   Dies   ist   eine   wichtige   Quelle   für   die   Ermittlung   der
funktionalen Anforderungen (Thema Funktionale Anforderungen).

Anforderungen werden nicht nur aus Geschäftsprozessen abgeleitet, sondern können auch dazu führen, dass
bereits   etablierte   Geschäftsprozesse   angepasst   werden   müssen.   Daher   sind   in   diesem   Thema   auch   die
Geschäftsprozesse   aufzuführen,   die   Abhängigkeiten   zu   den   (neu)   umzusetzenden   Geschäftsprozessen
aufweisen und daher ggf. angepasst werden müssen.

Somit enthält dieses Thema eine Liste von Geschäftsprozessen, die sich auch in  Abgrenzung des Systems
wiederfinden müssen. Die hier gelisteten betroffenen Geschäftsprozesse stellen eine Teilmenge der gelisteten
Geschäftsprozesse des Themas Abgrenzung des Systems dar.

Stakeholder

Es werden alle Personen und Organisationen benannt, die im Rahmen der Anforderungserhebung zu dem zu
entwickelnden System berücksichtigt werden sollten, weil sie gegebenenfalls einen direkten oder indirekten
Einfluss auf die Anforderungen haben.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

125

Bei   den   Personen   kann   es   sich   um   konkrete   Personen   handeln   oder   auch   um   Rollen,   während   unter
Organisationen im Allgemeinen konkrete Referate oder Abteilungen gesehen werden.

Während   konkrete   namentlich   benannte   Personen   im  Projekthandbuch  erfasst   werden,   werden   hier   die
Funktionen bzw. Rollen sowie die Organisationen, die Stakeholder darstellen, aufgeführt.

Zu typischen Stakeholdern zählen beispielsweise

➢ Fachabteilung,

➢ Anwender des Systems,

➢ IT-Abteilungen,

➢ Architektur,

➢ Betrieb,

➢ Management usw.

Als zusätzliche Information kann an dieser Stelle auch beschrieben werden, welches spezielle Wissen der
Stakeholder zur Thematik hat, in welcher Form der Stakeholder Einfluss auf das neue zu schaffende System
hat und auf welchen Bereich des Systems.

Für die Erfassung empfiehlt sich entweder eine einfache Aufzählungsliste oder für detaillierte Informationen
eine tabellarische Erfassung.

Organisatorischer und technischer Rahmen

Dieses   Thema   dokumentiert   erkennbare   und   vorgegebene   Rahmenbedingungen.   Zu   diesen
Rahmenbedingungen   zählen   beispielsweise   technische   Vorgaben   (z.B.   im   Rahmen   von  SAGA).   Des
Weiteren   können   die   organisatorische   Einbettung   (wie   ordnen   sich   die   betroffenen   Bereiche   in   das
Gesamtorganigramm ein) und speziell vorgegebene IT-Strategien der jeweiligen Behörde eine Rolle spielen.

Aus diesem vorgegebenen organisatorischen und technischen Rahmen lassen sich dann  Randbedingungen
ableiten. Randbedingungen sind nicht-funktionale Anforderungen, die bei der Erstellung des Systems  zu
beachten sind, auf die die Projektbeteiligten jedoch keinen Einfluss haben. Randbedingungen können sich
sowohl   auf   das   zu   realisierende   System   als   auch   auf   den   Entwicklungsprozess   beziehen.   Beispiele   für
Randbedingungen sind dann z.B. Entwicklungsmethoden oder Programmiersprachen, die dem Projekt von
extern vorgegeben werden.

C.1.10.11.2

Funktionale Anforderungen

Funktionale   Anforderungen   sind   die   zentralen   Vorgaben   für   die   Systementwicklung.   Sie   werden   im
Anschluss   durch   den  Auftragnehmer   in   das  Pflichtenheft   (Gesamtsystementwurf)  übernommen   und   bei
Bedarf konkretisiert. Sie beschreiben die Fähigkeiten eines Systems, die ein Anwender erwartet, um mit
Hilfe   des   Systems   ein   Problem   zu   lösen.   Die   Anforderungen   werden   aus   den   zu   unterstützenden
Geschäftsprozessen und den Ablaufbeschreibungen zur Nutzung des Systems abgeleitet.

Für die Beschreibung der funktionalen Anforderungen können verschiedene Darstellungsmittel, wie:

➢ Text (natürliche Sprache)

➢ Anwendungsfälle (Text, Tabelle)

➢ Modelle

verwendet werden. Welche Technik im Detail verwendet wird, ist im Thema Organisation und Vorgaben zum
Anforderungsmanagement im Projekthandbuch festzulegen.

Unabhängig von der gewählten Darstellungsform sind bei der Erfassung der funktionalen Anforderungen
immer die folgenden Aspekte zu berücksichtigen:

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

126

 Referenz Produkte

➢ Inhalt: Was wird gemacht?

➢ Akteur

 e  : Wer ist involviert/beteiligt?

➢ Daten: Welche Daten werden genutzt, benötigt etc.?

➢ Schnittstellen: Mit welchen (Nachbar-)Systemen interagiert das System? Welche Schnittstellen zu

Anwendern hat das System?

Die   Struktur   und   die   Tiefe   der   Erfassung   der   funktionalen   Anforderungen   ist   ebenfalls   im   Thema
Organisation und Vorgaben zum Anforderungsmanagement im Projekthandbuch festzulegen.

C.1.10.11.3 Nicht-Funktionale Anforderungen

Im Gegensatz zu den funktionalen Anforderungen (Thema:  Funktionale Anforderungen), die beschreiben,
was  das   System  leisten  soll,   geben  die   nicht-funktionalen Anforderungen  an,  wie   gut  das   System  diese
Funktionen leisten soll. Nicht-funktionale Anforderungen beschreiben also Anforderungen an das System
und an das Projekt, die nicht-fachlicher Natur sind, jedoch entscheidend zur Anwendbarkeit des Systems
beitragen.

Die   in   den  Vorgaben   zur   Informationssicherheit,   zum   Datenschutz   und   zum   IT-Betrieb   enthaltenen
Regelungen beschreiben ebenfalls nicht-funktionale Anforderungen und müssen in diesem Thema aufgeführt
oder   referenziert   werden.   Gleichermaßen   hier   aufgeführt   oder   referenziert   werden   muss   die
Schutzbedarfsfeststellung, die zusammen mit den vorgenannten Vorgaben die Grundlage der zu erstellenden
Sicherheitskonzeption bildet.

Nicht-funktionale Anforderungen entstehen in der Regel parallel zu den funktionalen Anforderungen und
können diesen daher zugeordnet werden. Die nicht-funktionalen Anforderungen können die funktionalen
einschränken und sie konkreter beschreiben.

Nicht-funktionale Anforderungen können unterschiedlichster Art sein. Sie lassen sich generell unterscheiden
in Qualitätsanforderungen (Qualitätskriterien gemäß ISO 9126) und Randbedingungen (Anforderungen, die
nicht   an   das   System   direkt,   jedoch   an   die   Entwicklung   des   Systems   gestellt   werden).   Zur   einfachen
Strukturierung der Anforderungen werden diejenigen Anforderungen, die nicht eindeutig zu den funktionalen
Anforderungen gehören, den nicht-funktionalen Anforderungen zugeordnet.

Die Darstellung und Beschreibung erfolgt bei nicht-funktionalen Anforderungen überwiegend in Textform.
Die nicht-funktionalen Anforderungen sollten dabei messbar, prüfbar und entscheidbar formuliert sein. Für
die Messbarkeit müssen geeignete Metriken definiert werden.

Funktionalität

Nicht-funktionale Anforderungen im Bereich Funktionalität betreffen das Vorhandensein von Funktionen mit
festgelegten Eigenschaften. Beispiele hierfür sind Angaben zu Genauigkeiten von berechneten Werten oder
die Erfüllung von Normen oder gesetzlichen Vorschriften.

Zuverlässigkeit

Nicht-funktionale  Anforderungen   im   Bereich   Zuverlässigkeit   betreffen   die   Fähigkeit   des   Systems,   sein
Leistungsniveau unter festgelegten Bedingungen über einen festgelegten Zeitraum zu bewahren. Beispiele
hierfür sind Angaben zur Verfügbarkeit oder zur Wiederherstellbarkeit nach Ausfällen hinsichtlich Aufwand
und Zeit.

Benutzbarkeit

Nicht-funktionale Anforderungen im Bereich Benutzbarkeit betreffen alle Eigenschaften, die zur Benutzung
erforderlich   sind   bzw.   eine   ordnungsgemäßen   Benutzung   ermöglichen.   Dazu   gehören   Anforderungen
bezüglich Verständlichkeit, Erlernbarkeit und Bedienbarkeit des Systems.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


C.1 Produkte

Effizienz

127

Nicht-funktionale   Anforderungen   im   Bereich   Effizienz   betreffen   Performanceanforderungen   sowie
Anforderungen zum Verbrauchsverhalten beim Betrieb des Systems.

Änderbarkeit

Nicht-funktionale  Anforderungen   im   Bereich   Änderbarkeit   betreffen   den  Aufwand,   der   erforderlich   ist,
Änderungen an der Software vorzunehmen. Anlässe für Änderungen können Korrekturen, Verbesserungen
oder geänderte Anforderungen sein.

Übertragbarkeit

Nicht-funktionale Anforderungen im Bereich Übertragbarkeit betreffen die Eignung des Systems, von einer
Umgebung in eine andere übertragen zu werden. Dabei kann es sich um eine organisatorische Umgebung,
eine andere Hardware- oder Softwareumgebung handeln.

Randbedingungen

Randbedingungen legen Bedingungen und Einschränkungen fest, unter denen das Projekt durchgeführt wird
und die für die Entwicklung des Systems zu beachten sind. Randbedingungen sind häufig eine direkte Folge
des vorgegebenen organisatorischen und technischen Rahmens (dieser ist im Thema  Organisatorischer und
technischer Rahmen vorgegeben). Beispiele für Randbedingungen sind

➢ Richtlinien,

➢ einzuhaltende Standards wie z.B. Referenzarchitekturen,

➢ Entwicklungsmethoden,

➢ technologische Vorgaben wie Hardware- oder Software-Plattformen und

➢ zwingend einzuhaltende Terminvorgaben.

C.1.10.11.4 Skizze des Lebenszyklus und der Gesamtsystemarchitektur

Für die Einordnung, Systematisierung, Kategorisierung und auch Priorisierung von Anforderungen ist ein
Koordinierungsrahmen hilfreich, um die Visualisierung der Anwenderanforderungen zu erleichtern. Diese
Aufgabe   kann   eine  Gesamtsystemarchitektur  leisten,   die   die   Sichtweise   des   Anwenders   und/oder   des
Betriebs repräsentiert. Sie ist ein  nicht verbindlicher  Vorschlag, der organisatorische, fachliche aber auch
technische Sichten darstellen kann.

Die Gesamtsystemarchitektur muss eine Verbindung zu den im Thema Abgrenzung des Systems benannten
Geschäftsprozessen, (Nachbar-)Systemen und im Weiteren zu den Anforderungen herstellen. Dieses dient
Thema dazu,

➢ Fakten   wie   z.B.   verbindlich   einzusetzende,   bereits   etablierte   Systeme   zu   benennen   (etwa   ein

konkretes Datenbankmanagementsystem).

➢ Vorstellungen   zu   artikulieren,   wie   die   Realisierung   und   die   Einbettung   des   zu   entwickelnden

Systems möglich ist (etwa Zugriff über mobile Rechner).

Festlegungen werden an dieser Stelle nur insofern getroffen, als dass sie Fakten betreffen, die die Entwickler
zwingend berücksichtigen müssen. Ansonsten dient dieses Thema dazu, Erwartungen an die Einbettung des
Systems hinsichtlich der fachlichen Funktion und der technischen Einbettung zu formulieren.

Zur   Darstellung   der   fachlichen   Architektur   eignen   sich   einfache   Grafiken.   Auch   eine   modellbasierte
Darstellung, z.B. mittels UML-Komponentendiagrammen, kann erfolgen.

Lebenszyklus

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

128

 Referenz Produkte

Der   Lebenszyklus   des   zu   entwickelnden   Systems   endet   nicht   mit   der   Erstellung   des   Produkts,   sondern
umfasst   auch   noch   die   Zeit   nach   der   Überführung   in   den   Wirkbetrieb,   in   der   Fehlerbehebungen,
Anpassungen   und   Erweiterungen   der   Funktionalität   vorgenommen   werden.   Der   Lebenszyklus   endet
schließlich mit der Ablösung des Systems durch ein Nachfolgeprodukt. Es wird daher dargelegt,

➢ wie die Weiterentwicklung des Systems nach dem Projekt weitergeht,

➢ wie Nutzung und Betrieb verlaufen,

➢ ob und welche Ausbaustufen des Systems geplant sind,

➢ wann und wie das System stillgelegt werden soll.

Diese Punkte besitzen einen entscheidenden Einfluss auf die Entwicklung des Systems und insbesondere auf
die Erstellung der Systemarchitektur.

C.1.10.11.5

Lieferumfang

Es   werden  alle   Gegenstände   und   Dienstleistungen   aufgelistet,   die   während  des   Projektverlaufs   oder   bei
Abschluss des Projektes vom Auftragnehmer an den Auftraggeber zu liefern sind. Jede Lieferung (von AN)
erfordert eine Abnahmeprüfung. Der Lieferumfang kann je nach Vereinbarung das zu entwickelnde System,
Teile   des   Systems,   ein   unterstützendes   System,   Teile   eines   unterstützenden   Systems,   Dokumente   und
vereinbarte Dienstleistungen enthalten.

C.1.10.11.6 Abnahmekriterien

Abnahmekriterien   legen   fest,   welche   Kriterien   die  Lieferung   (von  AN)  erfüllen   muss,   um   den   an   sie
gestellten Anforderungen zu entsprechen. Sie sollen prüfbar dargestellt werden. Abnahmekriterien beziehen
sich sowohl auf funktionale als auch auf nicht-funktionale Anforderungen.

In der Phase bis zur Auftragsvergabe können die Abnahmekriterien nur in einer allgemeinen Form, z.B. als
K.O.-Kriterien, angegeben werden. Die allgemeinen Abnahmekriterien sollten auch die Forderung nach einer
Erstellung von Abnahmekriterien durch den Auftragnehmer enthalten. Dabei sind der Aufbau und die Anzahl
der Abnahmekriterien durch den Auftraggeber zu skizzieren. Eine Strukturierung der Abnahmekriterien nach
ihren drei wesentlichen Bestandteilen

➢ Ausgangssituation,

➢ Aktion(en) und

➢ erwartetes Ergebnis

ist   anzustreben.   In   jedem   Fall   müssen   die   erwarteten   Ergebnisse   der  Abnahme   pro  Abnahmekriterium
festgelegt werden.

Die Abnahmekriterien sind Grundlage der Abnahmeprüfung und ggf. auch für die Prüfung zur betriebliche
Freigabe  und gehen  als  Anforderungen in  die  Abnahmespezifikation  sowie  ggf.  in  die  Prüfspezifikation
Inbetriebnahme ein.

Erzeugt

Abnahme der Lieferungen:
Abnahmeerklärung
Prüfung der Lieferungen:
Abnahmeprotokoll, Abnahmespezifikation

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

129

C.1.10.12 Bewertung Lastenheft Gesamtprojekt

Ziel der Bewertung Lastenheft Gesamtprojekt ist es, Erfassung und Erstellung der Anwenderanforderungen
zu bewerten und das mögliche Realisierungsrisiko des Auftraggebers so weit als möglich transparent und
beherrschbar zu gestalten. Somit hat der Auftraggeber auf der Basis seiner Bewertungsmöglichkeiten bereits
überprüft, ob die Anwenderanforderungen aus seiner Sicht technisch machbar, finanzierbar, wirtschaftlich
und wichtig sind.

Bei   wirtschaftlich   fraglichen   Anforderungen   beziehungsweise   bei   kostenseitig   nicht   ausreichend
abschätzbaren Anforderungen kann der Auftraggeber hilfsweise auf eine Optionierung der Leistungen, das
heißt Einholung von optional anzubietenden Leistungen beziehungsweise Leistungspaketen, zurückgreifen,
um auf Basis tatsächlicher Kostenangaben eine Bewertung durchzuführen.

Das Produkt Bewertung Lastenheft Gesamtprojekt dokumentiert die Bewertungsergebnisse für die bis dahin
erfassten Anwenderanforderungen.  Dabei   ist  die  Bewertung kaum durchführbar,  wenn  nicht  bereits  eine
Skizze des Lebenszyklus und der Gesamtsystemarchitektur oder eine konkrete Systemarchitektur vorliegen,
also bereits Lösungsansätze vorhanden sind. Hierzu kann eine  Evaluierung von Fertigprodukten  wertvolle
Beiträge leisten.

Die   Bewertung   Lastenheft   Gesamtprojekt   baut   auf   vorher   festgelegten   Bewertungskriterien   auf.   Die
Bewertungsergebnisse   der  Anforderungsbewertung  werden   in   das   Produkt   Lastenheft   Gesamtprojekt
eingearbeitet.

Verantwortlich

Anforderungsanalytiker (AG)

Mitwirkend

Aktivität

Vorlagen

Anwender, Projektleiter, Projekteigner, Fachverantwortlicher

Lastenheft Gesamtprojekt bewerten

Bewertung Lastenheft Gesamtprojekt(.odt|.doc)

Entscheidungsrelevant
bei

Gesamtprojekt aufgeteilt

Sonstiges

Initial

C.1.10.12.1 Bewertungskriterien Gesamtprojekt

In diesem Thema werden die Bewertungskriterien festgelegt, die bei der Anforderungsbewertung bzw. der
Bewertung des Produkts Lastenheft Gesamtprojekt zu berücksichtigen sind. Die Bewertungskriterien sollten
folgende Aspekte abdecken:

➢ die Plausibilität der definierten Anforderungen,

➢ die Beherrschbarkeit der Komplexität,

➢ die Prüfung der Möglichkeiten zum Einsatz von Fertigprodukten,

➢ die   Übereinstimmung   der

 Schutzbedarfsfeststellung  mit   den   Anforderungen   an   die

Informationssicherheit und den Datenschutz,

➢ die Auswirkungen auf die vorhandene IT-Infrastruktur,

➢ die Kostenschätzungen für einzelne Anforderungen,

➢ die Übereinstimmung mit gesetzlichen Verpflichtungen sowie

➢ die   Übereinstimmung   mit   Anforderungen   an   die   Regeltreue   (Compliance),   soweit   diese   über

gesetzliche Verpflichtungen hinausgehen.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

130

 Referenz Produkte

Für   eine   Bewertung   der   wirtschaftlichen   Umsetzbarkeit   der   Anforderungen   sollte   eine
Wirtschaftlichkeitsbetrachtung des zu entwickelnden Systems durchgeführt werden, die unter anderem zu
beachtende laufende Kosten aufführen und Grenzwerte für Kosten von Maßnahmen festlegen sollte.

C.1.10.12.2 Bewertungsergebnisse Gesamtprojekt

Zu   den   Ergebnissen   der  Anforderungsbewertung  gehört   insbesondere   eine   Gesamtbewertung   der
Anwenderanforderungen.   Sie   bewertet,   inwieweit   vorgegebene   Restriktionen,   die   entweder   vom
Haushalt/Budget, von Terminplänen oder von verfügbaren Ressourcen gesetzt werden, eingehalten werden
können beziehungsweise überschritten werden. Des Weiteren werden alle erfassten Anwenderanforderungen
geprüft und ihre Einstufung bewertet:

➢ Es werden die zurückgestellten Anwenderanforderungen und die Begründung der Zurückstellung

geprüft (zum Beispiel ist die Notwendigkeit nicht nachweisbar).

➢ Es werden die modifizierten Anwenderanforderungen und die Begründung der Modifikation geprüft

(zum Beispiel durch den wirtschaftlicheren Einsatz von Fertigprodukten).

➢ Es werden neu hinzugekommene Anwenderanforderungen hinsichtlich ihrer Notwenigkeit geprüft

(zum Beispiel sind wichtige nicht-funktionale Anwenderanforderungen nicht erfasst worden).

Zu den Bewertungsergebnissen gehören zusätzlich die Ergebnisse der Betrachtung der Wirtschaftlichkeit der
Anwenderanforderungen,   beispielsweise   Kosten-Nutzen-Abwägungen,   Aufzeigen   von   kostentreibenden
Anwenderanforderungen sowie die Finanzierbarkeit der Anwenderanforderungen.

C.1.11 Systementwurf

C.1.11.1 Pflichtenheft (Gesamtsystementwurf)

Das  Pflichtenheft   (Gesamtsystementwurf)  ist   das   Pendant   zu   dem   Auftraggeberprodukt  Lastenheft
(Anforderungen)  auf   Auftragnehmerseite.   Es   wird   vom   Auftragnehmer   in   Zusammenarbeit   mit   dem
Auftraggeber erstellt und stellt das zentrale Ausgangsdokument der Systemerstellung dar.

Wesentliche Inhalte des Gesamtsystementwurfs sind die funktionalen und nicht-funktionalen Anforderungen
an das zu entwickelnde Gesamtsystem. Die Anforderungen werden aus dem Lastenheft (Anforderungen)
übernommen und geeignet aufbereitet. Eine erste Grobarchitektur des Systems wird entwickelt und in einer
Schnittstellenübersicht   beschrieben.   Das   zu   entwickelnde   System   sowie   weitere   ggf.   zu   entwickelnde
Systeme werden identifiziert und den Anforderungen zugeordnet. Zusätzliche Anforderungen an die Logistik
werden   in   Zusammenarbeit   mit   dem   Logistikverantwortlichen   erarbeitet.   Abnahmekriterien   und
Lieferumfang für das fertige Gesamtsystem werden aus dem Lastenheft (Anforderungen) übernommen und
konkretisiert.   Um   sicher   zu   stellen,   dass   alle   Anforderungen   berücksichtigt   sind,   wird   eine
Anforderungsverfolgung,   sowohl   hin   zum   Lastenheft   (Anforderungen)   als   auch   zu   den   Systemen,
durchgeführt.

Zur   Erstellung   des   Gesamtsystementwurfs   sind   Kenntnisse   aus   unterschiedlichen   Disziplinen   wie
Systementwicklung,   Sicherheit,   Ergonomie   und   Logistik   notwendig,   die   üblicherweise   nicht   von   einer
Person   abgedeckt   werden   können.   Da  Anforderungen   den   Kern   der   Spezifikation   darstellen,   fällt   dem
Anforderungsanalytiker (AN)  die verantwortliche  Rolle  für die Erstellung des Gesamtsystementwurfs zu.
Für   die   inhaltliche   Ausarbeitung   benötigt   er   jedoch   intensive   Unterstützung   durch   Experten   der
verschiedenen Disziplinen.

Zu   jedem   im   Gesamtsystementwurf   identifizierten   System   und  Segment  werden   die   entsprechenden
Produkte  wie   Spezifikation   und   Architektur   erstellt.   Anforderungen   an   die   Logistik   werden   in   der
Spezifikation logistische Unterstützung weiterverfolgt.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

Verantwortlich

Mitwirkend

Aktivität

Methoden

Werkzeuge

Vorlagen

Inhaltlich abhängig

131

Anforderungsanalytiker (AN)

Ergonomieverantwortlicher, Prüfer, QS-Verantwortlicher, Systemarchitekt,
Systemintegrator, Informationssicherheitsverantwortlicher,
Datenschutzverantwortlicher, Betriebsverantwortlicher

Gesamtsystem entwerfen

Anforderungsanalyse, Systemanalyse

Anforderungsmanagement, Integrierte Entwicklungsumgebung,
Modellierungswerkzeug

Pflichtenheft (Gesamtsystementwurf)(.odt|.doc)

Berücksichtigung der Informationssicherheit und des Datenschutzes bei der
Systemerstellung:
Sicherheitskonzeption, Erweiterung der Vorgaben zur Informationssicherheit,
Erweiterung der Vorgaben zum Datenschutz
Berücksichtigung des IT-Betriebs bei der Systemerstellung:
Erweiterung der Vorgaben zum IT-Betrieb
Einfluss der Altsystemanalyse auf die Systemerstellung:
Altsystemanalyse
Konsistenz von Anwenderaufgabenanalyse und Gesamtsystementwurf:
Anwenderaufgabenanalyse
Konsistenz von Lasten- und Pflichtenheft (ohne Vertrag):
Lastenheft (Anforderungen)
Vorgaben im Gesamtsystementwurf bezüglich Fertigprodukten:
Make-or-Buy-Entscheidung

Entscheidungsrelevant
bei

Gesamtsystem entworfen

Sonstiges

Initial

C.1.11.1.1 Ausgangssituation und Zielsetzung

In diesem Thema werden die Ausgangssituation und der Anlass zur Durchführung des Projektes anschaulich
dargestellt.   Es   wird   beschrieben,   welche   Defizite   bzw.   Probleme   existierender   Systeme   oder   auch   der
aktuellen Situation zur Entscheidung geführt haben, das Projekt durchzuführen, und welche Vorteile durch
den Einsatz des neuen Systems erwartet werden.

Es werden zusätzlich alle relevanten Stakeholder des Projektes benannt und die technische und fachliche
Einbettung   des   zu   entwickelnden   Systems   in   seine   Umgebung   skizziert.   Zusätzlich   werden   erste
Rahmenbedingungen   für   die   Entwicklung   identifiziert   und   beschrieben.   Rahmenbedingungen   können
beispielsweise technische Vorgaben oder Vorgaben zur Sicherheit sein.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

132

 Referenz Produkte

C.1.11.1.2 Dekomposition des Gesamtsystems

In der Dekomposition des Gesamtsystems  wird das zentrale System mit  allen ggf. zusätzlich benötigten
Systemen   identifiziert   und   festgelegt,   welche  Logistikelemente  erstellt   werden.   Zudem   werden   die   zu
erstellenden   Architekturdokumente   und   Implementierungs-,   Integrations-   und   Prüfkonzepte   benannt.
Grundlage   sind   die   funktionalen   und   nicht-funktionalen   Anforderungen   sowie   die   Skizze   der
Gesamtsystemarchitektur aus dem Lastenheft. Beistellungen des Auftraggebers werden berücksichtigt.

Die   Gesamtsystemarchitektur  wird  hinsichtlich  der   möglichen Verwendung  von Fertigprodukten  geprüft.
Gegebenenfalls   wird  deshalb   bereits   auf   Basis   des   Pflichtenhefts   eine  Marktsichtung  für   Fertigprodukte
durchgeführt,   um   den   Einfluss   möglicher   Fertigproduktkandidaten   auf   die   Anforderungen   und   die
Systemarchitektur abschätzen zu können.

Erzeugt

Architekturen und Realisierung der Systeme:
Implementierungs-, Integrations- und Prüfkonzept System (System),
Systemarchitektur (System)
Elemente des Gesamtsystems:
Ausbildungsunterlagen, Logistische Unterstützungsdokumentation,
Nutzungsdokumentation, System
Migration von Altsystemen:
Altsystemanalyse (System), Migrationskonzept (System)

C.1.11.1.3

Funktionale Anforderungen

Funktionale Anforderungen beschreiben die Fähigkeiten eines Systems, die ein Anwender erwartet, um mit
Hilfe des Systems ein fachliches Problem zu lösen. Die Anforderungen werden aus den zu unterstützenden
Geschäftsprozessen und den Ablaufbeschreibungen zur Nutzung des Systems abgeleitet.

Die Beschreibung der funktionalen Anforderungen erfolgt beispielsweise in Form von Anwendungsfällen
(Use   Cases).   Ein   Anwendungsfall   beschreibt   dabei   einen   konkreten,   fachlich   in   sich   geschlossenen
Teilvorgang. Die Gesamtheit der Anwendungsfälle definiert das Systemverhalten. Ein Anwendungsfall kann
in   einfachem  Textformat   beschrieben   werden,   häufig   stehen   jedoch   organisationsspezifische   Muster   zur
Beschreibung zur Verfügung. Für datenzentrierte Systeme wird im Rahmen der funktionalen Anforderungen
ein erstes fachliches  Datenmodell  erstellt, das als Grundlage des späteren  Datenbankentwurf
 s    dient. Das
fachliche Datenmodell des Systems wird aus den Entitäten des Domänenmodells abgeleitet.

Die funktionalen Anforderungen sind die zentralen Vorgaben für die Systementwicklung. Sie werden in das
Pflichtenheft (Gesamtsystementwurf) übernommen und bei Bedarf konkretisiert.

C.1.11.1.4

Lebenszyklusanalyse

Ausgehend von den Anforderungen werden die zu unterstützenden Phasen im Lebenszyklus (Entwicklung,
Wartung   und   Stilllegung)   bestimmt.   Es   wird   festgelegt,   für   welche   der   im   Thema  Dekomposition   des
Gesamtsystems identifizierten Systeme ein Logistisches Unterstützungskonzept zu erstellen ist.

C.1.11.1.5 Nicht-funktionale Anforderungen

In diesem Thema werden die im Lastenheft beschriebenen nicht-funktionalen Anforderungen aufgeführt, ggf.
konkretisiert und deren Umsetzung erläutert.

Sofern das Lastenheft Vorgaben zur Informationssicherheit, zum Datenschutz oder zum IT-Betrieb enthält, ist
basierend auf diesen Vorgaben, den übrigen Anforderungen, der Dekomposition des Gesamtsystems und der
Schnittstellenübersicht festzulegen,

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


C.1 Produkte

133

➢ ob   bereits   auf   der   Ebene   des   Gesamtsystems   eine  Sicherheitskonzeption  zu   erstellen   ist,   um
Bedrohungen   und   Maßnahmen   dokumentieren   zu   können.   Hierbei   ist   zusätzlich   die   vom
Auftraggeber bereitgestellte Schutzbedarfsfeststellung zu berücksichtigen.

➢ ob   diese   Vorgaben   geändert   oder   erweitert   werden   müssen.   Beabsichtigte   Änderungen   und
Erweiterungen   müssen   mit   dem   Auftraggeber   abgestimmt   werden   und   führen   ggf.   zu   einer
Vertragsanpassung.

Erzeugt

Berücksichtigung der Vorgaben zum Datenschutz auf Ebene des
Gesamtsystems:
Erweiterung der Vorgaben zum Datenschutz (Gesamtsystem)
Berücksichtigung der Vorgaben zum IT-Betrieb auf Ebene des
Gesamtsystems:
Erweiterung der Vorgaben zum IT-Betrieb (Gesamtsystem)
Berücksichtigung der Vorgaben zur Informationssicherheit auf Ebene des
Gesamtsystems:
Erweiterung der Vorgaben zur Informationssicherheit (Gesamtsystem)
Berücksichtigung ergonomischer Aspekte:
Anwenderaufgabenanalyse (System), Mensch-Maschine-Schnittstelle
(Styleguide) (System)
Erstellung einer Sicherheitskonzeption auf Ebene des Gesamtsystems:
Sicherheitskonzeption (Gesamtsystem)

C.1.11.1.6 Schnittstellenübersicht

Zur   Darstellung   der   Zusammenhänge   zwischen   dem   System   und   seiner   Umgebung   wird   eine
Schnittstellenübersicht erstellt. Ausgehend vom System werden Schnittstellen zum Anwender, zu anderen im
Projekt zu entwickelnden Systemen, zur Logistik und zu Nachbarsystemen identifiziert und in geeigneter
Form dokumentiert.

Die konkrete Beschreibung der Schnittstellen erfolgt in den Spezifikationen der Systemelemente sowie in der
Spezifikation logistische Unterstützung.

C.1.11.1.7

Lieferumfang

Es   sind   alle   Gegenstände   und   Dienstleistungen   aufzulisten,   die   während   des   Projektverlaufs   oder   bei
Abschluss des Projektes vom Auftragnehmer an den Auftraggeber zu liefern sind. Jede Lieferung erfordert
eine  Abnahmeprüfung.   Der   Lieferumfang   kann   je   nach   Vereinbarung   ein   System,   Teile   eines   Systems,
Dokumente und Dienstleistungen enthalten.

Erzeugt

Lieferumfang der Auslieferungen:
Lieferung

C.1.11.1.8 Abnahmekriterien und Vorgehen zur Ausgangsprüfung

Abnahmekriterien   legen   fest,   welche   Kriterien   die  Lieferung  erfüllen   muss,   um   den  Anforderungen   zu
entsprechen. Sie sollten messbar dargestellt werden und können nach ihren drei wesentlichen Bestandteilen -
Ausgangssituation,   Aktion(en)   und   erwartetes   Ergebnis   -   strukturiert   werden.   Aus   vertraglicher   Sicht
beschreiben die Abnahmekriterien die Bedingungen für die Entscheidung, ob das Endprodukt die gestellten
Anforderungen erfüllt oder nicht. Abnahmekriterien können sich sowohl auf einzelne Anforderungen ("Unter
welchen   Bedingungen   gilt   die   Anforderung   als   erfüllt?")   als   auch   auf   den   Lieferumfang   ("Welche
Bedingungen   müssen   erfüllt   sein,   damit   eine   konkrete   Lieferung   abgenommen   wird?")   beziehen.   Die

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

134

 Referenz Produkte

Definition der Abnahmekriterien ist Aufgabe des Auftraggebers; der Auftragnehmer sollte sie aber kennen
und in seinem Pflichtenheft auch benennen, um Klarheit darüber zu besitzen, unter welchen Bedingungen
das System abgenommen wird. Unter Umständen und bei entsprechender vertraglicher Vereinbarung kann es
außerdem sinnvoll sein, dass der Auftragnehmer die konkreten Abnahmekriterien definiert.

Der Auftragnehmer sollte vor der Auslieferung möglichst sicher sein, dass die Lieferung auch abgenommen
wird und deswegen eine geeignete Ausgangsprüfung durchführen. Die zu liefernden Systemelemente werden
anhand einer Prüfspezifikation Systemelement, die zu liefernden Dokumente (insbesondere die Logistische
Unterstützungsdokumentation)   anhand   einer  Prüfspezifikation  geprüft.   Die   dazu   notwendigen   Prüffälle
werden aus den Abnahmekriterien abgeleitet, können aber in der Regel nicht vollständig identisch mit den
Prüffällen des Auftraggebers sein, da der Auftragnehmer z.B. keinen Zugang zur Zielplattform hat oder die
tatsächlichen Anwender nicht einbinden kann.

Erzeugt

Prüfung der Auslieferungen:
Prüfprotokoll, Prüfprotokoll Systemelement, Prüfprozedur Systemelement,
Prüfspezifikation, Prüfspezifikation Systemelement

C.1.11.1.9 Anforderungsverfolgung zum Lastenheft

Im   Rahmen   der   Anforderungsverfolgung   zum   Lastenheft   wird   zusammenfassend   die   Zuordnung   der
funktionalen   und   nicht-funktionalen   Anforderungen   aus   dem   Lastenheft   zu   den   Anforderungen   im
Pflichtenheft dargestellt. Die bidirektionale Verfolgbarkeit muss dabei sichergestellt werden. Die Darstellung
kann beispielsweise anhand einer Matrix erfolgen.

C.1.11.1.10 Anforderungsverfolgung zu den Spezifikationen

Im   Rahmen   der   Anforderungsverfolgung   wird   im   Pflichtenheft   zusammenfassend   die   Zuordnung   der
funktionalen   und   nicht-funktionalen   Anforderungen   zu   den   Elementen   der   Gesamtsystemarchitektur
(System,  Segment  oder   Logistik)   dargestellt.   Die   bidirektionale  Verfolgbarkeit   muss   dabei   sichergestellt
werden. Die Darstellung kann beispielsweise anhand einer Matrix erfolgen.

C.1.11.1.11 Glossar

Das Glossar ist eine Sammlung aller verwendeten Fachbegriffe und dient dazu, allen Projektbeteiligten ein
gemeinsames   Verständnis   zu   ermöglichen.   Damit   können   unterschiedliche   Interpretationen   und
Missverständnisse vermieden werden und das Verständnis der Anforderungen wird erhöht. Das Glossar ist
für alle Projektbeteiligten verbindlich.

Es   empfiehlt   sich,   neben   der   Erläuterung   der   Begriffe   auch   mögliche  Abkürzungen   und   für   eventuelle
Rückfragen auch die Herkunft bzw. die Quelle der Erläuterung anzugeben.

C.1.11.2 Systemarchitektur

Ausgehend von den funktionalen und nicht-funktionalen Anforderungen an das System ist es Aufgabe des
Systemarchitekten, eine geeignete Systemarchitektur zu entwerfen. Die Architekturprodukte dienen dabei
sowohl als Leitfaden als auch zur Dokumentation der Entwurfsentscheidungen.

In   einem   ersten   Schritt   werden   richtungsweisende   Architekturprinzipien   festgelegt   und   mögliche
Entwurfsalternativen   untersucht.   Entsprechend   der   gewählten   Entwurfsalternative   wird   die   Zerlegung
(Dekomposition)   des   Systems   in  Segment
 e  ,   HW-,   SW-   und  Externe   Einheit  beschrieben   (vergleiche
Produktstrukturierung).

Beziehungen und Schnittstellen zwischen den Elementen und zur Umgebung werden identifiziert und im
Überblick   dargestellt.   Zusätzlich   werden   querschnittliche   Systemeigenschaften   wie   Sicherheitskonzept,
Transaktionskonzept oder Loggingkonzept festgelegt.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


C.1 Produkte

135

Die gewählte Architektur wird hinsichtlich ihrer Eignung für das zu entwickelnde System bewertet. Offene
Fragen können beispielsweise im Rahmen einer prototypischen Entwicklung geklärt werden.

Hauptverantwortlicher   für   den   Architekturentwurf   ist   der  Systemarchitekt.   Unterstützt   wird   er   von
verschiedenen Experten zu Einzelthemen wie HW-Entwicklung, SW-Entwicklung, Logistik, Sicherheit oder
Ergonomie.

Die Architektur stellt das zentrale Dokument für die Erstellung weiterer Produkte dar. Sie legt alle Segmente,
HW-, SW- und Externe Einheiten des Systems fest. Entsprechend den Vorgaben werden für jede HW- oder
SW-Einheit eine Architektur sowie für die jeweiligen Elemente die Spezifikationen erstellt.

Verantwortlich

Systemarchitekt

Mitwirkend

Aktivität

Methoden

Werkzeuge

Vorlagen

Erzeugt durch

SW-Architekt, Informationssicherheitsverantwortlicher,
Datenschutzverantwortlicher, Betriebsverantwortlicher

System entwerfen

Designverifikation, Prototyping, Systemdesign

Modellierungswerkzeug

Systemarchitektur(.odt|.doc)

Systementwurf:
Pflichtenheft (Gesamtsystementwurf) (Dekomposition des Gesamtsystems)

Entscheidungsrelevant
bei

System entworfen

C.1.11.2.1 Architekturprinzipien und Entwurfsalternativen

Grundsätzlich gibt es für ein System mehrere Architekturlösungen, von denen jede ihre Vor- und Nachteile
hat.   Durch   die   Beschreibung   der   zugrunde   liegenden   Architekturprinzipien   sowie   möglicher
Entwurfsalternativen wird der  Entscheidungsprozess  zur  letztendlich gewählten Architektur  dokumentiert
und die Basis für eine Architekturbewertung gelegt.

Architekturprinzipien   sind   Vorgaben,   die   beispielsweise   auf   Grund   der   Systemart   oder   anderer
Systemeigenschaften   richtungweisend   für   den   Architekturentwurf   sind.   Auf   Systemebene   kann   dies
beispielsweise die Festlegung der Anwendungsdomäne (Eingebettetes System, Informationssystem) oder die
Entscheidung für ein verteiltes System sein.

Entwurfsalternativen   beschreiben   unterschiedliche   Möglichkeiten   der  Dekomposition   des   Systems  in
 e  ,   HW-,   SW-   und  Externe   Einheit.   Für   jede  Alternative   werden   anhand   einer   zu   definierenden
Segment
Kriterienliste Vor- und Nachteile identifiziert und die Lösung bewertet. Als Grundlage für die Suche nach
möglichen Entwurfsalternativen eignen sich auf Systemebene beispielsweise Musterarchitekturen.

Vorgaben zu Architekturprinzipien sowie Einschränkungen bei möglichen Entwurfsalternativen ergeben sich
vor allem aus den Anforderungen der Systemspezifikation beziehungsweise des Gesamtsystementwurfs.

C.1.11.2.2 Dekomposition des Systems

 s    festgelegt. Die statische Struktur
Im Rahmen der Dekomposition wird die statische Struktur des  System
beschreibt   die   Zerlegung   in   Segmente   und   Einheiten.   Das   Entwurfsergebnis   wird   als   Graph   der   zu
realisierenden   Segmenttypen   und   Einheitentypen   sowie   ihrer   Beziehungen   untereinander   dokumentiert.
Grundlage der Dekomposition sind die Anforderungen aus der  Systemspezifikation. Randbedingungen für
die  Zerlegung  werden  durch die  in der  Systemarchitektur  identifizierten Architekturprinzipien sowie  die
getroffenen Entwurfsentscheidungen vorgegeben.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland



136

 Referenz Produkte

Für jede im Rahmen der Dekomposition identifizierte Einheit wird festgelegt, ob es sich um eine HW-, eine
SW- oder eine Externe Einheit handelt und für welche HW- und SW-Einheiten die Erstellung einer separaten
Architektur   notwendig   ist.   Abhängig   vom   Umfang   und   der   Komplexität   kann   die   Architektur   des
übergeordneten Systems auch bereits eine Betrachtung bis auf Modulebene enthalten.

Für   Externe   Einheiten,   die   dem   Projekt   noch   nicht   vorliegen,   muss   dokumentiert   werden,   wie   deren
Beschaffung   erfolgt.   Bei   einer   Marktsichtung   von   Fertigprodukten   muss   auf   die   Verfügbarkeit   des
Quellcodes   geachtet   werden.   Fertigprodukte   ohne   verfügbaren  Quellcode   sollten  nur   mit   entsprechender
Begründung verwendet werden ("Comply-or-Explain"). Zudem sollten bei der Auswahl von Fertigprodukten
solche mit vorhandener IT-Sicherheitsprüfung (z.B. durch das BSI) bevorzugt werden.

Erzeugt

Architekturen der Einheiten des Systems:
SW-Architektur (SW-Einheit)
Beschaffung der Externen Einheiten des Systems:
Make-or-Buy-Entscheidung (Externe Einheit), Marktsichtung für Fertigprodukte
(Externe Einheit)
Elemente des Systems:
Externe Einheit, SW-Einheit, Segment

C.1.11.2.3 Externe Systemelemente

In diesem Thema werden alle zum Einsatz kommenden Fertigprodukte zusammenfassend aufgeführt. Hierzu
zählen auch eingesetzte Frameworks und Laufzeitumgebungen externer Anbieter. Jedes Fertigprodukt ist mit
dessen Namen, Version, Lizenz und Anbieter zu beschreiben. Ziel ist es, einen automatisierbaren Abgleich
der   verwendeten   externen   Systemelemente   zu   ermöglichen,   um   diese   beispielsweise   regelmäßig
automatisiert auf bekannt gewordene Sicherheitslücken zu prüfen.

C.1.11.2.4 Querschnittliche Systemeigenschaften

In   einem   System   lassen   sich   systemelementspezifische   und   systemübergreifende   Eigenschaften
unterscheiden.   Lösungen  für   systemelementspezifische   Eigenschaften  werden  in  den  Spezifikationen  der
jeweiligen   Systemelemente   ausgearbeitet.   Lösungen   für   systemübergreifende   Eigenschaften   werden   hier
beschrieben.

Zu   typischen   systemübergreifenden   Eigenschaften   zählen   bei   SW-Systemen   beispielsweise
Transaktionsanforderungen, Persistierung von Daten oder Anforderungen an Logging und Tracing. Für HW-
Systeme   können   dies   beispielsweise   einheitliche   Steckerbelegungen   oder   systemübergreifende
Sicherheitsanforderungen sein. Welche querschnittlichen Systemeigenschaften zu berücksichtigen sind, wird
im Rahmen dieses Themas festgelegt.

C.1.11.2.5 Schnittstellenübersicht

In   der   Schnittstellenübersicht   der   Systemarchitektur   werden   die   Schnittstellen   des   Systems   sowie   die
Schnittstellen seiner Systemelemente im Überblick dargestellt. Zur Beschreibung der Schnittstellenübersicht
wird jeweils nur die Kommunikation auf einer Ebene betrachtet:

➢ Auf Ebene des Systems werden die Schnittstellen der Systeme untereinander sowie zur Umgebung

beschrieben.

➢ Auf Ebene der Segment

 e   werden die Schnittstellen zwischen den Segmenten innerhalb des Systems

beschrieben.

➢ Auf Ebene der Einheiten werden die Schnittstellen zwischen den Einheiten innerhalb des Segments

beschrieben.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


C.1 Produkte

137

Umgebungsschnittstellen eines Systems oder eines Systemelements können beispielsweise zum Anwender
(Anwenderschnittstelle),   zur   Logistik   (Dokumentation)   oder   zu   anderen   im   Projekt   zu   entwickelnden
Systemen   (Mess-   und  Prüfgeräte,   Ersatzteile)   existieren.   Die   detaillierte   Beschreibung   der   Schnittstellen
erfolgt in den jeweiligen Spezifikationen der Systemelemente.

C.1.11.2.6 Übergreifender Datenkatalog

Systeme und Systemelemente tauschen zur Kommunikation Daten aus. Auf Hardwareebene handelt es sich
beispielsweise   um   Signale,   auf   Softwareebene   um   serialisierbare   Objekte   zum   Datentransport.   Im
übergreifenden Datenkatalog des Systems werden alle Datenstrukturen und Signale beschrieben, die an den
Schnittstellen ausgetauscht werden, sowie mögliche Wertebelegungen.

Daten und Signale des Systems dienen als Vorgaben für den Datenkatalog der  SW-Einheit
Daten- und Signalkatalog der HW-Einheiten.

 en     sowie den

Erzeugt

Datenbankentwurf für das System:
Datenbankentwurf (System)

C.1.11.2.7

Zu spezifizierende Systemelemente

Die Erstellung einer Spezifikation für ein Systemelement ist aufwändig und nicht in allen Fällen erforderlich.
Zur individuellen Anpassung des Spezifikationsaufwands an die Projekterfordernisse hat der Systemarchitekt
abhängig von den Vorgaben im Projekthandbuch und den Anforderungen die Möglichkeit festzulegen, für
welche Systemelemente eine Systemspezifikation zu erstellen ist.

Kriterien   für   die   Notwendigkeit   einer   Spezifikation   können   beispielsweise   sein:   die   Sicherheit   des
Systemelements, die Komplexität der Anforderungen an das Systemelement oder die Vorgaben zur Prüfung
aus   dem  QS-Handbuch  sowie   dem   jeweiligen   Implementierungs,   Integrations-   und   Prüfkonzept.   Für
Systemelemente,   die   einer   Prüfung   unterzogen   werden,   ist   in   jedem   Fall   eine   Systemspezifikation   zu
erstellen, da sie als Vorgabe der Prüfspezifikation Systemelement dient.

Wenn Systemelemente als nicht zu spezifizieren eingestuft werden, ist jeweils eine Begründung aufzuführen.

Erzeugt

Spezifikation des Systems:
Externe-Einheit-Spezifikation (Externe Einheit), Systemspezifikation (Segment;
System)

C.1.11.2.8

Informationssicherheits- und datenschutzkritische Systemelemente

Für   das   System   selbst   und   jedes   im   Thema  Dekomposition   des   Systems  identifizierte   Systemelement
(Segmente   und   Externe   Einheiten)   ist   festzulegen,   ob   das   Systemelement   als   kritisch   bzgl.
Informationssicherheit und Datenschutz einzustufen ist. Die Einstufung leitet sich aus den in der jeweiligen
Spezifikation beschriebenen Anforderungen sowie den vom Auftraggeber bereitgestellten Produkten

➢ Schutzbedarfsfeststellung,

➢ Vorgaben zur Informationssicherheit und

➢ Vorgaben zum Datenschutz

ab. Für jedes informationssicherheits- und datenschutzkritische Systemelement muss angegeben werden, ob
eine eigenständige Sicherheitskonzeption erforderlich ist oder die Sicherheitskonzeption des Gesamtsystems
ergänzt wird.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


138

 Referenz Produkte

Sofern für die Realisierung oder den Einsatz eines Systemelements die Vorgaben des Auftraggebers geändert
oder erweitert werden müssen, sind die notwendigen Änderungen und Erweiterungen mit einer Begründung
in   die  Erweiterung   der   Vorgaben   zur   Informationssicherheit  bzw.   zum   Datenschutz   aufzunehmen.  Alle
geplanten Änderungen und Erweiterungen müssen vorab mit dem Auftraggeber abgestimmt und von diesem
bewilligt werden.

Erzeugt

Berücksichtigung der Vorgaben zum Datenschutz auf Ebene des Systems:
Erweiterung der Vorgaben zum Datenschutz (Externe Einheit; Segment; System)
Berücksichtigung der Vorgaben zur Informationssicherheit auf Ebene des
Systems:
Erweiterung der Vorgaben zur Informationssicherheit (Externe Einheit; Segment;
System)
Erstellung einer Sicherheitskonzeption auf Ebene des Systems:
Sicherheitskonzeption (Externe Einheit; Segment; System)

C.1.11.2.9 Auswirkungen auf den IT-Betrieb

Entwurfsentscheidungen und der Einsatz externer Systemelemente können Auswirkungen auf den späteren
IT-Betrieb   haben.   Sofern   diese  Auswirkungen   nicht   mit   den  Vorgaben   zum   IT-Betrieb   übereinstimmen,
sondern Änderungen oder Erweiterungen erfordern, sind sie in Abstimmung mit dem Auftraggeber in der
Erweiterung der Vorgaben zum IT-Betrieb zu dokumentieren.

Für   das   System   selbst   und   jedes   im   Thema  Dekomposition   des   Systems  identifizierte   Systemelement
(Segmente und Externe Einheiten) ist festzulegen, ob für dessen Realisierung oder Einsatz die Vorgaben des
Auftraggebers   erweitert   werden   müssen.   Die   notwendigen   Erweiterungen   sind   aufzuführen   und   zu
begründen.

Erzeugt

Berücksichtigung der Vorgaben zum IT-Betrieb auf Ebene des Systems:
Erweiterung der Vorgaben zum IT-Betrieb (Externe Einheit; Segment; System)

C.1.11.2.10 Designabsicherung

Wurde ein Architekturentwurf gewählt und bis auf Einheitenebene ausgearbeitet, so ist sicherzustellen, dass
der   gewählte   Entwurf   Anforderungen   in   geeigneter   Weise   umsetzt.   Dies   wird   im   Rahmen   einer
Designverifikation geprüft und dokumentiert.

Im Thema Designabsicherung wird festgelegt, welche Methoden zur Designverifikation eingesetzt werden
und nach welchen Kriterien geprüft wird, ob das Design die Anforderungen abdeckt. Eine häufig eingesetzte
Methode   zur   Designverifikation  ist   die   Entwicklung  von  Prototypen.  Werden  diese   in  einem Vorprojekt
eingesetzt, haben die Anwender zusätzlich die Möglichkeit, anhand des Prototypen die Anforderungen auf
Vollständigkeit zu prüfen.

Vorgaben   zur   Designverifikation   sind   die   funktionalen   und   nicht-funktionalen   Anforderungen   der
Systemspezifikation  sowie   die   identifizierten   Architekturprinzipien.   Durchführung   und   Ergebnisse   der
Verifikation werden dokumentiert. Sie können eventuell eine Neubewertung der Entwurfsentscheidungen
sowie eine Überarbeitung der Architektur nach sich ziehen.

C.1.11.3 SW-Architektur

Für jede in der Systemarchitektur identifizierte  SW-Einheit  wird eine  SW-Architektur  erstellt. Ausgehend
von den funktionalen und nicht-funktionalen Anforderungen an die SW-Einheit ist  es  Aufgabe  des  SW-
 en   , eine geeignete SW-Architektur zu entwerfen. Das Produkt SW-Architektur dient dabei sowohl
Architekt
als Leitfaden zum Entwurf als auch zur Dokumentation der Entwurfsentscheidungen.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


C.1 Produkte

139

Wie   in   der   Systemarchitektur   werden   richtungweisende  Architekturprinzipien   festgelegt   und   mögliche
Entwurfsalternativen   untersucht.   Entsprechend   der   gewählten   Entwurfsalternative   wird   die   Zerlegung
(Dekomposition) der SW-Einheit in  SW-Komponente
 e    und Produkte vom Typ  Externes SW-
Modul beschrieben (vergleiche Produktstrukturierung).

 n  ,  SW-Modul

Beziehungen und Schnittstellen zwischen den Elementen und zur Umgebung werden identifiziert und im
Überblick   dargestellt.   Ein  Datenkatalog  der   an   den   Schnittstellen   ausgetauschten   Datenstrukturen   wird
erstellt.

Die gewählte Architektur wird hinsichtlich ihrer Eignung für das geforderte System bewertet. Offene Fragen
können beispielsweise im Rahmen einer prototypischen Entwicklung geklärt werden.

Der Entwurf der SW-Architektur kann Änderungen der Systemarchitektur nach sich ziehen. Abhängig von
den Vorgaben im Projekthandbuch wird die Änderung vom  Systemarchitekt
 en     geprüft und gegebenenfalls
direkt eingearbeitet. Im Einzelfall kann ein expliziter Änderungsantrag notwendig sein.

Hauptverantwortlicher für den Entwurf der SW-Architektur ist der SW-Architekt. Unterstützt wird er dabei
vom  SW-Entwickler  sowie   von   verschiedenen   Experten   zu   Einzelthemen   wie   Logistik,   Sicherheit   oder
Ergonomie.

Die SW-Architektur stellt das zentrale Dokument für die Erstellung weiterer Produkte dar. Sie legt alle SW-
 e    der SW-Einheit fest. Entsprechend ihren Vorgaben werden die jeweiligen
Komponenten und  SW-Modul
Elemente mit ihren Spezifikationen erstellt.

Verantwortlich

SW-Architekt

Mitwirkend

Aktivität

Methoden

Werkzeuge

Vorlagen

Erzeugt durch

SW-Entwickler, Systemarchitekt, Systemintegrator,
Informationssicherheitsverantwortlicher, Datenschutzverantwortlicher,
Betriebsverantwortlicher

SW-Einheit entwerfen

Designverifikation, Prototyping, Systemdesign

Modellierungswerkzeug

SW-Architektur(.odt|.doc)

Systementwurf:
Systemarchitektur (Dekomposition des Systems)

Entscheidungsrelevant
bei

Einheit(en) entworfen

C.1.11.3.1 Architekturprinzipien und Entwurfsalternativen

Die Beschreibung des Themas Architekturprinzipien und Entwurfsalternativen entspricht weitgehend dem
Thema Architekturprinzipien und Entwurfsalternativen der Systemarchitektur.

Zu   den   Architekturprinzipien   auf   SW-Ebene   zählen   beispielsweise   die   Entscheidung   für   ein
Programmierparadigma (objektorientiert, prozedural), die Entscheidung für eine Technologie (CORBA, EJB)
oder   auch   die   Vorgabe   für   eine   spezielle   Systemart   (verteilte   Internetanwendung,   Desktopanwendung).
Hilfestellung   bei   Entwurfsalternativen   für   die   SW-Entwicklung   geben   beispielsweise   Entwurfsmuster,
Musterarchitekturen und Entwurfsheuristiken.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland





140

 Referenz Produkte

C.1.11.3.2 Dekomposition der SW-Einheit

Im Rahmen der Dekomposition wird die statische Struktur der SW-Einheit festgelegt. Die statische Struktur
beschreibt die Zerlegung in SW-Komponenten und SW-Module. Das Entwurfsergebnis wird als Graph der
zu   realisierenden   SW-Elemente   sowie   ihrer   Beziehungen   untereinander   dokumentiert.   Zur   Darstellung
können   beispielsweise   Komponenten-   und/oder   Klassendiagramme   verwendet   werden.   Grundlage   der
Dekomposition sind die Anforderungen aus der SW-Spezifikation der SW-Einheit oder eines übergeordneten
Systemelements.   Randbedingungen   werden   durch   die   in   der   SW-Architektur   identifizierten
Architekturprinzipien sowie die getroffenen Entwurfsentscheidungen vorgegeben.

Für   Externe   SW-Module,   die   dem  Projekt   noch   nicht   vorliegen,   muss   dokumentiert   werden,   wie   deren
Beschaffung   erfolgt.   Bei   einer   Marktsichtung   von   Fertigprodukten   muss   auf   die   Verfügbarkeit   des
Quellcodes   geachtet   werden.   Fertigprodukte   ohne   verfügbaren  Quellcode   sollten  nur   mit   entsprechender
Begründung verwendet werden ("Comply-or-Explain"). Zudem sollten bei der Auswahl von Fertigprodukten
solche mit vorhandener IT-Sicherheitsprüfung (z.B. durch das BSI) bevorzugt werden.

Erzeugt

Beschaffung der Externen SW-Module der SW-Einheit:
Make-or-Buy-Entscheidung (Externes SW-Modul), Marktsichtung für
Fertigprodukte (Externes SW-Modul)
Elemente der SW-Einheit:
Externes SW-Modul, SW-Komponente, SW-Modul

C.1.11.3.3 Externe SW-Elemente

In diesem Thema werden alle zum Einsatz kommenden Fertigprodukte zusammenfassend aufgeführt. Hierzu
zählen auch eingesetzte Programmbibliotheken externer Anbieter. Jedes Fertigprodukt ist mit dessen Namen,
Version, Lizenz und Anbieter zu beschreiben. Ziel ist es, einen automatisierbaren Abgleich der verwendeten
externen   SW-Elemente   zu   ermöglichen,   um   diese   beispielsweise   regelmäßig   automatisiert   auf
bekanntgewordene Sicherheitslücken zu prüfen.

C.1.11.3.4 Schnittstellenübersicht

In   der   Schnittstellenübersicht   der  SW-Architektur  werden   die   Schnittstellen   der  SW-Einheit  sowie   die
Schnittstellen   ihrer  SW-Element
 e    im  Überblick   dargestellt.   Zur   Beschreibung   der   Schnittstellenübersicht
wird jeweils nur die Kommunikation auf einer Ebene betrachtet:

➢ Auf Ebene der SW-Einheit werden die Schnittstellen zu anderen Einheiten sowie zur Umgebung

beschrieben.

➢ Auf Ebene der  SW-Komponente

 n    werden die Schnittstellen zwischen den Komponenten innerhalb

der Einheit beschrieben.

➢ Auf   Ebene   der  SW-Modul
Komponente beschrieben.

 e    werden   die   Schnittstellen   zwischen   den   Modulen   innerhalb   der

Umgebungsschnittstellen eines SW-Elements können beispielsweise zum Anwender, zur Logistik oder zu
anderen im Projekt zu entwickelnden Systemen existieren. Die detaillierte Beschreibung der Schnittstellen
erfolgt in den jeweiligen Spezifikationen der SW-Elemente.

C.1.11.3.5 Datenkatalog

Im  Datenkatalog  der  SW-Architektur  werden   die   an   den   Schnittstellen   der  SW-Einheit  ausgetauschten
Datenstrukturen mit Attributen, Datentypen und Wertebereichen beschrieben. Jede Programmiersprache und
Plattform bietet hier eigene Lösungen, die bei der Definition zu berücksichtigen sind.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland




C.1 Produkte

Erzeugt

Datenbankentwurf für die SW-Einheit:
Datenbankentwurf (SW-Einheit)

141

C.1.11.3.6

Zu spezifizierende SW-Elemente

Die Erstellung einer Spezifikation für ein SW-Element ist aufwändig und nicht in allen Fällen erforderlich.
Zur individuellen Anpassung des Spezifikationsaufwands an die Projekterfordernisse hat der SW-Architekt,
abhängig von den Vorgaben im Projekthandbuch und den Anforderungen, die Möglichkeit festzulegen, für
welche SW-Elemente eine SW-Spezifikation zu erstellen ist.

Kriterien für die Notwendigkeit einer Spezifikation können beispielsweise sein: die Kritikalität des SW-
Elements,   die   Komplexität   der  Anforderungen   an   das   SW-Element   oder   die   Vorgaben   zur   Prüfung   im
Implementierungs-,   Integrations-   und   Prüfkonzept   SW.   Für   SW-Elemente,   die   einer   Prüfung   unterzogen
werden,   ist   in   jedem   Fall   eine   SW-Spezifikation   zu   erstellen,   da   sie   als   Vorgabe   der  Prüfspezifikation
Systemelement  dient. Für SW-Elemente, die als nicht zu spezifizieren eingestuft wurden, ist jeweils eine
Begründung aufzuführen.

Erzeugt

Spezifikation der SW-Einheit:
Externes-SW-Modul-Spezifikation (Externes SW-Modul), SW-Spezifikation
(SW-Einheit; SW-Komponente; SW-Modul)

C.1.11.3.7

Informationssicherheits- und datenschutzkritische SW-Elemente

Für die SW-Einheit selbst und jedes im Thema  Dekomposition der SW-Einheit  identifizierte SW-Element
(SW-Komponenten   und   (Externe)   SW-Module)   ist   festzulegen,   ob   das   SW-Element   als   kritisch   bzgl.
Informationssicherheit und Datenschutz einzustufen ist. Die Einstufung leitet sich aus den in der jeweiligen
Spezifikation beschriebenen Anforderungen sowie den vom Auftraggeber bereitgestellten Produkten

➢ Schutzbedarfsfeststellung,

➢ Vorgaben zur Informationssicherheit und

➢ Vorgaben zum Datenschutz

ab. Für jedes informationssicherheits- und datenschutzkritische SW-Element muss angegeben werden, ob
eine   eigenständige  Sicherheitskonzeption  erforderlich   ist   oder   die  Sicherheitskonzeption  eines
übergeordneten SW- oder Systemelements ergänzt wird.

Sofern für die Realisierung oder den Einsatz eines SW-Elements die Vorgaben des Auftraggebers geändert
oder erweitert werden müssen, sind die notwendigen Änderungen und Erweiterungen mit einer Begründung
in   die  Erweiterung   der   Vorgaben   zur   Informationssicherheit  bzw.   zum   Datenschutz   aufzunehmen.  Alle
geplanten Änderungen und Erweiterungen müssen vorab mit dem Auftraggeber abgestimmt und von diesem
bewilligt werden.

Erzeugt

Berücksichtigung der Vorgaben zum Datenschutz auf Ebene der SW-Einheit:
Erweiterung der Vorgaben zum Datenschutz (Externes SW-Modul; SW-Einheit;
SW-Komponente; SW-Modul)
Berücksichtigung der Vorgaben zur Informationssicherheit auf Ebene der
SW-Einheit:
Erweiterung der Vorgaben zur Informationssicherheit (Externes SW-Modul; SW-
Einheit; SW-Komponente; SW-Modul)
Erstellung einer Sicherheitskonzeption auf Ebene der SW-Einheit:
Sicherheitskonzeption (Externes SW-Modul; SW-Einheit; SW-Komponente; SW-
Modul)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

142

 Referenz Produkte

C.1.11.3.8 Auswirkungen auf den IT-Betrieb

Entwurfsentscheidungen und der Einsatz externer SW-Elemente können Auswirkungen auf den späteren IT-
Betrieb haben. Sofern diese Auswirkungen nicht mit den Vorgaben zum IT-Betrieb übereinstimmen, sondern
Änderungen   oder   Erweiterungen   erfordern,   sind   sie   in   Abstimmung   mit   dem   Auftraggeber   in   der
Erweiterung der Vorgaben zum IT-Betrieb zu dokumentieren.

Für die SW-Einheit selbst und jedes im Thema  Dekomposition der SW-Einheit  identifizierte SW-Element
(SW-Komponenten und (Externe) SW-Module) ist festzulegen, ob für dessen Realisierung oder Einsatz die
Vorgaben des Auftraggebers erweitert werden müssen. Die notwendigen Erweiterungen sind aufzuführen und
zu begründen.

Erzeugt

Berücksichtigung der Vorgaben zum IT-Betrieb auf Ebene der SW-Einheit:
Erweiterung der Vorgaben zum IT-Betrieb (Externes SW-Modul; SW-Einheit;
SW-Komponente; SW-Modul)

C.1.11.3.9 Designabsicherung

Wurde ein Architekturentwurf für die  SW-Einheit  gewählt und bis auf Modulebene ausgearbeitet, so ist
sicherzustellen, dass der gewählte Entwurf für die Anforderungen geeignet ist. Zur Designabsicherung von
 en     stehen verschiedene Methoden zur Verfügung. Zwei häufig eingesetzten Methoden sind
SW-Architektur
beispielsweise   die   Architekturevaluierung   mit   szenario-basierten   Methoden   und   die   prototypische
Entwicklung von Systemteilen. Durchführung und Ergebnisse der Designabsicherung werden dokumentiert.
Sie   können  gegebenenfalls   eine   Neubewertung   der   Entwurfsentscheidungen  und  eine   Überarbeitung   der
Architektur nach sich ziehen.

C.1.11.4 Implementierungs-, Integrations- und Prüfkonzept System

Das  Implementierungs-,   Integrations-   und   Prüfkonzept   System  definiert   den   Realisierungs-   und
Fertigstellungsprozess   für   ein   System.   Es   gibt   insbesondere   dem  Systemintegrator  und   dem  Prüfer
Richtlinien für ihre Aufgaben.

Das Konzept beschreibt detailliert Vorgehen, Werkzeuge und Umgebungen für Installation, Integration und
Prüfung von Systemelementen bis hin zum System. Grundlage der Integration auf Systemebene sind die im
Rahmen der SW- und HW-Entwicklung erstellten Einheiten sowie Implementierungen der in der Architektur
identifizierten   Externen   Einheiten.  Abhängig   von   der   Komplexität   des   Realisierungsprozesses   oder   der
Heterogenität des zu entwickelnden Systems kann das Konzept die gesamte Systementwicklung abdecken,
oder sich ausschließlich auf die oberen Hierarchieebenen bis zur Einheit konzentrieren. Zur Realisierung der
HW- und SW-Einheit

 en    wird im zweiten Fall jeweils ein eigenes Konzept erstellt.

Inhaltlich   ist   das   Implementierungs-,   Integrations-   und   Prüfkonzept   System   konsistent   zur   jeweiligen
Architektur zu halten. Die dort getroffenen Entwurfsentscheidungen sind in geeigneter Weise umzusetzen.
Bezüglich   Organisation   und   Randbedingungen   orientiert   sich   das   Konzept   an   den   Vorgaben   im
Projekthandbuch. Zur zeitlichen Planung von Integration und Prüfung ist das Konzept mit dem Integrations-
und Prüfplan Systemelemente im Projektplan abzustimmen.

Verantwortlich   für   die   Erstellung   des   Konzepts   ist   der  Systemarchitekt.   Unterstützt   wird   er   vom
Systemintegrator, der letztendlich die Verantwortung für das fertig entwickelte System trägt.

Für   Integration   und   Prüfung   ist   eine   ausgewogene   Strategie   bezüglich   Kundenvorgaben,   vorhandenen
Integrations- und Nachweismitteln und der Minimierung von Redundanzen im Hinblick auf die zu führenden
Nachweise zu berücksichtigen.

Die Beschreibung der zu verwendenden Umgebungen erfolgt üblicherweise in diesem Konzept. Wird eine
Umgebung   jedoch   zur   langfristigen   Unterstützung   des   Systemlebenszyklus   benötigt,   ist   sie   als
eigenständiges System zu realisieren.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland



C.1 Produkte

143

Abhängig von den Vorgaben zur Prüfung werden die Prüfprodukte für die einzelnen Systemelemente erstellt.

Verantwortlich

Systemarchitekt

Mitwirkend

Aktivität

Methoden

Werkzeuge

Vorlagen

Erzeugt durch

Inhaltlich abhängig

Prüfer, QS-Verantwortlicher, SW-Architekt, Systemintegrator

Implementierungs-, Integrations- und Prüfkonzept System erstellen

Systemdesign, Test

Anforderungsmanagement, Integrierte Entwicklungsumgebung, KM-Werkzeug,
Konstruktion/Simulation, Modellierungswerkzeug

Implementierungs-, Integrations- und Prüfkonzept System(.odt|.doc)

Systementwurf:
Pflichtenheft (Gesamtsystementwurf) (Dekomposition des Gesamtsystems)

Planung der Prüfung von Systemelementen:
Projektplan
Vorgaben zur Prüfung der Systemelemente:
QS-Handbuch

Entscheidungsrelevant
bei

System entworfen

C.1.11.4.1 Vorgehen zur Realisierung und Realisierungsumgebung

Die Realisierung eines Systemelements sollte in einer geeigneten Umgebung im Rahmen eines definierten
Realisierungsprozesses erfolgen. Auf Systemebene spielt dieser Aspekt jedoch nur eine untergeordnete Rolle.
Die Realisierungstätigkeit erfolgt hauptsächlich auf HW- beziehungsweise SW-Ebene.

C.1.11.4.2 Vorgehen zur Integration und Integrationsbauplan

Das Vorgehen zur Integration legt fest, in welcher Umgebung und mit welchen Werkzeugen die Integration
zu   erfolgen   hat.   Der   Integrationsbauplan   definiert   die   Integrationsarchitektur   und   die   Reihenfolge   der
Integration.   Er   legt   zu   den   Systemelementtypen   der   Architekturen   die   konkret   zu   realisierenden
Systemelementexemplare fest und bestimmt die Integrationsreihenfolge.

Für   jede   HW-   und  SW-Einheit  wird   festgelegt,   ob   die   Erstellung   eines   separaten   Implementierungs-,
Integrations-   und   Prüfkonzepts   notwendig   ist.  Abhängig   vom   Umfang   und   der   Komplexität   kann   das
Konzept des übergeordneten Systems den Realisierungsprozess auch bereits bis auf Modulebene abbilden.

Erzeugt

Realisierung des Systems:
Implementierungs-, Integrations- und Prüfkonzept SW (SW-Einheit)

C.1.11.4.3 Vorgehen zur Installation und Zielumgebungen

Teil   des   Entwicklungsprozesses   ist   die   Identifikation   der   geforderten   Zielumgebungen   sowie   die
Beschreibung   des   Installationsprozesses.   Es   sind   alle   Zielumgebungen,   in   denen   das   System   in   den
verschiedenen   Entwicklungsphasen   zu   laufen   hat,   zu   identifizieren   und   die   Installationsprozeduren
festzulegen. Vorgaben für die zu unterstützenden Zielumgebungen werden im Projekthandbuch definiert.
Häufig vorgegebene Zielumgebungen sind neben der Entwicklungsumgebung eine separate Prüfumgebung
sowie eine Integrationsumgebung zur Simulation der endgültigen Zielplattform.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

144

 Referenz Produkte

Für jede identifizierte Zielumgebung werden das Vorgehen zur Installation sowie die benötigten Werkzeuge
beschrieben. Die Beschreibung der Installation auf der Zielplattform beruht auf den Inhalten dieses Themas.
Sie wird im Rahmen der Nutzungsdokumentation erstellt und an den Auftraggeber ausgeliefert.

C.1.11.4.4 Vorgehen zur Prüfung und Prüfstrategie

Für   alle   Systemelemente   sind   eine   allgemeine   Prüfstrategie   und   ein   konkreter   Prüfprozess   festzulegen.
Hierbei   spielen   Faktoren   wie   Wirtschaftlichkeit,   Verfügbarkeit   der   Prüfumgebungen,   Prüfbarkeit   oder
Prüfdauer eine wichtige Rolle.

Der Prüfprozess legt Algorithmen, Prüfwerkzeuge und Prüfmethoden fest, die zur Durchführung der Prüfung
einzusetzen   sind.   Die   konkrete   Ausgestaltung   des   Prüfvorgehens   erfolgt   in   den   jeweiligen
Prüfspezifikationen der Systemelemente.

Die   Prüfstrategie   wird   aus   den   Vorgaben   in   Projekthandbuch   und  QS-Handbuch  abgeleitet.   Sie   legt
allgemeine Richtlinien und Kriterien fest, nach denen Prüfungen an Systemelementen durchzuführen sind.
Insbesondere   sind   in   der   Prüfstrategie   die   vom   Auftraggeber   explizit   geforderten   Nachweise   und
Randbedingungen zu berücksichtigen.

Die   Prüfstrategie   sollte   speziell   hinsichtlich   Redundanz   und   Risikominimierung   sowie   hinsichtlich   der
Verfügbarkeit von bereits existierenden Hilfsmitteln betrachtet werden.

C.1.11.4.5

Zu prüfende Systemelemente

Die Prüfung eines Systemelements ist aufwändig und nicht in allen Fällen erforderlich. Zur individuellen
Anpassung des Aufwands an die Projekterfordernisse hat der Systemarchitekt, abhängig von den Vorgaben
im   Projekthandbuch   und   der   festgelegten   Prüfstrategie,   die   Möglichkeit   festzulegen,   für   welche
Systemelemente eine Prüfung durchzuführen ist.

Kriterien für die Notwendigkeit einer Prüfung können beispielsweise die Sicherheitsaspekte und Komplexität
des Systemelements sowie seine zentrale Rolle im System sein. Für Systemelemente, die als nicht zu prüfen
eingestuft wurden, ist jeweils eine Begründung aufzuführen.

Erzeugt

Prüfung des Systems:
Prüfprotokoll Systemelement (Externe Einheit; Segment; System), Prüfprozedur
Systemelement (Externe Einheit; Segment; System), Prüfspezifikation
Systemelement (Externe Einheit; Segment; System)

C.1.11.5 Implementierungs-, Integrations- und Prüfkonzept SW

Das
 Implementierungs-,   Integrations-   und   Prüfkonzept   SW  definiert   den   Entwicklungs-   und
Fertigstellungsprozess für eine SW-Einheit des Systems. Es gibt insbesondere dem SW-Entwickler und dem
Prüfer Richtlinien für ihre Aufgaben.

Das   Konzept   beschreibt   detailliert   Programmierkonventionen,   Vorgaben   bezüglich   Dokumentation,
Vorgehen, Werkzeuge und Umgebungen für Implementierung, Installation, Integration und Prüfung der SW-
Element
  Werkzeuge   und
Programmiersprachen ein.

  die   Beschreibung   der   Entwicklungsumgebung,

  Dies   schließt

 e  .

Inhaltlich ist das Implementierungs-, Integrations- und Prüfkonzept SW konsistent zur  SW-Architektur  zu
halten.   Die   dort   getroffenen   Entwurfsentscheidungen   sind   in   geeigneter  Weise   umzusetzen.   Hinsichtlich
Organisation und Randbedingungen orientiert sich das Konzept an den Vorgaben im Projekthandbuch.

Verantwortlich   für   die   Erstellung   des   Konzepts   ist   der  SW-Architekt.   Unterstützt   wird   er   vom   SW-
Entwickler, der letztendlich die Verantwortung für die fertig entwickelte SW-Einheit trägt. Abhängig von den
Vorgaben zur Qualitätssicherung werden die Prüfprodukte für die einzelnen SW-Elemente erstellt.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


C.1 Produkte

145

Verantwortlich

SW-Architekt

Mitwirkend

Aktivität

Methoden

Werkzeuge

Vorlagen

Erzeugt durch

Inhaltlich abhängig

Prüfer, QS-Verantwortlicher, SW-Entwickler

Implementierungs-, Integrations- und Prüfkonzept SW erstellen

Review, Test

Compiler, KM-Werkzeug

Implementierungs-, Integrations- und Prüfkonzept SW(.odt|.doc)

Systementwurf:
Implementierungs-, Integrations- und Prüfkonzept System (Vorgehen zur
Integration und Integrationsbauplan)

Planung der Prüfung von Systemelementen:
Projektplan
Vorgaben zur Prüfung der Systemelemente:
QS-Handbuch

Entscheidungsrelevant
bei

Einheit(en) entworfen

C.1.11.5.1 Vorgehen zur Realisierung und Realisierungsumgebung

Die   Realisierung   einer  SW-Einheit  sollte   in   einer   geeigneten   Umgebung   im   Rahmen   eines   definierten
sicheren Entwicklungsprozesses (Secure Software Development Life Cycle, SSDLC) erfolgen. Konkret sind
die   Entwicklungsumgebung   sowie   Werkzeuge   wie   Compiler,   Frameworks   oder   Kryptografiehilfsmittel
festzulegen.   Das  Vorgehen   zur   Realisierung   sollte   mit   geeigneten  Werkzeugen   weitgehend   automatisiert
werden   und   Vorgaben   zu   Übersetzungs-   und   Laufzeiteinstellungen,   die   Festlegung   relevanter
Codebestandteile,   das   Übersetzen   von   Quellcode   sowie   das   Verpacken   in   die   zur   Ausführung   bzw.
Integration notwendige Form enthalten.

Es ist zu beschreiben, wer auf welches Werkzeug Zugriff hat und wo es betrieben wird. Dabei ist zu prüfen,
ob   der   Betriebsort   von   Werkzeugen   entsprechend   der   Vorgaben   zum   Datenschutz   oder   zur
Informationssicherheit auf Deutschland oder EU-Mitgliedsstaaten einzuschränken ist.

Wird eine Entwicklungsumgebung langfristig zur Unterstützung des Systems in seinen Lebenszyklusphasen
benötigt, ist hierfür ein eigenständiges System zu erstellen.

C.1.11.5.2 Vorgehen zur Integration und Integrationsbauplan

Die   Architektur   einer  SW-Einheit  legt   fest,   welche   SW-Elementtypen   benötigt   werden   und   wie   der
strukturelle Aufbau der SW-Einheit aussieht. Zur Integrationsplanung sind die konkret zu entwickelnden
 e    und die Reihenfolge der Integration aus der  SW-Architektur  abzuleiten und ein geeigneter
SW-Element
Integrationsprozess zu definieren.

Das Vorgehen zur Integration legt fest, in welcher Umgebung und mit welchen Werkzeugen die Integration
zu   erfolgen   hat.   Dabei   muss   sichergestellt   sein,   dass   Werkzeuge   der   Realisierungs-   und   der
Integrationsumgebung zusammenpassen und einander in geeigneter Weise ergänzen. Der Integrationsbauplan
definiert die Integrationsarchitektur und die Reihenfolge der Integration. Er legt zu den SW-Elementtypen
der   SW-Architektur   die   konkret   zu   realisierenden   SW-Elemente   fest   und   bestimmt   die
Integrationsreihenfolge.   Noch   nicht   realisierte   SW-Elemente,   die   von   anderen   SW-Elementen   benötigt
werden, sollten bis zu ihrer Realisierung durch Fassaden-Objekte (Mock-Objekte) ersetzt werden.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


146

 Referenz Produkte

C.1.11.5.3 Vorgehen zur Installation und Zielumgebungen

Teil des Entwicklungsprozesses ist die Identifikation der geforderten Zielumgebungen und die Beschreibung
des  Installationsprozesses.  Es  sind alle  Zielumgebungen,  in  denen die  SW-Einheit  in  den  verschiedenen
Entwicklungsphasen zu laufen hat, zu identifizieren und die Installationsprozeduren festzulegen. Vorgaben
für die zu unterstützenden Zielumgebungen werden im Projekthandbuch definiert.

In   der   SW-Entwicklung   werden   häufig   eine   Prüfumgebung   zur   Durchführung   von   Prüfungen   und   eine
Integrationsumgebung zur Simulation der endgültigen Zielplattform vorgegeben.

Für jede identifizierte Zielumgebung sind das Vorgehen zur Installation und die benötigten Werkzeuge zu
beschreiben. Die Beschreibung der Installation auf der Zielplattform beruht auf den Inhalten dieses Themas.
Sie   wird   im   Rahmen   der  Nutzungsdokumentation  in   der   Logistik   erstellt   und   an   den   Auftraggeber
ausgeliefert.

C.1.11.5.4 Vorgehen zur Prüfung und Prüfstrategie

Für alle SW-Elemente sind eine allgemeine Prüfstrategie und ein konkreter Prüfprozess festzulegen. Hierbei
spielen Faktoren wie Wirtschaftlichkeit, Verfügbarkeit der Prüfumgebung, Prüfbarkeit oder Prüfdauer eine
wichtige Rolle.

Der   Prüfprozess   legt   Algorithmen,   Prüfwerkzeuge   und   Prüfmethoden   fest,   die   zur   Durchführung   der
Prüfungen   einzusetzen   sind.   Die   konkrete   Ausgestaltung   des   Prüfvorgehens   erfolgt   in   den   jeweiligen
Prüfspezifikationen der SW-Elemente. Dabei sollten folgende Aspekte berücksichtigt werden:

➢ Entwurf   und   Änderungen   der   Architektur   sollten   von   SW-/Systemarchitekt

 en     mit   fundierten
Kenntnissen   zur   Informationssicherheit   gegengelesen   werden.   Zudem   sollten   regelmäßig   Code
Reviews   (z.B.   nach   IEEE   1028)   zur  Aufdeckung   von   Qualitätsmängeln   und   Sicherheitslücken
durchgeführt werden.

➢ Die Einhaltung von Architekturvorgaben und Programmierrichtlinien und die Vermeidung typischer
Fehler und Schwachstellen sollte mit entsprechenden Werkzeugen überwacht werden. Beispiele für
solche Werkzeuge sind SonarQube, FindBugs, Linter, PMD, Metasploit.

➢ Für alle Systemelemente sollten (z.B. nach ISO/IEC/IEEE 29119) Vorgaben zur Abdeckung durch
Unit-Tests   und   zur  Abdeckung   durch   Tests   mit   ungültigen,   unerwarteten   oder   zufälligen   Daten
(Fuzzing)   erstellt   werden.   Unit-Test   Frameworks   sind   für   alle   gängigen   Programmiersprachen
verfügbar   (siehe  https://en.wikipedia.org/wiki/List_of_unit_testing_frameworks).   Frei   und   im
Quelltext verfügbare Werkzeuge für Fuzzing / Random Testing sind beispielsweise w3af, skipfish,
wfuzz und wapiti sowie mit Einschränkungen nessus und burp suite.

➢ Für   die   in   der  Sicherheitskonzeption  festgelegten   Maßnahmen   sollten   Testverfahren   festgelegt

werden, die deren Wirksamkeit überprüfen.

➢ Mindestens für Informationssicherheitsmaßnahmen, die ein hohes Risiko verringern sollen, und für
Bestandteile mit erhöhtem Schutzbedarf sollten Vorgaben für Penetrationstests festgelegt werden.
Für deren Durchführung durch Dritte muss das erlaubte Vorgehen exakt definiert werden.

➢ Der jeweils aktuelle Stand des Systems sollte automatisiert übersetzt, verpackt und getestet werden.

Dazu sollte eine entsprechende Build- und Testumgebung bereitgestellt werden.

➢ Die Testergebnisse sollten regelmäßig ausgewertet und Maßnahmen zur Verbesserung der Qualität

und der Informationssicherheit abgeleitet werden.

Die   Prüfstrategie   wird   aus   der   Prüfstrategie   des   übergeordneten   Implementierungs-,   Integrations-   und
Prüfkonzepts, sowie aus den Vorgaben im Projekthandbuch und QS-Handbuch abgeleitet. Sie legt allgemeine
Richtlinien und Kriterien fest, nach denen Prüfungen an SW-Elementen durchzuführen sind. Insbesondere
sind in der Prüfstrategie die vom Auftraggeber explizit geforderten Nachweise und Randbedingungen zu
berücksichtigen.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


C.1 Produkte

147

Die   Prüfstrategie   sollte   speziell   hinsichtlich   Redundanz   und   Risikominimierung   sowie   hinsichtlich   der
Verfügbarkeit von bereits existierenden Hilfsmitteln betrachtet werden.

C.1.11.5.5

Zu prüfenden SW-Elemente

Die   Prüfung   eines  SW-Element
 s    ist   aufwändig  und   nicht   in  allen   Fällen  erforderlich.   Zur   individuellen
Anpassung des Aufwandes an die Projekterfordernisse hat der SW-Architekt, abhängig von den Vorgaben im
Projekthandbuch und der festgelegten Prüfstrategie, die Möglichkeit festzulegen, für welche SW-Elemente
der  SW-Einheit  eine   Prüfung   durchzuführen   ist.   Kriterien   für   die   Notwendigkeit   einer   Prüfung   können
beispielsweise die Kritikalität und Komplexität des SW-Elements, sowie seine zentrale Rolle innerhalb der
SW-Einheit sein. Für SW-Elemente, die als nicht zu prüfen eingestuft wurden, ist jeweils eine Begründung
aufzuführen.

Erzeugt

Prüfung der SW-Einheit:
Prüfprotokoll Systemelement (Externes SW-Modul; SW-Einheit; SW-
Komponente; SW-Modul), Prüfprozedur Systemelement (Externes SW-Modul;
SW-Einheit; SW-Komponente; SW-Modul), Prüfspezifikation Systemelement
(Externes SW-Modul; SW-Einheit; SW-Komponente; SW-Modul)

C.1.11.6 Sicherheitskonzeption

Die  Sicherheitskonzeption  enthält eine modellhafte Beschreibung des zu entwickelnden Systemelements,
eine   Bewertung   seines   Schutzbedarfs,   eine  Auflistung   möglicher   Bedrohungen,   eine  Abschätzung   und
Bewertung   identifizierter   Risiken   sowie   eine   Dokumentation   der   Risikobehandlung.   Sie   beschreibt
vorhandene   und   umzusetzende   Informationssicherheits-Maßnahmen   und   bewertet   deren   Fähigkeit   zur
Reduzierung von Bedrohungen und Risiken.

Eine Sicherheitskonzeption wird immer für ein konkretes Systemelement erstellt. Hierbei wird zwischen
einer Sicherheitskonzeption für

➢ das Gesamtsystem,

➢ ein System, ein Segment oder eine Externe Einheit,

➢ eine SW-Einheit, eine SW-Komponente oder ein (Externes) SW-Modul

unterschieden.

Die   Produktexemplare   weisen   eine   identische   Themenstruktur   auf   und   unterscheiden   sich   in   der
Betrachtungsebene und der Detailtiefe. Es ist daher möglich, innerhalb einer  Sicherheitskonzeption  auch
mehrere   Systemelemente   zu   betrachten   bzw.   die  Sicherheitskonzeption  eines   übergeordneten
Systemelements fortzuschreiben.

Ob   eine  Sicherheitskonzeption
für   das   Gesamtsystem   erforderlich   ist,   wird   im  Pflichtenheft
(Gesamtsystementwurf) festgelegt. Sofern diese erstellt wird, ist sie zum Entscheidungspunkt Gesamtsystem
entworfen vorzulegen und

➢ analysiert,   ob   die   Inhalte   des   Pflichtenhefts   den   Nicht-funktionalen   Anforderungen   bzgl.
Informationssicherheit   und   Datenschutz   aus   dem   Lastenheft   und   der   Schutzbedarfsfeststellung
entsprechen,

➢ stellt die notwendigen Maßnahmen dar, die zu diesem Zeitpunkt bereits ersichtlich sind,

➢ berücksichtigt die vom Auftraggeber geforderten Maßnahmen aus dem Lastenheft sowie aus den

Vorgaben zur Informationssicherheit / zum Datenschutz / zum IT-Betrieb und

➢ beschreibt die Auswirkungen der Maßnahmen auf sonstige Produkte (z.B. neue Anforderungen im

Pflichtenheft).

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


148

 Referenz Produkte

Die Sicherheitskonzeption
 en    auf Systemebene (für Systeme, Segmente und Externe Einheiten) verfeinern die
Sicherheitskonzeption  des   Gesamtsystems.   Ob   und   für   welches   Systemelement   eine   eigenständige
Sicherheitskonzeption  erstellt   wird   oder   ob   ggf.   die  Sicherheitskonzeption  des   Gesamtsystems
 en    der Systemebene
fortgeschrieben wird, ist in der Systemarchitektur festzulegen. Die Sicherheitskonzeption
sind zum Entscheidungspunkt System entworfen vorzulegen.

 en     auf Softwareebene (für SW-Einheiten, SW-Komponenten und (Externe) SW-
Die  Sicherheitskonzeption
 en     der Systemebene. Ob und für welches SW-Element eine
Module) verfeinern die  Sicherheitskonzeption
eigenständige  Sicherheitskonzeption  erstellt   wird   oder   ob   ggf.   die  Sicherheitskonzeption  eines
übergeordneten SW- oder Systemelements fortgeschrieben wird, ist in der SW-Architektur festzulegen. Die
 en    der Softwareebene sind zum Entscheidungspunkt Einheit(en) entworfen vorzulegen.
Sicherheitskonzeption

 en     sind   deren   Inhalte   auf   Korrektheit,
Bei   der   Erstellung   und   Fortschreibung   der  Sicherheitskonzeption
Konsistenz   und   Vollständigkeit   bezüglich   der   jeweiligen   Modellierungstiefe   zu   überprüfen   und   ggf.
anzupassen.   Die   enthaltenen   Informationssicherheitsmaßnahmen   sind   bei   der   Realisierung   des
Systemelements zu berücksichtigen und umzusetzen. Ergeben sich daraus neue Anforderungen, müssen diese
im Pflichtenheft ergänzt und ggf. ein Vertragszusatz geschlossen werden.

Die   betreffende  Sicherheitskonzeption
ist   bei   allen   Änderungen   eines   Systemelements,   der
Rahmenbedingungen oder der Bedrohungslage auf Anpassungsbedarf zu prüfen und ggf. fortzuschreiben.
 Sicherheitskonzeption  auf
Informationssicherheitsmaßnahmen   sind   bei   einer   Fortschreibung   der
Anpassungsbedarf   zu   prüfen   und   müssen   ggf.   geändert   oder   ergänzt   werden.   Dies   kann   zu   weiteren
Systemänderungen führen, die wiederum auf ihre Auswirkungen bzgl. der Sicherheitskonzeption zu prüfen
sind.

Verantwortlich

Mitwirkend

Aktivität

Werkzeuge

Vorlagen

Erzeugt durch

Informationssicherheitsverantwortlicher

SW-Architekt, Systemarchitekt, Datenschutzverantwortlicher,
Betriebsverantwortlicher

Sicherheitskonzeption erstellen

Tools zum IT-Grundschutz

Sicherheitskonzeption(.odt|.doc)

Systementwurf:
Pflichtenheft (Gesamtsystementwurf) (Nicht-funktionale Anforderungen), SW-
Architektur (Informationssicherheits- und datenschutzkritische SW-Elemente),
Systemarchitektur (Informationssicherheits- und datenschutzkritische
Systemelemente)

Inhaltlich abhängig

Berücksichtigung der Informationssicherheit und des Datenschutzes bei der
Systemerstellung:
Pflichtenheft (Gesamtsystementwurf)

Entscheidungsrelevant
bei

Gesamtsystem entworfen, System entworfen, Einheit(en) entworfen

C.1.11.6.1 Verwendete Methode

Hier wird die zur Durchführung der Risikoanalyse benutzte Methode beschrieben oder durch Angabe einer
Quelle für  eine  etablierte Methode definiert (z.B.  BSI-Standard 200-2:  IT-Grundschutz-Vorgehensweise).
Weiterhin   wird   offengelegt,   welche   Bewertungsgrundlagen   verwendet   werden.   Beispielsweise   werden
mögliche Schadensszenarien und deren Bewertung aufgelistet.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland







C.1 Produkte

C.1.11.6.2 Vorgaben

149

In diesem Thema werden alle Vorgaben zur Informationssicherheit, zum Datenschutz und zum IT-Betrieb
aufgeführt, die in dieser Sicherheitskonzeption berücksichtigt werden müssen.

C.1.11.6.3 Annahmen

In diesem Thema  werden Annahmen zum Systemelement und seiner Umgebung und zu dessen Risiken,
Bedrohungen und Maßnahmen dokumentiert. Die Annahmen beziehen sich auf relevante Eigenschaften der
Elemente der betrachteten Ebene, deren Beziehungen untereinander, deren Abgrenzung voneinander und
deren Kontext. Beispiele für solche Annahmen sind

➢ der   Betrieb   eines   Systemelements   in   einer   Umgebung,   die   es   vor   dem   physikalischen   Zugriff

unbefugter Personen schützt,

➢ die   Beschreibung   eines   Angreifermodells   einschließlich   der   Fähigkeiten   und   Voraussetzungen

möglicher Angreifer,

➢ sicherheitsrelevante Eigenschaften vorgesehener externer Systemelemente, die bei deren Auswahl

und Test berücksichtigt werden müssen.

Solche  Annahmen   können  Anforderungen  an  Dritte   zur   Folge   haben,   die   an   diese   zur   Umsetzung   oder
Gewährleistung weitergegeben werden müssen, beispielsweise

➢ Anforderungen an den späteren Betrieb des Systemelements, die in das Produkt   Erweiterung der

Vorgaben zum IT-Betrieb einfließen müssen,

➢ Annahmen bezüglich einer vorgesehenen Software-Bibliothek, die durch analytische Maßnahmen
zur Qualitätssicherung verifiziert oder validiert und in entsprechende QS-Prozesse aufgenommen
werden müssen.

C.1.11.6.4 Systembeschreibung aus Sicht der Informationssicherheit

In diesem Thema   wird  das   betrachtete   Systemelement   aus   Sicht   der   Informationssicherheit  beschrieben,
insbesondere dessen wesentliche Funktionalitäten, die Infrastruktur und relevante Datenflüsse. Das Ziel ist
ein  Modell   der   Funktionsweise   des   Systemelements   mit   einer   handhabbaren  Komplexität   als   Grundlage
weiterer  Analysen.   Die   Infrastruktur   kann   bei   Bedarf   auf   einzelne   Hardware-   oder   Software-Bausteine
verfeinert werden.

Bei   der   Modellierung   werden   Informationssicherheitsmaßnahmen   und   deren   Abhängigkeiten   von
Schutzzielen   berücksichtigt.   Beispielsweise   muss   für   eine   verschlüsselte   Verbindung   festgelegt   werden,
welche   Elemente   der   Infrastruktur   Kenntnis   des   Schlüsselmaterials   haben,   und   dieses   Schlüsselmaterial
entsprechend in die Modellierung aufgenommen werden.

C.1.11.6.5 Schutzbedarf

In   diesem   Thema   wird   der   Schutzbedarf   des   zu   entwickelnden   Systemelements   basierend   auf   der
Schutzbedarfsfeststellung   und   den   Schutzbedarfskategorien   des   Auftraggebers   sowie   den   modellierten
Funktionen,   Daten  und  Infrastrukturelementen  ermittelt.   Der   Schutzbedarf   charakterisiert   schützenswerte
Eigenschaften des zu entwickelnden Systemelements und die Schadensszenarien, die bei Verletzung dieser
Eigenschaften auftreten können.

Für   jedes   Modellelement   wird   geprüft,   ob   die   Verletzung   eines   Grundwerts   der   Informationssicherheit
(üblicherweise Vertraulichkeit, Verfügbarkeit, Integrität) zu einem erkennbaren Schaden führt. Das Ergebnis
der   Prüfung   wird   dokumentiert   und   ein   erkennbarer   Schaden   bewertet.   Die   Gesamtheit   der   hinsichtlich
möglicher   Schadensszenarien   bewerteten   Schutzziele   ergibt   den   Schutzbedarf   des   zu   entwickelnden
Systemelements. Zur Verbesserung der Übersichtlichkeit können die dokumentierten Schutzziele passend
zusammengefasst werden.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

150

 Referenz Produkte

Bei der Ermittlung des Schutzbedarfs sind alle relevanten Stakeholder zu berücksichtigen. Der Schutzbedarf
muss mit der Schutzbedarfsfeststellung des Auftraggebers abgeglichen werden. Abweichungen bringt der
Auftragnehmer in das Problem- und Änderungsmanagement ein. Sie können zu Vertragszusätzen führen.

C.1.11.6.6 Bedrohungen

In diesem Thema werden basierend auf dem Modell des Systemelements mögliche Bedrohungen ermittelt.
Hierfür werden sowohl mögliche Angriffe auf die Infrastruktur und Datenflüsse ermittelt, als auch daraus
resultierende   Verletzungen   von   Schutzzielen   dokumentiert.   Die   Bedrohungen   werden   hinsichtlich   der
Umsetzbarkeit durch Angreifer bewertet.

C.1.11.6.7

Informationssicherheitsmaßnahmen

In   diesem   Thema   werden   die   für   das   zu   entwickelnde   Systemelement
  relevanten
Informationssicherheitsmaßnahmen   dokumentiert   und   analog   den   Bedrohungen   hinsichtlich   der
Schwierigkeit bewertet, die jeweilige Maßnahme zu brechen. Die Maßnahmen werden hierbei für die spätere
Umsetzbarkeit klassifiziert, z.B. als technisch, organisatorisch, personell oder materiell. Es werden sowohl
Bestandsmaßnahmen der verwendeten Infrastruktur als auch neu umzusetzende Maßnahmen erfasst.

C.1.11.6.8 Risikoabschätzung, Risikobehandlung und Restrisiken

In   diesem   Thema   werden   die   durch   die   Bedrohungen   entstehenden   Risiken   abgeschätzt   und   für   jedes
abgeschätzte   Risiko   die   Risikobehandlung   festgelegt   (vgl.   ISO/IEC   27005).   Hierfür   werden   die
Schwierigkeit   der   Umsetzung   einer   Bedrohung,   die   dagegenwirkenden   Maßnahmen   sowie   die
Schadensszenarien bei Verletzung der bedrohten Schutzziele herangezogen. Als Maßstab dient die Definition
der Schutzbedarfskategorien des Auftraggebers. Das jeweilige Risiko wird entweder

➢ akzeptiert,

➢ übertragen (z.B. Abdeckung des Schadensfalls durch eine Versicherung),

➢ vermieden (durch eine Änderung des Systemelements, die das Risiko beseitigt) oder

➢ verringert   (durch   eine   dem   Systemelement   zugeordnete   Maßnahme,   die   das   Risiko   auf   ein
akzeptables   Maß   senkt.   Die   Verringerung   des   Risikos   durch   Maßnahmen   muss   durch   eine
Fortschreibung der Sicherheitskonzeption dargelegt werden.).

Risiken,   die   nach  dem  Maßstab  des  Auftraggebers   ein  erhöhtes   Schadenspotential   haben  und  durch  die
Risikobehandlung nicht vermieden werden können, sind Restrisiken, auf die deutlich hingewiesen werden
sollte.

Auftraggeber   und   Auftragnehmer   stimmen   sich   im   Rahmen   der   Risikodiskussion   über   die   jeweilige
Risikobehandlung   ab.   Maßgeblich   ist   die   jeweilige   Entscheidung   des  Auftraggebers,   die   ebenfalls   hier
dokumentiert und spätestens in der Abnahmeerklärung von ihm bestätigt wird.

C.1.11.7 Erweiterung der Vorgaben zur Informationssicherheit

Der  Auftragnehmer   leitet   aus   der  Schutzbedarfsfeststellung,   dem   Pflichtenheft,   der   System-   bzw.   SW-
Architektur und der  Sicherheitskonzeption  die Informationssicherheitsmaßnahmen bei der Umsetzung des
IT-Systems   ab   und   vergleicht   sie   mit   den  Vorgaben   zur   Informationssicherheit.   Die   notwendigen
Ergänzungen und Änderungen dieser Vorgaben werden in den nachfolgenden Themen beschrieben.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

151

Die   Themen   entsprechen   denen   der   Vorgaben   zur   Informationssicherheit.   Zu   jedem   Thema   können
begründete   Empfehlungen   zur   Aufnahme,   Änderung   oder   Streichung   von   Vorgaben   zur
Informationssicherheit aufgeführt werden. Änderungen an verbindlichen Vorgaben und Ausschlüssen dürfen
nur beim Vorliegen entsprechender Vereinbarungen mit dem Auftraggeber aufgeführt werden und müssen auf
die jeweiligen Vertragszusätze verweisen.

Das   Produkt  Erweiterung   der  Vorgaben   zur   Informationssicherheit  ist   Bestandteil   der  Lieferung  an   den
Auftraggeber. Dieser sorgt für die Weitergabe des Produkts an den Informationssicherheitsbeauftragten der
Organisation.

Verantwortlich

Informationssicherheitsverantwortlicher

Mitwirkend

Aktivität

Vorlagen

Erzeugt durch

Datenschutzverantwortlicher

Vorgaben zur Informationssicherheit erweitern

Erweiterung der Vorgaben zur Informationssicherheit(.odt|.doc)

Systementwurf:
Pflichtenheft (Gesamtsystementwurf) (Nicht-funktionale Anforderungen), SW-
Architektur (Informationssicherheits- und datenschutzkritische SW-Elemente),
Systemarchitektur (Informationssicherheits- und datenschutzkritische
Systemelemente)

Inhaltlich abhängig

Berücksichtigung der Informationssicherheit und des Datenschutzes bei der
Systemerstellung:
Pflichtenheft (Gesamtsystementwurf)

Entscheidungsrelevant
bei

Gesamtsystem entworfen, System entworfen, Einheit(en) entworfen

C.1.11.7.1 Verbindlich einzuhaltende Vorgaben

Hier werden die in den Vorgaben zur Informationssicherheit nicht enthaltenen, aber im Projektverlauf als
notwendig   erkannten   Informationssicherheitsmaßnahmen   aufgeführt.
  In   den   Vorgaben   zur
Informationssicherheit verlangte Maßnahmen, die eine dem Zweck des IT-Systems entsprechende Nutzung
be- oder verhindern und daher nicht eingehalten werden konnten, sind mit einer Begründung und einem
Verweis auf die entsprechende vertragliche Anpassung aufzuführen.

C.1.11.7.2 Ausschlüsse

Hier werden die in den Vorgaben zur Informationssicherheit nicht enthaltenen, aber bei der Systemerstellung
als notwendig erkannten Verbote und Beschränkungen von Informationssicherheitsmaßnahmen aufgeführt.
In den Vorgaben zur Informationssicherheit verbotene oder beschränkte Maßnahmen, die eine dem Zweck
des   IT-Systems   entsprechende   Nutzung  be-   oder   verhindern  und   daher   dennoch   genutzt   oder   umgesetzt
wurden,   sind   mit   einer   Begründung   und   einem   Verweis   auf   die   entsprechende   vertragliche  Anpassung
aufzuführen.

C.1.11.7.3 Empfehlungen

Dieser Abschnitt beschreibt Informationssicherheitsmaßnahmen, die dem Stand der Technik entsprechen und
in künftigen Projekten umgesetzt werden sollten.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

152

 Referenz Produkte

C.1.11.8 Erweiterung der Vorgaben zum Datenschutz

Der  Auftragnehmer   leitet   aus   der  Schutzbedarfsfeststellung,   dem   Pflichtenheft,   der   System-   bzw.   SW-
Architektur und der  Sicherheitskonzeption  die datenschutzrechtlichen Maßnahmen bei der Umsetzung des
IT-Systems ab und vergleicht sie mit den  Vorgaben zum Datenschutz. Die notwendigen Ergänzungen und
Änderungen dieser Vorgaben werden in den nachfolgenden Themen beschrieben.

Die   Themen   entsprechen   denen   der   Vorgaben   zum   Datenschutz.   Zu   jedem   Thema   können   begründete
Empfehlungen zur Aufnahme, Änderung oder Streichung von Vorgaben zum Datenschutz aufgeführt werden.
Änderungen   an   verbindlichen   Vorgaben   und   Ausschlüssen   dürfen   nur   beim   Vorliegen   entsprechender
Vereinbarungen mit dem Auftraggeber aufgeführt werden und müssen auf die jeweiligen Vertragszusätze
verweisen.

Das Produkt Erweiterung der Vorgaben zum Datenschutz ist Bestandteil der Lieferung an den Auftraggeber.
Dieser sorgt für die Weitergabe des Produkts an den Datenschutzbeauftragten der Organisation.

Verantwortlich

Datenschutzverantwortlicher

Aktivität

Vorlagen

Erzeugt durch

Vorgaben zum Datenschutz erweitern

Erweiterung der Vorgaben zum Datenschutz(.odt|.doc)

Systementwurf:
Pflichtenheft (Gesamtsystementwurf) (Nicht-funktionale Anforderungen), SW-
Architektur (Informationssicherheits- und datenschutzkritische SW-Elemente),
Systemarchitektur (Informationssicherheits- und datenschutzkritische
Systemelemente)

Inhaltlich abhängig

Berücksichtigung der Informationssicherheit und des Datenschutzes bei der
Systemerstellung:
Pflichtenheft (Gesamtsystementwurf)

Entscheidungsrelevant
bei

C.1.11.8.1 Vorgehen

Gesamtsystem entworfen, System entworfen, Einheit(en) entworfen

Sofern   der   Auftragnehmer   ein   von   den   Vorgaben   zum   Datenschutz   abweichendes   Vorgehen   zur
Gewährleistung des Datenschutzes verwendet, ist dieses hier zu beschreiben. Dabei muss insbesondere das
Mapping auf die vom Auftraggeber gewählte Methodik dokumentiert werden. Die Abweichungen sind mit
dem Auftraggeber abzustimmen.

C.1.11.8.2 Kategorisierung

Sofern der Auftragnehmer eine von den Vorgaben zum Datenschutz abweichende Kategorisierung der Daten
verwendet, ist diese hier zu beschreiben. Dabei muss insbesondere das Mapping auf die vom Auftraggeber
gewählten Kategorien dokumentiert werden. Die Abweichungen sind mit dem Auftraggeber abzustimmen.

C.1.11.8.3 Verbindlich einzuhaltende Vorgaben

Hier werden die in den Vorgaben zum Datenschutz nicht enthaltenen, aber im Projektverlauf als notwendig
erkannten technischen und organisatorischen Maßnahmen (TOMs) zur Gewährleistung des Datenschutzes
aufgeführt.   In   den   Vorgaben   zum   Datenschutz   verlangte   TOMs,   die   eine   dem   Zweck   des   IT-Systems
entsprechende Nutzung be- oder verhindern und daher nicht eingehalten werden konnten, sind mit einer
Begründung und einem Verweis auf die entsprechende vertragliche Anpassung aufzuführen.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

C.1.11.8.4 Ausschlüsse

153

Hier werden die in den Vorgaben zum Datenschutz nicht enthaltenen, aber bei der Systemerstellung als
notwendig   erkannten   Verbote   und   Beschränkungen   von   Systemeigenschaften   zur   Gewährleistung   des
Datenschutzes   aufgeführt.   In   den   Vorgaben   zum   Datenschutz   verbotene   oder   beschränkte
Systemeigenschaften, die eine dem Zweck des IT-Systems entsprechende Nutzung be- oder verhindern und
daher   dennoch   genutzt   oder   umgesetzt   wurden,   sind   mit   einer   Begründung   und   einem Verweis   auf   die
entsprechende vertragliche Anpassung aufzuführen.

C.1.11.8.5 Empfehlungen

Dieser Abschnitt beschreibt technische und organisatorische Maßnahmen, die in künftigen Projekten zur
Verbesserung des Datenschutzes umgesetzt werden sollten.

C.1.11.9 Datenbankentwurf

Datenzentrierte   SW-Systeme,   wie   beispielsweise   Informationssysteme,   benötigen   einen   persistenten
Speicher   zur   Datenhaltung.  In  der   Regel   handelt   es  sich  dabei   um  eine  oder  mehrere  Datenbanken.   Im
Rahmen   des   Systementwurfs   ist   in   diesem   Fall   zusätzlich   ein  Datenbankentwurf  zu   erstellen.   Der
 s   aus den
Datenbankentwurf unterstützt den SW-Architekt
Anforderungen sowie beim Entwurf des physikalischen Datenbankschemas.

 en    bei der Ableitung des technischen Datenmodell

Grundlage   des   Datenbankentwurfs   sind   die   zu   persistierenden   Entitäten   des   Systems.   Die   Entitäten
(relationales Datenmodell) bzw. Klassen (objektorientiertes Datenmodell) repräsentieren in ihrer Gesamtheit
das fachliche Datenmodell des Systems. Für den Datenbankentwurf werden alle Entitäten bzw. Klassen des
Systems  identifiziert und im technischen Datenmodell zusammengefasst. Technisches und physikalisches
Datenmodell sind Verfeinerungen und Konkretisierungen des fachlichen Datenmodells auf dem Weg hin zum
Datenbankschema. Verantwortlich für den Datenbankentwurf ist der SW-Architekt.

Verantwortlich

Mitwirkend

Aktivität

Methoden

Vorlagen

Erzeugt durch

SW-Architekt

SW-Entwickler

Datenbankentwurf erstellen

Datenbankmodellierung

Datenbankentwurf(.odt|.doc)

Systementwurf:
SW-Architektur (Datenkatalog), Systemarchitektur (Übergreifender
Datenkatalog)

C.1.11.9.1

Technisches Datenmodell

Das   technische  Datenmodell  beschreibt   die   Entitäten   bzw.   die   Klassen   des   Geschäftsmodells   im
Zusammenhang. Die relevanten Eigenschaften (Attribute) sowie die Beziehungen der Entitäten bzw. Klassen
zu einander werden identifiziert und beschrieben.

Das   technische   Datenmodell   kann  als   Entity-Relationship-Diagramm,   Klassendiagramm  oder   als  Tabelle
dargestellt werden. Es ist die Grundlage für den Entwurf des physikalischen Datenmodells.

C.1.11.9.2 Physikalisches Datenmodell

Das physikalische  Datenmodell  beschreibt den konkreten  Datenbankentwurf. Es wird abgeleitet aus dem
technischen Datenmodell und dient als Vorlage für das Datenbankschema in der Datenbank.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland



154

 Referenz Produkte

Im  physikalischen   Datenmodell   werden   den  Attributen   der   Entitäten   bzw.   Klassen   konkrete   Datentypen
zugeordnet. Es  werden Primär- und Fremdschlüssel  festgelegt sowie Beziehungen definiert.  Das Modell
definiert Konsistenzbedingungen für Datenänderungen. Handelt es sich um relationale Datenbanken, werden
Entitäten und Attribute konkreten Tabellen und Feldern im Schema zugeordnet.

Der  Entwurf  des  physikalischen Datenmodells  erfolgt  in der  Regel  über  Entity-Relationship-Diagramme
oder Klassendiagramme. Bei Verwendung geeigneter Werkzeuge kann das Datenbankschema direkt aus dem
Diagramm generiert werden.

C.1.11.10 Mensch-Maschine-Schnittstelle (Styleguide)

Um den Entwurf einer (grafischen) Benutzerschnittstelle einheitlich zu gestalten beziehungsweise auf ein
vorgegebenes Layout abzustimmen, sind verbindliche Vorgaben notwendig. Das Produkt Mensch-Maschine-
Schnittstelle, im Rahmen der Softwareentwicklung häufig auch Styleguide genannt, definiert Regeln und
Gestaltungskriterien, nach denen die Mensch-Maschine-Schnittstelle zu gestalten ist.

Die   Regeln   umfassen   beispielsweise   Gestaltungsregeln   zu   den   Oberflächenelementen,   zum   Beispiel
haptische   und   optische   Eigenschaften,   Gestaltungsregeln   für   die   grafische   Benutzeroberfläche   sowie
Gestaltungsregeln für die Hardwareschnittstelle.

Verantwortlich für den Styleguide ist der  Ergonomieverantwortlicher. Seine Aufgabe ist es, die Regeln aus
den Anforderungen sowie der  Anwenderaufgabenanalyse  abzuleiten, beziehungsweise in Zusammenarbeit
mit dem Auftraggeber zu erarbeiten. Alle im Rahmen der System-, HW- und SW-Spezifikation erarbeiteten
Entwürfe müssen die Vorgaben des Styleguides umsetzen.

Verantwortlich

Ergonomieverantwortlicher

Aktivität

Werkzeuge

Vorlagen

Erzeugt durch

Mensch-Maschine-Schnittstelle definieren

GUI-Werkzeug

Mensch-Maschine-Schnittstelle (Styleguide)(.odt|.doc)

Systementwurf:
Pflichtenheft (Gesamtsystementwurf) (Nicht-funktionale Anforderungen)

Inhaltlich abhängig

Vorgaben zur Benutzungsschnittstelle:
Systemspezifikation, SW-Spezifikation

C.1.11.10.1 Gestaltungsprinzipien und -alternativen

Gestaltungsprinzipien legen die generellen Richtlinien zur Gestaltung der Mensch-Maschine-Schnittstelle
fest.   Diese   werden   aus   den   Ergebnissen   der  Anwenderaufgabenanalyse  abgeleitet   sowie   anhand   von
allgemein anerkannten Normen identifiziert.

Einzuhaltende Grundsätze  zur  Gestaltung ergonomischer Benutzerschnittstellen werden von der EN ISO
9241 Norm wie folgt definiert:

➢ Aufgabenangemessenheit

➢ Selbstbeschreibungsfähigkeit

➢ Steuerbarkeit

➢ Erwartungskonformität

➢ Fehlertoleranz

➢ Individualisierbarkeit

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

➢ Lernförderlichkeit.

155

C.1.11.10.2

Identifikation und Aufbau der Benutzungselemente

Erster Schritt zur Festlegung der Gestaltungsregeln einer Benutzerschnittstelle ist die Identifikation aller am
Aufbau der Schnittstelle beteiligten Benutzungselemente.

Die Liste der Benutzungselemente wird aus den Anforderungen abgeleitet und im Rahmen des Entwurfs der
Benutzerschnittstelle   ergänzt   und   vervollständigt.   Für   zusammengesetzte   Benutzungselemente   wird   der
Aufbau beschrieben.

C.1.11.10.3 Gestaltungsregeln der Benutzungselemente

Gestaltungsregeln   definieren   das   ‚Look   and   Feel’   von   Benutzungselementen.   Jedem   identifizierten
modularen beziehungsweise zusammengesetzten Benutzungselement werden Gestaltungsregeln zugewiesen.
Beispielsweise kann für eine grafische Benutzeroberfläche das Aussehen eines Textfeldes, das Design einer
Tabelle oder die Farbe des Hintergrundes festgelegt werden. Die Vorgaben sind in den Spezifikationen der
Systemelemente umzusetzen.

C.1.11.11 Migrationskonzept

Das  Migrationskonzept  ist Grundlage und Verfahrenshandbuch für die Migration von Systemteilen eines
Altsystems auf ein Neusystem. Es beschreibt Aufgaben, Verantwortlichkeiten und Abläufe zur Überführung
relevanter Systemteile des Altsystems auf die neue Zielumgebung.

Das   Migrationskonzept   beschreibt   im   Detail,   welche   Teile   des   Altsystems   betroffen   sind,   welche
Änderungen   zur   Migration  durchzuführen   sind  und  an   welcher   Stelle   die   migrierten  Systemteile   in  das
Neusystem   zu   integrieren   sind.   Abhängig   von   Aspekten   der   Sicherheit   des   Altsystems   wird   für   die
Geschäftsprozesse   eine   Migrations-   und   eine  Rollbackstrategie  gewählt   und   eine   detaillierte
Migrationsplanung festgelegt.

Der Systemarchitekt trägt, als Verantwortlicher für den Entwurf des Neusystems, auch die Verantwortung für
das Migrationskonzept. So ist sichergestellt, dass die zu migrierenden Systemteile im Architekturentwurf
ausreichend   berücksichtigt   werden.   Unterstützt   wird   der   Systemarchitekt   vom  Systemintegrator,   der   die
Verantwortung für das zu entwickelnde Neusystem trägt.

Für die Migration relevante Informationen zum Altsystem werden aus der  Altsystemanalyse  übernommen.
Informationen   zum   Neusystem   werden   aus   dem   Gesamtsystementwurf   beziehungsweise   der
Systemarchitektur und dem Datenbankentwurf ermittelt.

Verantwortlich

Systemarchitekt

Mitwirkend

Aktivität

Werkzeuge

Vorlagen

Erzeugt durch

Systemintegrator

Migrationskonzept erstellen

Integrierte Entwicklungsumgebung

Migrationskonzept(.odt|.doc)

Systementwurf:
Pflichtenheft (Gesamtsystementwurf) (Dekomposition des Gesamtsystems)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

156

C.1.11.11.1 Migrationsüberblick

 Referenz Produkte

Der Migrationsüberblick unterstützt den Systemarchitekt
 en    bei der Planung und Vorbereitung der Migration.
Hier wird beschrieben, welche Systeme an der Migration beteiligt sind, welche Ziele mit der Migration
verfolgt werden und welche Rahmenbedingungen zur Migration einzuhalten sind.

Eine   typische   Rahmenbedingung   für   die   Durchführung   einer   Migration   ist   die   Beschränkung   auf   einen
festgelegten   Zeitraum.   Häufig   haben   zu   migrierende  Anwendungen   hohe   Verfügbarkeitsanforderungen.
Diese müssen bei der Migration erfüllt werden.

C.1.11.11.2 Migrationsstrategie

Die Migrationsstrategie legt die Strategie für die Durchführung der Migration fest. Für die Ablösung eines
Altsystems stehen grundsätzlich zwei Strategien zur Auswahl, die stufenweise Einführung oder die 'Big-
Bang'   Strategie,   also   die   Einführung   in   einem   Schritt.   Welche   der   Strategien   für   einen   konkreten   Fall
geeignet ist, muss im Detail untersucht und festgelegt werden.

Bei einer 'Big-Bang' Strategie werden innerhalb eines festgelegten Zeitraums - häufig an einem Wochenende
- das Altsystem abgeschaltet, das Neusystem installiert sowie Systemteile und Daten migriert.

Bei   einer   stufenweisen   Migration   wird   das  Altsystem   in   mehreren   Schritten   migriert.   Die   stufenweise
Migration ist im Allgemeinen unkritischer als die 'Big-Bang' Strategie. Die Anwender können sich langsam
an die neuen Funktionalitäten gewöhnen. Falls das neue System noch nicht stabil sein sollte, kann im Notfall
auf das Altsystem zurückgegriffen werden. Man unterscheidet zwei Arten der stufenweisen Einführung:

➢ Das Neusystem liefert die volle Funktionalität, steht jedoch nur einer beschränkten Nutzergruppe zur
Verfügung. Neu- und Altsystem laufen parallel. Mit jeder Stufe wird der Kreis der Nutzer erweitert.
Problematisch ist hier die parallele Nutzung von Alt- und Neusystem und damit insbesondere die
Erhaltung der Datenkonsistenz.

➢ Eine andere Art der stufenweisen Einführung ist die Bereitstellung einer Teilfunktionalität für alle
Nutzer.   Die   Anwender   arbeiten   parallel   auf   Neu-   und   Altsystem.   Mit   jeder   Stufe   wird   die
Funktionalität der Neusystems erweitert, bis das Altsystem vollständig abgelöst wurde.

C.1.11.11.3 Rollbackstrategie

Zu   jeder   in   der   Migrationsplanung   festgelegten   Stufe   ist   eine  Rollbackstrategie  festzulegen.   Eine
Rollbackstrategie beschreibt alle Aktivitäten, die durchgeführt werden müssen, um Änderungen im Falle
eines   Scheiterns   der   Migration   zeitgerecht   zurückzusetzen.   Für   jede   Migrationsstufe   wird   individuell
festgelegt

➢ nach welchen Kriterien die Entscheidung für ein Zurücksetzen der Änderungen und damit für einen

Abbruch der Migration getroffen wird,

➢ welche Aufgaben zur Vorbereitung des Abbruchs durchgeführt werden müssen,

➢ welche Aktivitäten zur Durchführung des Abbruchs durchgeführt werden müssen, insbesondere wie

der ursprüngliche Datenbestand wieder hergestellt werden kann und

➢ welche Aktivitäten nach Durchführung des Abbruchs durchzuführen sind. Hier ist insbesondere eine
Teststrategie   notwendig,   mit   der   sichergestellt   wird,   dass   das   Altsystem   wieder   mit   voller
Funktionalität zur Verfügung steht.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


C.1 Produkte

C.1.11.11.4 Datenmigration

157

Daten sind das zentrale Element der Migration. Daten aus dem Altsystem müssen eventuell in ein neues
Format transformiert und in die Datenbank(en) des Neusystems  geladen werden. Die   Datenmigration  ist
detailliert zu planen. Der Datenfluss von den Quelldatenbanken zu den Zieldatenbanken wird festgelegt.
Zusätzlich werden alle notwendigen Datentransformationen definiert.

Der Detaillierungsgrad geht hier bis auf die Ebene der Felder in einer Datenbanktabelle. Grundlage für die
Planung der Datenmigration ist das Datenmodell der Altsystemanalyse als Quelle des Datenflusses und der
Datenbankentwurf des Neusystems als Ziel.

C.1.11.11.5 Planung der Durchführung

Abhängig   von  der   gewählten  Migrationsstrategie  wird  die   Durchführung  der   Migration   zeitlich  geplant.
Innerhalb   der   definierten   Migrationsstufen   werden   weitere   Stufen,   jeweils   mit   einer  Rollbackstrategie,
festgelegt. Die durchzuführenden Aktivitäten werden geplant und die Verantwortlichkeiten zugeordnet. Für
jede   Stufe   sowie   für   die   Migrationsplanung   insgesamt   wird   festgelegt,   ab   wann   ein   Abbruch
beziehungsweise ein Rollback nicht mehr möglich ist (Point of no Return).

C.1.12 Systemspezifikation

C.1.12.1 Systemspezifikation

Die Systemspezifikation dient während der Entwicklung als Vorgabe und Hilfsmittel für den Entwurf und die
Dekomposition   der  Systemarchitektur.   Nach   der   Entwicklung   ist   sie   als   abstrakte   Beschreibung   des
Verhaltens des jeweiligen Systemelements essentiell für die Pflege und Weiterentwicklung.

Sie beschreibt alle funktionalen und nicht-funktionalen Anforderungen an ein Systemelement (System oder
Segment).   Zur   Erstellung   einer   Systemspezifikation   werden   die  Anforderungen   aus   den   Spezifikationen
übergeordneter Systemelemente beziehungsweise dem Gesamtsystementwurf abgeleitet. Sollten im Laufe
der   weiteren   Entwicklung   des   Systemelements   Änderungen   nötig   sein,   ist   zunächst   immer   die
Systemspezifikation anzupassen. Die Prüfspezifikation Systemelement definiert die Prüffälle zum Nachweis
der Schnittstellen und Anforderungen der Spezifikation.

Wesentliche   Inhalte   der   Systemspezifikation   sind   die   Beschreibung   der   Anforderungen   an   das
Systemelement   und   die   Festlegung   der   Schnittstellen,   die   es   zu   bedienen   hat.   Zusätzlich   wird   die
Verfeinerung und Zuordnung von Anforderungen und Schnittstellen zu untergeordneten Systemelementen
beschrieben.

Im Rahmen der Anforderungsverfolgung wird sichergestellt, dass alle Anforderungen an das Element bei der
Verfeinerung   auf   die   nächste   Hierarchieebene   berücksichtigt   werden.   Die   Erstellung   der
Systemspezifikationen erfolgt Hand in Hand mit dem Architekturentwurf eines Systems. Zur Sicherstellung
der   Konsistenz   zwischen   Spezifikationen  und Architektur   ist   der  Systemarchitekt  verantwortlich   für   die
Erstellung der Produkte.

Anforderungen aus der Systemspezifikation können sich auf die Spezifikation Logistische Unterstützung
auswirken. Ebenso können Anforderungen der Logistik die Systemspezifikation beeinflussen.

Verantwortlich

Systemarchitekt

Mitwirkend

Aktivität

Methoden

Ergonomieverantwortlicher, Prüfer, Systemintegrator

System/Segment spezifizieren

Anforderungsanalyse, Prototyping, Systemanalyse

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

158

Werkzeuge

Vorlagen

Erzeugt durch

Anforderungsmanagement, Integrierte Entwicklungsumgebung,
Modellierungswerkzeug

Systemspezifikation(.odt|.doc)

Systementwurf:
Systemarchitektur (Zu spezifizierende Systemelemente)

 Referenz Produkte

Inhaltlich abhängig

Vorgaben zur Benutzungsschnittstelle:
Mensch-Maschine-Schnittstelle (Styleguide)

Entscheidungsrelevant
bei

System entworfen

C.1.12.1.1 Systemelementüberblick

Der   Systemelementüberblick   gibt   einen   groben   Überblick   über   das   zu   realisierende   Systemelement.
Aufgaben und Ziele des Systemelements werden überblickartig beschrieben sowie seine Rolle innerhalb des
Systems dargestellt.

C.1.12.1.2 Schnittstellenbeschreibung

Eine   Schnittstelle   repräsentiert   die   Grenze   eines   Systemelements   zu   seiner   Umgebung.   Sie   beschreibt,
welche Daten an der Systemgrenze ausgetauscht werden, und die logischen Abhängigkeiten. Damit definiert
die Schnittstelle die Dienste, die vom Systemelement zu erbringen sind. Ein Systemelement kann mehrere
Schnittstellen unterstützen.

In der Schnittstellenbeschreibung werden die funktionalen Anforderungen an das Systemelement gesammelt,
alle   Schnittstellen   festgelegt   und   im   Zusammenhang   dargestellt.   Zusammen   mit   den   nicht-funktionalen
Anforderungen enthält die Schnittstellenbeschreibung die notwendigen Informationen zur Entwicklung des
Systemelements.   In   der   Schnittstellenbeschreibung   werden   neben   den   Schnittstellen   zu   anderen
Systemelementen   auch   die   Schnittstellen   zur   Umgebung   beschrieben,   wie   die   Mensch-Maschine-
Schnittstelle oder Schnittstellen zu anderen im Projekt zu entwickelnden Systemen.

Die   Beschreibung   der   funktionalen   Schnittstelle   teilt   sich   in   die   Beschreibung   ihres   statischen   und
dynamischen   Verhaltens   auf.   Das   statische   Verhalten   legt   die   Struktur   der   Schnittstelle   fest,   über   die
Funktionalitäten   des   Systemelements   genutzt   werden   können.   Das   dynamische   Verhalten   bestimmt   die
Reihenfolge der Nutzung und die logischen Abhängigkeiten der übermittelten Daten und Signale.

Inhalt und Beschreibung der Schnittstellen können variieren, je nachdem, ob es sich um HW- oder SW-
Anteile   des   Systemelements   handelt.   HW-Anteile   werden   durch   die   Angabe   von   elektrischen   und
mechanischen   Daten   spezifiziert,   SW-Anteile   durch   die   Beschreibung   von   Methoden,   Parametern   und
Informationen zum Verhalten.

Zu   den   statischen   Elementen   einer   HW-Schnittstelle   zählen   beispielsweise   Angaben   zu   elektrischen
Leistungsdaten (Leistung,  Spannung,  Strom,   Frequenz,  Polarität),  Angaben zur  mechanischen Auslegung
(Steckertyp,   Steckerbelegung,   Kabeltyp)   oder  Angaben   zum   technischen  Aufbau   (Funktionsaufruf   und
Parameterliste, Übertragungsrichtung, Layout einer Nutzerschnittstelle). Zur Beschreibung des dynamischen
Verhaltens zählen beispielsweise die Festlegung von Kommunikationsprotokollen und deren Spezifikationen,
die Beschreibung von Synchronisationsmechanismen sowie Hinweise zur Benutzung und Bedienung der
Schnittstelle.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

159

Das statische Verhalten einer SW-Schnittstelle legt die Struktur der Aufrufe fest, über die Dienste des  SW-
Element
 s    genutzt   werden   können.   Zur   Beschreibung   dienen   insbesondere   Methodensignaturen   und
Definitionen von Datentypen. Das dynamische Verhalten bestimmt die Reihenfolge, in der Aufrufe erfolgen
  Zur   Beschreibung   des   dynamischen   Verhaltens   werden   häufig   Ablaufdiagramme
können.
(Sequenzdiagramme, Message Sequence Charts) oder Zustandübergangsdiagramme verwendet.

Grundlage   für   die   Schnittstellenbeschreibung   sind   die   Schnittstellenübersicht   der  Architektur   sowie   die
Schnittstellenrealisierungen der Systemspezifikation

 en    übergeordneter Systemelemente.

Die Schnittstellenbeschreibung sollte sich daran orientieren, ob eine Wiederverwendung bereits bestehender
Systemelemente möglich ist. Darüber hinaus ist bei der Beschreibung der Schnittstellen darauf zu achten,
dass   die   Schnittstellen   stabil   sein   sollen,   und   damit   eine   möglichst   lange   Nutzung   des   Systemelements
möglich wird.

C.1.12.1.3 Nicht-funktionale Anforderungen

Neben   den   funktionalen   Anforderungen   hat   ein   Systemelement   eine   Reihe   von   nicht-funktionalen
Anforderungen   zu   erfüllen.   Häufig   geforderte   nicht-funktionale   Anforderungen   an   ein   System   sind
beispielsweise Qualitäts-Merkmale wie Leistung, Sicherheit, Verfügbarkeit, Performance und Wartbarkeit.

Die   nicht-funktionalen  Anforderungen   werden   im   Detail   beschrieben   und   mit   den   konkret   geforderten
Werten belegt.  Die  für  das  Systemelement  relevanten nicht-funktionalen Anforderungen werden aus den
Spezifikationen der übergeordneten Systemelemente beziehungsweise dem Gesamtsystementwurf abgeleitet.

C.1.12.1.4 Schnittstellenrealisierung

In   der   Schnittstellenrealisierung   erfolgt   die   Verfeinerung   der   funktionalen   Anforderungen   aus   der
Schnittstellenbeschreibung.   Anforderungen   und   Schnittstellen   werden   konkretisiert,   verfeinert   und   den
Systemelementen der darunter liegenden Hierarchieebene zugeordnet.

Grundlage   der   Schnittstellenrealisierung   ist   die   Systemarchitektur   des   übergeordneten   Systems.   Die
hierarchische Struktur wird in den Architekturen im Rahmen der Dekomposition identifiziert.

C.1.12.1.5 Verfeinerung nicht-funktionaler Anforderungen

Die   Verfeinerung   nicht-funktionaler   Anforderungen   erfolgt   parallel   zur   Verfeinerung   der   funktionalen
Anforderungen in der Schnittstellenrealisierung. Die nicht-funktionalen Anforderungen werden konkretisiert,
verfeinert und den Systemelementen der darunter liegenden Hierarchiestufe zugeordnet.

Die   verfeinerten  Anforderungen   bleiben   als   eigenständige  Anforderungen   bestehen   oder   werden   in   die
Schnittstellenrealisierung integriert.

C.1.12.1.6 Anforderungsverfolgung

Im Rahmen der Anforderungsverfolgung wird zusammenfassend die Zuordnung der funktionalen und nicht-
funktionalen   Anforderungen   an   das   Systemelement   auf   die   verfeinerten   Anforderungen   und   auf
untergeordnete   Systemelemente   dargestellt.   Grundlage   sind   die   Ergebnisse   der   Schnittstellenrealisierung
sowie   der   Verfeinerung   nicht-funktionaler   Anforderungen.   Die   bidirektionale   Verfolgbarkeit   (d.h.   von
übergeordneten zu untergeordneten Systemelementen und umgekehrt) muss dabei sichergestellt werden. Die
Darstellung kann beispielsweise anhand einer Matrix erfolgen.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland



160

 Referenz Produkte

C.1.12.2 Externe-Einheit-Spezifikation

Für jede im Rahmen des Architekturentwurfs identifizierte potentielle  Externe Einheit  wird eine  Externe-
Einheit-Spezifikation  erstellt. Die Spezifikation ist Grundlage für die Auswahl eines Fertigprodukts, eines
zur Wiederverwendung verfügbaren Systemelements oder einer Beistellung. Im Falle eines Unterauftrags
dient sie als Anforderungsdokument. Sie dient zusätzlich als Grundlage der Prüfung.

In der Externe-Einheit-Spezifikation werden alle funktionalen und nicht-funktionalen Anforderungen an die
Externe Einheit definiert. Handelt es sich um ein mögliches Fertigprodukt, werden anhand der Spezifikation
eine   Marktsichtung   und   eine  Evaluierung   von   Fertigprodukten  durchgeführt.   Bei   Vergabe   über   einen
Unterauftrag bildet die Spezifikation die Grundlage des Vertrags mit dem Unterauftragnehmer.

Verantwortlich für die Erstellung der Externe-Einheit-Spezifikation ist der Systemarchitekt. Unterstützt wird
er vom Systemintegrator, der sicherstellt, dass die letztendlich gewählte Externe Einheit allen Anforderungen
zur Integration in das System genügt.

Verantwortlich

Systemarchitekt

Mitwirkend

Aktivität

Methoden

Werkzeuge

Vorlagen

Erzeugt durch

Inhaltlich abhängig

Ergonomieverantwortlicher, Prüfer, SW-Architekt, Systemintegrator

Externe-Einheit spezifizieren

Anforderungsanalyse, Systemanalyse

Anforderungsmanagement, Integrierte Entwicklungsumgebung,
Modellierungswerkzeug

Externe-Einheit-Spezifikation(.odt|.doc)

Systementwurf:
Systemarchitektur (Zu spezifizierende Systemelemente)

Einfluss eines Fertigprodukts auf die Spezifikation externer Systemelemente:
Make-or-Buy-Entscheidung
Externe-Einheit/Externes-SW-Modul-Spezifikation als Bestandteil der
Vergabeunterlagen (Ausschreibung):
Vergabeunterlagen (Ausschreibung)

Entscheidungsrelevant
bei

System entworfen

C.1.12.2.1 Systemelementüberblick

Der Systemelementüberblick gibt einen groben Überblick über die  Externe Einheit. Aufgaben und Ziele
werden überblickartig beschrieben sowie ihre Rolle innerhalb des Systems dargestellt.

C.1.12.2.2 Schnittstellenbeschreibung

Eine Schnittstelle repräsentiert die Grenze einer Externen Einheit zu ihrer Umgebung. Sie beschreibt welche
Daten an der Elementgrenze ausgetauscht werden, und die logischen Abhängigkeiten. Damit definiert die
Schnittstelle die Dienste, die von der Externen Einheit zu erbringen sind. Eine Externe Einheit kann durchaus
mehrere Schnittstellen haben.

In der Schnittstellenbeschreibung werden die funktionalen Anforderungen an die Externe Einheit gesammelt,
alle   Schnittstellen   festgelegt   und   im   Zusammenhang   dargestellt.   Zusammen   mit   den   nicht-funktionalen
Anforderungen enthält die Schnittstellenbeschreibung alle notwendigen Informationen zur Auswahl einer

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

161

Externen   Einheit.   Neben   den   Schnittstellen   zu   anderen   Systemelementen   werden   in   ihr   auch   die
Schnittstellen  zur   Umgebung   beschrieben,   wie   die   Mensch-Maschine-Schnittstelle   oder   Schnittstellen  zu
anderen im Projekt zu entwickelnden Systemen.

Die   Beschreibung   der   funktionalen   Schnittstelle   teilt   sich   in   die   Beschreibung   ihres   statischen   und
dynamischen   Verhaltens   auf.   Das   statische   Verhalten   legt   die   Struktur   der   Schnittstelle   fest,   über   die
Funktionalitäten   der   Externen   Einheit   genutzt   werden   können.   Das   dynamische  Verhalten   bestimmt   die
Reihenfolge der Nutzung.

Inhalt und Beschreibung der Schnittstellen können variieren, je nachdem, ob es sich um HW- oder SW-
Anteile   der   Externen   Einheit   handelt.   HW-Anteile   werden   durch   die   Angabe   von   elektrischen   und
mechanischen   Daten   spezifiziert,   SW-Anteile   durch   die   Beschreibung   von   Methoden,   Parametern   und
Informationen zum Verhalten.

Zu   den   statischen   Elementen   einer   HW-Schnittstelle   zählen   beispielsweise   Angaben   zu   elektrischen
Leistungsdaten (Leistung,  Spannung,  Strom,   Frequenz,  Polarität),  Angaben zur  mechanischen Auslegung
(Steckertyp,   Steckerbelegung,   Kabeltyp)   oder  Angaben   zum   technischen  Aufbau   (Funktionsaufruf   und
Parameterliste, Übertragungsrichtung, Layout einer Nutzerschnittstelle). Zur Beschreibung des dynamischen
Verhaltens zählen beispielsweise die Festlegung von Kommunikationsprotokollen und deren Spezifikationen,
die Beschreibung von Synchronisationsmechanismen sowie Hinweise zur Benutzung und Bedienung der
Schnittstelle.

Das statische Verhalten einer SW-Schnittstelle legt die Struktur der Aufrufe fest, über die Dienste des  SW-
Element
 s    genutzt   werden   können.   Zur   Beschreibung   dienen   insbesondere   Methodensignaturen   und
Definitionen von Datentypen.

Das dynamische Verhalten bestimmt die Reihenfolge, in der Aufrufe erfolgen können. Zur Beschreibung des
dynamischen Verhaltens werden häufig Ablaufdiagramme (Sequenzdiagramme, Message Sequence Charts)
oder Zustandübergangsdiagramme verwendet.

Grundlage   für   die   Schnittstellenbeschreibung   sind   die   Schnittstellenübersicht   der  Architektur   sowie   die
Schnittstellenrealisierungen der Systemspezifikation

 en    übergeordneter Systemelemente.

C.1.12.2.3 Nicht-funktionale Anforderungen

Neben   den   funktionalen   Anforderungen   hat   eine  Externe   Einheit  eine   Reihe   nicht-funktionaler
Anforderungen   zu   erfüllen.   Die   nicht-funktionalen  Anforderungen   an   eine   Externe   Einheit   entsprechen
weitgehend den nicht-funktionalen Anforderungen, die an ein Systemelement gestellt werden.

Die   nicht-funktionalen  Anforderungen   werden   im   Detail   beschrieben   und   mit   den   konkret   geforderten
Werten belegt. Die für die Externe Einheit relevanten nicht-funktionalen Anforderungen werden aus den
Spezifikationen   der   übergeordneten   Systemelemente   beziehungsweise   aus   dem   Gesamtsystementwurf
abgeleitet.

C.1.12.2.4

Lieferumfang

Es   sind   alle   Gegenstände   und   Dienstleistungen   aufzulisten,   die   während   des   Projektverlaufs   oder   bei
Abschluss des Projektes vom Auftragnehmer an den Auftraggeber zu liefern sind. Jede Lieferung erfordert
eine  Abnahmeprüfung.   Der   Lieferumfang   kann   je   nach   Vereinbarung   ein   System,   Teile   eines   Systems,
Dokumente und Dienstleistungen enthalten.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland



162

 Referenz Produkte

C.1.12.2.5 Abnahmekriterien und Vorgehen zur Abnahmeprüfung

Abnahmekriterien   legen   fest,   welche   Kriterien   die   gelieferte  Externe   Einheit  erfüllen   muss,   um   den
Anforderungen der Externe-Einheit-Spezifikation zu entsprechen. Sie sollen messbar dargestellt werden. Aus
vertraglicher Sicht beschreiben die Abnahmekriterien die Bedingungen für die Entscheidung, ob die Externe
Einheit  die  gestellten Anforderungen erfüllt  oder  nicht.  Die Abnahmekriterien beziehen sich sowohl  auf
funktionale als auch auf nicht-funktionale Anforderungen.

Aufbau und Anzahl der Abnahmekriterien sind durch den Auftraggeber zu skizzieren. Eine Strukturierung
der   Abnahmekriterien   nach   ihren   drei   wesentlichen   Bestandteilen,   Ausgangssituation,   Aktion(en)   und
erwartetes   Ergebnis,   ist  anzustreben.   In jedem Fall  müssen  die   erwarteten Ergebnisse   der  Abnahme   pro
Abnahmekriterium festgelegt werden.

Die   Erfüllung   der   Abnahmekriterien   wird   im   Rahmen   der   Eingangsprüfung   festgestellt.   Die
Abnahmekriterien gehen somit als Anforderungen in die Abnahmespezifikation ein.

Erzeugt

Prüfung der Lieferungen (Externe Einheit):
Abnahmeprotokoll, Abnahmespezifikation

C.1.12.3 SW-Spezifikation

Die SW-Spezifikation dient während der Entwicklung als Vorgabe und Hilfsmittel für den Entwurf und die
Dekomposition der SW-Architektur. Nach der Entwicklung ist sie als abstrakte Beschreibung des Verhaltens
des jeweiligen Systemelements essentiell für die Pflege und Weiterentwicklung.

Sie  beschreibt  alle  funktionalen  und  nicht-funktionalen Anforderungen  an  ein  SW-Element  (SW-Einheit,
SW-Komponente  oder  SW-Modul).  Zur  Erstellung der  Spezifikation werden  die  Anforderungen aus  den
Spezifikationen übergeordneter Systemelemente beziehungsweise SW-Elemente abgeleitet. Sollten im Laufe
der   weiteren   Entwicklung   des   SW-Elements   Änderungen   nötig   sein,   ist   zunächst   immer   die   SW-
Spezifikation anzupassen. Die  Prüfspezifikation Systemelement  definiert die Prüffälle zum Nachweis der
Schnittstellen und Anforderungen der Spezifikation.

Wesentliche Inhalte der SW-Spezifikation sind die Beschreibung der Anforderungen an das SW-Element
sowie   die   Festlegung   der   Schnittstellen,   die   es   zu   bedienen   hat.   Zusätzlich   wird   die   Verfeinerung   und
Zuordnung von Anforderungen und Schnittstellen zu untergeordneten SW-Elementen beschrieben.

Im Rahmen der Anforderungsverfolgung wird sichergestellt, dass alle Anforderungen an das Element bei der
Verfeinerung auf die nächste Hierarchieebene berücksichtigt werden. Die Erstellung der SW-Spezifikationen
 en   . Zur Sicherstellung der Konsistenz
erfolgt Hand in Hand mit dem Architekturentwurf der  SW-Einheit
zwischen   Spezifikationen   und  Architektur   ist   der  SW-Architekt  verantwortlich   für   die   Erstellung   beider
Produkte.

Anforderungen   aus   der   SW-Spezifikation   können   sich   auf   die   Spezifikation   Logistische   Unterstützung
auswirken. Ebenso können Anforderungen der Logistik die SW-Spezifikation beeinflussen.

Verantwortlich

SW-Architekt

Mitwirkend

Aktivität

Methoden

Werkzeuge

Vorlagen

Ergonomieverantwortlicher, Prüfer, SW-Entwickler

SW-Einheit/-Komponente/-Modul spezifizieren

Systemanalyse

Modellierungswerkzeug

SW-Spezifikation(.odt|.doc)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


C.1 Produkte

Erzeugt durch

Systementwurf:
SW-Architektur (Zu spezifizierende SW-Elemente)

Inhaltlich abhängig

Vorgaben zur Benutzungsschnittstelle:
Mensch-Maschine-Schnittstelle (Styleguide)

Entscheidungsrelevant
bei

Einheit(en) entworfen

C.1.12.3.1 SW-Element-Überblick

163

Der  SW-Element-Überblick  gibt einen groben Überblick über das zu realisierende  SW-Element. Aufgaben
und Ziele des SW-Elements werden überblickartig beschrieben. Zum besseren Verständnis wird die Rolle des
Elements innerhalb eines Systems oder einer SW-Einheit dargestellt.

C.1.12.3.2 Schnittstellenbeschreibung

Eine Schnittstelle repräsentiert die Grenze eines SW-Element
 s   zu seiner Umgebung. Sie beschreibt, welche
Daten an der Elementgrenze ausgetauscht werden, und die logischen Abhängigkeiten. Damit definiert die
Schnittstelle   die   Dienste,   die   vom   SW-Element   zu   erbringen   sind.   Ein   SW-Element   kann   mehrere
Schnittstellen besitzen.

In der Schnittstellenbeschreibung werden die funktionalen Anforderungen an das SW-Element gesammelt,
alle   Schnittstellen   festgelegt   und   im   Zusammenhang   dargestellt.   Zusammen   mit   den   nicht-funktionalen
Anforderungen enthält die Schnittstellenbeschreibung die notwendigen Informationen zur Entwicklung des
SW-Elements. In der Schnittstellenbeschreibung werden neben den Schnittstellen zu anderen SW-Elementen
auch   die   Schnittstellen   zur   Umgebung   beschrieben,   wie   die   grafische   Benutzerschnittstelle   oder
Schnittstellen zu anderen im Projekt zu entwickelnden Systemen.

Die   Beschreibung   der   funktionalen   Schnittstelle   teilt   sich   in   die   Beschreibung   ihres   statischen   und
dynamischen Verhaltens auf. Das statische Verhalten legt die Struktur der Aufrufe fest, über die Dienste des
SW-Elements   genutzt   werden   können.   Zur   Beschreibung   dienen   insbesondere   Methodensignaturen   und
Definitionen von Datentypen. Das  dynamische  Verhalten bestimmt  die Reihenfolge der Aufrufe  und die
logischen Abhängigkeiten der übermittelten Daten. Zur Beschreibung des dynamischen Verhaltens werden
häufig   Ablaufdiagramme
oder
Zustandübergangsdiagramme verwendet.

(Sequenzdiagramme,

  Sequence

  Message

  Charts)

Grundlage   für   die   Schnittstellenbeschreibung   sind   die   Schnittstellenübersicht   der  Architektur   sowie   die
Schnittstellenrealisierungen   der
  Die
Schnittstellenbeschreibung sollte sich daran orientieren, ob eine Wiederverwendung bereits bestehender SW-
Elemente möglich ist. Darüber hinaus ist bei der Beschreibung der Schnittstellen darauf zu achten, dass die
Schnittstellen stabil sind und damit eine möglichst lange Nutzung des SW-Elements möglich wird.

 Systemspezifikation

  Systemelemente.

übergeordneter

 en

C.1.12.3.3 Nicht-funktionale Anforderungen

Neben den funktionalen Anforderungen hat ein SW-Element eine Reihe nicht-funktionaler Anforderungen zu
erfüllen. Zu den häufig geforderten nicht-funktionalen Anforderungen speziell an ein SW-Element gehören
beispielsweise Benutzbarkeit, Antwortzeit, Transaktionsrate, Vertraulichkeit oder Datenintegrität.

Die nicht-funktionalen Anforderungen werden im Detail beschrieben und mit konkret geforderten Werten
belegt.   Die   für   das   SW-Element   relevanten   nicht-funktionalen   Anforderungen   werden   aus   den
Spezifikationen der übergeordneten Systemelemente beziehungsweise SW-Elemente abgeleitet.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland





164

 Referenz Produkte

C.1.12.3.4 Schnittstellenrealisierung

In   der   Schnittstellenrealisierung   erfolgt   die   Verfeinerung   der   funktionalen   Anforderungen   aus   der
Schnittstellenbeschreibung. Die Anforderungen werden konkretisiert, verfeinert und den SW-Element
 en    der
darunter liegenden Hierarchieebene zugeordnet.

Grundlage   der   Schnittstellenrealisierung   ist   die  SW-Architektur  der   übergeordneten  SW-Einheit  .  SW-
Komponente
 e    der   verschiedenen   Hierarchieebenen   werden   dort   im   Rahmen   der
Dekomposition identifiziert.

 n    und  SW-Modul

C.1.12.3.5 Verfeinerung nicht-funktionaler Anforderungen

Die   Verfeinerung   nicht-funktionaler   Anforderungen   erfolgt   parallel   zur   Verfeinerung   der   funktionalen
Anforderungen in der Schnittstellenrealisierung. Die nicht-funktionalen Anforderungen werden konkretisiert,
verfeinert und den SW-Element

 en    der darunter liegenden Hierarchiestufe zugeordnet.

So  kann  beispielsweise   eine   in  der   Schnittstellenbeschreibung  geforderte  Antwortzeit   von  höchstens   0,5
Sekunden auf zwei SW-Elemente mit der Anforderung von je 0,25 Sekunden verfeinert werden.

Die   verfeinerten  Anforderungen   bleiben   als   eigenständige  Anforderungen   bestehen   oder   werden   in   die
Schnittstellenrealisierung integriert.

C.1.12.3.6 Anforderungsverfolgung

Im   Rahmen   der  Anforderungsverfolgung   wird   die   Zuordnung   der   funktionalen   und   nicht-funktionalen
Anforderungen   an   das  SW-Element  auf   die   verfeinerten   Anforderungen   und   auf   untergeordnete   SW-
Elemente zusammenfassend dargestellt. Grundlage sind die Ergebnisse der Schnittstellenrealisierung sowie
der   Verfeinerung   nicht-funktionaler   Anforderungen.   Die   bidirektionale   Verfolgbarkeit   (d.h.   von
übergeordneten zu untergeordneten SW-Elementen und umgekehrt) muss dabei sichergestellt werden. Die
Darstellung kann beispielsweise anhand einer Matrix erfolgen.

C.1.12.4 Externes-SW-Modul-Spezifikation

Die  Externes-SW-Modul-Spezifikation  beschreibt alle funktionalen und nicht-funktionalen Anforderungen
an   ein  Externes   SW-Modul.   Zur   Erstellung   der   Spezifikation   werden   die   Anforderungen   aus   den
Spezifikationen   übergeordneter   Systemelemente   abgeleitet.   Sollten   im   Laufe   der   weiteren   Entwicklung
Änderungen   nötig   sein,   ist   zunächst   immer   die   jeweils   relevante   Spezifikation   anzupassen.   Die
Prüfspezifikation Systemelement definiert die Prüffälle zum Nachweis der Schnittstellen und Anforderungen
der Spezifikation.

Wesentliche Inhalte der Externes-SW-Modul-Spezifikation sind die Beschreibung der Anforderungen an das
Externes SW-Modul sowie die Festlegung der Schnittstellen, die es zu bedienen hat.

Im   Rahmen   der  Anforderungsverfolgung   wird   sichergestellt,   dass   alle  Anforderungen   an   das   Element
berücksichtigt werden. Die Erstellung der Externes-SW-Modul-Spezifikation erfolgt Hand in Hand mit dem
Architekturentwurf   der  SW-Einheit
 en   .   Zur   Sicherstellung   der   Konsistenz   zwischen   Spezifikationen   und
Architektur ist der SW-Architekt verantwortlich für die Erstellung beider Produkte.

Anforderungen   aus   der  Externes-SW-Modul-Spezifikation  können   sich   auf   die  Spezifikation   logistische
Unterstützung auswirken. Ebenso können Anforderungen der Logistik die Externes-SW-Modul-Spezifikation
beeinflussen.

Verantwortlich

SW-Architekt

Mitwirkend

Aktivität

Ergonomieverantwortlicher, Prüfer, SW-Entwickler

Externes-SW-Modul spezifizieren

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland






C.1 Produkte

Methoden

Werkzeuge

Vorlagen

Erzeugt durch

Inhaltlich abhängig

165

Anforderungsanalyse, Systemanalyse

Anforderungsmanagement, Integrierte Entwicklungsumgebung,
Konstruktion/Simulation, Modellierungswerkzeug

Externes-SW-Modul-Spezifikation(.odt|.doc)

Systementwurf:
SW-Architektur (Zu spezifizierende SW-Elemente)

Einfluss eines Fertigprodukts auf die Spezifikation externer Systemelemente:
Make-or-Buy-Entscheidung
Externe-Einheit/Externes-SW-Modul-Spezifikation als Bestandteil der
Vergabeunterlagen (Ausschreibung):
Vergabeunterlagen (Ausschreibung)

Entscheidungsrelevant
bei

Einheit(en) entworfen

C.1.12.4.1 Externes-SW-Modul-Überblick

Der Externes-SW-Modul-Überblick gibt einen groben Überblick über das zu realisierende Produkt Externes
SW-Modul  . Aufgaben und Ziele des Produktes  Externes SW-Modul  werden überblickartig beschrieben.
Zum besseren Verständnis wird die Rolle des Elements innerhalb einer SW-Einheit dargestellt.

C.1.12.4.2 Schnittstellenbeschreibung

Eine Schnittstelle repräsentiert die Grenze für ein Externes SW-Modul zu seiner Umgebung. Sie beschreibt,
welche Daten an der Elementgrenze ausgetauscht werden, und die logischen Abhängigkeiten. Damit definiert
die Schnittstelle die Dienste, die vom Produkt  Externes SW-Modul  zu erbringen sind. Ein  Externes SW-
Modul kann mehrere Schnittstellen besitzen.

In  der  Schnittstellenbeschreibung werden  die  funktionalen Anforderungen an das  Produkt  Externes  SW-
Modul  gesammelt,   alle   Schnittstellen   festgelegt   und   im  Zusammenhang   dargestellt.   Zusammen   mit   den
nicht-funktionalen Anforderungen enthält die Schnittstellenbeschreibung die notwendigen Informationen zur
Entwicklung   des   Produktes  Externes   SW-Modul.   In   der   Schnittstellenbeschreibung   werden   neben   den
 en     auch   die   Schnittstellen   zur   Umgebung   beschrieben,   wie   die
Schnittstellen   zu   anderen  SW-Element
grafische Benutzerschnittstelle oder Schnittstellen zu anderen im Projekt zu entwickelnden Systemen.

Die   Beschreibung   der   funktionalen   Schnittstelle   teilt   sich   in   die   Beschreibung   ihres   statischen   und
dynamischen Verhaltens auf. Das statische Verhalten legt die Struktur der Aufrufe fest, über die Dienste des
Produktes  Externes   SW-Modul  genutzt   werden   können.   Zur   Beschreibung   dienen   insbesondere
Methodensignaturen und Definitionen von Datentypen. Das dynamische Verhalten bestimmt die Reihenfolge
der Aufrufe und die logischen Abhängigkeiten der übermittelten Daten. Zur Beschreibung des dynamischen
Verhaltens   werden   häufig   Ablaufdiagramme   (Sequenzdiagramme,   Message   Sequence   Charts)   oder
Zustandübergangsdiagramme verwendet.

Grundlage   für   die   Schnittstellenbeschreibung   sind   die   Schnittstellenübersicht   der  Architektur   sowie   die
Schnittstellenrealisierungen   der
  Die
Schnittstellenbeschreibung sollte sich daran orientieren, ob eine Wiederverwendung bereits bestehender SW-
Elemente möglich ist. Darüber hinaus ist bei der Beschreibung der Schnittstellen darauf zu achten, dass die
Schnittstellen   stabil   sind   und   damit   eine   möglichst   lange   Nutzung   des   Produktes  Externes   SW-Modul
möglich wird.

 Systemspezifikation

  Systemelemente.

übergeordneter

 en

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland



166

 Referenz Produkte

C.1.12.4.3 Nicht-funktionale Anforderungen

Neben   den   funktionalen   Anforderungen   hat   ein  Externes   SW-Modul  eine   Reihe   nicht-funktionaler
Anforderungen zu erfüllen. Zu den häufig geforderten nicht-funktionalen Anforderungen speziell an ein SW-
Element  gehören   beispielsweise   Benutzbarkeit,   Antwortzeit,   Transaktionsrate,   Vertraulichkeit   oder
Datenintegrität.

Die nicht-funktionalen Anforderungen werden im Detail beschrieben und mit konkret geforderten Werten
belegt.   Die   für   das   Produkt   vom  Typ  Externes   SW-Modul  relevanten   nicht-funktionalen  Anforderungen
werden   aus   den   Spezifikationen   der   übergeordneten   Systemelemente   beziehungsweise   SW-Elemente
abgeleitet.

C.1.12.4.4

Lieferumfang

Es   sind   alle   Gegenstände   und   Dienstleistungen   aufzulisten,   die   während   des   Projektverlaufs   oder   bei
Abschluss des Projektes vom Auftragnehmer an den Auftraggeber zu liefern sind. Jede Lieferung erfordert
eine  Abnahmeprüfung.   Der   Lieferumfang   kann   je   nach   Vereinbarung   ein   System,   Teile   eines   Systems,
Dokumente und Dienstleistungen enthalten.

C.1.12.4.5 Abnahmekriterien und Vorgehen zur Abnahmeprüfung

Abnahmekriterien legen fest, welche Kriterien das gelieferte Produkt des Typs Externes SW-Modul erfüllen
muss,   um  den  Anforderungen  der  Externes-SW-Modul-Spezifikation  zu  entsprechen.   Sie   sollen   messbar
dargestellt   werden.  Aus   vertraglicher   Sicht   beschreiben   die  Abnahmekriterien   die   Bedingungen   für   die
Entscheidung, ob das Produkt vom Typ Externes SW-Modul die gestellten Anforderungen erfüllt oder nicht.
Die Abnahmekriterien beziehen sich sowohl auf funktionale als auch auf nicht-funktionale Anforderungen.

Aufbau und Anzahl der Abnahmekriterien sind durch den Auftraggeber zu skizzieren. Eine Strukturierung
der   Abnahmekriterien   nach   ihren   drei   wesentlichen   Bestandteilen,   Ausgangssituation,   Aktion(en)   und
erwartetes   Ergebnis,   ist  anzustreben.   In jedem Fall  müssen  die   erwarteten Ergebnisse   der  Abnahme   pro
Abnahmekriterium festgelegt werden.

Die   Erfüllung   der   Abnahmekriterien   wird   im   Rahmen   der   Eingangsprüfung   festgestellt.   Die
Abnahmekriterien gehen somit als Anforderungen in die Abnahmespezifikation ein.

Erzeugt

Prüfung der Lieferungen (Externes SW-Modul):
Abnahmeprotokoll, Abnahmespezifikation

C.1.13 Logistikelemente

C.1.13.1 Logistische Unterstützungsdokumentation

Die logistische Unterstützungsdokumentation ist eine inhaltlich zusammengehörende Menge auszuliefernder
Dokumentationselemente   eines   Systems   (siehe   auch  Produktstrukturierung).   Sie   besteht   aus
 en     und  Ausbildungsunterlagen  sowie   zusätzlich   -   abhängig   vom   erforderlichem
Nutzungsdokumentation
Umfang   der   Logistik   -   aus  Instandhaltungsdokumentationen,
 Instandsetzungsdokumentationen  und
Ersatzteilkatalogen.

Aus Produkthaftungsgründen sind in allen Dokumentationen vollständige und verbindliche Aussagen zum
bestimmungsgemäßen   Gebrauch   des   Systems   zu   machen.  Auch   der   vorhersehbare   bestimmungswidrige
Gebrauch   ist   zu   berücksichtigen.   Entsprechende   Hinweise   und   Warnungen   sind   unter   Aufzeigen   der
Gefahren und Risiken aufzunehmen. Hinweise zur Nutzung, Instandhaltung, Instandsetzung und Entsorgung
sind - auch unter Berücksichtigung des voraussichtlichen Benutzers - zu verfassen.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


C.1 Produkte

167

Allen  Geräten  sind eine  Bedienungsanleitung und die  sicherheitsrelevanten  Informationen  in  Papierform
beizulegen.   Eine   ausschließlich   elektronische   Bedienungsanleitung   ist   auch   bei
 Produkte  mit
Anzeigemöglichkeiten nicht ausreichend.

Verantwortlich

Technischer Autor

Aktivität

Methoden

Werkzeuge

Besteht aus

Erzeugt durch

Zur logistischen Unterstützungsdokumentation integrieren

Review, Test

Konstruktion/Simulation

Nutzungsdokumentation, Ausbildungsunterlagen

Systementwurf:
Pflichtenheft (Gesamtsystementwurf) (Dekomposition des Gesamtsystems)

Entscheidungsrelevant
bei

System integriert

Sonstiges

Keine Produktvorlage

C.1.13.2 Nutzungsdokumentation

Die  Nutzungsdokumentation  enthält   alle   Angaben,   die   ein   Nutzer   benötigt,   um   das   System
bestimmungsgemäß bedienen zu können und bei Problemen richtig zu reagieren. Die Art und Anzahl der zu
erstellenden   Nutzungsdokumentationen   entspricht
  den   Vorgaben   aus   dem  Pflichtenheft
(Gesamtsystementwurf).

Verantwortlich

Mitwirkend

Aktivität

Vorlagen

Teil von

Erzeugt durch

Technischer Autor

Ergonomieverantwortlicher, QS-Verantwortlicher, SW-Architekt, SW-Entwickler,
Systemarchitekt

Nutzungsdokumentation erstellen

Nutzungsdokumentation(.odt|.doc)

Logistische Unterstützungsdokumentation

Systementwurf:
Pflichtenheft (Gesamtsystementwurf) (Dekomposition des Gesamtsystems)

C.1.13.2.1 Warn- und Sicherheitshinweise

Die  Warn-   und   Sicherheitshinweise  beschreiben   die   für   den   Nutzer   sicherheitsrelevanten  Aspekte   des
Systems.   Diese   müssen   während   des   gesamten   Systemlebenszyklus   beachtet   und   eingehalten   werden,
angefangen   von   der   Inbetriebnahme   bis   zur  Aussonderung  des   Systems.  Warn-   und   Sicherheitshinweise
müssen unübersehbar, möglichst am Anfang der Dokumentation, eingebracht werden.

C.1.13.2.2 Umfang und Funktionsweise des Systems

In diesem Thema wird das System ausgerichtet auf den Nutzer dargestellt. Über die Beschreibung lernt der
Nutzer die für ihn relevanten Bestandteile und die Funktionsweise des Systems kennen. Die Beschreibung
des Systems beinhaltet unter anderem eine Gesamtansicht des Systems, eine technische Beschreibung des
Systems und dessen technische Daten.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

168

 Referenz Produkte

C.1.13.2.3

Installation und Bedienung

Die   Bedienungsanleitung   beschreibt   den   sachgerechten   Gebrauch   des   Systems.   Sie   beschreibt
Arbeitsabläufe, wie sie Nutzer mit dem System ausführen.

Abhängig   von   der   Nutzungsart   kann   die   Bedienungsanleitung   verschiedene   Aspekte   beinhalten   wie
beispielsweise Inbetriebnahme, Administration, Bedienung und Fehlerüberwachung. Die Beschreibung der
Bedienung muss sich in Tiefe und Detaillierung an den Kenntnissen der zu erwartenden Nutzer orientieren.

C.1.13.2.4 Pflegeanleitung für das System

Die Pflege umfasst alle einfachen Instandhaltungstätigkeiten, die der Nutzer ohne Hilfsmittel durchführen
kann, zum Beispiel die Reinigung des Systems, Austausch von Verschleißteilen und Betriebsflüssigkeiten
und   Überwachung   von   Betriebskennzahlen,   Update   des   Antivirenschutzes   oder   Durchführung   eines
Backups.

C.1.13.3 Ausbildungsunterlagen

Die   Ausbildung   für   ein   System   gliedert   sich   in   unterschiedliche   Ausbildungsmaßnahmen.   Für   diese
Maßnahmen sind diverse Unterlagen notwendig, zum Beispiel Lehrplan und Lernunterlagen. Die Ausbildung
kann auf unterschiedlichen Medien realisiert werden, beispielsweise auf Printmedien oder als Computer-
Unterstützte Ausbildung (CUA).

Ausbildungen   werden   in   der   Regel   auf   Tätigkeitsprofile   ausgerichtet,   zum   Beispiel   Bediener-,
Instandhaltungs-,   Instandsetzungs-   und   Serviceausbildung.   Für   sicherheitskritische   Systeme   findet   eine
gesonderte Sicherheitsausbildung statt.

Verantwortlich

Technischer Autor

Mitwirkend

Aktivität

Vorlagen

Teil von

Erzeugt durch

C.1.13.3.1

Lehrplan

QS-Verantwortlicher, SW-Architekt, SW-Entwickler, Systemarchitekt

Ausbildungsunterlagen erstellen

Ausbildungsunterlagen(.odt|.doc)

Logistische Unterstützungsdokumentation

Systementwurf:
Pflichtenheft (Gesamtsystementwurf) (Dekomposition des Gesamtsystems)

Der Lehrplan gibt einen Überblick über die Inhalte, Ziele und die Gestaltung einer Ausbildungsmaßnahme.
Dabei   enthält   er   Informationen   über   z.B.   Stundenplan,   minimale   und   maximale   Teilnehmerzahl   und
geforderte Vorbildung der Teilnehmer, die notwendig sind, um eine konkrete Ausbildung durchführen zu
können.

C.1.13.3.2

Lehrunterlagen

Die Lehrunterlagen dienen dem Dozenten als Leitfaden und Unterrichtsmaterial für die Durchführung der
Ausbildung. Sie beinhalten alle für die Vermittlung des Stoffes benötigten Mittel, Kommentare und Notizen,
inklusive der didaktischen Erläuterungen zu den Unterlagen. Die Lehrunterlagen können in unterschiedlicher
Form bereitgestellt werden, zum Beispiel als Präsentationen, Schautafeln, Video- und Audiomaterial oder als
Computer-Unterstützte Ausbildung (CUA).

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

C.1.13.3.3

Lernunterlagen

169

Die Lernunterlagen sind die Unterlagen für die Auszubildenden. Die Unterlagen dienen zum individuellen
Vor- und Nachbereiten von Ausbildungsmaßnahmen. Sie beschreiben den vollständigen Lernstoff und geben
über   zusätzliche   Übungsaufgaben   eine   Möglichkeit   zur   Lernkontrolle.   Die   Lernunterlagen   können   in
unterschiedlicher Form bereitgestellt werden, wie zum Beispiel als Präsentationen, Ausbildungshandbuch,
Video- und Audiomaterial oder als Computer Unterstützte Ausbildung (CUA).

C.1.13.3.4 Durchführungsnachweis

Es gibt zwei Arten von Durchführungsnachweis
 en   . Die eine bescheinigt dem Teilnehmer die Teilnahme an
einer Ausbildungsmaßnahme mit einem bestimmten Erfolg, beispielsweise durch ein Zeugnis. Die andere ist
der zahlungsbegründende Nachweis für den Dozenten, dass die Ausbildung erfolgreich und im vereinbarten
Umfang durchgeführt wurde, wie bespielsweise eine Teilnehmerliste mit Unterschriften.

C.1.14 Softwareentwicklung nach Scrum (AG)

C.1.14.1 Anforderungskonzept

Das  Anforderungskonzept  ersetzt   bei   der   agilen   Softwareentwicklung   das   Lastenheft   und   enthält   die
(grobgranulare)   funktionale   Leistungsbeschreibung   des   gewünschten   Systems.   Auf   Grundlage   des
Anforderungskonzept
 s    erstellt   der  Product   Owner  im  Projektverlauf   die   Einträge   des   Product   Backlogs.
Hierfür können verschiedene Methoden (Epics/User Stories, Use Case 2.0 etc.) zur Anwendung kommen. In
jedem Fall sind für die Einträge Akzeptanzkriterien zu definieren, anhand derer die Umsetzung überprüft
werden kann.

Für   eine   geeignete   Struktur   des   Anforderungskonzepts   kann   sich   der  Product   Owner  am   Lastenheft
orientieren.   Das  Anforderungskonzept  ist   jedoch   deutlich   gröber,   kürzer   und   enthält   keine   detaillierten
(konstruktiven) Anforderungen.

Verantwortlich

Product Owner

Aktivität

Anforderungskonzept erstellen

Entscheidungsrelevant
bei

Anforderungen festgelegt, Produktvision entworfen

Sonstiges

Initial

C.1.14.2 Product Backlog

Das Product Backlog ist die geordnete Liste der Anforderungen samt ihrer spezifischen Akzeptanzkriterien
an das zu erstellende System. Es dient als alleinige Quelle für sämtliche Änderungen und Erweiterungen
während der Projektlaufzeit und der Verständigung zwischen Product Owner und dem Entwicklungsteam des
Auftragnehmers über die zu leistende Arbeit. Üblicherweise bilden User Stories und Epics die Backlog-
Einträge, es sind aber auch andere Einträge möglich.

Im  Product Backlog  sind alle zur Umsetzung in einem zukünftigen Release vorgesehenen Eigenschaften,
Funktionen, Verbesserungen und Fehlerbehebungen aufgeführt. Ein Eintrag (Product Backlog Item) wird
mindestens mit

➢ einer eindeutigen Nummer,

➢ einer Beschreibung (Nutzen),

➢ der Priorität,

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland



170

 Referenz Produkte

➢ den zu erfüllenden Kriterien für die Einplanung im Sprint (Definition of Ready),

➢ der relativen Umfangsschätzung des Entwicklungsteams (z.B. Story Points) und

➢ den Akzeptanzkriterien

beschrieben. Die Priorität leitet sich aus der Position des Eintrages im Backlog ab (der Wichtigkeit nach
absteigend). Jeder Eintrag erhält dadurch eine eindeutige Priorisierung gegenüber den übrigen Einträgen.
Backlog-Einträge werden nach Ihrer Abarbeitung nicht mehr geändert. Veränderte Anforderungen werden
durch neue Einträge im Backlog in das Projekt eingebracht.

Für   die   Inhalte,   den   Zugriff   und   die   Reihenfolge   (Priorität)   der   Einträge   ist   der  Product   Owner
verantwortlich. Das Product Backlog wird während der Projektlaufzeit kontinuierlich fortgeschrieben.

Der  Product   Owner  prüft   und   akzeptiert   anhand   der   von   ihm   in   den   Backlog-Einträgen   hinterlegten
Akzeptanzkriterien die Umsetzungsergebnisse.

Verantwortlich

Product Owner

Aktivität

Product Backlog erstellen/fortgeschreiben

Entscheidungsrelevant
bei

Sprint gestartet

Sonstiges

Initial

C.1.14.3 Inkrement (von AN)

Das Inkrement (von AN) ist das vom Auftragnehmer am Ende eines Sprints gelieferte Ergebnis aus den im
Sprint   fertiggestellten   Product   Backlog   Items   und   den   Inkrementen   aller   vorangegangenen   Sprints.   Ein
Inkrement in der Softwareentwicklung ist immer eine lauffähige Software, die potentiell produktivfähig sein
sollte. Ob und in welchem Zyklus sie einer Abnahme und betrieblichen Freigabe unterworfen und in Betrieb
genommen wird, wird anhand des Releaseplans entschieden.

Verantwortlich

Product Owner

Entscheidungsrelevant
bei

Sprint abgeschlossen

Sonstiges

Extern

C.1.15 IT-Organisation und Betrieb

C.1.15.1 Vorgaben zum IT-Betrieb

Im Produkt Vorgaben zum IT-Betrieb sind die Voraussetzungen zu beschreiben, die ein IT-System für einen
nachhaltigen und sicheren Betrieb in der Organisation erfüllen muss. Sie sind Teil der Anforderungen an das
zu   entwickelnde   System   und   werden   in   der   Regel   von   den   Vorgaben   des  Informationssicherheits-
Managementsystem
 s    (ISMS) der Organisation abgeleitet. Die Einhaltung der  Vorgaben zum IT-Betrieb  ist
die Voraussetzung für die Betriebliche Freigabeerklärung eines IT-Systems.

Das Produkt Vorgaben zum IT-Betrieb kann neben verpflichtenden Vorgaben Empfehlungen enthalten, deren
Einhaltung den nachhaltigen und sicheren Betrieb des IT-Systems erleichtert oder verbessert.

Verantwortlich

Mitwirkend

Betriebsverantwortlicher

Betriebsbeauftragter

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


C.1 Produkte

Aktivität

Vorlagen

Erzeugt durch

Inhaltlich abhängig

Entscheidungsrelevant
bei

C.1.15.1.1

Fertigprodukte

171

Vorgaben zum IT-Betrieb festlegen

Vorgaben zum IT-Betrieb(.odt|.doc)

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zum IT-Betrieb)

Berücksichtigung des IT-Betriebs bei der Anforderungsfestlegung:
Lastenheft (Anforderungen)
Zusammenhang zwischen betrieblichen Anforderungen und
Leistungsvereinbarung:
Leistungsvereinbarung (SLA/OLA/UC)

Anforderungen festgelegt, Produktvision entworfen

In   diesem   Thema   wird   beschrieben,   welche   Fertigprodukte   (z.B.   Betriebssysteme,   Infrastruktur-
Anwendungen,   Datenbanken,   Frameworks,   Querschnittsdienste)   der   IT-Betrieb   zur   Nutzung   durch   IT-
Systeme  betreibt  oder  zum Betrieb  freigegeben hat.  Die  Fertigprodukte  sind so präzise  wie  möglich zu
beschreiben,   insbesondere   mit   Produktname,   Hersteller,   Version,   Lizenz   und   Schnittstellen.   Das
Zusammenspiel   der   Fertigprodukte   im   Betrieb   sollte   grafisch   aufbereitet   werden,   beispielsweise   in
Architektur-Diagrammen.   Zu   benennen   sind   auch   die   vom   IT-Betrieb   explizit   ausgeschlossenen
Fertigprodukte (Blacklist).

Strategien und Richtlinien zu Auswahl und Ausschluss von Fertigprodukten sollten beschrieben werden, um
den Lösungsraum für die Entwicklung neuer IT-Systeme zu präzisieren. Sie resultieren beispielsweise aus

➢ dem vorhandenen Betriebs-Know-How der Administratoren und Mitarbeiter,

➢ vorhandenen Rahmenverträgen mit Basis-Infrastruktur-Anbietern,

➢ vorhandenen Richtlinien zur Verwendung von Open Source Software,

➢ vorhandenen Richtlinien zum System-Management, z.B. Patch-Management,

➢ vorhandenen Richtlinien zum Application-Monitoring,

➢ vorhandenen Richtlinien zum Freigabeprozess, einschließlich des Tests, oder

➢ Inkompatibilitäten mit vorhandener Software- oder Systemarchitektur.

C.1.15.1.2

IT-Systeme

Hier wird beschrieben, welche grundlegenden Eigenschaften IT-Systeme aufweisen müssen oder sollen, um
vom   IT-Betrieb   nachhaltig   und   sicher   betrieben   werden   zu   können.   Aufzuführen   sind   notwendige,
empfohlene   und   erlaubte   IT-Spezifikationen   für   Kommunikationsprotokolle   und   Datenformate   sowie
Vorgaben für verlangte Eigenschaften, beispielsweise

➢ Isolierbarkeit (Trennung der Umgebungen miteinander agierender Komponenten),

➢ Virtualisierbarkeit (Befähigung zum Betrieb in einer virtuellen Maschine),

➢ Härtbarkeit (Zuschaltung betrieblicher Sicherheitsmaßnahmen ohne funktionale Einbußen),

➢ Belastbarkeit (Performance, Lese-/Schreibdurchsatz, etc.),

➢ Testbarkeit (Durchführung von funktionalen, Last- und Sicherheitstests),

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

172

 Referenz Produkte

➢ sichere Wartbarkeit (z.B. Management der Betriebsumgebung über separates Wartungsnetz),

➢ Aktualisierbarkeit (Einspielen neuer Versionen und Komponenten, ggf. im laufenden Betrieb).

Solche Vorgaben können sich aus Strategiedokumenten, Architekturvorgaben, Sicherheitsrichtlinien und IT-
Bebauungsplänen der Organisation ergeben, aber auch aus spezifischen Richtlinien für bestimmte Server-
Rollen wie Domain-Controller, Web- und Applikationsserver. Sie haben in der Regel Auswirkungen auf die
Systemarchitektur   eines   zu   entwickelnden   IT-Systems   und   sollten   daher   so   beschrieben   sein,   dass   ein
Auftragnehmer auf dieser Grundlage eine passende Systemarchitektur erstellen kann. Die den Vorgaben zu
Grunde liegenden Strategien und Grundsätze sollten offengelegt werden. Beispiele dafür sind

➢ bestmögliche Absicherung von Systemen,

➢ Vorrang der Interoperabilität,

➢ Reduzierung von Hersteller-Abhängigkeiten,

➢ vorrangige oder ausschließliche Verwendung offener IT-Standards,

➢ vorrangiger oder ausschließlicher Betrieb von IT-Systemen in virtualisierter Umgebung.

C.1.15.1.3 Netze

Hier   wird   beschrieben,   welchen   Rahmenbedingungen   Netze   und   Subnetze   eines   zu   entwickelnden   IT-
Systems genügen müssen. Netz-Zugänge, Netz-Segmente mit jeweiligem Schutzbedarf und Eigenschaften
(Latenzen, Bandbreiten) für Regelbetrieb, Entwicklung, Test und Schulung neuer IT-Systeme sowie für die
Verwaltung   ihrer   Betriebsumgebungen   müssen   klar   ausgewiesen   und   freigegebene   Ports   und   Protokolle
benannt sein.

Anforderungen   an   Netze   resultieren   beispielsweise   aus   Netz-   und   Sicherheitskonzepten,
Servicevereinbarungen,   Richtlinien   für   aktive   Netzkomponenten,   bisherigen  Schutzbedarfsfeststellung
 en
oder Kommunikationsbeziehungen zu externen Providern, Liegenschaften und Netzteilnehmern. Falls daraus
Anforderungen an neue IT-Systeme resultieren, müssen sie benannt und erläutert werden.

Beispiele für Netz-Vorgaben sind

➢ Einschränkungen bei der Verwendung von Netzwerk-Protokollen und Ports,

➢ Maßnahmen zur Port-Security ab hohem Schutzbedarf,

➢ Vorgaben zur Konfiguration und Software-Aktualisierung von Routern,

➢ Latenzen oder Bandbreitenbeschränkung beim Zugriff auf bestimmte Netze.

Konkrete   Netzvorgaben   sind   von   zunehmender   Bedeutung,   da   moderne   Softwaresysteme   häufig   von
beliebigen   Kommunikationsverbindungen   zu   anderen   Netzen   und   insbesondere   zum   Internet   (z.B.   zur
automatischen Aktualisierung oder beim Build-Prozess) ausgehen.

C.1.15.1.4 Prozesse

In diesem Thema ist zu beschreiben, welchen Rahmenbedingungen neue IT-Systeme hinsichtlich etablierter
Prozesse des Betreibers genügen müssen. Insbesondere ist zu beschreiben, welche prozessualen Vorgaben
neue IT-Systeme in welcher Weise unterstützen müssen.

Solche Vorgaben können aus einem prozessualen Vorgehensmodell wie ITIL, aus rechtlichen Pflichten wie
der   EU-Datenschutz-Grundverordnung  oder   aus   sicherheitsbezogenen   Betriebsprozessen   für   Auswahl,
Installation, Härtung, Systemaktualisierung und Aussonderung herrühren.

Beispiele für solche Vorgaben sind

➢ die Bereitstellung bestimmter Auswertungen,

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


C.1 Produkte

173

➢ die Bereitstellung von Systemdokumentation,

➢ die   Bereitstellung   verfahrensspezifischer   Sicherheitskonzepte   in   einem   bestimmten   Format   nach
vorgegebener Namenskonvention und Vorgehensweise (z.B. zum Import in ein ISMS-Werkzeug),

➢ die   Bereitstellung   von   Log-Informationen   in   einem   bestimmten   Format   einschließlich   der
Gewährleistung von Authentizität und Vertraulichkeit (z.B.: zur Integration in eine Logging- und
Monitoringlösung des Betreibers),

➢ die automatisierbare Überprüfbarkeit bestimmter (Sicherheits-)Parameter des IT-Systems.

C.1.15.2 Erweiterung der Vorgaben zum IT-Betrieb

Der   Auftragnehmer   leitet   aus   dem   Pflichtenheft,   der   System-   bzw.   SW-Architektur   und   der
Sicherheitskonzeption  die   betrieblichen  Anforderungen   des   IT-Systems   ab   und   vergleicht   sie   mit   den
Vorgaben zum IT-Betrieb. Die für den Betrieb des IT-Systems notwendigen Ergänzungen und Änderungen
dieser Vorgaben werden in den nachfolgenden Themen beschrieben.

Die   Themen   entsprechen   denen   der   Vorgaben   zum   IT-Betrieb.   Zu   jedem   Thema   können   begründete
Empfehlungen zur Aufnahme, Änderung oder Streichung von Vorgaben zum IT-Betrieb aufgeführt werden.
Änderungen   an   verbindlichen   Vorgaben   und   Ausschlüssen   dürfen   nur   beim   Vorliegen   entsprechender
Vereinbarungen mit dem Auftraggeber aufgeführt werden und müssen auf die jeweiligen Vertragszusätze
verweisen.

Das Produkt  Erweiterung der Vorgaben zum IT-Betrieb  ist Bestandteil der  Lieferung  an den Auftraggeber.
Dieser sorgt für die Weitergabe des Produkts an den Betriebsbeauftragten der Organisation.

Verantwortlich

Betriebsverantwortlicher

Aktivität

Vorlagen

Erzeugt durch

Vorgaben zum IT-Betrieb erweitern

Erweiterung der Vorgaben zum IT-Betrieb(.odt|.doc)

Systementwurf:
Pflichtenheft (Gesamtsystementwurf) (Nicht-funktionale Anforderungen), SW-
Architektur (Auswirkungen auf den IT-Betrieb), Systemarchitektur
(Auswirkungen auf den IT-Betrieb)

Inhaltlich abhängig

Berücksichtigung des IT-Betriebs bei der Systemerstellung:
Pflichtenheft (Gesamtsystementwurf)

Entscheidungsrelevant
bei

C.1.15.2.1

Fertigprodukte

Gesamtsystem entworfen, System entworfen, Einheit(en) entworfen

Hier   werden   die   in   den   Vorgaben   zum   IT-Betrieb   nicht   enthaltenen,   aber   zum   Betrieb   des   IT-Systems
notwendigen   Fertigprodukte   bzw.   Produktversionen   aufgeführt.   Fertigprodukte,   die   den   Betrieb   des   IT-
Systems   be-   oder   verhindern   und   daher   ausgeschlossen   werden   sollten,   sind   mit   einer   entsprechenden
Begründung aufzuführen.

C.1.15.2.2

IT-Systeme

Hier   werden   die   in   den   Vorgaben   zum   IT-Betrieb   nicht   enthaltenen,   aber   zum   Betrieb   des   IT-Systems
notwendigen IT-Spezifikationen aufgeführt. In den Vorgaben zum IT-Betrieb verlangte Eigenschaften, die
den Betrieb des IT-Systems be- oder verhindern und daher nicht eingehalten werden können, sind mit einer
entsprechenden Begründung aufzuführen.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

174

C.1.15.2.3 Netze

 Referenz Produkte

Hier   werden   die   in   den   Vorgaben   zum   IT-Betrieb   nicht   enthaltenen,   aber   zum   Betrieb   des   IT-Systems
notwendigen Netzwerk-Eigenschaften (z.B. Zugriffserlaubnis für Netzsegmente, Portfreigaben, Einrichtung
von Subnetzen, separates Wartungsnetz, Mindest-Bandbreiten etc.) aufgeführt. Netzwerk-Vorgaben, die den
Betrieb des IT-Systems  be- oder verhindern und daher nicht eingehalten werden können, sind mit einer
entsprechenden Begründung aufzuführen.

C.1.15.2.4 Prozesse

Hier   werden   die   in   den   Vorgaben   zum   IT-Betrieb   nicht   enthaltenen,   aber   zum   Betrieb   des   IT-Systems
notwendigen Prozess-Vorgaben (z.B. regelmäßiges Pentesting durch Dritte) aufgeführt. Prozessvorgaben, die
den Betrieb des IT-Systems be- oder verhindern und daher nicht eingehalten werden können, sind mit einer
entsprechenden Begründung aufzuführen.

C.1.15.3 Betriebliche Freigabeerklärung

Die  Betriebliche   Freigabeerklärung  bestätigt,   dass   das   entwickelte   (Teil-)System  den  Vorgaben   zum   IT-
Betrieb entspricht und in den Betrieb überführt werden kann.

Verantwortlich

Betriebsverantwortlicher

Vorlagen

Erzeugt durch

Inhaltlich abhängig

Betriebliche Freigabeerklärung(.odt|.doc)

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zum IT-Betrieb)

Relevanz des Prüfprotokolls Inbetriebnahme für die Betriebliche
Freigabeerklärung:
Prüfprotokoll Inbetriebnahme

Entscheidungsrelevant
bei

Systembetrieb freigegeben

Sonstiges

Extern

C.1.15.3.1 Beurteilung des Systems aus Sicht des Betriebes

Das   Thema   enthält   eine   auf   die  Vorgaben   zum   IT-Betrieb  bezogene   Bewertung   der   im  Prüfprotokoll
Inbetriebnahme  aufgeführten   Prüfergebnisse.   Entsprechend   der   Bewertung   ist   festzulegen,   ob   eine
Inbetriebnahme aus Betriebssicht erfolgen kann.

C.1.15.3.2 Beurteilung des Systems aus Sicht der Informationssicherheit

Das   Thema   enthält   eine   auf   die  Vorgaben   zur   Informationssicherheit  bezogene   Bewertung   der   im
Prüfprotokoll Inbetriebnahme aufgeführten Prüfergebnisse. Entsprechend der Bewertung ist festzulegen, ob
eine Inbetriebnahme aus Sicht der Informationssicherheit erfolgen kann.

C.1.15.3.3 Beurteilung des Systems aus Sicht des Datenschutzes

Das  Thema   enthält   eine   auf   die  Vorgaben   zum   Datenschutz  bezogene   Bewertung   der   im  Prüfprotokoll
Inbetriebnahme  aufgeführten   Prüfergebnisse.   Entsprechend   der   Bewertung   ist   festzulegen,   ob   eine
Inbetriebnahme aus datenschutzrechtlicher Sicht erfolgen kann.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

175

C.1.15.3.4 Anhang: Prüfprotokoll Inbetriebnahme

Das   entsprechende  Prüfprotokoll   Inbetriebnahme  wird   der   Betrieblichen   Freigabeerklärung   als  Anhang
beigefügt.

C.1.15.4 Leistungsvereinbarung (SLA/OLA/UC)

Dieses Produkt beschreibt die nach dem Projektende getroffenen Leistungsvereinbarungen zwischen den
folgenden Rollen bzw. Parteien:

➢ Anwender

➢ Verfahrensverantwortlicher (Fachseite)

➢ Verfahrensverantwortlicher (IT-Betrieb)

➢ Verfahrensverantwortlicher (Weiterentwicklung)

Die   Leistungsvereinbarung   betrifft   die   laufende   Erbringung   eines   Dienstes   bzw.   Services,   insbesondere
zwischen der Fachseite und dem IT-Betrieb. Wenn die Fachseite gegenüber anderen Behörden (Anwender
 n  )
als Dienstleister auftritt, dann kann auch hier eine Leistungsvereinbarung durch das Projekt geschlossen oder
vorbereitet   werden.   Ebenso  kann   es   notwendig   sein,   die   Pflege   und Weiterentwicklung   (Bugfixes,   neue
fachliche Anforderungen, etc.) zu regeln.

ITIL V3 kennt 3 Arten einer Leistungsvereinbarung:

➢ Ein  Service Level Agreement (SLA)  oder Leistungsvereinbarung (DGV) bezeichnet einen Vertrag
bzw.   die   Schnittstelle   zwischen   Auftraggeber   und   Dienstleister   für   wiederkehrende   IT-
Dienstleistungen.

➢ Ein  Operational Level Agreement (OLA)  dient oft der Unterstützung bzw. der Absicherung eines
SLA.   Da   diese   Vereinbarungen   zwischen   Abteilungen   der   gleichen   Organisation   geschlossen
werden, gelten diese in der Regel nur für den Dienstleister intern.

➢ Ein Underpinning Contract (UC) wiederum ist ein Absicherungsvertrag einer vereinbarten Leistung

zwischen dem IT-Service-Anbieter und einem für ihn tätigen Dienstleister.

Das   V-Modell   kann   nicht   vorgeben,   in   welcher   organisatorischen   Konstellation   die   einzelnen   Parteien
zueinander stehen. Deshalb sind grundsätzlich alle drei Arten einer Leistungsvereinbarung denkbar und es
muss individuell entschieden werden, ob es sich um SLA, OLA oder UC handelt.

Unabhängig   von   ihrer  Art   fasst   eine   Leistungsvereinbarung   die   Dienstleistungen   und   die   Qualität   der
Erbringung  verbindlich auf  Basis  der  Anforderungen  an das  System  (siehe  Lastenheft  (Anforderungen))
zusammen. Folgende Informationen sind dabei zu dokumentieren:

➢ Bezeichnung der zu erbringenden Dienstleistung

➢ Freigabeinformationen (Fach- und IT-Seite)

➢ Laufzeit, inkl. Beginn, Ende und Regelungen bzgl. der Beendigung der Vereinbarung

➢ Beschreibung des angestrebten Ergebnisses

➢ Verweis auf mitgeltende Vereinbarungen/Verträge

➢ Servicezeiten

➢ Erforderliche Support-Typen und Support Levels

➢ Anforderungen an die einzelnen Service Levels

➢ Verpflichtende Standards

➢ Verantwortlichkeiten

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland










176

➢ Kosten

Verantwortlich

Projektleiter

 Referenz Produkte

Mitwirkend

Aktivität

Vorlagen

Erzeugt durch

Inhaltlich abhängig

Anwender, Verfahrensverantwortlicher (Fachseite), Verfahrensverantwortlicher
(IT-Betrieb), Verfahrensverantwortlicher (Weiterentwicklung)

Leistungsvereinbarung (SLA/OLA/UC) erstellen

Leistungsvereinbarung (SLAOLAUC)(.odt|.doc)

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zum IT-Betrieb)

Zusammenhang zwischen betrieblichen Anforderungen und
Leistungsvereinbarung:
Vorgaben zum IT-Betrieb

Entscheidungsrelevant
bei

Projekt abgeschlossen

C.1.15.4.1

Freigabeinformationen der Fach- und IT-Seite

In   diesem   Thema   sind   alle   für   die   Freigabe   relevanten   Informationen   der   Fach-   und   der   IT-Abteilung
dokumentiert. Insbesondere sind hier die Ansprechpartner bzw. Vertragspartner zu nennen, zwischen denen
die Leistungsvereinbarung (SLA/OLA/UC) geschlossen wird.

C.1.15.4.2

Leistungsvertrag

Der Leistungsvertrag in der Leistungsvereinbarung (SLA/OLA/UC) muss folgende Inhalte dokumentieren:

➢ Bezeichnung des Service

➢ Regelungen zur Laufzeit (Beginn, Befristung, Kündbarkeit)

➢ Regelungen zur Vergütung

➢ Regelungen zur Service-Erbringung

➢ Verantwortlichkeiten (Pflichten der IT- und der Fachseite)

Gegebenenfalls   sind   hier   neben   den   kaufmännischen   und   rechtlichen   Einheiten   auch   allgemeine
Geschäftsbedingungen zu referenzieren.

C.1.15.4.3

Leistungsumfang

Der Leistungsumfang der Leistungsvereinbarung (SLA/OLA/UC) umfasst verschiedene Aspekte, die hier zu
dokumentieren sind. Insbesondere zählen dazu:

➢ die zu unterstützenden Geschäftsprozesse und Aktivitäten

➢ die Servicezeiten

➢ die relevanten Support-Typen und Levels

Bei   der   Beschreibung   der   Geschäftsprozesse   ist   insbesondere   die   Kritikalität   der   einzelnen   Services   zu
beschreiben,   die   die   Geschäftsprozesse   abdecken.   Hierbei   sind   die   kritischen   Geschäftsprozesse   (vital
business function, VBF), die verwendeten Geschäftsdaten sowie eine Risiko- und Schadensbewertung für
den Fall des Verlusts der Services und/oder Daten zu dokumentieren.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

177

Ebenfalls im Rahmen des Leistungsumfangs sind die Servicezeiten zu dokumentieren, in denen ein Service
zur Verfügung steht und ob es Ausnahmen, z.B. für Wartungsarbeiten gibt etc. Diese Informationen sind in
die   Aussagen   zu   den   gewünschten   Support-Typen   und   Levels   zu   integrieren,   in   denen   z.B.   die
Vereinbarungen hinsichtlich Reaktions- und Lösungszeiten beschrieben sind.

C.1.15.4.4 Anforderungen

Dieses   Thema   fasst   die   Anforderungen   zusammen,   die   Grundlage   für   den  Leistungsvertrag  und   den
Leistungsumfang sind. Die Anforderungen, insbesondere an den Service-Level, sind unter Berücksichtigung
der Aspekte:

➢ Verfügbarkeit (Service Availability)

➢ Verfügbarkeit im Katastrophenfall (Service Continuity)

➢ Performanz (Performance, Capacity)

zu   dokumentieren.   Insbesondere   bei   den   Verfügbarkeitsanforderungen   müssen   verschiedene   Parameter
definiert werden, wie z.B. Ziele bzgl. der Verfügbarkeit, der Zuverlässigkeit (Mean Time Between Failures,
Mean  Time   Between   Incidents)   und   der  Wartbarkeit   (Mean  Time   to   Restore,   Downzeiten   für  Wartung,
Ankündigungsfristen, Einschränkungen)

Zusätzlich dazu muss dokumentiert sein, welche Anforderungen bzgl. der Verfügbarkeit im Katastrophenfall
bestehen. Im Detail sind hier Festlegungen bzgl. der Zeiträume zu treffen, in denen ein festgelegter Service
Level wieder erreicht sein muss und innerhalb dessen der "normale" Service Level wieder verfügbar sein
muss.

Im Bereich der Performance sind die benötigten Parameter ebenfalls detailliert darzustellen, also z.B.:

➢ Welche Kapazitäten (Anzahl der Anwender, Transaktionen etc.) müssen zur Verfügung stehen?

➢ Über welche Antwortzeiten müssen die Systeme (Services) verfügen?

➢ Ist   eine   mittel-/langfristige   Skalierung   des   Systems   zu   berücksichtigen   und   wie   sehen   die

entsprechenden Anforderungen hierzu aus?

C.1.16 Ausschreibungswesen (Vergabeakte)

C.1.16.1 Beschaffungskonzeption

Die  Beschaffungskonzeption  bildet gemäß  UfAB  den Abschluss der ersten Phase einer Beschaffung und
behandelt folgende Aspekte:

➢ Aspekte einer produktspezifischen Beschaffung

➢ Aspekte im Zusammenhang mit dem Gebot der losweisen Vergabe

➢ Aspekte der Nachhaltigkeit

➢ Vorgabe eines Selbstausführungsgebotes

➢ Aspekte im Zusammenhang mit optionalen Leistungen

➢ Einbeziehung von Know-how der Anbietermärkte

➢ Verhandlungsverfahren / Verhandlungsvergaben ohne Teilnahmewettbewerb

➢ Festlegung von Eignungskriterien

➢ Festlegung von Zuschlagskriterien

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

178

 Referenz Produkte

➢ Mitwirkung von Externen und Maßnahmen zum unverfälschten Wettbewerb

➢ Gründe für Sicherheitsrelevanz des Auftrages

➢ Gründe für Notwendigkeit einer Sicherheitsüberprüfung

➢ Gründe für Geheimschutzbedürftigkeit

Weiterführende   Erläuterungen   zu   den   genannten   Aspekten   finden   sich   im   Kapitel   B   (Planung   einer
Beschaffung) der UfAB.

Verantwortlich

Ausschreibungs- und Vertragsverantwortlicher

Mitwirkend

Aktivität

Erzeugt durch

Vergabestelle

Beschaffung planen

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zur Vergabe von
Entwicklungsleistungen)
Systemanalyse:
Make-or-Buy-Entscheidung (Bewertung und Ergebnis)

Entscheidungsrelevant
bei

Ausschreibung freigegeben

Sonstiges

Keine Produktvorlage

C.1.16.2 Kriterienkatalog

Der  Kriterienkatalog  mit den darin enthaltenen Ausschluss- und Bewertungskriterien (A- und B-Kriterien)
beschreibt das geschuldete Leistungssoll des Auftragnehmers nach Zuschlagserteilung und Vertragsschluss.
Zu  A-Kriterien   enthält   der  Kriterienkatalog  vorformulierte  Angaben   des   Bieters   (z.   B.   "ja"   oder   "nein"
beziehungsweise "erfüllt" oder "nicht erfüllt"). Die Nichterfüllung einer als A-Kriterium gekennzeichneten
Anforderung   führt   zwingend   zum  Ausschluss   des  Angebotes.   Zu   B-Kriterien   sieht   der  Kriterienkatalog
entweder   vorformulierte   Angaben   oder   Freifelder   für   Angaben   des   Bieters   vor.   Je   nach   Umfang   der
Anforderungen   kann   der  Kriterienkatalog  in   Kriterienhauptgruppen   und   Kriteriengruppen   untergliedert
werden.

Als leistungsbeschreibendes Element der  Vergabeunterlagen (Ausschreibung)  ist der  Kriterienkatalog  Teil
der   Vertragsunterlagen.   Die   B-Kriterien   aus   dem  Kriterienkatalog  bilden   die   Grundlage   der
Leistungsbewertungsmatrix  für   die   Ermittlung   des   wirtschaftlichsten  Angebotes.   In   der   Praxis   können
Kriterienkatalog und Leistungsbewertungsmatrix daher in einem Dokument zusammengefasst werden.

Verantwortlich

Ausschreibungs- und Vertragsverantwortlicher

Mitwirkend

Aktivität

Methoden

Teil von

Anforderungsanalytiker (AG), Vergabestelle, Projektleiter, Projekteigner

Leistungssoll festlegen

Vom Lastenheft zum Kriterienkatalog

Leistungsbewertungsmatrix, Vergabeunterlagen (Ausschreibung)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

Erzeugt durch

179

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zur Vergabe von
Entwicklungsleistungen)
Systemanalyse:
Make-or-Buy-Entscheidung (Bewertung und Ergebnis)

Entscheidungsrelevant
bei

Ausschreibung freigegeben

Sonstiges

Keine Produktvorlage

C.1.16.2.1 Kriterien zur Gewährleistung der Informationssicherheit und des Datenschutzes

In Projekten, in denen Aspekte der Informationssicherheit und des Datenschutzes zu berücksichtigen sind,
müssen   die   Bieter   spezifische   Kriterien   erfüllen,   die   in   diesem   Thema   zusammengefasst   werden.   Die
nachfolgend beispielhaft aufgeführten Kriterien können nach Bedarf erweitert, eingeschränkt, konkretisiert
oder verpflichtend gefordert werden. Die Bieter sollten im Angebot

➢ die Durchführung einer Sicherheitskonzeption zusichern,

➢ ihren sicheren Software-Entwicklungs-Lebenszyklus (SSDLC) darstellen,

➢ ihr   Informationssicherheits-Managementsystem   (ISMS)   vorstellen   und   darlegen,   wie   die   für   das

Projekt benötigten Bestandteile in das ISMS integriert sind oder werden,

➢ angeben, welche Software-Werkzeuge für das Design, die Entwicklung, die Integration und den Test
des Systems zum Einsatz kommen, in welchen Ländern die dafür ggf. benötigten Server betrieben
werden und welches Personal auf die Werkzeuge Zugriff hat,

➢ angeben, in welchen Ländern das eingesetzte Personal tätig ist (On-/Off-/Nearshore-Entwicklung),

➢ angeben, ob das eingesetzte Personal über eine Sicherheitsüberprüfung der Stufe Ü1/2/3 verfügt oder

einer Sicherheitsüberprüfung zustimmt,

➢ angeben, ob und welche Sicherheits-Zertifizierungen für das Unternehmen, das eingesetzte Personal

oder die verwendete Methodik vorliegen.

C.1.16.3 Leistungsbewertungsmatrix

Bei   Vergabeverfahren,   in   denen   der   Preis   nicht   das   alleinige   Zuschlagkriterium   ist,   dient   die
Leistungsbewertungsmatrix  zur   Ermittlung   der   Leistungspunktzahl   „L“   im   Rahmen   der   Einfachen   und
Erweiterten Richtwertmethode. Die Bewertung erfolgt anhand der bereits im Kriterienkatalog definierten B-
Kriterien.

Die Leistungsbewertungsmatrix enthält folgende Bestandteile:

➢ Auflistung   mindestens   aller   B-Kriterien   aus   dem   korrespondierenden  Kriterienkatalog,
gegebenenfalls   untergliedert   nach   Kriteriengruppierungen   gemäß   dem   korrespondierenden
Kriterienkatalog

➢ Kennzeichnung aller Kriterien entweder als A- oder B-Kriterium gemäß dem korrespondierenden

Kriterienkatalog

➢ Festlegung   der   Gewichtungen   zu   allen   B-Kriterien   in   Form   der   Bestimmung   von

Gewichtungspunkten für jedes B-Kriterium

➢ Festlegung   der   Bewertungsmaßstäbe   zu   allen   B-Kriterien   in   Form   der   Definition   von

Zielerfüllungsgraden und zugehörigen Bewertungspunkte für jedes B-Kriterium

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

180

 Referenz Produkte

➢ Gegebenenfalls Festlegung einer zu erreichenden Mindestpunktzahl zu der Leistungspunktzahl "L",

zu einzelnen Kriterienhauptgruppen, Kriteriengruppen oder auch einzelnen B-Kriterien

Weiterführende   Erläuterungen   zu   den   genannten   Bestandteilen   finden   sich   im   Kapitel   F   (Vertiefung   zu
ausgewählten Themen) der UfAB.

Verantwortlich

Ausschreibungs- und Vertragsverantwortlicher

Mitwirkend

Aktivität

Methoden

Vorlagen

Teil von

Besteht aus

Erzeugt durch

Anforderungsanalytiker (AG), Vergabestelle, Projektleiter, Projekteigner

Zuschlagskriterien festlegen

Bewertungsverfahren

UfAB 2018 Bewertungsmatrix (Excel) (Externe Kopiervorlage),
Bewertungsmatrix (Muster, Microsoft Excel) (Externe Kopiervorlage)

Vergabeunterlagen (Ausschreibung)

Kriterienkatalog

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zur Vergabe von
Entwicklungsleistungen)
Systemanalyse:
Make-or-Buy-Entscheidung (Bewertung und Ergebnis)

Entscheidungsrelevant
bei

Ausschreibung freigegeben

Sonstiges

Keine Produktvorlage

C.1.16.4 Eignungsbewertungsmatrix

Die  Eignungsbewertungsmatrix  mit   den   darin   enthaltenen   Eignungskriterien   dient   im   Rahmen   der
Eignungsprüfung   der   Beantwortung   der   Frage,   ob   und   inwieweit   ein   Bewerber   /   Bieter   für   die
ausgeschriebene   Leistung   geeignet   ist.   Die   Eignungsprüfung   erfolgt   in   Vergabeverfahrensarten   mit
Teilnahmewettbewerb   vorgezogen,   das   heißt   vor   der   Aufforderungen   zur   Angebotsabgabe.   In
Vergabeverfahrensarten   ohne   Teilnahmewettbewerb   erfolgt   die   Eignungsprüfung   grundsätzlich   erst   im
Rahmen der Angebotsprüfung und -wertung.

Der  Aufbau und die Struktur  der  Eignungsbewertungsmatrix  können aus der  Leistungsbewertungsmatrix
übertragen werden. Dies gilt insbesondere für die Kriterienklassifizierung in A- und B-Kriterien sowie die
Festlegung von Gewichtungspunkten, Bewertungsmaßstäben und Punktesystemen. Mindestanforderungen an
die Eignung der Bewerber / Bieter werden dann als A-Kriterien definiert.

Insbesondere für den Fall einer Vergabeverfahrensart mit Teilnahmewettbewerb, bei der der Auftraggeber die
Zahl der Bieter begrenzt, die er anschließend zur Angebotsabgabe auffordern möchte, sind innerhalb der
aufzustellenden Eignungsbewertungsmatrix dann auch B-Kriterien zu definieren.

Verantwortlich

Mitwirkend

Aktivität

Teil von

Ausschreibungs- und Vertragsverantwortlicher

Vergabestelle, Projektleiter, Projekteigner

Eignungskriterien festlegen

Vergabeunterlagen (Ausschreibung)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

Erzeugt durch

181

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zur Vergabe von
Entwicklungsleistungen)
Systemanalyse:
Make-or-Buy-Entscheidung (Bewertung und Ergebnis)

Entscheidungsrelevant
bei

Ausschreibung freigegeben

Sonstiges

Keine Produktvorlage

C.1.16.5 Vergabeunterlagen (Ausschreibung)

Die  Vergabeunterlagen  (Ausschreibung)  setzen  sich  in  der   Regel   aus   den Verfahrensunterlagen  und  den
Vertragsunterlagen zusammen. Die UfAB enthält eine Übersicht der wesentlichen Bestandteile und gliedert
die Vergabeunterlagen wie folgt:

Verfahrensunterlagen

➢ Anschreiben

➢ Bewerbungsbedingungen

Vertragsunterlagen

➢ Leistungsbeschreibung

➢ Kriterienkatalog

➢ Vertragsbedingungen (in der Regel: EVB-IT)

➢ Angebotsschreiben

➢ Preisblatt

Weiterführende   Erläuterungen   zu   den   genannten   Bestandteilen   finden   sich   im   Kapitel   C   (Design   einer
Beschaffung) der UfAB.

Verantwortlich

Ausschreibungs- und Vertragsverantwortlicher

Mitwirkend

Aktivität

Vorlagen

Anforderungsanalytiker (AG), Vergabestelle, Projektleiter, Projekteigner

Vergabeunterlagen zusammenstellen

Ergänzende Vertragsbedingungen für die Erstellung eines IT-Systems (EVB-IT
System) (Externe Kopiervorlage), Ergänzende Vertragsbedingungen für die
Erstellung bzw. Anpassung von Software (EVB-IT Erstellung) (Externe
Kopiervorlage), Nutzungshinweise EVB-IT System (Externe Kopiervorlage),
EVB-IT Systemvertrag (Word) (Externe Kopiervorlage), EVB-IT
Erstellungsvertrag (Word) (Externe Kopiervorlage), UfAB 2018
Bewertungsmatrix (Excel) (Externe Kopiervorlage), Bewertungsmatrix (Muster,
Microsoft Excel) (Externe Kopiervorlage)

Besteht aus

Kriterienkatalog, Leistungsbewertungsmatrix, Eignungsbewertungsmatrix

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

182

Erzeugt durch

Inhaltlich abhängig

 Referenz Produkte

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zur Vergabe von
Entwicklungsleistungen)
Systemanalyse:
Make-or-Buy-Entscheidung (Bewertung und Ergebnis)

Anforderungen als Bestandteil der Vergabeunterlagen (Ausschreibung):
Lastenheft (Anforderungen)
Externe-Einheit/Externes-SW-Modul-Spezifikation als Bestandteil der
Vergabeunterlagen (Ausschreibung):
Externe-Einheit-Spezifikation, Externes-SW-Modul-Spezifikation
Vorgaben für den Auftragnehmer:
Projekthandbuch, QS-Handbuch

Entscheidungsrelevant
bei

Ausschreibung freigegeben

Sonstiges

Keine Produktvorlage

C.1.16.6 Verfahrensdokumentation

Bei Beschaffung hat der Auftraggeber das Vergabeverfahren von Beginn an fortlaufend in Textform nach §
126b  BGB  zu  dokumentieren,   soweit   dies   für   die   Begründung  von  Entscheidungen  auf   jeder   Stufe   des
Vergabeverfahrens erforderlich ist. Dazu gehört zum Beispiel die Dokumentation

➢ der Kommunikation mit Unternehmen und interner Beratungen,

➢ der Vorbereitung der Auftragsbekanntmachung und der Vergabeunterlagen,

➢ der Öffnung der Angebote und Teilnahmeanträge,

➢ der Verhandlungen und der Dialoge mit den teilnehmenden Unternehmen

➢ sowie der Gründe für Auswahlentscheidungen und den Zuschlag.

Verantwortlich

Aktivität

Erzeugt durch

Ausschreibungs- und Vertragsverantwortlicher

Vergabeverfahren dokumentieren

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zur Vergabe von
Entwicklungsleistungen)
Systemanalyse:
Make-or-Buy-Entscheidung (Bewertung und Ergebnis)

Entscheidungsrelevant
bei

Ausschreibung freigegeben, Beauftragung erteilt

Sonstiges

Keine Produktvorlage

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.1 Produkte

C.1.16.7 Vergabevermerk

183

Der   Auftraggeber   hat   über   jedes   Vergabeverfahren   einen   Vermerk   in   Textform   nach   §   126b   BGB
anzufertigen. Im Bereich oberhalb der EU-Schwellenwerte gibt § 8 Abs. 2 VgV den Mindestinhalt dieses
Vergabevermerk
 s   wie folgt vor (im Bereich unterhalb der EU-Schwellenwerte kann sich der Auftraggeber an
diesem Katalog orientieren):

➢ Name und Anschrift des Auftraggebers

➢ Gegenstand   und   Wert   des   Auftrages,   der   Rahmenvereinbarung   oder   des   dynamischen

Beschaffungssystems

➢ Namen der berücksichtigten Bewerber oder Bieter und die Gründe für ihre Auswahl

➢ nicht berücksichtigte Angebote und Teilnahmeanträge sowie die Namen der nicht berücksichtigten

Bewerber oder Bieter und die Gründe für ihre Nichtberücksichtigung

➢ Gründe für die Ablehnung von Angeboten, die für ungewöhnlich niedrig befunden wurden

➢ Name   des   erfolgreichen   Bieters   und  die   Gründe   für   die  Auswahl   seines  Angebotes   sowie,   falls
bekannt, den Anteil am Auftrag oder an der Rahmenvereinbarung, den der Zuschlagsempfänger an
Dritte   weiterzugeben   beabsichtigt,   und   gegebenenfalls,   soweit   zu   jenem   Zeitpunkt   bekannt,   die
Namen der Unterauftragnehmer des Hauptauftragnehmers

➢ bei   Verhandlungsverfahren   und   wettbewerblichen   Dialogen   die   in   den   Vorschriften   über   die
Zulässigkeit   dieser   Vergabeverfahrensarten   geregelten   Umstände,   die   die   Anwendung   dieser
Vergabeverfahrensarten rechtfertigen

➢ bei Verhandlungsverfahren ohne Teilnahmewettbewerb die in § 14 Abs. 4 VgV genannten Umstände,

die die Anwendung dieser Vergabeverfahrensart rechtfertigen

➢ gegebenenfalls   die   Gründe,   aus   denen   der  Auftraggeber   auf   die   Vergabe   eines  Auftrages,   den
Abschluss einer Rahmenvereinbarung oder die Einrichtung eines dynamischen Beschaffungssystems
verzichtet hat

➢ gegebenenfalls   die   Gründe,   aus   denen   andere   als   elektronische   Mittel   für   die   Einreichung   der

Angebote verwendet wurden

➢ gegebenenfalls Angaben zu aufgedeckten Interessenkonflikten und getroffenen Abhilfemaßnahmen

➢ gegebenenfalls die Gründe, aufgrund derer mehrere Teil- oder Fachlose zusammen vergeben wurden

➢ gegebenenfalls die Gründe für die Nichtangabe der Gewichtung von Zuschlagskriterien (§ 58 Abs. 3

S. 3 VgV)

Weiterführende   Erläuterungen   zu   den   genannten   Inhalten   finden   sich   im   Kapitel   F   (Vertiefung   zu
ausgewählten Themen) der UfAB.

Für die Berücksichtigung behördenspezifischer Regelungen zur Verantwortlichkeit und Durchführung von
Beschaffungen sollte in jedem Fall Rücksprache mit der zuständigen Vergabestelle gehalten werden.

Verantwortlich

Ausschreibungs- und Vertragsverantwortlicher

Aktivität

Vorlagen

Vergabevermerk anfertigen

Ergänzende Vertragsbedingungen für die Erstellung eines IT-Systems (EVB-IT
System) (Externe Kopiervorlage), Ergänzende Vertragsbedingungen für die
Erstellung bzw. Anpassung von Software (EVB-IT Erstellung) (Externe
Kopiervorlage), Nutzungshinweise EVB-IT System (Externe Kopiervorlage)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


184

Erzeugt durch

 Referenz Produkte

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zur Vergabe von
Entwicklungsleistungen)
Systemanalyse:
Make-or-Buy-Entscheidung (Bewertung und Ergebnis)

Entscheidungsrelevant
bei

Ausschreibung freigegeben, Beauftragung erteilt

Sonstiges

Keine Produktvorlage

C.1.16.8 Angebot (von AN)

Das  Angebot   (von  AN)  ist   eine   Kopie   des  Angebots   eines  Auftragnehmers,   das   in   Reaktion   auf   die
Ausschreibung   erstellt   und   dem  Auftraggeber   zugestellt   wurde.  Alle   erhaltenen  Angebote   werden   vom
Auftraggeber bewertet. Das Ergebnis der Bewertung wird im Vergabevermerk dokumentiert.

Verantwortlich

Vergabestelle

Sonstiges

Extern, Keine Produktvorlage

C.1.17 Vertragswesen

C.1.17.1 Vertrag

Der  Vertrag  bildet   die   rechtliche   Grundlage   für   die   Erbringung  der   Leistungen   von Auftragnehmer   und
Auftraggeber, regelt die Zusammenarbeit zwischen den beiden Parteien und legt die Liefergegenstände fest.

Der Vertrag kommt durch eine beiderseitige Willenserklärung zwischen Auftraggeber und Auftragnehmer zu
Stande: Diese Willenserklärung erfolgt durch ein Angebot (von AN) und durch die Erteilung des Zuschlags
auf dieses Angebot. Zur Beweissicherung und Rechtssicherheit wird meist zusätzlich eine Vertragsurkunde
unterzeichnet. Der Vertrag besteht also aus folgenden Elementen:

➢ Angebot (von AN)

➢ Zuschlag

➢ Vertragsurkunde

Für   öffentliche   Auftraggeber   gibt   es   vorgefertigte   Vertragsbedingungen,   zum   Beispiel
 EVB-IT
beziehungsweise BVB, die entsprechend zu verwenden und gegebenenfalls auszugestalten sind. Damit diese
Vorgaben   Vertragsbestandteil   werden,   müssen   sie   Teil   des   Angebots   sein   und   daher   bereits   den
Vergabeunterlagen (Ausschreibung) beigefügt werden.

Verantwortlich

Ausschreibungs- und Vertragsverantwortlicher

Mitwirkend

Aktivität

Anforderungsanalytiker (AG), Vergabestelle, Projektleiter

Vertrag abschließen

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland



C.1 Produkte

Vorlagen

Erzeugt durch

185

Vertrag(.odt|.doc), Ergänzende Vertragsbedingungen für die Erstellung eines IT-
Systems (EVB-IT System) (Externe Kopiervorlage), Ergänzende
Vertragsbedingungen für die Erstellung bzw. Anpassung von Software (EVB-IT
Erstellung) (Externe Kopiervorlage), Nutzungshinweise EVB-IT System (Externe
Kopiervorlage), EVB-IT Systemvertrag (Word) (Externe Kopiervorlage), EVB-IT
Erstellungsvertrag (Word) (Externe Kopiervorlage)

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zur Vergabe von
Entwicklungsleistungen)
Systemanalyse:
Make-or-Buy-Entscheidung (Bewertung und Ergebnis)

Entscheidungsrelevant
bei

Beauftragung erteilt

C.1.17.2 Vertragszusatz

Ein Vertragszusatz ist eine vertragliche vereinbarte Änderung des Produkts Vertrag, beispielsweise bezüglich
des Leistungsumfangs, der Kosten und der Termine. Vertragszusätze können vom Auftragnehmer und vom
Auftraggeber initiiert werden, zum Beispiel über das Problem- und Änderungsmanagement.

Verantwortlich

Ausschreibungs- und Vertragsverantwortlicher

Mitwirkend

Aktivität

Vorlagen

Vergabestelle

Vertragszusatz abschließen

Vertragszusatz(.odt|.doc), Ergänzende Vertragsbedingungen für die Erstellung
eines IT-Systems (EVB-IT System) (Externe Kopiervorlage), Ergänzende
Vertragsbedingungen für die Erstellung bzw. Anpassung von Software (EVB-IT
Erstellung) (Externe Kopiervorlage), Nutzungshinweise EVB-IT System (Externe
Kopiervorlage), EVB-IT Systemvertrag (Word) (Externe Kopiervorlage), EVB-IT
Erstellungsvertrag (Word) (Externe Kopiervorlage)

Erzeugt durch

Problem- und Änderungsmanagement:
Änderungsentscheidung (Entscheidung und Begründung)

Entscheidungsrelevant
bei

Beauftragung erteilt

C.1.17.3 Vertragsübersicht

In der Vertragsübersicht sind sämtliche das Projekt betreffenden Verträge zusammenfassend aufgeführt. Zu
jedem Vertrag sind der aktuelle Status, die gemäß Vertrag zu erbringenden Leistungen (Liefergegenstände)
sowie die vereinbarten Liefertermine zu dokumentieren.

Ebenfalls   in   der  Vertragsübersicht   enthalten   sind   die   im   Fall   nicht   erbrachter   Leistungen   zu   zahlenden
Vertragsstrafen sowie die im Projektverlauf vorgenommenen Vertragsanpassungen.

Verantwortlich

Aktivität

Ausschreibungs- und Vertragsverantwortlicher

Vertragsübersicht führen

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

186

Erzeugt durch

 Referenz Produkte

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zur Vergabe von
Entwicklungsleistungen)
Systemanalyse:
Make-or-Buy-Entscheidung (Bewertung und Ergebnis)

C.1.18 Angebots- und Auftragswesen

C.1.18.1 Angebotsaufforderung

Die Angebotsaufforderung ist die formale Aufforderung an einen IT-Dienstleister des Bundes ein Angebot
für die Entwicklung des Systems abzugeben. Sie erfolgt in schriftlicher Form und wird gemeinsam mit dem
Lastenheft (Anforderungen) an den IT-Dienstleister übermittelt.

Verantwortlich

Aktivität

Erzeugt durch

Ausschreibungs- und Vertragsverantwortlicher

Angebotsaufforderung erstellen

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zur Beauftragung eines IT-
Dienstleisters des Bundes)
Systemanalyse:
Make-or-Buy-Entscheidung (Bewertung und Ergebnis)

Entscheidungsrelevant
bei

Angebotsaufforderung erstellt

C.1.18.2 Auftrag

Der Auftrag bildet die Grundlage für die Erbringung der Leistungen im Projekt, regelt die Zusammenarbeit
zwischen Auftraggeber und Auftragnehmer und legt die Liefergegenstände fest. Der  Auftrag  kommt durch
eine beiderseitige Willenserklärung mit der Unterzeichnung des Angebots durch den Auftraggeber zu Stande.

Verantwortlich

Aktivität

Erzeugt durch

Ausschreibungs- und Vertragsverantwortlicher

Auftrag erteilen

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zur Beauftragung eines IT-
Dienstleisters des Bundes)
Systemanalyse:
Make-or-Buy-Entscheidung (Bewertung und Ergebnis)

Entscheidungsrelevant
bei

Beauftragung erteilt

C.1.18.3 Änderungsvereinbarung (Change Request)

Die   Änderungsvereinbarung   dient   dem   Auftraggeber   (Projekt)   bzw.   dem   Auftragnehmer   dazu,   einen
 s   anzuzeigen. Der Änderungsbedarf bezieht sich
Änderungsbedarf bezüglich des aktuell vorliegenden Auftrag
auf die organisatorischen Aspkete eines Projekts, wie z.B. Verschiebungen bzgl. Zeit und Ressourcen, oder
Änderungen grundlegender Technologien.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


C.1 Produkte

187

Hinweis:  Er ist nicht mit den Produkten der Disziplin  Problem- und Änderungsmanagement  (siehe auch
Vorgehensbaustein  Problem-   und   Änderungsmanagement)   zu   verwechseln,   welche   nur   im   Kontext   des
Projektgegenstands angewendet werden.

Verantwortlich

Aktivität

Erzeugt durch

Ausschreibungs- und Vertragsverantwortlicher

Änderung vereinbaren

Anbahnung und Organisation:
Projekthandbuch (Organisation und Vorgaben zur Beauftragung eines IT-
Dienstleisters des Bundes)

Sonstiges

Extern, Keine Produktvorlage

C.1.19 Lieferung und Abnahme

C.1.19.1 Lieferung

Die Lieferung besteht aus den im Vertrag (von AG) festgelegten Liefergegenständen. Dabei kann es sich um
Systemelemente wie Software und/oder Dokumente handeln.

Verantwortlich

Projektleiter

Mitwirkend

Aktivität

Erzeugt durch

Systemintegrator

Lieferung erstellen und ausliefern

Systementwurf:
Pflichtenheft (Gesamtsystementwurf) (Lieferumfang)

Entscheidungsrelevant
bei

Lieferung durchgeführt

Sonstiges

Keine Produktvorlage

C.1.19.2 Abnahmeerklärung

In   der  Abnahmeerklärung  erklärt   der   Auftraggeber   sein   Einverständnis   mit   der   vom   Auftragnehmer
erbrachten   (Teil-)Lieferung  oder   ihre  Ablehnung.   Bei   allen   Lieferungen,   die   laut  Vertrag  abgenommen
werden müssen, hat der Auftragnehmer  ein Recht auf die Ausstellung einer Abnahmeerklärung. Mit der
Abnahmeerklärung können rechtliche Folgen, wie die Fälligkeit vereinbarter Zahlungen, verbunden sein.

Im   Falle   der   Ablehnung   der   Abnahme   obliegt   es   dem   Auftragnehmer   nachzuweisen,   dass   der
Liefergegenstand doch vertragsgemäß erstellt wurde, oder er muss die festgestellten Mängel innerhalb der
gesetzten   Frist   beseitigen.   Die  Ablehnung   der  Abnahme   kann   für   beide   Seiten   erhebliche   Folgen,   wie
vereinbarte Vertragsstrafen, nach sich ziehen.

Verantwortlich

Projekteigner

Mitwirkend

Vergabestelle, Projektleiter, QS-Verantwortlicher,
Informationssicherheitsverantwortlicher, Ausschreibungs- und
Vertragsverantwortlicher

Aktivität

Abnahmeerklärung ausstellen (AG)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

188

Vorlagen

Erzeugt durch

 Referenz Produkte

Abnahmeerklärung(.odt|.doc)

Systemanalyse:
Lastenheft (Anforderungen) (Abnahmekriterien), Lastenheft Gesamtprojekt
(Abnahmekriterien)

Entscheidungsrelevant
bei

Abnahme erklärt

C.1.19.2.1 Beurteilung der Lieferung

Der   Liefergegenstand   ist   in   Art   und   Umfang   zu   beschreiben.   Die   Abnahmeprüfergebnisse   werden
zusammengefasst   und   beurteilt.  Anhand   der   Prüfergebnisse   ist   zu   entscheiden,   ob   die  Abnahme   erteilt
werden kann, unter Vorbehalt erfolgt oder nicht erteilt wird. Im Fall einer Abnahme unter Vorbehalt wird die
Mängelliste mit Fristsetzung zur Nachbesserung ebenfalls hier dokumentiert.

C.1.19.2.2 Bestätigung der Risikobehandlung

Der Auftraggeber bestätigt seine Entscheidungen zur Risikobehandlung, die in den Produktexemplaren der
Sicherheitskonzeption dokumentiert sind.

C.1.19.2.3 Anhang: Abnahmeprotokoll

Im Anhang   befindet   sich  eine   Kopie   vom  Abnahmeprotokoll.   Es   dient   der   Dokumentation   der   Prüfung
gegenüber dem Auftragnehmer.

C.1.19.3 Lieferung (von AN)

Die Lieferung (von AN) ist die physische Lieferung beziehungsweise Teillieferung des Auftragnehmers an
den Auftraggeber. Umfang und Anzahl der (Teil-)Lieferungen entspricht den Vorgaben im Vertrag. Für jede
Lieferung (von AN) ist vom Auftraggeber, falls nicht anders vereinbart, eine Abnahmeerklärung zu erstellen.

Verantwortlich

Projektleiter

Entscheidungsrelevant
bei

Abnahme erklärt

Sonstiges

Extern

C.2 Produktabhängigkeiten

C.2.1 Inhaltliche Produktabhängigkeiten

C.2.1.1 Anforderungen als Bestandteil der Vergabeunterlagen (Ausschreibung)

Die   im   Lastenheft   beschriebenen   Anforderungen   an   das   zu   erstellende   System   sind   Bestandteil   der
Vergabeunterlagen (Ausschreibung).

Produkt (Gruppe 1)

Vergabeunterlagen (Ausschreibung)

Produkt (Gruppe 2)

Lastenheft (Anforderungen)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.2 Produktabhängigkeiten

189

C.2.1.2 Berichte des Auftragnehmers im Projektabschlussbericht

Wesentliche Inhalte des Produkts  Projektabschlussbericht (von AN)  werden in den  Projektabschlussbericht
des Auftraggeber-Projekts übernommen.

Produkt (Gruppe 1)

Projektabschlussbericht

Produkt (Gruppe 2)

Projektabschlussbericht (von AN)

C.2.1.3 Berichte des Auftragnehmers im Projektstatusbericht

Wesentliche   Inhalte   des   Produkts  Projektstatusbericht   (von  AN)  werden   in   den  Projektstatusbericht  des
Auftraggeber-Projekts übernommen.

Produkt (Gruppe 1)

Projektstatusbericht

Produkt (Gruppe 2)

Projektstatusbericht (von AN)

C.2.1.4 Berücksichtigung der Informationssicherheit und des Datenschutzes bei der
Anforderungsfestlegung

Die  Schutzbedarfsfeststellung  sowie   die  Vorgaben  zur   Informationssicherheit  und  zum  Datenschutz   sind
Bestandteil des Themas Nicht-Funktionale Anforderungen im Lastenheft (Anforderungen).

Produkt (Gruppe 1)

Lastenheft (Anforderungen)

Produkte (Gruppe 2)

Schutzbedarfsfeststellung, Vorgaben zur Informationssicherheit, Vorgaben zum
Datenschutz

C.2.1.5 Berücksichtigung der Informationssicherheit und des Datenschutzes bei der
Systemerstellung

Die  Sicherheitskonzeption  sowie notwendige Erweiterungen der Vorgaben zur Informationssicherheit und
zum Datenschutz müssen mit den funktionalen und nichtfunktionalen Anforderungen, den identifizierten
Systemelementen und den beschriebenen Schnittstellen im Pflichtenheft abgeglichen werden. Zudem greifen
die Vorgaben eines Bereichs mitunter die des anderen Bereichs auf und detaillieren diese.

Produkte (Gruppe 1)

Sicherheitskonzeption, Erweiterung der Vorgaben zur Informationssicherheit,
Erweiterung der Vorgaben zum Datenschutz

Produkt (Gruppe 2)

Pflichtenheft (Gesamtsystementwurf)

C.2.1.6 Berücksichtigung der Marktsichtung

In der Marktsichtung für Fertigprodukte werden Fertigproduktkandidaten für eine Externe Einheit oder ein
Externes   SW-Modul  identifiziert.   Im   Rahmen   der  Make-or-Buy-Entscheidung  müssen   diese   Kandidaten
evaluiert werden (siehe Evaluierung der Fertigprodukte).

Produkt (Gruppe 1)

Make-or-Buy-Entscheidung

Produkt (Gruppe 2)

Marktsichtung für Fertigprodukte

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

190

 Referenz Produkte

C.2.1.7 Berücksichtigung der Projektvorstudie

Die in der  Projektvorstudie  enthaltenen Informationen sind im  Projektauftrag  und im  Projekthandbuch  zu
berücksichtigen.

Produkte (Gruppe 1)

Projekthandbuch, Projektauftrag

Produkt (Gruppe 2)

Projektvorstudie

C.2.1.8 Berücksichtigung der WiBe im Projektabschlussbericht

Die WiBe (Fortschreibung) ist in den Projektabschlussbericht zu integrieren. Hierfür können die durch das
Werkzeug WiBe-Kalkulator bereitgestellten Reports als Anlage verwendet werden.

Produkt (Gruppe 1)

Projektabschlussbericht

Produkt (Gruppe 2)

WiBe (Fortschreibung)

C.2.1.9 Berücksichtigung der WiBe in den Anforderungen

Die  WiBe   (Fortschreibung)  ist   bei   der   Erstellung   des   Lastenhefts   im   Bezug   auf   die   wirtschaftliche
Notwendigkeit oder Finanzierbarkeit einzelner Anforderungen zu berücksichtigen.

Produkt (Gruppe 1)

Lastenheft (Anforderungen)

Produkt (Gruppe 2)

WiBe (Fortschreibung)

C.2.1.10 Berücksichtigung des IT-Betriebs bei der Anforderungsfestlegung

Die Vorgaben zum IT-Betrieb sind Bestandteil des Themas Nicht-Funktionale Anforderungen im Lastenheft
(Anforderungen).

Produkt (Gruppe 1)

Lastenheft (Anforderungen)

Produkt (Gruppe 2)

Vorgaben zum IT-Betrieb

C.2.1.11 Berücksichtigung des IT-Betriebs bei der Systemerstellung

Notwendige   Erweiterungen   der   Vorgaben   zum   IT-Betrieb   müssen   mit   den   funktionalen   und
nichtfunktionalen Anforderungen, den identifizierten Systemelementen und den beschriebenen Schnittstellen
im Pflichtenheft abgeglichen werden.

Produkt (Gruppe 1)

Erweiterung der Vorgaben zum IT-Betrieb

Produkt (Gruppe 2)

Pflichtenheft (Gesamtsystementwurf)

C.2.1.12 Einfluss der Altsystemanalyse auf die Systemerstellung

Die in der Altsystemanalyse ermittelte Funktionalität sowie die bestehenden Schnittstellen des abzulösenden
Systems müssen im Pflichtenheft (Gesamtsystementwurf) berücksichtigt werden.

Produkt (Gruppe 1)

Pflichtenheft (Gesamtsystementwurf)

Produkt (Gruppe 2)

Altsystemanalyse

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.2 Produktabhängigkeiten

191

C.2.1.13 Einfluss eines Fertigprodukts auf die Spezifikation externer Systemelemente

Die Spezifikation eines externen Systemelements (Externe Einheit, Externes SW-Modul) ist die Basis für die
Evaluierung der Fertigprodukte im Rahmen einer Make-or-Buy-Entscheidung. Ist das Ergebnis der Make-or-
Buy-Entscheidung   der   Einsatz   eines   Fertigprodukts,   hat   dies   üblicherweise   Rückwirkungen   auf   die
Spezifikation, da das Fertigprodukt in der Regel nur einen Teil der Anforderungen erfüllt. Der verbleibende
Umfang muss von anderen/neuen Systemteilen erbracht oder die Anforderungen müssen angepasst/reduziert
werden. Dies kann wiederum Auswirkungen auf die Architektur und Spezifikation des Systems oder der
Software, bis hin zum Pflichten- und Lastenheft haben.

Produkt (Gruppe 1)

Make-or-Buy-Entscheidung

Produkte (Gruppe 2)

Externe-Einheit-Spezifikation, Externes-SW-Modul-Spezifikation

C.2.1.14 Externe-Einheit/Externes-SW-Modul-Spezifikation als Bestandteil der
Vergabeunterlagen (Ausschreibung)

Die Spezifikation eines externen Systemelements (Externe Einheit, Externes SW-Modul) ist Bestandteil der
Vergabeunterlagen (Ausschreibung).

Produkt (Gruppe 1)

Vergabeunterlagen (Ausschreibung)

Produkte (Gruppe 2)

Externe-Einheit-Spezifikation, Externes-SW-Modul-Spezifikation

C.2.1.15 Fortschreibung der WiBe

Die WiBe wird im Verlauf eines Projekts kontinuierlich aktualisiert. Die WiBe (Vorkalkulation) bildet dafür
die Grundlage und enthält die ersten Betrachtungen, Kalkulationen und Schätzungen. Auf ihrer Basis wird
die WiBe (Fortschreibung) erstellt.

Produkt (Gruppe 1)

WiBe (Fortschreibung)

Produkt (Gruppe 2)

WiBe (Vorkalkulation)

C.2.1.16 Inhalte im Projektstatusbericht

Der Projektstatusbericht fasst wesentliche Inhalte der Änderungsstatusliste und der QS-Bericht

 e   zusammen.

Produkt (Gruppe 1)

Projektstatusbericht

Produkte (Gruppe 2)

QS-Bericht, Änderungsstatusliste

C.2.1.17 Konsistenz von Anwenderaufgabenanalyse und Gesamtsystementwurf

Die in der  Anwenderaufgabenanalyse  ermittelten  Anwenderaufgaben, Anwenderprofile und die physische
Benutzungsumgebung   sind   als   Input   für   das   Thema  Funktionale   Anforderungen  im  Pflichtenheft
(Gesamtsystementwurf) zu berücksichtigen.

Produkt (Gruppe 1)

Pflichtenheft (Gesamtsystementwurf)

Produkt (Gruppe 2)

Anwenderaufgabenanalyse

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


192

 Referenz Produkte

C.2.1.18 Konsistenz von Lasten- und Pflichtenheft (ohne Vertrag)

Sofern   kein   Vertrag   vorliegt,   sind   die   im   Lastenheft   festgelegten   Anforderungen   im  Pflichtenheft
(Gesamtsystementwurf) vollständig abzudecken und ggf. zu verfeinern.

Produkt (Gruppe 1)

Pflichtenheft (Gesamtsystementwurf)

Produkt (Gruppe 2)

Lastenheft (Anforderungen)

C.2.1.19 Konsistenz von Teilprojekt-Anforderungen zum Lastenheft Gesamtprojekt

Die Lastenhefte der Teilprojekte müssen die Anforderungen aus dem Lastenheft Gesamtprojekt vollständig
und konsistent abdecken.

Produkt (Gruppe 1)

Lastenheft (Anforderungen)

Produkt (Gruppe 2)

Lastenheft Gesamtprojekt

C.2.1.20 Planung der Prüfung von Systemelementen

Das in den Implementierungs-, Integrations- und Prüfkonzepten beschriebene Vorgehen zur Prüfung von
Systemelementen muss im Projektplan berücksichtigt werden.

Produkt (Gruppe 1)

Projektplan

Produkte (Gruppe 2)

Implementierungs-, Integrations- und Prüfkonzept System, Implementierungs-,
Integrations- und Prüfkonzept SW

C.2.1.21 Projektvorstudie, Projektauftrag und Anforderungen

Im  Lastenheft   (Anforderungen)  bzw.
Systemidee und der Lösungsansatz aus der Projektvorstudie und dem Projektauftrag zu berücksichtigen.

 Lastenheft   Gesamtprojekt  sind   die   Rahmenbedingungen,   die

Produkte (Gruppe 1)

Lastenheft Gesamtprojekt, Lastenheft (Anforderungen)

Produkte (Gruppe 2)

Projektvorstudie, Projektauftrag

C.2.1.22 Prüfprotokolle im QS-Bericht

Der  QS-Bericht fasst wesentliche Inhalte der verschiedenen Prüfprotokolle zusammen. Hierzu zählen etwa
der Umfang und die Ergebnisse der Prüfungen sowie aufgetretene Qualitätsprobleme.

Produkt (Gruppe 1)

QS-Bericht

Produkte (Gruppe 2)

Prüfprotokoll, Prüfprotokoll Systemelement, Prüfprotokoll Inbetriebnahme,
Abnahmeprotokoll

C.2.1.23 Prüfprotokolle in der Nachweisakte

Die   Prüfprotokolle   der   Systemelemente   dienen   als   Nachweis   für   die   durchgeführten   Softwaretests   und
Hardwareprüfungen und werden in der Nachweisakte referenziert.

Produkt (Gruppe 1)

Nachweisakte

Produkt (Gruppe 2)

Prüfprotokoll Systemelement

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.2 Produktabhängigkeiten

193

C.2.1.24 Relevanz des Prüfprotokolls Inbetriebnahme für die Betriebliche
Freigabeerklärung

Das im Prüfprotokoll Inbetriebnahme dokumentierte Prüfergebnis dient als Grundlage für die Erteilung der
betrieblichen Freigabe und muss bei der Entscheidung berücksichtigt werden.

Produkt (Gruppe 1)

Betriebliche Freigabeerklärung

Produkt (Gruppe 2)

Prüfprotokoll Inbetriebnahme

C.2.1.25 Vorgaben des QS-Handbuchs zu Fertigprodukten

In   jeder  Prüfspezifikation   Systemelement,   die   sich   auf   ein   Systemelement   bezieht,   weleches   durch   ein
Fertigprodukt   realisiert   wird,   sind   die  Vorgaben   für   die   Prüfspezifikation   von   Fertigprodukten  im  QS-
Handbuch zu beachten.

Produkt (Gruppe 1)

Prüfspezifikation Systemelement

Produkt (Gruppe 2)

QS-Handbuch

C.2.1.26 Vorgaben für den Auftragnehmer

Das Projekthandbuch und das QS-Handbuch des Auftraggebers enthalten Vorgaben für den Auftragnehmer.
Diese sind Bestandteil der Vergabeunterlagen (Ausschreibung).

Produkt (Gruppe 1)

Vergabeunterlagen (Ausschreibung)

Produkte (Gruppe 2)

Projekthandbuch, QS-Handbuch

C.2.1.27 Vorgaben im Gesamtsystementwurf bezüglich Fertigprodukten

Werden   im  Pflichtenheft   (Gesamtsystementwurf)  konkrete   Vorgaben   zum   Einsatz   von   Fertigprodukten
gemacht, sind diese in der Make-or-Buy-Entscheidung zu berücksichtigen.

Diese Vorgaben können beispielsweise sein:

➢ Verwendung eines konkreten Produkts oder einer konkreten Produktfamilie,

➢ Beauftragung eines eindeutig bestimmten Unterauftragnehmers,

➢ Realisierungskriterien, welche nur bestimmte Produkte oder Produktfamilien zulassen.

Produkt (Gruppe 1)

Make-or-Buy-Entscheidung

Produkt (Gruppe 2)

Pflichtenheft (Gesamtsystementwurf)

C.2.1.28 Vorgaben zur Benutzungsschnittstelle

Die Beschreibung der Benutzungsschnittstelle in der  Systemspezifikation  oder der  SW-Spezifikation  muss
sich an den Vorgaben der Mensch-Maschine-Schnittstelle (Styleguide) orientieren.

Produkte (Gruppe 1)

Systemspezifikation, SW-Spezifikation

Produkt (Gruppe 2)

Mensch-Maschine-Schnittstelle (Styleguide)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

194

 Referenz Produkte

C.2.1.29 Vorgaben zur Prüfung der Systemelemente

Das  QS-Handbuch  enthält   Vorgaben   zur   Prüfung   der   Systemelemente,   die   in   den   Implementierungs-,
Integrations- und Prüfkonzepten berücksichtigt werden müssen.

Produkte (Gruppe 1)

Implementierungs-, Integrations- und Prüfkonzept System, Implementierungs-,
Integrations- und Prüfkonzept SW

Produkt (Gruppe 2)

QS-Handbuch

C.2.1.30 Zusammenhang zwischen betrieblichen Anforderungen und
Leistungsvereinbarung

Bei der Erstellung von Leistungsvereinbarungen (SLA/OLA/UC) sind die in den Vorgaben zum IT-Betrieb
enthaltenen Anforderungen (bspw. Verfügbarkeit, Reaktions- oder Supportzeiten) zu berücksichtigen.

Produkt (Gruppe 1)

Leistungsvereinbarung (SLA/OLA/UC)

Produkt (Gruppe 2)

Vorgaben zum IT-Betrieb

C.3 Produktindex
Modellelement

Abnahmeerklärung

Abnahmeprotokoll

Abnahmespezifikation

Altsystemanalyse

Änderungsentscheidung

Änderungsstatusliste

Änderungsvereinbarung (Change Request)

Anforderungsbewertung

Anforderungskonzept

Angebot (von AN)

Angebotsaufforderung

Anwenderaufgabenanalyse

Aufgabenliste

Auftrag

Ausbildungsunterlagen

Beschaffungskonzeption

Besprechungsdokument

Typ

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Seite

187

89

87

121

77

78

186

115

169

184

186

120

72

186

168

177

94

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.3 Produktindex

Modellelement

Betriebliche Freigabeerklärung

Bewertung Lastenheft Gesamtprojekt

Checkliste für das Interview zur Schutzbedarfsfeststellung

Checkliste Informationssicherheit

Datenbankentwurf

Eignungsbewertungsmatrix

Erweiterung der Vorgaben zum Datenschutz

Erweiterung der Vorgaben zum IT-Betrieb

Erweiterung der Vorgaben zur Informationssicherheit

Externe Einheit

Externe-Einheit-Spezifikation

Externes SW-Modul

Externes-SW-Modul-Spezifikation

Implementierungs-, Integrations- und Prüfkonzept SW

Implementierungs-, Integrations- und Prüfkonzept System

Informationssicherheits-Managementsystem

Informationssicherheits-Navigator

Inkrement (von AN)

Kennzahlenauswertung

Kriterienkatalog

Lastenheft (Anforderungen)

Lastenheft Gesamtprojekt

Leistungsbewertungsmatrix

Leistungsvereinbarung (SLA/OLA/UC)

Lieferung

Lieferung (von AN)

Logistische Unterstützungsdokumentation

Make-or-Buy-Entscheidung

Marktsichtung für Fertigprodukte

Mensch-Maschine-Schnittstelle (Styleguide)

Typ

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

195

Seite

174

129

113

56

153

180

152

173

150

101

160

103

164

144

142

80

59

170

93

178

104

123

179

175

187

188

166

118

117

154

196

Modellelement

Messdaten

Migrationskonzept

Nachweisakte

Nutzungsdokumentation

Pflichtenheft (Gesamtsystementwurf)

Problem-/Änderungsbewertung

Problemmeldung/Änderungsantrag

Product Backlog

Produktbibliothek

Produktkonfiguration

Projektabschlussbericht

Projektabschlussbericht (von AN)

Projektauftrag

Projektfortschrittsentscheidung

Projekthandbuch

Projektplan

Projektstatusbericht

Projektstatusbericht (von AN)

Projekttagebuch

Projektvorstudie

Prüfprotokoll

Prüfprotokoll Inbetriebnahme

Prüfprotokoll Systemelement

Prüfprozedur Systemelement

Prüfspezifikation

Prüfspezifikation Inbetriebnahme

Prüfspezifikation Systemelement

QS-Bericht

QS-Handbuch

Risikoliste

 Referenz Produkte

Seite

93

155

92

167

130

77

76

169

79

79

98

99

57

68

59

70

95

99

94

55

83

91

86

86

83

90

84

97

80

75

Typ

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

C.3 Produktindex

Modellelement

Schätzung

Schutzbedarfsfeststellung

Segment

Sicherheitskonzeption

SW-Architektur

SW-Einheit

SW-Komponente

SW-Modul

SW-Spezifikation

System

Systemarchitektur

Systemspezifikation

Verfahrensdokumentation

Vergabeunterlagen (Ausschreibung)

Vergabevermerk

Vertrag

Vertragsübersicht

Vertragszusatz

Vorgaben zum Datenschutz

Vorgaben zum IT-Betrieb

Vorgaben zur Informationssicherheit

WiBe (Fortschreibung)

WiBe (Vorkalkulation)

Typ

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

Produkt

197

Seite

73

114

100

147

138

101

102

103

162

100

134

157

182

181

183

184

185

185

112

170

111

74

74

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

198

 Referenz Rollen

D Referenz Rollen

D.1 Projektteamrollen

D.1.1 Änderungssteuerungsgruppe (Change Control Board)
Die Änderungssteuerungsgruppe wird bei wichtigen (Festlegung hierzu im Projekthandbuch) Änderungen
einberufen und entscheidet, wie über eine oder mehrere zusammenhängende Änderungen verfahren werden
soll. Die Durchführung der Änderung selbst wird durch das Projektmanagement geplant und angestoßen.

Aufgaben und
Befugnisse

➢ Bewerten der Projektsituation als Ausgangsbasis der zu treffenden

Entscheidung,

➢ Erstellen von managementspezifischen Entscheidungskriterien als Basis

der zu treffenden Entscheidung,

➢ Treffen der Entscheidung zu einer oder mehreren

Problemmeldungen/Änderungsanträgen auf Basis der
Problem-/Änderungsbewertung,

➢ Festlegen des weiteren Vorgehens, um Änderungsanträge umzusetzen.

Fähigkeitsprofil

➢ Erfahrung im Projektmanagement und in der Bewertung von

unvorhergesehenen Projektsituationen,

➢ Erfahrung mit der Bewertung von möglichen Auswirkungen von

Änderungen (Aufwand, Zeit, Budget, Ressourcen, Qualität) und deren
Konsequenzen für den Projekterfolg,

➢ Beurteilungskompetenz bezüglich der Relevanz von Änderungsanträgen

im Hinblick auf den Projekterfolg,

➢ Kommunikationsfähigkeit und Eignung zur Konsensfindung bei

kontroversen Vorstellungen zum weiteren Vorgehen
(Verhandlungsgeschick),

➢ Durchsetzungsvermögen im Projekt.

Die Änderungssteuerungsgruppe besteht aus projektinternen Vertretern, die auf
operationaler Ebene arbeiten, beispielsweise aus Projektleitung,
Entwicklungsdisziplinen, QS und KM.
Bei großen und abstimmungsintensiven Projekten kann zusätzlich eine
projektübergreifende Änderungssteuerungsgruppe mit Vertretern von
Auftraggeber und Auftragnehmer gebildet werden.

Rollenbesetzung

Verantwortlich für

Änderungsentscheidung

D.1.2 Änderungsverantwortlicher
Der Änderungsverantwortliche ist ein erfahrener Fachmann auf seinem Gebiet. Er wird vom  Projektleiter je
nach dem Thema der Problemmeldung bzw. des Änderungsantrags ausgewählt und bearbeitet dieses Thema
selbstständig, indem er

➢ das Problem analysiert,

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

D.1 Projektteamrollen

199

➢ Lösungsvorschläge zu dem Problem erarbeitet,

➢ diese bewertet und eine Empfehlung ausspricht.

Aufgaben und
Befugnisse

➢ Recherchieren der Ursache des geschilderten Problems,
➢ Festlegen von technischen Entscheidungskriterien zur Bewertung der

Lösungen,

➢ Suchen einer geeigneten Lösung für das geschilderte Problem,
➢ Empfehlung der technisch sinnvollsten Lösung.

Fähigkeitsprofil

➢ Fachliche Erfahrung auf dem Themengebiet, das der Problemmeldung

bzw. dem Änderungsantrag zugrunde liegt,

➢ Technisches Verständnis und Kenntnis des Systems
(anwendungsbezogen/Einsatzgebiet/Technik),

➢ Gute Fachkenntnisse zwecks Ermittlung geeigneter Lösungsvorschläge

zum vorliegenden Problem/Fehler/Verbesserungsvorschlag,

➢ Erfahrung in der technischen Bewertung der Lösungsvorschläge (Vor-

und Nachteile),

➢ Gute Kenntnisse des V-Modells, um den Ansatzpunkt der erforderlichen

Änderung identifizieren zu können,

➢ Fähigkeit, Abhängigkeiten und Auswirkungen zu erkennen,
➢ Fähigkeit, zu erkennen, ob der Änderungswunsch den Rahmen der

vereinbarten Anwenderforderungen überschreitet (Vertragsänderung).

Rollenbesetzung

Der Änderungsverantwortliche ist immer für die
Problemmeldungen/Änderungsanträge verantwortlich, wenn auch in
Abhängigkeit vom Themengebiet der Änderungswünsche unterschiedliche
Änderungsverantwortliche für unterschiedliche Gebiete benannt werden können
(z.B. System-Themen, SW-Themen, HW-Themen, Logistik etc.).

Verantwortlich für

Änderungsstatusliste, Problem-/Änderungsbewertung,
Problemmeldung/Änderungsantrag

Wirkt mit bei

Projektstatusbericht, Änderungsentscheidung

D.1.3 Anforderungsanalytiker (AG)
Der  Anforderungsanalytiker (AG)  ist nach Erteilung des Projektauftrags für die Erstellung des Lastenhefts
und   der  Anforderungsbewertung  zuständig.   Bei   Bedarf   führt   er   zusätzlich   eine  Marktsichtung   für
Fertigprodukte  durch.   Deren   Ergebnisse   werden   im   Rahmen   der  Anforderungsbewertung  evaluiert   und
entsprechend berücksichtigt, analog einer Make-or-Buy-Entscheidung.

Er   hat   die   Qualität   der   Anwenderanforderungen   sicherzustellen   und   die   Voraussetzungen   für   die
Verfolgbarkeit und die Veränderbarkeit der Anforderungen über alle Lebenszyklusabschnitte zu schaffen. Der
Anforderungsanalytiker   (AG)   hat   die   Grundlagen   der   Fachgebiete   "Requirements   Engineering"   und
"Procurement Planning" bei der Aufgabendurchführung zu beachten.

Aufgaben und
Befugnisse

➢ Erarbeiten der Grundlagen für die Erstellung und das Management von

Anforderungen,

➢ Auswahl und Einrichten der Werkzeuge für die Erfassung und

Verwaltung der Anforderungen,

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

200

 Referenz Rollen

➢ Analyse von Geschäftsprozessen,
➢ Mitarbeit bei Realisierungsuntersuchungen,
➢ Analyse von Bedrohung und Risiko,
➢ Durchführung von Schwachstellenanalyse und Sicherheits- und

Leistungsanalyse,

➢ Erfassen und Beschreiben der funktionalen und nicht-funktionalen

Anforderungen,

➢ Abstimmen und Harmonisieren der erfassten Anforderungen mit allen

Beteiligten,

➢ Systematisieren und Priorisieren der erfassten Anforderungen,
➢ Erstellen von Abnahmekriterien,
➢ Erstellen des Entwurfs eines Anforderungsdokuments,
➢ Qualitätssicherndes Überprüfen der Anforderungen nach vorgegebenen

Qualitätskriterien,

➢ Überprüfen des Systementwurfs auf Einhaltung der

Anwenderanforderungen,

➢ Mängelbeseitigung bei Anforderungen,
➢ Aufbereiten der Anforderungen für das Anforderungscontrolling,
➢ Analyse der operationellen Notwendigkeit und der technischen

Machbarkeit von Anforderungen,

➢ Bewerten der Anforderungen nach deren Wirtschaftlichkeit (Kosten-

Nutzen-Analysen),

➢ Erstellen eines ausschreibungsreifen Anforderungsdokumentes.

➢ Kenntnisse und Erfahrungen in den Disziplinen "Requirements

Engineering" (Anforderungserstellung und Anforderungsmanagement)
und "Procurement Planning" (Beschaffungsplanung),
➢ Kenntnis über Anwendung und Einsatzgebiete des Systems,
➢ Erfahrung in der Bewertung von Architekturen,
➢ Erfahrung im Umgang mit den Werkzeugen für Requirements

Engineering,

➢ Fähigkeit, zu abstrahieren, zu modellieren und zu vereinfachen,
➢ Fähigkeit, Abhängigkeiten zu erkennen,
➢ Fähigkeit, zu moderieren,
➢ Befähigung zum systematischen Vorgehen,
➢ Kommunikationsfähigkeit mit dem Auftragnehmer/Anwender und

Projektpersonal.

Fähigkeitsprofil

Verantwortlich für

Wirkt mit bei

Bewertung Lastenheft Gesamtprojekt, Lastenheft Gesamtprojekt, Lastenheft
(Anforderungen), Anforderungsbewertung

Marktsichtung für Fertigprodukte, WiBe (Fortschreibung), Kriterienkatalog,
Leistungsbewertungsmatrix, Vergabeunterlagen (Ausschreibung), Vertrag

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

D.1 Projektteamrollen

201

D.1.4 Anforderungsanalytiker (AN)
Der Anforderungsanalytiker (AN) ist nach Erhalt der Anwenderanforderungen (Lastenheft) für die Erstellung
des   Produkts  Pflichtenheft   (Gesamtsystementwurf)  zuständig.   Für   diese   komplexe   Aufgabe   hat   er
fachspezifische   Mitarbeiter   einzubinden,   um   die   Qualität   der   Anforderungen   sicherzustellen   und   die
Voraussetzungen für die Verfolgbarkeit aller Anforderungen über alle Lebenszyklusabschnitte zu schaffen.
Der Anforderungsanalytiker (AN) hat die Grundlagen des Fachgebietes Requirements Engineering bei der
Aufgabendurchführung zu beachten.

Aufgaben und
Befugnisse

➢ Erarbeiten der Grundlagen für die Erstellung und das Management von

Anforderungen,

➢ Auswahl und Einrichten der Werkzeuge für die Erfassung und

Verwaltung der Anforderungen,
➢ Analyse von Geschäftsprozessen,
➢ Bewertung, Verfeinerung und Erstellung von funktionalen

Anforderungen,

➢ Bewertung, Verfeinerung und Erstellung von nicht-funktionalen

Anforderungen,

➢ Abstimmen und Harmonisieren der Anforderungen mit allen Beteiligten,
➢ Systematisieren und Priorisieren der Anforderungen,
➢ Erstellung einer Grobarchitektur bzgl. System und Logistischer

Unterstützung,

➢ Erstellen von Abnahmekriterien,
➢ Erstellen des Entwurfs eines Anforderungsdokuments,
➢ Qualitätssicherndes Überprüfen der Anforderungen nach vorgegebenen

Qualitätskriterien,

➢ Mängelbeseitigung bei Anforderungen,
➢ Aufbereiten der Anforderungen für das Anforderungscontrolling,
➢ Bewerten von Anforderungen nach vorgegebenen Kriterien,
➢ Analyse der operationellen Notwendigkeit und der technischen

Machbarkeit von Anforderungen,

➢ Bewerten der Anforderungen nach deren Wirtschaftlichkeit (Kosten-

Nutzen-Analysen),

➢ Erstellen einer übergeordneten Systemspezifikation,
➢ Zuordnung von Anforderungen zu den Produktlebenszyklen,
➢ Mitarbeit bei Realisierungsuntersuchungen,
➢ Analysieren von Bedrohung und Risiko,
➢ Schwachstellenanalyse durchführen,
➢ Sicherheits- und Leistungsanalyse durchführen,
➢ Entwurf von Systemarchitekturen.

➢ Kenntnisse und Erfahrungen in den Disziplinen "Requirements

Engineering" (Anforderungserstellung und Anforderungsmanagement)
und "Planning Procurement" (Beschaffungsplanung),

➢ Erfahrungen im Umgang mit Werkzeugen für Requirements Engineering,
➢ Befähigung zum systematischen Vorgehen,

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

Fähigkeitsprofil

202

 Referenz Rollen

➢ Abstraktionsfähigkeit,
➢ Fähigkeit, zu moderieren,
➢ Kommunikationsfähigkeit,
➢ Kenntnis über Anwendung und Einsatzgebiete des Systems,
➢ Fähigkeit, Abhängigkeiten zu erkennen,
➢ Erfahrung in der Bewertung von Architekturen,
➢ Kommunikationsfähigkeit mit Auftraggeber/Anwender und

Projektpersonal.

Verantwortlich für

Pflichtenheft (Gesamtsystementwurf)

Wirkt mit bei

Anwenderaufgabenanalyse

D.1.5 Ausschreibungs- und Vertragsverantwortlicher
Der Ausschreibungs- und Vertragsverantwortliche verantwortet die Vergabe von Entwicklungsaufträgen an
externe Dienstleister im Projekt. Er ist damit das Bindeglied zwischen der Systementwicklung und dem
Vergaberecht,   da   es   seine   Aufgabe   ist,   durch   das   Vergabeverfahren   einen   geeigneten   Auftragnehmer
auszuwählen.

Aufgaben und
Befugnisse

Fähigkeitsprofil

➢ Planung und Organisation des Vergabeverfahrens,
➢ Abstimmung mit Anforderungsanalytiker (AG), Projektleiter und QS-

Verantwortlicher hinsichtlich der Leistungsbeschreibung und Bewertung
der Vorgaben aus vergaberechtlicher Sicht,

➢ rechtssichere Durchführung der Ausschreibung, angefangen bei der

Auswahl des geeigneten Beschaffungskonzeption bis hin zum Zuschlag
für einen oder mehrere Bieter,

➢ Beachtung des korrekten zeitlichen Ablaufs und der Einhaltung aller

Richtlinien und rechtlichen Vorgaben bei der Ausschreibung,

➢ Abstimmung mit der Vergabestelle bei der Auswahl von potentiellen

Auftragnehmern, falls ein Verteiler für die Ausschreibung erstellt werden
muss.

➢ Profunde Kenntnisse der rechtlichen Grundlagen und der Vorschriften im
Ausschreibungswesen, insbesondere der Richtlinien zur Erstellung der
Ausschreibungsunterlagen und des Vergaberechts wie z.B. UfAB, WiBe,
VgV, GWB, VOL, VOB,

➢ Erfahrung mit der Erstellung von Ausschreibungen,
➢ Erfahrung bei der Umsetzung von Anforderungen in

Bewertungskriterien,

➢ Erfahrung bei der Bewertung von Angeboten.

Rollenbesetzung

Verantwortlich für

Es ist sinnvoll, wenn die Vergabestelle einen oder mehrere Ausschreibungs- und
Vertragsverantwortliche zur Mitarbeit in den Projekten bereitstellt.

Beschaffungskonzeption, Kriterienkatalog, Leistungsbewertungsmatrix,
Eignungsbewertungsmatrix, Vergabeunterlagen (Ausschreibung),
Verfahrensdokumentation, Vergabevermerk, Vertrag, Vertragszusatz,
Vertragsübersicht, Angebotsaufforderung, Auftrag, Änderungsvereinbarung
(Change Request)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

D.1 Projektteamrollen

203

Wirkt mit bei

Anforderungsbewertung, Abnahmeerklärung

D.1.6 Betriebsverantwortlicher
Das   Ziel   des   Betriebsverantwortlichen   besteht   darin,   die   Überführung   des   Systems   in   den   Betrieb
reibungslos zu gestalten und einen sicheren und zuverlässigen Betrieb zu ermöglichen. Bei der Entwicklung
von   sicherheitskritischen   Systemen   arbeitet   der   Betriebsverantwortliche   dort   eng   mit   dem
Informationssicherheitsverantwortlichen   zusammen,   wo   Maßnahmen   des   Betriebs   zur   Vermeidung   oder
Reduzierung von Sicherheitsrisiken beitragen.

Auf der Auftraggeberseite gewährleistet der Betriebsverantwortliche die Einhaltung der organisationsweit
geltenden Regelungen im zu entwickelnden IT-System. In Abstimmung mit dem Betriebsbeauftragten erstellt
er mit den Vorgaben zum IT-Betrieb einen für das Projekt relevanten Auszug dieser Regelungen und achtet
auf dessen Einhaltung. Der Betriebsverantwortliche wirkt diesbezüglich mindestens bei der Erhebung und
Verfeinerung von Anforderungen und bei der Abnahme des Systems mit. Er prüft ggf. die  Erweiterung der
Vorgaben zum IT-Betrieb des Auftragnehmers und leitet sie an den Betriebsbeauftragten zur Übernahme in
die  allgemeinen Regelungen  weiter.  Darüber  hinaus  ist  der  Betriebsverantwortliche  dafür  zuständig eine
Betriebliche Freigabeerklärung für das entwickelte System vom Betreiber zu erwirken.

Auf   der   Auftragnehmerseite   agiert   der   Betriebsverantwortliche   als   Schnittstelle   zwischen   Betrieb   und
Entwicklung und unterstützt das Projekt im Verständnis und in der Umsetzung der betrieblichen Vorgaben.
Zudem erstellt er bei Bedarf eine Erweiterung der Vorgaben zum IT-Betrieb.

Aufgaben und
Befugnisse

➢ Herstellung der Kommunikation zwischen Entwicklung und Betrieb,
➢ Überwachung der Einhaltung betrieblicher Vorgaben und

Rahmenbedingungen,

➢ Ausgestaltung von Auswirkungen auf den IT-Betrieb,
➢ Ausgestaltung betrieblicher Maßnahmen im Rahmen der
Sicherheitskonzeption, dazu Abstimmung mit dem
Informationssicherheitsverantwortlichen.

Fähigkeitsprofil

➢ Kenntnisse über den Aufbau der IT-Organisation, insbesondere über

Aufgabenverteilung und Ansprechpartner,

➢ Kenntnisse der Vorgaben zum IT Betrieb und Fähigkeit, diese an andere

Projektbeteiligte zu vermitteln,

➢ Kenntnisse über generelle Maßnahmen zur Verbesserung der IT-

Sicherheit im Betrieb,

➢ Aufbau einer direkten Kommunikation zwischen Entwicklung und

Betrieb.

Verantwortlich für

Wirkt mit bei

Vorgaben zum IT-Betrieb, Prüfspezifikation Inbetriebnahme, Prüfprotokoll
Inbetriebnahme, Betriebliche Freigabeerklärung, Erweiterung der Vorgaben zum
IT-Betrieb

Projekthandbuch, Lastenheft Gesamtprojekt, Lastenheft (Anforderungen),
Pflichtenheft (Gesamtsystementwurf), Systemarchitektur, SW-Architektur,
Sicherheitskonzeption, Abnahmeprotokoll, Abnahmespezifikation

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

204

 Referenz Rollen

D.1.7 Datenschutzverantwortlicher
Der   Datenschutzverantwortliche   ist   der   zentrale  Ansprechpartner   im   Projekt   für   alle  Aspekte,   die   den
Datenschutz   im   zu   entwickelnden   System   betreffen.   Als   Experte   hat   er   weitgehende   Kenntnisse   und
umfangreiche   Erfahrungen   in   der   Ausgestaltung   technischer   und   organisatorischer   Maßnahmen   zur
Gewährleistung   des   Datenschutzes.   Der   Datenschutzverantwortliche   unterstützt   das   Projektteam   im
gesamten Projektverlauf.

Auf   der   Auftraggeberseite   gewährleistet   der   Datenschutzverantwortliche   die   Einhaltung   der
organisationsweit   geltenden   Regelungen   im   zu   entwickelnden   IT-System.   In   Abstimmung   mit   dem
Datenschutzbeauftragten erstellt  er  mit   den  Vorgaben  zum  Datenschutz  einen für   das  Projekt  relevanten
Auszug   dieser   Regelungen   und   achtet   auf   dessen   Einhaltung.   Der   Datenschutzverantwortliche   wirkt
diesbezüglich mindestens bei der Erhebung und Verfeinerung von Anforderungen und bei der Abnahme des
Systems mit und arbeitet eng mit dem Informationssicherheitsverantwortlichen zusammen. Er prüft ggf. die
Erweiterung   der   Vorgaben   zum   Datenschutz  des   Auftragnehmers   und   leitet   sie   an   den
Datenschutzbeauftragten zur Übernahme in die allgemeinen Regelungen weiter.

Auf der Auftragnehmerseite achtet der Datenschutzverantwortliche bei der Systemerstellung darauf, dass der
Datenschutz fest im System verankert wird ("Privacy by Design") und dass etwaige Voreinstellungen bei der
Erhebung oder Verarbeitung von Daten datenschutzgerecht implementiert werden ("Privacy by Default").
Zudem erstellt er bei Bedarf eine Erweiterung der Vorgaben zum Datenschutz.

Aufgaben und
Befugnisse

Fähigkeitsprofil

➢ Beratung und Unterstützung des Projektteams in allen Fragen zum

Datenschutz,

➢ Erstellung der projektspezifischen Vorgaben zum Datenschutz,
➢ Mitgestaltung von Anforderungen an das IT-System zur Einhaltung der

Vorgaben des Datenschutzes,

➢ Durchgängige Unterstützung bei der Umsetzung von "Privacy by Design"

und "Privacy by Default",

➢ Ermittlung technischer, organisatorischer, personeller und materieller

Maßnahmen aus Sicht des Datenschutzes,

➢ Kommunikation und Abstimmung mit den entsprechenden Rollen der

beteiligten Organisationen,

➢ Prüfung und Weiterleitung der Erweiterung der Vorgaben zum

Datenschutz des Auftragnehmers.

➢ Kenntnis der relevanten Normen zum Datenschutz,
➢ Kenntnis der organisationsweiten Vorgaben zum Datenschutz,
➢ Kenntnisse über zielführende Maßnahmen zum Erreichen des

angestrebten Datenschutz-Niveaus,

➢ Durchsetzungsvermögen.

Verantwortlich für

Vorgaben zum Datenschutz, Erweiterung der Vorgaben zum Datenschutz

Wirkt mit bei

Projekthandbuch, Lastenheft Gesamtprojekt, Lastenheft (Anforderungen),
Pflichtenheft (Gesamtsystementwurf), Systemarchitektur, SW-Architektur,
Schutzbedarfsfeststellung, Vorgaben zur Informationssicherheit,
Sicherheitskonzeption, Erweiterung der Vorgaben zur Informationssicherheit,
Abnahmeprotokoll, Abnahmespezifikation

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

D.1 Projektteamrollen

205

D.1.8 Ergonomieverantwortlicher
Der   Ergonomieverantwortliche   ist   verantwortlich  für   die   Benutzbarkeit   und  Ergonomie   des   Systems.   Er
muss die Umsetzung ergonomischer Forderungen im Gesamtsystem (d.h. für System, SW, HW, Logistik,
etc.) sicherstellen und stellt ein wesentliches Bindeglied zwischen Benutzer und Auftragnehmer dar.

Außerdem ist der Ergonomieverantwortliche verantwortlich für die Gesamtgestaltung der Nutzeroberflächen.
Er   ist   maßgeblich   an   der   Festlegung   des   Bedien-   und   Darstellungskonzeptes   sowie   der   Festlegung   der
Regeln für die Gestaltung der Mensch-Maschine-Schnittstellen beteiligt.

Aufgaben und
Befugnisse

Fähigkeitsprofil

➢ Durchführung der Anwenderaufgabenanalyse und der Analyse von

Geschäftsprozessen,

➢ Erstellen und Abstimmen eines Styleguides,
➢ Einbringen von Ergonomie-Aspekten in die Prüfspezifikationen.

➢ Kenntnisse und Erfahrungen in der Disziplin Ergonomie und Usability,
➢ Erfahrungen beim Design von Nutzeroberflächen,
➢ Erfahrungen im Umgang mit den Werkzeugen für Usability Engineering,
➢ Befähigung zum systematischen Vorgehen,
➢ Fähigkeit, zu moderieren,
➢ Kommunikationsfähigkeit,
➢ Kenntnisse über Anwendung und Einsatzgebiete des Systems,
➢ Fähigkeit, zu abstrahieren, zu modellieren und zu vereinfachen,
➢ Fähigkeit, Abhängigkeiten zu erkennen.

Verantwortlich für

Anwenderaufgabenanalyse, Mensch-Maschine-Schnittstelle (Styleguide)

Wirkt mit bei

Externe-Einheit-Spezifikation, Pflichtenheft (Gesamtsystementwurf),
Nutzungsdokumentation, Prüfspezifikation Systemelement, Systemspezifikation,
Externes-SW-Modul-Spezifikation, SW-Spezifikation

D.1.9 Informationssicherheitsverantwortlicher
Der Informationssicherheitsverantwortliche ist der zentrale Ansprechpartner im Projekt für alle Aspekte, die
die   Informationssicherheit   des   zu   entwickelnden   Systems   betreffen.   Als   Experte   hat   er   weitgehende
Kenntnisse   und   umfangreiche   Erfahrungen   vor   allem   bei   der   Beurteilung   von   Bedrohungen   und   in   der
Ausgestaltung   technischer   und   organisatorischer   Maßnahmen   zur   Absicherung   eines   IT-Systems.   Der
Informationssicherheitsverantwortliche unterstützt das Projektteam im gesamten Projektverlauf.

Auf   der   Auftraggeberseite   gewährleistet   der   Informationssicherheitsverantwortliche   die   Einhaltung   der
organisationsweit   geltenden   Regelungen   im   zu   entwickelnden   IT-System.   In   Abstimmung   mit   dem
Informationssicherheitsbeauftragten erstellt er mit den  Vorgaben zur Informationssicherheit  einen für das
  Der
Projekt   relevanten   Auszug   dieser   Regelungen   und   achtet   auf   dessen   Einhaltung.
Informationssicherheitsverantwortliche wirkt diesbezüglich mindestens bei der Erhebung und Verfeinerung
von   Anforderungen   und   bei   der   Abnahme   des   Systems   mit   und   arbeitet   eng   mit   dem
 Erweiterung   der   Vorgaben   zur
Datenschutzverantwortlichen   zusammen.   Er   prüft   ggf.   die
Informationssicherheit  des  Auftragnehmers   und   leitet   sie   an   den   Informationssicherheitsbeauftragten   zur
Übernahme in die allgemeinen Regelungen weiter.

  der

  Auftragnehmerseite   verantwortet

Auf
Informationssicherheitsverantwortliche   die
Sicherheitskonzeption.   Er   analysiert   mögliche   Schwachstellen   und   Bedrohungen   des   zu   entwickelnden
Systems, stimmt geeignete Maßnahmen zur Behandlung der Risiken mit dem Auftraggeber ab und achtet auf

  der

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


206

 Referenz Rollen

deren   Umsetzung   bei   der   Systemerstellung   ("Security   by   Design").   Zudem   erstellt   der
Informationssicherheitsverantwortliche   bei
  Vorgaben   zur
Informationssicherheit.

 Erweiterung   der

  Bedarf

  eine

Aufgaben und
Befugnisse

Fähigkeitsprofil

➢ Sensibilisierung, Beratung und Unterstützung des Projektteams in allen

Fragen zur Informationssicherheit,

➢ Erstellung der projektspezifischen Vorgaben zur Informationssicherheit,
➢ Durchführung der Bedrohungsanalyse,
➢ Ermittlung technischer, organisatorischer, personeller und materieller

Maßnahmen zur Verbesserung der Informationssicherheit,

➢ Unterstützung beim Entwurf der SW-Architektur und bei der Erstellung

der Spezifikationen,

➢ Durchgängige Unterstützung bei der Umsetzung von "Security by

Design",

➢ Kommunikation und Abstimmung mit den entsprechenden Rollen der

beteiligten Organisationen,

➢ Prüfung und Weiterleitung der Erweiterung der Vorgaben zur

Informationssicherheit des Auftragnehmers.

➢ Kenntnisse einschlägiger Standards, Methoden und Leitlinien,
➢ Erfahrung in Projekten ähnlicher Zielsetzung und vergleichbarer Technik,
➢ Kenntnis typischer IT-Bedrohungen und zielführender

Sicherheitsanforderungen,

➢ Kenntnis bewährter Architekturprinzipien und relevanter

Referenzarchitekturen,

➢ Kenntnis moderner Methoden zur Systementwicklung und zum Testen

von Systemen,

➢ Fähigkeit, Probleme unter adäquater Berücksichtigung der Architektur zu

analysieren und entsprechende Lösungsvorschläge auszuarbeiten,

➢ Fähigkeit zu abstrahieren und zu vereinfachen,
➢ Fähigkeit, Abhängigkeiten zu erkennen,
➢ Kenntnisse über Systemintegration,
➢ Kommunikationsfähigkeit und Durchsetzungsvermögen.

Verantwortlich für

Wirkt mit bei

Vorgaben zur Informationssicherheit, Sicherheitskonzeption, Erweiterung der
Vorgaben zur Informationssicherheit

Projekthandbuch, Lastenheft Gesamtprojekt, Lastenheft (Anforderungen),
Pflichtenheft (Gesamtsystementwurf), Systemarchitektur, SW-Architektur,
Schutzbedarfsfeststellung, Abnahmeerklärung, Abnahmeprotokoll,
Abnahmespezifikation

D.1.10 KM-Verantwortlicher
Der KM-Verantwortliche leitet, koordiniert und steuert das  Konfigurationsmanagement  und legt alle dafür
notwendigen projektspezifischen Bedingungen im Projekthandbuch fest. Er verwaltet die Produktbibliothek
 en
und berichtet dem Projektleiter über den Projektfortschritt. Er ist zuständig für die  Produktkonfiguration

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


D.1 Projektteamrollen

207

sowie für die Sicherung und Archivierung der Produkte und Konfigurationen, so dass die gegenwärtige wie
auch die vergangenen Produktkonfigurationen des Systems jederzeit nachvollziehbar und wiederherstellbar
sind.

Aufgaben und
Befugnisse

➢ Erstellung des Anteils Konfigurationsmanagement im Projekthandbuch,
➢ Steuerung der Einrichtung des Konfigurationsmanagements und der

Produktbibliothek,

➢ Einrichtung und Verwaltung der Zugriffsberechtigungen,
➢ Steuerung zur Initialisierung und Verwaltung der Produktbibliothek,
➢ Steuerung zur Initialisierung und Fortschreibung der

Produktkonfigurationen,

➢ Umsetzung der Anforderungen an die Sicherung und Archivierung der

Produkte,

➢ Auswertung der Produktbibliothek und Berichterstattung an den

Projektleiter,

➢ Festlegung und Koordination der KM-Abläufe,
➢ Einrichtung des Konfigurationsmanagements und der Produktbibliothek,
➢ Durchführung der Initialisierung und Verwaltung der Produkte und

Produktkonfigurationen,

➢ Sicherung und Archivierung der Produkte und Konfigurationen,
➢ Dokumentation der Auslieferungsinformationen,
➢ Übergabe der Produktbibliothek in den Betrieb,
➢ Durchführung der KM-Abläufe bezogen auf den Datenaustausch mit z.B.

Auftraggeber (AG)/Partner/Unterauftragnehmer (UAN).

➢ Kann KM-Regeln durchsetzen,
➢ Kennt und beherrscht die für den Aufgabenbereich erforderlichen

Prozesse, Verfahren, Methoden und Werkzeuge des
Konfigurationsmanagements,

➢ Kennt die Rahmenbedingungen/Regelungen für die Konfigurations- und

Produktverwaltung (einheitliche Identifizierungssystematik,

➢ Kennt die Versionsvielfalt des Systems,
➢ Fähigkeit zu Organisation und Kommunikation.

Die Rolle des KM-Verantwortlichen muss in jedem Projekt besetzt werden. Da
im Problem- und Änderungsmanagement Änderungen an Produkten und
Konfigurationen beschlossen werden können, sollte der KM-Verantwortliche
Mitglied der Änderungssteuerungsgruppe (Change Control Board) sein. Ist die
Produktbibliothek über mehrere technische Systeme aufgeteilt (z.B.
Dokumentenmanagement vs. Codeverwaltung), so kann für jeden Teilbereich ein
eigener KM-Verantwortlicher benannt werden.

Fähigkeitsprofil

Rollenbesetzung

Verantwortlich für

Produktbibliothek, Produktkonfiguration

Wirkt mit bei

Projektabschlussbericht, Projekthandbuch, Projektplan, Projektstatusbericht,
Änderungsentscheidung, Problem-/Änderungsbewertung

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

208

 Referenz Rollen

D.1.11 Product Owner
Der  Product   Owner  ist   für   die  Wertmaximierung   und   die   fachlichen   Eigenschaften   des   zu   erstellenden
Systems   zuständig.   Für   jedes   Entwicklungsteam  beim Auftragnehmer   wird  ein   verantwortlicher  Product
Owner durch den Auftraggeber gestellt. Die Rolle verantwortet mit dem Product Backlog die verständliche
Formulierung sowie eindeutige Priorisierung der darin enthaltenen Einträge und vertritt die Interessen des
Auftraggebers innerhalb eines agilen Teams.

Der  Product   Owner  ist   zudem   für   die   Prüfung   der   umgesetzten   Backlog-Einträge   auf   Basis   der
Akzeptanzkriterien und der Definition of Done zuständig. Während des Sprints arbeitet der Product Owner
eng mit dem Entwicklungsteam des Auftragnehmers an der Umsetzung der User Stories.

Aufgaben und
Befugnisse

➢ Vertretung der Interessen des Auftraggebers im agilen Team, Einbindung

aller relevanten Stakeholder auf Auftraggeber-Seite

➢ Steuerung, welche Anforderungen mit dem für den Nutzer/Auftraggeber
höchsten (wirtschaftlichen und fachlichen) Wert im entstehenden System
umgesetzt werden

➢ Verantwortung für das Product Backlog, insbesondere alleinige Befugnis

zur Priorisierung und der für das Projektteam verständlichen
Priorisierung aller Product Backlog-Einträge

➢ Begleitung des Entwicklungsteams des Auftragnehmers im Sprint,
Beantwortung von Rückfragen zu den Product Backlog-Einträgen

➢ Steuerung der Produktqualität über die Definition und Überwachung der

Akzeptanzkriterien

➢ Prüfung der Umsetzung von Backlog-Einträgen auf Basis der

Akzeptanzkriterien und der Definition of Done

Verantwortlich für

Anforderungskonzept, Product Backlog, Inkrement (von AN)

D.1.12 Projektleiter
Der Projektleiter (engl.: Project Manager) übernimmt die operative Leitung des Projektes und besetzt damit
die   Schlüsselposition   innerhalb   des   Projektteams.   Er   plant,   koordiniert,   überwacht   und   steuert   den
Projektablauf, das Projektteam und das Projekt als Ganzes. Er hat stets alle Projektziele im Blick (auch die
Qualitätsziele), erkennt ggf. Zielkonflikte und eskaliert diese an den Projekteigner, wenn keine projektinterne
Lösung gefunden wird. In der Regel ist der Projektleiter gegenüber den Mitgliedern seines Projektteams
weisungsbefugt.

Aufgaben und
Befugnisse

Zusätzlich zu der im V-Modell festgelegten Verantwortung und Mitwirkung hat
der Projektleiter die folgenden Aufgaben:

➢ Regelmäßiger und auch außerplanmäßiger Bericht an den

Lenkungsausschuss bei anstehenden Problemen,

➢ Verantwortlichkeit für die technische Lösung und deren Realisierung,
➢ Überwachung der Termine, des Erfüllungsgrads der Arbeitspakete und

des Mittelabflusses sowie Bericht bei festgelegten
Projektfortschrittsentscheidungen im Lenkungsausschuss,

➢ Mitwirkung bei der Auswahl und der Überwachung der

Leistungserbringung von (Unter-) Auftragnehmern und Zulieferern.
➢ Federführung für die Vorbereitung der Entscheidung über Abgabe eines

Angebots.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

D.1 Projektteamrollen

Fähigkeitsprofil

Rollenbesetzung

209

➢ Kenntnis und Erfahrung in der Projektabwicklung,
➢ Kenntnis von betriebswirtschaftlichen Zusammenhängen,
➢ Kennt Anwendung, Einsatzgebiete und technische Ausprägung des

Systems,

➢ Kenntnis der Methoden und Werkzeuge des Projektmanagements,
➢ Durchsetzungsvermögen und Akzeptanz gegenüber den

Projektbeteiligten,

➢ Fähigkeit zu Führung, Motivation und Moderation,
➢ Fähigkeit zu Organisation und Kommunikation.

➢ Jedes Projekt hat zu jeder Zeit genau einen Projektleiter.
➢ Es ist sinnvoll, einen ständigen Vertreter des Projektleiters zu benennen,
der bei einem kurzfristigen Ausfall des Projektleiters dessen Arbeit
weiterführen kann.

➢ Bei größeren Projekten ist eine Aufteilung in mehrere Teilprojekte
sinnvoll, für die eigene Teilprojektleiter ernannt werden. Ein
Gesamtprojektleiter trägt dann die Gesamtverantwortung.

➢ Die eher administrativen Aufgaben können an weitere Mitarbeiter

delegiert werden, hierzu kann ein Projektbüro oder Projektsekretariat
eingerichtet werden.

➢ Der Projektleiter ist Mitglied im Lenkungsausschuss und in der

Änderungssteuerungsgruppe (Change Control Board).

➢ Der Projektleiter darf nicht gleichzeitig QS-Verantwortlicher sein.

Verantwortlich für

Wirkt mit bei

Aufgabenliste, Besprechungsdokument, Projektabschlussbericht,
Projekthandbuch, Projektplan, Projektstatusbericht, Projekttagebuch, Risikoliste,
Schätzung, Messdaten, Kennzahlenauswertung, Make-or-Buy-Entscheidung,
Marktsichtung für Fertigprodukte, Informationssicherheits-Navigator, Lieferung,
WiBe (Fortschreibung), Leistungsvereinbarung (SLA/OLA/UC), Lieferung (von
AN), Projektabschlussbericht (von AN), Projektstatusbericht (von AN)

Projektfortschrittsentscheidung, QS-Handbuch, Produktbibliothek, Bewertung
Lastenheft Gesamtprojekt, Lastenheft Gesamtprojekt, Lastenheft
(Anforderungen), Anforderungsbewertung, Abnahmeerklärung, Kriterienkatalog,
Leistungsbewertungsmatrix, Eignungsbewertungsmatrix, Vergabeunterlagen
(Ausschreibung), Vertrag

D.1.13 Prüfer
Der Prüfer erstellt die Prüfspezifikationen und prüft anhand dieser die Projektergebnisse. Er protokolliert das
Ergebnis der Prüfung in einem Prüfprotokoll.

Aufgaben und
Befugnisse

➢ Nutzung der Mess- und Prüfumgebung nach den Vorgaben der

Prüfdokumentation,

➢ Erstellen der Prüfspezifikation,
➢ Prüfen und Bewerten der Prüfobjekte anhand der vorgegebenen
Prüfspezifikation/Prüfprozedur und, falls nötig, Einleitung von
Korrekturmaßnahmen,

➢ Dokumentation der Prüfergebnisse im Prüfprotokoll.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

210

Fähigkeitsprofil

Rollenbesetzung

Verantwortlich für

Wirkt mit bei

 Referenz Rollen

➢ Kenntnis der Prüfmethoden und Prüfwerkzeuge,
➢ Kennt die Anwendung, Realisierung und den Einsatz der Prüfobjekte,
➢ Fähigkeit, Schwachstellen und Risiken zu identifizieren.

Der Prüfer ist in der Regel ein Mitglied des Projektteams, meist ein sachkundiger
Entwickler oder eine mit der Thematik des Prüfgegenstandes vertraute Person.
Der Prüfer darf nicht der Ersteller seines Prüfobjektes sein.

Prüfprotokoll, Prüfspezifikation, Prüfprotokoll Systemelement, Prüfprozedur
Systemelement, Prüfspezifikation Systemelement, Abnahmeprotokoll,
Abnahmespezifikation

Externe-Einheit-Spezifikation, Pflichtenheft (Gesamtsystementwurf),
Implementierungs-, Integrations- und Prüfkonzept System, Systemspezifikation,
Externes-SW-Modul-Spezifikation, Implementierungs-, Integrations- und
Prüfkonzept SW, SW-Spezifikation

D.1.14 QS-Verantwortlicher
Der QS-Verantwortliche ist mit der Überwachung der Qualität im Projekt beauftragt. Im Gegensatz zum
Projektleiter   (der   alle   Projektziele   verfolgt),   kümmert   sich  der   QS-Verantwortliche   insbesondere   um  die
Einhaltung der Qualitätsziele. Er ist damit kritischer Partner des Projektleiters und unterstützt ihn bei der
Projektdurchführung.

Aufgaben und
Befugnisse

Fähigkeitsprofil

➢ Mitarbeit in der Änderungssteuerungsgruppe,
➢ Durchführung von Audits,
➢ Sicherstellen der Funktion und Verfügbarkeit der erforderlichen Mess-

und Prüfumgebung in Zusammenarbeit mit dem Prüfer,

➢ Mitsprache im Projektteam,
➢ Uneingeschränkter Zugang zu allen qualitätsbezogenen Vorgängen und

alle Rechte, obige Aufgaben durchzuführen,

➢ Mitzeichnungsrecht bei allen Freigaben innerhalb seines

Aufgabengebiets,

➢ Erstellung des QS-Handbuchs und des QS-Berichtswesens,
➢ Mitwirkung bei der Planung der QS-bezogenen Aufgaben.

➢ Erfahren in Projektabwicklung,
➢ Kennt die Prüfmethoden und Prüfwerkzeuge,
➢ Durchsetzungsvermögen im Projektteam,
➢ Fähigkeit, Schwachstellen und Risiken zu identifizieren,
➢ Fähigkeit zu objektiver und konstruktiver Beurteilung,
➢ Fähigkeit zu Organisation und Kommunikation.

Rollenbesetzung

In jedem Projekt gibt es einen QS-Verantwortlichen. In kleinen Projekten lässt
sich die Rolle gut mit anderen Rollen, z.B. der des KM-Verantwortlichen,
vereinen. Die Rolle des QS-Verantwortlichen darf aufgrund ihrer Definition nicht
mit der Rolle des Projektleiters zusammengelegt werden.

Verantwortlich für

Nachweisakte, QS-Bericht, QS-Handbuch

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

D.1 Projektteamrollen

Wirkt mit bei

211

Projektabschlussbericht, Projektplan, Projektstatusbericht, Risikoliste,
Änderungsentscheidung, Problem-/Änderungsbewertung, Ausbildungsunterlagen,
Pflichtenheft (Gesamtsystementwurf), Implementierungs-, Integrations- und
Prüfkonzept System, Nutzungsdokumentation, Implementierungs-, Integrations-
und Prüfkonzept SW, Abnahmeerklärung

D.1.15 SW-Architekt
Der  SW-Architekt  ist der Verantwortliche für Entwurf und Entwicklung aller  SW-Einheit
vom Typ Externes SW-Modul des System

 s  .

 en     und Produkte

Aufgaben und
Befugnisse

➢ Entwurf der SW-Architektur,
➢ Umsetzung der Anforderungen an die SW-Einheit
➢ Definition der Anforderungen an die Produkte vom Typ Externes SW-

 en

Modul,

➢ Verantwortlichkeit für Implementierungs-, Integrations- und Prüfkonzept

SW,

➢ Verantwortlichkeit für die Externes-SW-Modul-Spezifikation,
➢ Mitarbeit bei der Integration zum Segment und gegebenenfalls zum

System

➢ Mitarbeit an der Systemarchitektur,
➢ Mitarbeit an der Systemspezifikation bzw. Externe-Einheit-Spezifikation.

Fähigkeitsprofil

➢ Kennt Anwendung, Rahmenbedingungen und Einsatzgebiete des

Systems,

➢ Kennt die Schnittstellen des Systems,
➢ Kennt Architekturprinzipien und verschiedene SW-Architekturen,
➢ Kennt die SW-Schnittstellen des Systems,
➢ Kennt Standard-SW,
➢ Kennt Methoden und Werkzeuge,
➢ Fähigkeit, Schwachstellen und Risiken zu erkennen,
➢ Fähigkeit, Probleme unter adäquater Berücksichtigung der SW/HW zu
analysieren und entsprechende Lösungsvorschläge auszuarbeiten,

➢ Fähigkeit, zu abstrahieren und zu vereinfachen,
➢ Fähigkeit, Abhängigkeiten zu erkennen,
➢ Kommunikationsfähigkeit mit HW-Entwicklern, mit Logistikexperten,

sowie mit Anwendern.

Verantwortlich für

Wirkt mit bei

Datenbankentwurf, Externes-SW-Modul-Spezifikation, Implementierungs-,
Integrations- und Prüfkonzept SW, SW-Architektur, SW-Spezifikation

Änderungsentscheidung, Problem-/Änderungsbewertung, Ausbildungsunterlagen,
Externe-Einheit-Spezifikation, Implementierungs-, Integrations- und Prüfkonzept
System, Make-or-Buy-Entscheidung, Nutzungsdokumentation, Prüfspezifikation
Systemelement, Systemarchitektur, Sicherheitskonzeption

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland




212

 Referenz Rollen

D.1.16 SW-Entwickler
Der SW-Entwickler ist für die Realisierung der SW-Element

 e   auf Basis der SW-Spezifikation zuständig.

Aufgaben und
Befugnisse

Fähigkeitsprofil

 e  ,

➢ Realisierung der SW-Modul
➢ Integration der SW-Modul
➢ Einbindung der SW-Einheit
➢ Durchführung von Entwicklertests,
➢ Unterstützung des Prüfer

 e   zu SW-Komponente
 en    in das System,

 n   und SW-Einheit

 en   ,

 s   bei der Prüfung der SW-Elemente.

➢ Kenntnis der Entwicklungsumgebung,
➢ Kenntnis des Entwicklungsstandards,
➢ Kenntnis von Programmierung und Programmierkonzepten,
➢ Kenntnis von Standard-SW, Programmiersprachen, Datendefinitions- und

Datenmanipulationssprachen,

➢ Kenntnis der SW/HW-Schnittstellen,
➢ Fähigkeit zur strukturierten Programmierung,
➢ Fähigkeit, Abhängigkeiten zu erkennen,
➢ Kommunikationsfähigkeit mit HW-Entwicklern, mit Logistikexperten,

sowie mit Anwendern.

Verantwortlich für

Externes SW-Modul, SW-Einheit, SW-Komponente, SW-Modul

Wirkt mit bei

Ausbildungsunterlagen, Nutzungsdokumentation, Prüfprotokoll Systemelement,
Datenbankentwurf, Externes-SW-Modul-Spezifikation, Implementierungs-,
Integrations- und Prüfkonzept SW, SW-Architektur, SW-Spezifikation

D.1.17 Systemarchitekt
Dem Systemarchitekt
 en    kommt die zentrale Rolle für Systementwurf und -spezifikation zu. Er entwirft auf
Basis des Pflichtenhefts die Systemarchitektur. Parallel dazu definiert er die Systemelemente mit Hilfe der
Systemspezifikation  bzw.
 Externe-Einheit-Spezifikation  und   die   dazugehörigen  Implementierungs-,
Integrations- und Prüfkonzept System. Zusätzlich ist der Systemarchitekt noch für die Altsystemanalyse und
das Migrationskonzept verantwortlich.

Aufgaben und
Befugnisse

➢ Entwicklung der Architektur der Systeme,
➢ Abbildung der Systemelement-Spezifikationen auf die entsprechenden

Systemelemente,

➢ Einbringen eigener Erfahrungen und Aufzeigen technischer Risiken und

Chancen,

➢ Definition der Systemelement-Spezifikation,
➢ Mitarbeit an den logistischen Konzepten,
➢ Technischer Entwurf des Systems,
➢ Untersuchung der Realisierbarkeit,
➢ Zuordnung der Anforderungen,
➢ Beschreibung der nichtfunktionalen Anforderungen,
➢ Beschreibung der Schnittstelle,
➢ Überprüfung der Infrastruktur,

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland









D.1 Projektteamrollen

213

➢ Spezifizierung der Systemintegration,
➢ Prüfung des Systems,
➢ Definition der Anforderungen an querschnittliche Nutzung von HW-/SW-

Einheiten,

➢ Bewertung von Altsystemen,
➢ Entwurf von Migrationskonzepten.

Fähigkeitsprofil

➢ Kennt Anwendung, Rahmenbedingungen und Einsatzgebiete des

Systems,

➢ Kennt die SW- und HW-Schnittstellen des Systems,
➢ Kennt Architekturprinzipien und verschiedene SW- bzw. HW-

Architekturen,

➢ Kennt Standard-SW und Standard-HW,
➢ Kennt die Methoden und Werkzeuge der Entwicklung,
➢ Fähigkeit, Schwachstellen und Risiken zu erkennen,
➢ Fähigkeit, Probleme unter adäquater Berücksichtigung der SW/HW zu
analysieren und entsprechende Lösungsvorschläge auszuarbeiten,

➢ Fähigkeit zu abstrahieren und zu vereinfachen,
➢ Fähigkeit, Abhängigkeiten zu erkennen,
➢ Kenntnisse über Systemintegration,
➢ Kommunikationsfähigkeit mit HW-Entwicklern, mit Logistikexperten,

sowie mit Anwendern,

➢ Kenntnisse über Systemnachweis.

Verantwortlich für

Wirkt mit bei

Externe-Einheit-Spezifikation, Implementierungs-, Integrations- und Prüfkonzept
System, Systemarchitektur, Systemspezifikation, Altsystemanalyse,
Migrationskonzept

Projekthandbuch, Projektplan, Änderungsentscheidung,
Problem-/Änderungsbewertung, Ausbildungsunterlagen, Pflichtenheft
(Gesamtsystementwurf), Make-or-Buy-Entscheidung, Nutzungsdokumentation,
Prüfspezifikation Systemelement, SW-Architektur, Marktsichtung für
Fertigprodukte, Sicherheitskonzeption

D.1.18 Systemintegrator
Dem  Systemintegrator  kommt die zentrale  Rolle  in der Phase der Systemrealisierung zu. Er integriert auf
Basis   des   Produkts  Implementierungs-,   Integrations-   und   Prüfkonzept   System  die   Systemelemente   zu
Segment
 en     berücksichtigt
werden.

 en     und zum  System. Bei der Integration müssen gegebenenfalls  Externe Einheit

Aufgaben und
Befugnisse

➢ Installation, Integration und Betreuung eines Systems,
➢ Fehlererkennung bei der Integration,
➢ Schnittstellenkoordination zwischen den Segmenten,
➢ Vorbereitung von Segmentprüfungen in der Entwicklung und

Systemprüfungen vor dem Kunden,

➢ Betreuung und Abnahme von Externen Einheiten,

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland



214

 Referenz Rollen

Fähigkeitsprofil

➢ Unterstützung bei der Erstellung der Schulungsunterlagen und der

Anwenderdokumentation,

➢ Unterstützung bei logistischen Aktivitäten,
➢ Unterstützung des Labormuster- und Prototypenbaus zwischen

Entwicklung und Produktion,
➢ Bereitstellung der Prüfumgebung.

➢ Kennt das System hinsichtlich Aufbau und Funktionsweise,
➢ Kenntnis von Maßnahmen der Entwicklung, Integration und Installation,
➢ Umfassendes Wissen über die Anwendung des Systems,
➢ Fähigkeit, auf bestehenden Konzepten aufzubauen und sich in fremde

Denkweisen einzuarbeiten,

➢ Kommunikationsfähigkeit mit Entwicklern und Anwendern,
➢ Technische Betreuung von Unterauftragnehmern.

Verantwortlich für

Externe Einheit, Segment, System

Wirkt mit bei

Externe-Einheit-Spezifikation, Pflichtenheft (Gesamtsystementwurf),
Implementierungs-, Integrations- und Prüfkonzept System, Make-or-Buy-
Entscheidung, Prüfprotokoll Systemelement, Prüfprozedur Systemelement,
Prüfspezifikation Systemelement, Systemspezifikation, SW-Architektur,
Marktsichtung für Fertigprodukte, Migrationskonzept, Abnahmeprotokoll,
Lieferung

D.1.19 Technischer Autor
Der technische Autor (technische Redakteur) konzipiert und erstellt die (technische) Dokumentation und die
Ausbildungsunterlagen und führt Kundenschulungen im Rahmen des V-Modell-Projekt

 es    durch.

Aufgaben und
Befugnisse

➢ Konzipierung der Kundendokumentation und Erstellung des

Dokumentationskonzepts,

➢ Aufnahme der technischen Informationen und Daten aus den logistischen
Datenbanken und technischen Archiven, die für die spätere Nutzung, den
Betrieb und die Wartung erforderlich sind,

➢ Erstellung der technischen Handbücher, bzw. der elektronischen
Dokumentation, gemäß festgelegtem Dokumentationskonzept,
➢ Mitarbeit bei Spezifikation und Überprüfung der Anforderungen für

Kundenschulungen in Angeboten und Verträgen,

➢ Erstellung von Schulungsunterlagen und CUA (Computer-unterstützter

Ausbildung),

➢ Vorbereiten (einschließlich Erstellung der Schulungsunterlagen) und

Durchführen von Kundenschulungen,

➢ Aufbereitung der Informationen und Daten, sowie Zuordnung zu

verschiedenen Zielgruppen.

➢ Technisches Verständnis,
➢ Fähigkeit zur Umsetzung technischer Sachverhalte und Zusammenhänge

in zielgruppenorientierte Beschreibungen und Schulungsinhalte,

➢ Ausdrucksfähigkeit in Text und Grafik,

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

Fähigkeitsprofil


D.1 Projektteamrollen

215

➢ Didaktische/rhetorische Fähigkeiten,
➢ Fremdsprachenkenntnisse im projektspezifisch erforderlichen Umfang,
➢ Fähigkeit, essentielle Aussagen zu identifizieren und hervorzuheben,
➢ Kenntnis und Beherrschen der für den Aufgabenbereich erforderlichen

Prozesse, Verfahren, Methoden und Werkzeuge,

➢ Qualifizierung als Trainer/Dozent,
➢ Kenntnis der gesetzlichen Regelungen und Normen.

Rollenbesetzung

Sobald Dokumentation oder Ausbildungsunterlagen erstellt bzw.
Kundenschulungen im Projekt durchgeführt werden, ist die Rolle des technischen
Autors zu besetzen.

Verantwortlich für

Ausbildungsunterlagen, Logistische Unterstützungsdokumentation,
Nutzungsdokumentation

Wirkt mit bei

Anwenderaufgabenanalyse

D.2 Projektrollen

D.2.1 Anwender
Der Anwender nutzt das System zur Erfüllung seiner Fachaufgaben nach der Auslieferung. Er leitet aus
seiner Erfahrung mit dem Einsatz und Betrieb sowie der Pflege und Wartung von Systemen Anforderungen
an das Gesamtsystem ab und bringt entsprechende Änderungsvorschläge ein.

Aufgaben und
Befugnisse

➢ Beteiligung bei der Erstellung des Lastenhefts,
➢ Mitwirkung bei der Erstellung der Anwenderaufgabenanalyse,
➢ Mitwirkung bei der Identifikation der zu realisierenden Funktionen,
➢ Beschreibung der Problemstellung unter Berücksichtigung der
technischen und organisatorischen Einbettung des Systems,
➢ Aufstellen von Anforderungen an die Sicherheit aus Sicht des

Anwenders,

➢ Beschreiben der Randbedingungen zum Systempflege- und

Änderungskonzept aus Anwendersicht,

➢ Zuarbeit bei der Festlegung der organisatorischen Regelungen für die

Nutzung des Systems,

➢ Zuarbeit bei der Bereitstellung der Infrastruktur und des Bedien- und

Abnahmepersonals,

➢ Zuarbeit bei der Bewertung von Anforderungen und deren

Wirtschaftlichkeit,

➢ Mitarbeit bei Prüfungen und Abnahmen,
➢ Erstellung von Änderungsanträgen zur Erweiterung und Verbesserung der

Funktionen des ausgelieferten Gesamtsystems.

Fähigkeitsprofil

➢ Kenntnis über das Fach- und Einsatzgebiet des Systems,
➢ Kommunikationsfähigkeit.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

216

Wirkt mit bei

Bewertung Lastenheft Gesamtprojekt, Lastenheft Gesamtprojekt, Lastenheft
(Anforderungen), Anforderungsbewertung, Anwenderaufgabenanalyse,
Abnahmeprotokoll, Leistungsvereinbarung (SLA/OLA/UC)

 Referenz Rollen

D.2.2 Fachverantwortlicher
Der   Fachverantwortliche   ist   aus   fachlicher   Sicht   für   das   zu   entwickelnde   IT-System   und   den   damit
unterstützten Geschäftsprozess verantwortlich. In der Linienorganisation besetzt der Fachverantwortliche die
niedrigste   Position,   die   den   gesamten   Anwendungsbereich   des   entwickelten   IT-Systems   (bzw.
Fachverfahrens) verantwortet.

Aufgaben und
Befugnisse

Rollenbesetzung

➢ Mitwirkung bei der Projektgenehmigung,
➢ Besetzung der Rolle Verfahrensverantwortlicher (Fachseite),
➢ Mitwirkung bei der Ernennung von Projekteigner und Projektleiter,
➢ Mitwirkung im Lenkungsausschuss.

Der Fachverantwortliche ergibt sich aus dem Einsatzbereich des entwickelten IT-
Systems. Wird ein IT-System ausschließlich in einer Abteilung oder einem
Referat angewandt, so ist in der Regel der jeweilige Leiter der
Fachverantwortliche. Es ist auch möglich, mehrere Fachverantwortliche zu
benennen, wenn das System beispielsweise in verschiedenen Abteilungen zum
Einsatz kommt. Der Fachverantwortliche sollte bereits im Projektauftrag benannt
sein.

Verantwortlich für

Wirkt mit bei

Checkliste für das Interview zur Schutzbedarfsfeststellung,
Schutzbedarfsfeststellung

Bewertung Lastenheft Gesamtprojekt, Lastenheft Gesamtprojekt, Lastenheft
(Anforderungen), Anforderungsbewertung, WiBe (Vorkalkulation)

D.2.3 Lenkungsausschuss
Der  Lenkungsausschuss  ist das oberste Entscheidungsgremium der Projektorganisation. In ihm sollten alle
Projektbeteiligten (Stakeholder) in geeigneter Weise vertreten sein.

Normalerweise ist der Projekteigner für die Projektfortschrittsentscheidung
 en    verantwortlich, weit reichende
Entscheidungen wie z.B. über den Abbruch des Projektes müssen jedoch an den Lenkungsausschuss eskaliert
werden.

Daher muss von Anfang an festgelegt sein, welche Entscheidungen der Lenkungsausschuss trifft. Weiterhin
 en     der   Lenkungsausschuss   als
muss   festgelegt   sein,   bei   welchen  Projektfortschrittsentscheidung
Entscheidungsinstanz   beteiligt   ist.   Diese   werden   im   V-Modell   in   Form   von  Entscheidungspunkt
 en
vorgegeben.

Aufgaben und
Befugnisse

Rollenbesetzung

➢ Beschluss über die festgelegten Projektfortschrittsentscheidung
➢ Herbeiführung von Lösungen zu Problemen, die auf Ausführungsebene

 en   ,

nicht gelöst werden können (Konfliktmanagement).

Im Lenkungsausschuss sollten alle Projekt-Stakeholder in geeigneter Weise
eingebunden sein. In jedem Fall ist der Projekteigner Teil des
Lenkungsausschusses und leitet ihn zumeist. Für die Zusammenstellung der
Mitglieder gelten außerdem folgende Hinweise:

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland





D.2 Projektrollen

217

Der Ausschuss sollte so klein wie möglich gehalten werden, um rasche
Entscheidungen herbeizuführen.
Ist das Projekt Teil einer Matrix-Organisation, so sollte für jedes
Projektteammitglied zumindest ein Vorgesetzter eingebunden sein, um etwaige
Ressourcenkonflikte direkt im Lenkungsausschuss auflösen zu können.
Fachverantwortlicher, Multi-Projektkoordination und Betriebsverantwortlicher
sollten in geeigneter Weise vertreten sein.
Hat die Personalvertretung gemäß BPersVG ein Mitbestimmungsrecht, sollte sie
in die Entscheidungsfindung einbezogen werden.

Wirkt mit bei

Projektfortschrittsentscheidung

D.2.4 Projektauftraggeber
Der Projektauftraggeber ist die Person, die Entität oder das Gremium, das den Projektauftrag erteilt und
damit   das  Projekt   genehmigt.   Eng   verwandt   ist   die   Rolle   deshalb   mit   dem   strategischen  Multi-
Projektmanagement. Da der Projektauftraggeber in der Regel auch das Projektbudget stellt, handelt es sich
meist gleichzeitig auch um einen Projektsponsor.

Hinweis: In der Praxis existieren viele ähnliche oder gleichbedeutende Begriffe, wie z.B. Projektmanager (V-
Modell XT), Projektverantwortlicher, Projektauftraggeber, Projektträger, Projektsponsor oder Projekteigner
(siehe   auch   [Mot06]).   Das   V-Modell   trifft   hier   eine   Unterscheidung,   um   die   Verantwortung   für   die
Beauftragung eines Projekts (Projektauftraggeber) von der Unterstützung eines  Projekts (Projektsponsor)
und von der Verantwortung während der Projektdurchführung (Projekteigner) zu trennen. Dennoch ist es
natürlich je nach Projekt möglich, dass ein und dieselbe Person gleichzeitig alle mehrere der dargestellten
Rollen wahrnimmt.

Aufgaben und
Befugnisse

Rollenbesetzung

➢ Festlegen der elementaren Rahmenbedingungen der Projektdurchführung

(siehe Projektauftrag)

➢ Formale Beauftragung der Projektdurchführung

Je nach Projektkonstellation kann es sich beim Projektauftraggeber um ein
Gremium (z.B. eine Runde aus Präsident und Abteilungsleitern), um eine
übergeordnete Behörde (z.B. Ministerium), um Stabsstellen (z.B. zum
Projektportfoliomanagement) oder um Einzelpersonen (z.B. Abteilungsleiter)
handeln.

Verantwortlich für

WiBe (Vorkalkulation), Projektvorstudie, Projektauftrag

D.2.5 Projekteigner
Der  Projekteigner (engl. Project Owner, Executive) ist der Eigentümer des Projektes und trägt letztendlich
auch die Ergebnisverantwortung. Die Rolle stellt die Schnittstelle zwischen dem Projekt und den Interessen
der   Behörde,   sowie   den   Interessen   weiterer   Stakeholder   dar.   Im   Gegensatz   zum  Projektleiter  ist   der
Projekteigner   meist   nicht   ins   Projekttagesgeschäft   eingebunden;   er   ist   aber   erste   Anlaufstation   des
Projektleiters,   wenn   es   im   Projekt   zu   Schwierigkeiten   und   Komplikationen   kommt.   Aufgrund   seiner
Persönlichkeit   und   der   Position   in   der   Linienorganisation   ist   der   Projekteigner   in   der   Lage,
Projekthindernisse   aus   dem   Weg   zu   räumen   und   dem   Projektleiter   den   Rücken   für   die   eigentliche
Projektarbeit freizuhalten.

Hinweis: In der Praxis existieren viele ähnliche oder gleichbedeutende Begriffe, wie z.B. Projektmanager (V-
Modell   XT),   Projektverantwortlicher,   Projektauftraggeber,   Projektträger   oder   Projektsponsor   (siehe   auch
[Mot06]). Das V-Modell trifft hier eine Unterscheidung, um die Verantwortung für die Beauftragung eines

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

218

 Referenz Rollen

Projekts   (Projektauftraggeber)   von   der   Unterstützung   eines   Projekts   (Projektsponsor)   und   von   der
Verantwortung während der Projektdurchführung (Projekteigner) zu trennen. Dennoch ist es natürlich je nach
Projekt möglich, dass ein und dieselbe Person gleichzeitig alle drei Rollen wahrnimmt.

Aufgaben und
Befugnisse

Fähigkeitsprofil

Rollenbesetzung

Verantwortlich für

Wirkt mit bei

➢ Eigentümer des Projekts nach der Beauftragung,
➢ Bindeglied zwischen Projektorganisation und umgebender

Linienorganisation,

➢ meist Leiter des Lenkungsausschusses,
➢ Entscheidung über den Projektfortschritt (zusammen mit dem

Lenkungsausschuss),

➢ Ständiges "offenes Ohr" für den Projektleiter und die Belange des

Projekts,

➢ Problem- und Konfliktlösung bei der Projektplanung, bei der

Projektabwicklung und beim Projektabschluss,

➢ Festlegung der Rahmenbedingungen für die Projektorganisation,
➢ Beeinflussung und Reaktion auf externe Einflüsse (Ressourcensituation,

Projektmarketing, politische Vorgaben).

➢ Erfahrung mit Projektarbeit,
➢ Führungsqualitäten,
➢ Kenntnis der Behördenorganisation und -struktur,
➢ Fähigkeit zu Organisation und Delegation.

Die Rolle sollte nicht mit dem Projektleiter selbst besetzt werden, da dadurch die
Kontrollfunktion und die Funktion als "erste Anlaufstelle" ausgehebelt wird. In
der Praxis ist es oft sinnvoll, einen direkten Vorgesetzten des Projektleiters (z.B.
Referatsleiter, Abteilungsleiter) als Projekteigner zu besetzen. Um die
Unterstützung des Projektes zu gewährleisten, sollte der Projekteigner auch
aufgrund seiner Position in der Linienorganisation ein Interesse am Projekterfolg
haben.

Projektfortschrittsentscheidung, Checkliste Informationssicherheit,
Abnahmeerklärung

Projekthandbuch, Projektplan, Bewertung Lastenheft Gesamtprojekt, Lastenheft
Gesamtprojekt, Lastenheft (Anforderungen), Anforderungsbewertung, Make-or-
Buy-Entscheidung, Kriterienkatalog, Leistungsbewertungsmatrix,
Eignungsbewertungsmatrix, Vergabeunterlagen (Ausschreibung)

D.2.6 Verfahrensverantwortlicher (Fachseite)
Der   Verfahrensverantwortliche   (Fachseite)   betreut   das   IT-System   nach   Projektende   aus   fachlicher   Sicht
weiter. Er überprüft in regelmäßigen Abständen, ob sich ggf. fachliche Anforderungen verändert haben und
ist für fachliche Fragen zum System der erste Ansprechpartner.

Aufgaben und
Befugnisse

➢ Mitwirkung bei der Anforderungsdefinition und der

Anforderungsbewertung,

➢ Unterstützung bei der Definition von Leistungsvereinbarungen,
➢ Mitwirkung beim Projektabschlussbericht.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

D.2 Projektrollen

Fähigkeitsprofil

Rollenbesetzung

219

➢ Kennt den fachlichen Hintergrund des IT-Systems,
➢ Kennt den Ablauf des Entwicklungsprojekts,
➢ Hat IT-Kenntnisse.

Wird im Rahmen des Projekts ein im Betrieb befindliches System
weiterentwickelt oder migriert, ist die Rolle entsprechend der bisherigen
Verantwortung bereits zu Projektbeginn besetzt. Handelt es sich um eine
Neuentwicklung oder ist mit der Entwicklung eine Übertragung der
Verantwortlichkeiten verbunden, sollte die Rolle so früh wie möglich, spätestens
jedoch vor Projektende besetzt werden.

Wirkt mit bei

Projektabschlussbericht, Lastenheft (Anforderungen), Anforderungsbewertung,
Leistungsvereinbarung (SLA/OLA/UC)

D.2.7 Verfahrensverantwortlicher (IT-Betrieb)
Der Verfahrensverantwortliche (IT-Betrieb) betreut den Betrieb des IT-Systems nach Projektende. Er prüft in
regelmäßigen   Abständen,   ob   sich   nichtfunktionale   Anforderungen   oder   Rahmenbedingungen   (z.B.
Systemarchitektur,   Sicherheitsanforderungen,   HW-Plattform,   etc.)   des   IT-Systems   verändert   haben,   und
steuert entsprechende Anpassungen des IT-Systems in den Änderungsprozess ein.

Aufgaben und
Befugnisse

Fähigkeitsprofil

Rollenbesetzung

➢ Unterstützung bei der Definition von Leistungsvereinbarungen,
➢ Mitwirkung beim Projektabschlussbericht.

➢ Hat Erfahrung im Betrieb von Systemen,
➢ Kennt die Systemarchitektur und die Infrastruktur des Systems.

Wird im Rahmen des Projekts ein im Betrieb befindliches System
weiterentwickelt oder migriert, ist die Rolle entsprechend der bisherigen
Verantwortung bereits zu Projektbeginn besetzt. Handelt es sich um eine
Neuentwicklung oder ist mit der Entwicklung eine Übertragung der
Verantwortlichkeiten verbunden, sollte die Rolle so früh wie möglich, spätestens
jedoch vor Projektende besetzt werden.

Wirkt mit bei

Projektabschlussbericht, Leistungsvereinbarung (SLA/OLA/UC)

D.2.8 Verfahrensverantwortlicher (Weiterentwicklung)
Der Verfahrensverantwortliche (Weiterentwicklung) betreut das IT-System aus Entwicklungssicht weiter. Er
kennt   die   fachliche   Implementierung   und   ist   erster   Ansprechpartner   bei   Wartung,   Pflege   und
Weiterentwicklung der Geschäftslogik.

Aufgaben und
Befugnisse

Fähigkeitsprofil

➢ Unterstützung bei der Definition von Leistungsvereinbarungen,
➢ Mitwirkung beim Projektabschlussbericht.

➢ Kennt die System- und SW-Architektur des Systems,
➢ Kennt den fachlichen Hintergrund des Systems,
➢ War idealerweise an der Systementwicklung beteiligt.

Rollenbesetzung

Wird im Rahmen des Projekts ein im Betrieb befindliches System
weiterentwickelt oder migriert, ist die Rolle entsprechend der bisherigen

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

220

 Referenz Rollen

Verantwortung bereits zu Projektbeginn besetzt. Handelt es sich um eine
Neuentwicklung oder ist mit der Entwicklung eine Übertragung der
Verantwortlichkeiten verbunden, sollte die Rolle so früh wie möglich, spätestens
jedoch vor Projektende besetzt werden.
Wird das System durch einen Auftragnehmer entwickelt, so kann die Wartung,
Pflege und Weiterentwicklung auch durch einen eigenständigen Wartungsvertrag
geregelt sein. In diesem Fall übernimmt der Auftragnehmer die Rolle.

Wirkt mit bei

Projektabschlussbericht, Leistungsvereinbarung (SLA/OLA/UC)

D.3 Organisationsrollen

D.3.1 Betriebsbeauftragter
Der Betriebsbeauftragte ist verantwortlich für den sicheren und zuverlässigen Betrieb aller IT-Systeme der
Organisation. Für geplante Systeme legt er organisatorische und technische Rahmenbedingungen fest und
prüft   bei   Lieferung   ihre   Einhaltung.   Zusammen   mit   der  Auslieferung   eines   fertigen   Systems   erhält   er
Konzepte für betriebliche Maßnahmen, die er vor der Inbetriebnahme des Systems plant und umsetzt.

Aufgaben und
Befugnisse

➢ Festlegung betrieblicher Vorgaben für IT-Systeme,
➢ Konzeption, Vorbereitung und Durchführung von Tests eines neuen IT-

Systems zur betrieblichen Abnahme,

➢ Ausgestaltung betrieblicher Maßnahmen im Rahmen der

Sicherheitskonzeption.

Wirkt mit bei

Vorgaben zum IT-Betrieb, WiBe (Vorkalkulation)

D.3.2 Datenschutzbeauftragter
Die   Rolle   repräsentiert   den   nach  Art.   37   Datenschutz-Grundverordnung   (DSGVO)   in   jeder   Behörde   zu
benennenden Beauftragten für den Datenschutz. Der Datenschutzbeauftragte ist dafür verantwortlich, die
relevanten Vorgaben zusammenzutragen, bekannt zu geben, Richtlinien für die eigenen Prozesse abzuleiten
und   ihre   Einhaltung   organisationsweit   zu   prüfen.   Das   betrifft   insbesondere   IT-Systeme,   die
personenbezogene Daten verarbeiten. Er ergänzt die organisationsweiten Vorgaben um neue Erkenntnisse aus
Projekten und dem IT-Betrieb.

Aufgaben und
Befugnisse

➢ Festlegung organisationsweiter Datenschutzvorgaben,
➢ Festlegung organisationsweiter Maßnahmen zur Einhaltung und

Umsetzung der Datenschutzvorgaben,

➢ Bewertung der Ziele, grundlegenden Eigenschaften und Funktionen des

zu entwickelnden Systems aus Sicht des Datenschutzes.

Wirkt mit bei

Vorgaben zum Datenschutz

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

D.3 Organisationsrollen

221

D.3.3 Geschäftsprozessmanager
Immer  mehr Behörden besitzen eine Organisationseinheit zur Dokumentation und zum Management der
unterstützten   Geschäftsprozesse.   Geschäftsprozessmodellierung   und   -strukturierung   in   der   Öffentlichen
Verwaltung   dient   zur   Dokumentation   von   bestehenden   und   zur   Beschreibung   neu   konzipierter   bzw.
optimierter Abläufe in der Verwaltung und geht damit über die Beschreibung von IT-Systemen hinaus (siehe
auch Prozess- und Datenmodellierung in der Bundesverwaltung).

Die   Modellierung   des   zugrunde   liegenden   Geschäftsprozesses   ist   die   Voraussetzung   für   die
Anforderungsdefinition   an   das   IT-System   und   sollte   idealerweise   vor   dem   Projekt   erfolgen.   Durch   die
Entwicklung   eines   IT-Systems   können   sich   aber   wiederum   Ergänzungen   oder   Anpassungen   des
Geschäftsprozesses ergeben.

Aufgaben und
Befugnisse

➢ Definition der zu unterstützenden Geschäftsprozesse (idealerweise vor

dem Projekt),

➢ Mitwirkung bei der Definition der funktionalen Anforderungen,
➢ Anpassung der Geschäftsprozesse an das entwickelte System,
➢ Mitwirkung beim Rollout des Systems,
➢ Definition behördlicher Geschäftsprozesse.

Rollenbesetzung

Dem Projekt sollte ein direkter Ansprechpartner benannt werden. Existiert diese
Rolle in der Organisation nicht, bleibt sie unbesetzt.

Wirkt mit bei

Lastenheft (Anforderungen)

D.3.4 Informationssicherheitsbeauftragter
Der Informationssicherheitsbeauftragte ist für alle Aspekte rund um die Informationssicherheit zuständig. Er
ist   dafür   verantwortlich,   relevante   Vorgaben   zusammenzutragen,   bekannt   zu   geben,   Richtlinien   für   die
eigenen Prozesse abzuleiten und ihre Einhaltung organisationsweit zu prüfen. Er implementiert und etabliert
dazu   ein  Informationssicherheits-Managementsystem,   achtet   auf   die   Einhaltung   der   dort   festgelegten
Maßnahmen und ergänzt sie um neue Erkenntnisse aus Projekten und dem IT-Betrieb.

Für das Projekt ist der Informationssicherheitsbeauftragte zuständiger Ansprechpartner für alle Werkzeuge
der Projektinfrastruktur. Gemeinsam mit ihm werden die zu nutzenden Werkzeuge festgelegt und gemäß den
Vorgaben des ISMS der Organisation für den Einsatz vorbereitet.

Aufgaben und
Befugnisse

➢ Erstellung organisationsweiter Vorgaben zur Informationssicherheit,
➢ Einführung und Etablierung des Informationssicherheits-

Managementsystem
festgelegter Vorgaben und Maßnahmen,

 s   sowie Koordination und Durchsetzung dort

➢ Ansprechpartner für die Informationssicherheitsverantwortlichen der

Projekte,

➢ Abstimmung der Projektinfrastruktur, soweit sie über die festgelegten

Standards hinausgeht,

➢ Überprüfung der Einhaltung der Vorgaben und Maßnahmen des ISMS in

Bezug auf die Infrastruktur in konkreten Projekten.

Verantwortlich für

Informationssicherheits-Managementsystem

Wirkt mit bei

Vorgaben zur Informationssicherheit

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


222

 Referenz Rollen

D.3.5 Multi-Projektkoordination
Die  Multi-Projektkoordination  koordiniert   die   Verzahnung   und   Abstimmung   mehrerer   einzelner
Projektorganisationen mit der Linienorganisation. Die Rolle repräsentiert ein organisationsweites, operatives
Multi-Projektmanagement.   Dies   umfasst   übergreifende   Projektmanagement-Aktivitäten,   übergreifendes
Controlling in Termin- und Kapazitätsplanung (Regelung des Zugriffs mehrerer Projekte auf gemeinsame
Ressourcen), übergreifendes Berichtswesen und Wissensmanagement, Standardisierung von Projektabläufen,
einheitliches Qualitätsmanagement und Projektbewertung.

Aufgaben und
Befugnisse

➢ Mitwirkung bei der Definition des Projektauftrags und der Genehmigung

eines Projekts,

➢ Beratung bei der Definition der Organisationsstruktur,
➢ Vorgabe von Berichtswesen und Kommunikationswegen,
➢ Vorschläge bei der Ernennung des Projektteams und bei der Besetzung

von Rollen,

➢ Mitwirkung bei den Projektfortschrittsentscheidungen.

Rollenbesetzung

Wirkt mit bei

Die Rolle wird meist durch ein ganzes Team ausgefüllt. Für ein konkretes Projekt
sollte daher ein fester Ansprechpartner definiert sein.

Projektfortschrittsentscheidung, WiBe (Vorkalkulation), Projektvorstudie,
Projektauftrag

D.3.6 Personalvertretung
Diese   Rolle   repräsentiert   die   nach   Bundespersonalvertretungsgesetz   [BPersVG]   zu   bildende
Personalvertretung. Dieser wird eine Menge von Mitbestimmungsrechten gewährt, die auch im Rahmen von
IT-Projekten   zu   beachten   sind.   Unter   anderem   bestimmt   die   Personalvertretung   gemäß   §75   und   §76
BPersVG mit bei:

➢ Maßnahmen zur Verhütung von Dienst- und Arbeitsunfällen und sonstigen Gesundheitsschädigungen

➢ Einführung und Anwendung technischer Einrichtungen, die dazu bestimmt sind, das Verhalten oder

die Leistung der Beschäftigten zu überwachen

➢ Maßnahmen zur Hebung der Arbeitsleistung und Erleichterung des Arbeitsablaufs

➢ Einführung grundlegend neuer Arbeitsmethoden

➢ Übertragung einer höher oder niedriger zu bewertenden Tätigkeit

➢ Maßnahmen, die der Durchsetzung der tatsächlichen Gleichberechtigung von Frauen und Männern,
insbesondere bei der Einstellung, Beschäftigung, Aus-, Fort- und Weiterbildung und dem beruflichen
Aufstieg dienen.

Die Rolle überwacht darüber hinaus die gemäß Behindertengleichstellungsgesetz [BGG] zu vermeidende
Benachteiligung von behinderten Menschen. Insbesondere §11 BGG macht hier Vorgaben zur barrierefreien
Informationstechnik.

Aufgaben und
Befugnisse

➢ Mitwirkung bei der Genehmigung und der Zieldefinition von relevanten

Projekten

➢ Mitwirkung bei der Anforderungsdefinition und dem Erreichen des

Entscheidungspunkts Anforderungen festgelegt
➢ Mitwirkung bei der Rollenbesetzung in Projekten

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

D.3 Organisationsrollen

223

➢ Mitwirkung bei der Abnahme von Systemen (insbesondere

Barrierefreiheit)

Rollenbesetzung

Das Projekt sollte sich unmittelbar nach Projektbeginn einen direkten
Ansprechpartner der Personalvertretung benennen lassen, der deren Belange im
Rahmen des Projekts vertritt.

Wirkt mit bei

Projekthandbuch, Projektauftrag

D.3.7 Qualitätsmanager
Der Qualitätsmanager hat Querschnittsaufgaben und ist in der gesamten Organisation verantwortlich für die
Erstellung und Pflege der Qualitätsmanagement-Vorschriften, sowie für deren Verteilung. Er verantwortet die
Umsetzung der Qualitätspolitik und ist zuständig für alle projektübergreifenden Qualitätsbelange bei der
System-/SW-/HW-Entwicklung. Er ist verantwortlich für den normengerechten Inhalt, die Wirtschaftlichkeit
und die Wirksamkeit des Qualitätsmanagementsystems und seine permanente Fortschreibung.

Aufgaben und
Befugnisse

➢ Erstellung und Pflege eines Know-how Zentrums für Qualitätsfragen,
➢ Erstellung von Vorgaben für das Qualitätsmanagement-Berichtswesen der

Projekte (als Grundlage für die Verbesserung des
Qualitätsmanagementsystems),

➢ Analyse der Wirksamkeit des Qualitätsmanagementsystems durch die

Auswertung von QS-Bericht

 en   ,

➢ Lieferung von Qualitätsstatistiken und Verbesserungsvorschlägen an die

Projekte,

➢ Erstellung verbindlicher Vorgaben zu QS-Handbüchern, Prüfplänen und

Prüfspezifikationen,

➢ Vorgabe von Regeln und Verfahren, nach denen die Projekte
qualitätssichernde Maßnahmen planen und durchführen,

➢ Beratung und Unterstützung der Projekte bei allen Fragen, die das

Qualitätsmanagement betreffen,

➢ Mitarbeit bei der Festlegung der projektspezifischen QS-Maßnahmen,
➢ Festlegung der Rahmenbedingungen und Regelungen für die

Organisation der QS-Maßnahmen,

➢ Freigabe von Prüfplänen/Prüfablaufplänen/QS-Handbüchern,
➢ Mitarbeit bei der Vereinbarung von Qualitätssicherungsmaßnahmen mit

Lieferanten,

➢ Unterstützung bei der Auftragnehmerauswahl,
➢ Durchführung von Projekt- und Auftragnehmeraudits,
➢ Durchführung von Audits bei Bedarf,
➢ Uneingeschränkter Zugang zu allen qualitätsbezogenen Vorgängen und

alle Rechte, obige Aufgaben durchzuführen.

Rollenbesetzung

Der Qualitätsmanager ist eine organisationsweite Rolle, muss in allen nach ISO
9001 zertifizierten Unternehmen existieren und ist dort für das
Qualitätsmanagement zuständig.

Wirkt mit bei

QS-Handbuch

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


224

 Referenz Rollen

D.3.8 Vergabestelle
Die  Vergabestelle  unterstützt   Projekte   bei   der   Auftragsvergabe   bzw.   bei   der   Beschaffung   von
Fertigprodukten. Außerdem ist sie verantwortlich für die eingeholten Angebote (von AN).

Aufgaben und
Befugnisse

➢ Erstellung und Pflege einer Auftragnehmerdatenbasis,
➢ Sammeln von Berichten über Erfahrungen mit

Auftragnehmern/Fertigprodukten und Bewertung und Ablage dieser
Erfahrungen in der Auftragnehmerdatenbasis,
➢ Durchführung von Auftragnehmerbewertungen,
➢ Strategische Aktivitäten wie Auswahl bevorzugter

Auftragnehmer/Fertigprodukte,

➢ Abschluss von Rahmenverträgen und Preisverhandlungen.

Die Vergabestelle unterstützt die Projekte beispielsweise

➢ bei der Auswahl von potentiellen Auftragnehmern/Fertigprodukten,
➢ beim Aushandeln individueller Verträge,
➢ bei der Abwicklung von Bestellvorgängen.

Rollenbesetzung

Bei der Vergabestelle handelt es sich um eine organisationsweite Rolle, die als
Dienstleister für Projekte fungiert. Für das Projekt sollte ein Ansprechpartner
innerhalb der Vergabestelle benannt werden.

Verantwortlich für

Angebot (von AN)

Wirkt mit bei

Externe Einheit, Make-or-Buy-Entscheidung, Externes SW-Modul,
Marktsichtung für Fertigprodukte, Abnahmeerklärung, Beschaffungskonzeption,
Kriterienkatalog, Leistungsbewertungsmatrix, Eignungsbewertungsmatrix,
Vergabeunterlagen (Ausschreibung), Vertrag, Vertragszusatz

D.4 Rollenindex
Modellelement

Änderungssteuerungsgruppe (Change Control Board)

Änderungsverantwortlicher

Anforderungsanalytiker (AG)

Anforderungsanalytiker (AN)

Anwender

Ausschreibungs- und Vertragsverantwortlicher

Betriebsbeauftragter

Betriebsverantwortlicher

Datenschutzbeauftragter

Datenschutzverantwortlicher

Ergonomieverantwortlicher

Typ

Seite

Projektteamrolle

Projektteamrolle

Projektteamrolle

Projektteamrolle

Projektrolle

Projektteamrolle

Organisationsrolle

Projektteamrolle

Organisationsrolle

Projektteamrolle

Projektteamrolle

198

198

199

201

215

202

220

203

220

204

205

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

D.4 Rollenindex

Modellelement

Fachverantwortlicher

Geschäftsprozessmanager

Informationssicherheitsbeauftragter

Informationssicherheitsverantwortlicher

KM-Verantwortlicher

Lenkungsausschuss

Multi-Projektkoordination

Personalvertretung

Product Owner

Projektauftraggeber

Projekteigner

Projektleiter

Prüfer

QS-Verantwortlicher

Qualitätsmanager

SW-Architekt

SW-Entwickler

Systemarchitekt

Systemintegrator

Technischer Autor

Verfahrensverantwortlicher (Fachseite)

Verfahrensverantwortlicher (IT-Betrieb)

Verfahrensverantwortlicher (Weiterentwicklung)

Vergabestelle

Typ

Projektrolle

Organisationsrolle

Organisationsrolle

Projektteamrolle

Projektteamrolle

Projektrolle

Organisationsrolle

Organisationsrolle

Projektteamrolle

Projektrolle

Projektrolle

Projektteamrolle

Projektteamrolle

Projektteamrolle

Organisationsrolle

Projektteamrolle

Projektteamrolle

Projektteamrolle

Projektteamrolle

Projektteamrolle

Projektrolle

Projektrolle

Projektrolle

Organisationsrolle

225

Seite

216

221

221

205

206

216

222

222

208

217

217

208

209

210

223

211

212

212

213

214

218

219

219

224

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

226

 Referenz Abläufe

E Referenz Abläufe

E.1 Entscheidungspunkte

E.1.1 Projekt genehmigt
Die Aktivitäten des Projektvorlaufs münden in der Erstellung der Produkte  Projektvorstudie  sowie  WiBe
(Vorkalkulation). Diese werden bereits im Vorfeld erstellt, um die "Projektwürdigkeit" einer Idee oder Vision
festzustellen.   Weiterhin   werden   durch   ihre   Erstellung   erste   Anforderungen   aufgenommen,
Lösungsmöglichkeiten erfasst und abgewogen sowie der Bedarf an Haushaltsmitteln festgestellt.

Wird entschieden, dass aufgrund der vorliegenden Produkte aus dem Vorlauf ein Projekt gestartet werden
soll,   wird   das   Produkt  Projektauftrag  erstellt.   Dieses   legt   die   grundsätzlichen   Rahmenbedingungen
(organisatorisch, finanziell) fest und beschreibt die wesentlichen Ziele, die mit dem Projekt verfolgt werden.

Wird der  Projektauftrag  positiv beschieden, ist der Entscheidungspunkt  Projekt genehmigt  erreicht, womit
das V-Modell-Projekt gestartet ist. Ist das Projekt genehmigt, sind Abschriften an folgende Personenkreise zu
verteilen:

➢ alle Projektmitglieder und deren Vorgesetzte

➢ die zuständige Personalvertretung

➢ die Verantwortlichen für den Bereich Betrieb und Sicherheit

Zugeordnete Produkte

Projektauftraggeber:
Projektauftrag, Projektvorstudie, WiBe (Vorkalkulation)
Projekteigner:
Checkliste Informationssicherheit

E.1.2 Projekt initialisiert
In   dem  Entscheidungspunkt  Projekt   initialisiert  wird   untersucht,   ob   das  Projekthandbuch  und   das  QS-
Handbuch das Projekt korrekt wiedergeben.

Im   Falle   einer   positiven   Bewertung   legen   das  Projekthandbuch  sowie   das  QS-Handbuch  erste
Rahmenbedingungen   für   das   Projekt   fest,   die   es   ermöglichen,   im   folgenden   Projektverlauf   auf
Auftraggeberseite die Anforderungen festzulegen, beziehungsweise auf Auftragnehmerseite das System zu
erstellen.

Ein   detaillierter
Projektstatusbericht  dokumentiert   den   Projektfortschritt   und   der
Qualitätseigenschaften des Projekts.

 Projektplan  enthält   die   Planung   für   die   nächste  Projektfortschrittsstufe.   Der
 QS-Bericht  beschreibt   die

Alle   projektrelevanten   Dokumente   werden   in   der  Produktbibliothek  abgelegt.   Die   Produktbibliothek
unterliegt dem Konfigurationsmanagement und ihre Struktur wird spätestens im Entscheidungspunkt Projekt
initialisiert festgelegt.

Es wird eine Projektfortschrittsentscheidung getroffen, um zum nächsten Entscheidungspunkt überzugehen.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

227

E.1 Entscheidungspunkte

Zugeordnete Produkte

Informationssicherheitsbeauftragter:
Informationssicherheits-Managementsystem
KM-Verantwortlicher:
Produktbibliothek
Projekteigner:
Projektfortschrittsentscheidung
Projektleiter:
Projekthandbuch, Projektplan, Projektstatusbericht
QS-Verantwortlicher:
QS-Bericht, QS-Handbuch

E.1.3 Anforderungen festgelegt
In   dem   Entscheidungspunkt  Anforderungen   festgelegt  werden   die   erstellten   Anforderungen   und   ihre
Prioritätsbewertung   vom  Lenkungsausschuss  des   Auftraggebers   bzw.   durch   den   Anwender   auf
Vollständigkeit und Korrektheit hin untersucht.

Im   Falle   einer   positiven   Bewertung   sind   die   Anforderungen   in   Form   des   Produkts  Lastenheft
(Anforderungen) dokumentiert. Zudem liegt eine Anforderungsbewertung gemäß der Priorität der einzelnen
Anforderungen   vor.   Darüber   hinaus   wird   die   Wirtschaftlichkeitsbetrachtung   durch   das   Produkt  WiBe
(Fortschreibung) verfeinert. Auf Basis dieser Dokumente kann das System entwickelt werden.

Ein   detaillierter
Projektstatusbericht  dokumentiert   den   Projektfortschritt   und   der
Qualitätseigenschaften des Projekts.

 Projektplan  enthält   die   Planung   für   die   nächste  Projektfortschrittsstufe.   Der
 QS-Bericht  beschreibt   die

Es wird eine Projektfortschrittsentscheidung getroffen, um zum nächsten Entscheidungspunkt überzugehen.

Zugeordnete Produkte

Anforderungsanalytiker (AG):
Anforderungsbewertung, Lastenheft (Anforderungen)
Betriebsverantwortlicher:
Vorgaben zum IT-Betrieb
Datenschutzverantwortlicher:
Vorgaben zum Datenschutz
Fachverantwortlicher:
Schutzbedarfsfeststellung
Informationssicherheitsverantwortlicher:
Vorgaben zur Informationssicherheit
Product Owner:
Anforderungskonzept
Projekteigner:
Projektfortschrittsentscheidung
Projektleiter:
Projektplan, Projektstatusbericht, WiBe (Fortschreibung)
QS-Verantwortlicher:
QS-Bericht

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

228

 Referenz Abläufe

E.1.4 Produktvision entworfen
Zum Entscheidungspunkt Produktvision entworfen ist eine grobe Leistungsbeschreibung des zu erstellenden
Systems in Form eines Anforderungskonzepts vorzulegen. Sofern für das Projekt relevant, müssen dabei die
Vorgaben zur Informationssicherheit, zum Datenschutz und zum IT-Betrieb in das Konzept integriert oder
referenziert werden. Das  Anforderungskonzept  dient als Grundlage für die anschließende Ausschreibung
bzw.
  Beauftragung   eines   IT-Dienstleisters   des   Bundes   zur   Durchführung   eines   agilen
Softwareentwicklungsprojekts.

Zugeordnete Produkte

Betriebsverantwortlicher:
Vorgaben zum IT-Betrieb
Datenschutzverantwortlicher:
Vorgaben zum Datenschutz
Fachverantwortlicher:
Schutzbedarfsfeststellung
Informationssicherheitsverantwortlicher:
Vorgaben zur Informationssicherheit
Product Owner:
Anforderungskonzept
Projekteigner:
Projektfortschrittsentscheidung
Projektleiter:
Projektplan, Projektstatusbericht, WiBe (Fortschreibung)
QS-Verantwortlicher:
QS-Bericht

E.1.5 Ausschreibung freigegeben
In   dem   Entscheidungspunkt  Ausschreibung   freigegeben  wird   untersucht,   ob   die  Vergabeunterlagen
(Ausschreibung) veröffentlicht werden können. Die Entscheidung wird im Vergabevermerk dokumentiert. Im
Falle einer positiven Bewertung wird das Vergabeverfahren eingeleitet. Der Entscheidungspunkt bildet das
Ende der zweiten Phase einer Beschaffung gemäß UfAB.

Ein   detaillierter
Projektstatusbericht  dokumentiert   den   Projektfortschritt   und   der
Qualitätseigenschaften des Projekts.

 Projektplan  enthält   die   Planung   für   die   nächste  Projektfortschrittsstufe.   Der
 QS-Bericht  beschreibt   die

Es wird eine Projektfortschrittsentscheidung getroffen, um zum nächsten Entscheidungspunkt überzugehen.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

E.1 Entscheidungspunkte

Zugeordnete Produkte

229

Ausschreibungs- und Vertragsverantwortlicher:
Beschaffungskonzeption, Eignungsbewertungsmatrix, Kriterienkatalog,
Leistungsbewertungsmatrix, Verfahrensdokumentation, Vergabeunterlagen
(Ausschreibung), Vergabevermerk
Projekteigner:
Projektfortschrittsentscheidung
Projektleiter:
Projektplan, Projektstatusbericht
QS-Verantwortlicher:
QS-Bericht

E.1.6 Angebotsaufforderung erstellt
In dem Entscheidungspunkt Angebotsaufforderung erstellt wird untersucht, ob die Angebotsaufforderung an
den IT-Dienstleister des Bundes übermittelt werden kann.

Ein   detaillierter
Projektstatusbericht  dokumentiert   den   Projektfortschritt   und   der
Qualitätseigenschaften des Projekts.

 Projektplan  enthält   die   Planung   für   die   nächste  Projektfortschrittsstufe.   Der
 QS-Bericht  beschreibt   die

Es wird eine Projektfortschrittsentscheidung getroffen, um zum nächsten Entscheidungspunkt überzugehen.

Zugeordnete Produkte

Ausschreibungs- und Vertragsverantwortlicher:
Angebotsaufforderung
Projekteigner:
Projektfortschrittsentscheidung
Projektleiter:
Projektplan, Projektstatusbericht
QS-Verantwortlicher:
QS-Bericht

E.1.7 Beauftragung erteilt
In dem Entscheidungspunkt Beauftragung erteilt wird vom Lenkungsausschuss entschieden, ob ein Vertrag
mit einem Auftragnehmer abgeschlossen werden soll. Hierbei gibt es drei mögliche Ausgangssituationen:

1. Auftraggeber und Auftragnehmer treffen die erste vertragliche Vereinbarung in diesem Projekt. Auf
Auftraggeberseite   wird   die   Entscheidung,   ob   ein   Zuschlag   erteilt   wird,   auf   Grundlage   der   im
Vergabevermerk dokumentierten Angebotswertung getroffen.

2. Auftraggeber   und  Auftragnehmer   haben   bereits   eine   vertragliche  Vereinbarung   und   ein  Teil   der
Anforderungen ist bereits realisiert worden. Der Auftraggeber entscheidet in diesem Fall, ob eine
Zusammenarbeit mit dem Auftragnehmer für die gesamte Realisierung wünschenswert ist.

3. Falls der Auftraggeber im Laufe der Systementwicklung neue Erkenntnisse über die Anforderungen
gewinnt, kann er neue oder abgewandelte Anforderungen formulieren. Insbesondere kann hieraus ein
Vertragszusatz  entstehen.   Im   Falle   einer   öffentlichen   Ausschreibung   sind   dabei   jedoch
vergaberechtliche Richtlinien zu beachten.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

230

 Referenz Abläufe

Im   Falle   einer   positiven   Entscheidung   wird   ein  Vertrag  zwischen   Auftraggeber   und   Auftragnehmer
geschlossen. Der Auftraggeber dokumentiert den Vertragsschluss im Vergabevermerk. Für die Beauftragung
eines IT-Dienstleisters des Bundes wird anstellte des Vertragsschlusses ein  Auftrag  erteilt. Dieser entsteht
durch die Unterzeichnung des zuvor vom IT-Dienstleister eingereichten Angebots.

Der Inhalt des Vertrags (bzw. Auftrags) und der darin enthaltenen Anforderungen haben Einfluss auf die
Abnahmespezifikation und die Prüfspezifikation Inbetriebnahme, die für die Abnahmeprüfung der Lieferung
(von AN) maßgeblich sind.

 Projektplan  enthält   die   Planung   für   die   nächste  Projektfortschrittsstufe.   Der
Ein   detaillierter
Projektstatusbericht  dokumentiert   den   Projektfortschritt   und   der
 QS-Bericht  beschreibt   die
Qualitätseigenschaften   des   Projekts.   Es   wird   eine  Projektfortschrittsentscheidung  getroffen,   um   zum
nächsten Entscheidungspunkt überzugehen.

Zugeordnete Produkte

Ausschreibungs- und Vertragsverantwortlicher:
Auftrag, Verfahrensdokumentation, Vergabevermerk, Vertrag, Vertragszusatz
Projekteigner:
Projektfortschrittsentscheidung
Projektleiter:
Projektplan, Projektstatusbericht
Prüfer:
Abnahmespezifikation
QS-Verantwortlicher:
QS-Bericht

E.1.8 Iteration geplant
In   dem  Entscheidungspunkt  Iteration   geplant  wird   die   Planung   für   die   folgenden   Schritte   der
Systementwicklung vorgelegt. Die Planung erfolgt jeweils mindestens bis zur Lieferung und Abnahme eines
Inkrements, kann aber darüber hinausgehen. Für jede vorgesehene Lieferung muss eine Abnahmeprüfung
durchgeführt werden.

Es   werden   alle   offenen   Änderungsanträge   der  Änderungsstatusliste  geprüft   und   Auftraggeber   und
Auftragnehmer einigen sich über die weitere Vorgehensweise.

Auf Auftraggeberseite wird die Erstellung der für die Abnahmeprüfung erforderlichen  Produkte  wie z.B.
Prüfspezifikationen geplant.

Der Auftragnehmer plant detailliert das Vorgehen durch die Entscheidungspunkte der Systementwicklung bis
zur Lieferung und der Abnahme.

Ein   detaillierter
Projektstatusbericht  dokumentiert   den   Projektfortschritt   und   der
Qualitätseigenschaften des Projekts.

 Projektplan  enthält   die   Planung   für   die   nächste  Projektfortschrittsstufe.   Der
 QS-Bericht  beschreibt   die

Es wird eine Projektfortschrittsentscheidung getroffen, um zum nächsten Entscheidungspunkt überzugehen.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

E.1 Entscheidungspunkte

Zugeordnete Produkte

Projekteigner:
Projektfortschrittsentscheidung
Projektleiter:
Projekthandbuch, Projektplan, Projektstatusbericht
QS-Verantwortlicher:
QS-Bericht, QS-Handbuch
Änderungsverantwortlicher:
Änderungsstatusliste

231

E.1.9 Gesamtsystem entworfen
In dem Entscheidungspunkt Gesamtsystem entworfen wird bewertet, ob der Gesamtsystementwurf in seinem
Umfang wie geplant vollständig und den Anforderungen entsprechend ausgearbeitet wurde.

Im Falle einer positiven Bewertung liegt das Pflichtenheft (Gesamtsystementwurf) vor. Außerdem ist für alle
Systemelemente die  Prüfspezifikation Systemelement  fertig gestellt und gegebenenfalls wird für jedes zu
liefernde Dokument eine Prüfspezifikation

  Dokument

  erstellt.

Ein   detaillierter
Projektstatusbericht  dokumentiert   den   Projektfortschritt   und   der
Qualitätseigenschaften des Projekts.

 Projektplan  enthält   die   Planung   für   die   nächste  Projektfortschrittsstufe.   Der
 QS-Bericht  beschreibt   die

Es wird eine Projektfortschrittsentscheidung getroffen, um zum nächsten Entscheidungspunkt überzugehen.

Zugeordnete Produkte

Anforderungsanalytiker (AN):
Pflichtenheft (Gesamtsystementwurf)
Betriebsverantwortlicher:
Erweiterung der Vorgaben zum IT-Betrieb
Datenschutzverantwortlicher:
Erweiterung der Vorgaben zum Datenschutz
Informationssicherheitsverantwortlicher:
Erweiterung der Vorgaben zur Informationssicherheit, Sicherheitskonzeption
Projekteigner:
Projektfortschrittsentscheidung
Projektleiter:
Projektplan, Projektstatusbericht
Prüfer:
Prüfspezifikation, Prüfspezifikation Systemelement
QS-Verantwortlicher:
QS-Bericht

E.1.10 System entworfen
In  dem  Entscheidungspunkt  System  entworfen  wird   die  Systemarchitektur  bezüglich  ihrer  Tragfähigkeit
bewertet.

Im Falle einer positiven Bewertung sind die  Systemspezifikation  und die  Prüfspezifikation Systemelement
für das System und alle Segmente fertig gestellt. Die grundlegenden Verfahren für Implementierung, Prüfung
und Integration stehen in Form des Produkts Implementierungs-, Integrations- und Prüfkonzept System fest.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland



232

 Referenz Abläufe

Für die einzelnen Systemelemente liegt darüber hinaus jeweils eine Prüfspezifikation Systemelement vor. So
kann beispielsweise ein nachfolgender Feinentwurf lokal innerhalb einer Einheit auf Basis eines stabilen
Grobentwurfs   durchgeführt   werden.   Außerdem   wurden   externe   Einheiten   in   der  Externe-Einheit-
Spezifikation behandelt.

Ein   detaillierter
Projektstatusbericht  dokumentiert   den   Projektfortschritt   und   der
Qualitätseigenschaften des Projekts.

 Projektplan  enthält   die   Planung   für   die   nächste  Projektfortschrittsstufe.   Der
 QS-Bericht  beschreibt   die

Es wird eine Projektfortschrittsentscheidung getroffen, um zum nächsten Entscheidungspunkt überzugehen.

Zugeordnete Produkte

Betriebsverantwortlicher:
Erweiterung der Vorgaben zum IT-Betrieb
Datenschutzverantwortlicher:
Erweiterung der Vorgaben zum Datenschutz
Informationssicherheitsverantwortlicher:
Erweiterung der Vorgaben zur Informationssicherheit, Sicherheitskonzeption
Projekteigner:
Projektfortschrittsentscheidung
Projektleiter:
Projektplan, Projektstatusbericht
Prüfer:
Prüfspezifikation Systemelement
QS-Verantwortlicher:
QS-Bericht
Systemarchitekt:
Externe-Einheit-Spezifikation, Implementierungs-, Integrations- und Prüfkonzept
System, Systemarchitektur, Systemspezifikation

E.1.11 Einheit(en) entworfen
In dem  Entscheidungspunkt  Einheit(en) entworfen  wird die Software-Architektur abschließend bezüglich
ihrer Tragfähigkeit bewertet.

Im Falle einer positiven Entscheidung sind die Produkte des Typs SW-Spezifikation sowie die Produkte des
Typs Externes-SW-Modul-Spezifikation vollständig verfeinert, anhand derer die Einheiten realisiert werden
können. Zusätzlich sind die Prüf- und Integrationskonzepte für Software fertig gestellt, mit deren Hilfe später
die Implementierung der Einheiten auf ihre Funktionalität hin geprüft werden kann. Darüber hinaus liegt
auch   die  SW-Architektur  vor.   Mithilfe   dieser   Produkte   kann   die   Realisierung   der   Systemelemente
vorgenommen   werden,   oder   es   können   geeignete   Produkte   der  Typen  Externes   SW-Modul  und  Externe
Einheit ausgewählt werden, die zunächst zu Einheiten und dann zum System integriert werden. Außerdem ist
für alle Systemelemente die Prüfspezifikation Systemelement fertig gestellt.

Ein   detaillierter
Projektstatusbericht  dokumentiert   den   Projektfortschritt   und   der
Qualitätseigenschaften des Projekts.

 Projektplan  enthält   die   Planung   für   die   nächste  Projektfortschrittsstufe.   Der
 QS-Bericht  beschreibt   die

Es wird eine Projektfortschrittsentscheidung getroffen, um zum nächsten Entscheidungspunkt überzugehen.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

E.1 Entscheidungspunkte

Zugeordnete Produkte

233

Betriebsverantwortlicher:
Erweiterung der Vorgaben zum IT-Betrieb
Datenschutzverantwortlicher:
Erweiterung der Vorgaben zum Datenschutz
Informationssicherheitsverantwortlicher:
Erweiterung der Vorgaben zur Informationssicherheit, Sicherheitskonzeption
Projekteigner:
Projektfortschrittsentscheidung
Projektleiter:
Projektplan, Projektstatusbericht
Prüfer:
Prüfspezifikation Systemelement
QS-Verantwortlicher:
QS-Bericht
SW-Architekt:
Externes-SW-Modul-Spezifikation, Implementierungs-, Integrations- und
Prüfkonzept SW, SW-Architektur, SW-Spezifikation

E.1.12 Einheit(en) realisiert
In dem  Entscheidungspunkt  Einheit(en) realisiert  wird anhand des Produkts  Prüfprotokoll Systemelement
untersucht, ob alle Einheiten für sich gemäß ihren Spezifikationen funktionieren.

Im   Falle   einer   positiven   Bewertung   liegen   die   einzelnen   funktionsfähigen  SW-Einheit
Gesamtsystem integriert werden können.

 en     vor,   die   zum

Ein   detaillierter
Projektstatusbericht  dokumentiert   den   Projektfortschritt   und   der
Qualitätseigenschaften des Projekts.

 Projektplan  enthält   die   Planung   für   die   nächste  Projektfortschrittsstufe.   Der
 QS-Bericht  beschreibt   die

Es wird eine Projektfortschrittsentscheidung getroffen, um zum nächsten Entscheidungspunkt überzugehen.

Zugeordnete Produkte

Projekteigner:
Projektfortschrittsentscheidung
Projektleiter:
Projektplan, Projektstatusbericht
Prüfer:
Prüfprotokoll Systemelement
QS-Verantwortlicher:
QS-Bericht
SW-Entwickler:
Externes SW-Modul, SW-Einheit, SW-Komponente, SW-Modul

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


234

 Referenz Abläufe

E.1.13 System integriert
In dem Entscheidungspunkt System integriert wird vom Auftragnehmer anhand des Produkte
 s   Prüfprotokoll
Systemelement  bewertet, ob das  System  den Anforderungen des Auftraggebers entspricht. Im Falle einer
positiven Bewertung liegen das integrierte  System  mit allen  Segment
 en     und Produkte vom
Typ  Externe   Einheit  sowie   die  Logistische   Unterstützungsdokumentation  (mit   Ausbildungs-   und
Nutzungsdokumentation etc.) in einer lieferbaren Form vor.

 en   ,  SW-Einheit

Ein   detaillierter
Projektstatusbericht  dokumentiert   den   Projektfortschritt   und   der
Qualitätseigenschaften des Projekts.

 Projektplan  enthält   die   Planung   für   die   nächste  Projektfortschrittsstufe.   Der
 QS-Bericht  beschreibt   die

Es wird eine Projektfortschrittsentscheidung getroffen, um zum nächsten Entscheidungspunkt überzugehen.

Zugeordnete Produkte

Projekteigner:
Projektfortschrittsentscheidung
Projektleiter:
Projektplan, Projektstatusbericht
Prüfer:
Prüfprotokoll Systemelement
QS-Verantwortlicher:
QS-Bericht
Systemintegrator:
Externe Einheit, Segment, System
Technischer Autor:
Logistische Unterstützungsdokumentation

E.1.14 Sprint gestartet
Bei   der   agilen   Softwareentwicklung   wird   das   System   in   kurzen,   aufeinanderfolgenden   Zyklen   (Sprints)
erstellt. Jeder Sprint beginnt mit dem Entscheidungspunkt  Sprint gestartet, zu dem der  Product Owner  die
aktuelle Version des Product Backlogs dem Entwicklungsteam des Auftragnehmers bereitstellt.

Zugeordnete Produkte

Product Owner:
Product Backlog

E.1.15 Sprint abgeschlossen
Der   Entscheidungspunkt
 Sprint   abgeschlossen  kennzeichnet   das   Ende   eines   Sprints   im   agilen
Softwareentwicklungsprojekt. Der Auftragnehmer stellt dem Auftraggeber zum Entscheidungspunkt das im
Sprint erarbeitete Ergebnis als Inkrement (von AN) bereit.

Zugeordnete Produkte

Product Owner:
Inkrement (von AN)

E.1.16 Lieferung durchgeführt
Ziel  des  Entscheidungspunkt
 es     Lieferung durchgeführt  ist  es  das  System  an den Auftraggeber  bzw.  den
Anwender auszuliefern. Dazu wird das System bzw. die zu liefernden Dokumente geprüft und das Ergebnis
der Prüfung im Produkt Prüfprotokoll Systemelement bzw. Prüfprotokoll festgehalten.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland





E.1 Entscheidungspunkte

235

Im Falle einer positiven Bewertung durch die Prüfung ist das (Teil-)System in Form der  Lieferung an den
Auftraggeber   bzw.   den   Anwender   zu   übergeben,   der   im   Folgenden   überprüfen   kann,   ob   es   seinen
Anforderungen entspricht.

Ein   detaillierter
Projektstatusbericht  dokumentiert   den   Projektfortschritt   und   der
Qualitätseigenschaften des Projekts.

 Projektplan  enthält   die   Planung   für   die   nächste  Projektfortschrittsstufe.   Der
 QS-Bericht  beschreibt   die

Es wird eine Projektfortschrittsentscheidung getroffen, um zum nächsten Entscheidungspunkt überzugehen.

Zugeordnete Produkte

Projekteigner:
Projektfortschrittsentscheidung
Projektleiter:
Lieferung, Projektplan, Projektstatusbericht
Prüfer:
Prüfprotokoll, Prüfprotokoll Systemelement
QS-Verantwortlicher:
QS-Bericht

E.1.17 Projektfortschritt überprüft
In  dem  Entscheidungspunkt  Projektfortschritt   überprüft  wird  durch  den Auftraggeber   überprüft,   wie   das
Projekt   auf  Auftragnehmerseite   voranschreitet.  Während   der  Auftragnehmer   mit   der   Systementwicklung
beschäftigt ist, gehört es zu den Aufgaben des Auftraggebers, ihn in fachlichen Fragen zu unterstützen und
den Projektfortschritt zu beobachten.

Die zeitliche Planung dieses Entscheidungspunktes wird in Abhängigkeit vom Auftragnehmer gestaltet. Der
Auftragnehmer   legt   den  Projektstatusbericht   (von   AN)  als   Entscheidungsgrundlage   für   diesen
Entscheidungspunkt vor.

Ein   detaillierter
Projektstatusbericht  dokumentiert   den   Projektfortschritt   und   der
Qualitätseigenschaften des Projekts.

 Projektplan  enthält   die   Planung   für   die   nächste  Projektfortschrittsstufe.   Der
 QS-Bericht  beschreibt   die

Es wird eine Projektfortschrittsentscheidung getroffen, um zum nächsten Entscheidungspunkt überzugehen.

Zugeordnete Produkte

Projekteigner:
Projektfortschrittsentscheidung
Projektleiter:
Projektplan, Projektstatusbericht, Projektstatusbericht (von AN)
QS-Verantwortlicher:
QS-Bericht

E.1.18 Abnahme erklärt
In dem  Entscheidungspunkt  Abnahme erklärt  wird durch den  Lenkungsausschuss  des Auftraggebers bzw.
 s    untersucht,   ob   das   gelieferte   (Teil-)System  seinen
durch   den  Anwender  anhand   des  Abnahmeprotokoll
Anforderungen entspricht. Bei einem positiven Ergebnis kann die Abnahmeerklärung unterzeichnet werden.

Im Falle einer positiven Bewertung ist das (Teil-)System fertig gestellt und im Rahmen der Lieferung (von
AN) nun im Besitz des Auftraggebers.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


236

 Referenz Abläufe

Ein   detaillierter
Projektstatusbericht  dokumentiert   den   Projektfortschritt   und   der
Qualitätseigenschaften des Projekts.

 Projektplan  enthält   die   Planung   für   die   nächste  Projektfortschrittsstufe.   Der
 QS-Bericht  beschreibt   die

Es wird eine Projektfortschrittsentscheidung getroffen, um zum nächsten Entscheidungspunkt überzugehen.

Für den Fall, dass die Abnahme aufgrund mangelnder Qualität der Lieferung nicht ausgesprochen werden
kann, ergeben sich folgende Möglichkeiten:

1. Teilzahlungen   können   an   die   Abnahme   gebunden   sein.   Ohne   ausgesprochene   Abnahme   kann
vereinbart werden, dass diese Teilzahlungen für eine Iteration auf die nächste Iteration verschoben
werden. Die Arbeit läuft also weiter wie geplant, nur dass die Mängel in der folgenden Iteration
behoben werden müssen.

2.

Im Projekt wird die nötige Anzahl Entscheidungspunkte zurückgegangen und die Arbeit in Richtung
Abnahme wiederholt.

3. Das Projekt wird abgebrochen.

Zugeordnete Produkte

Projekteigner:
Abnahmeerklärung, Projektfortschrittsentscheidung
Projektleiter:
Lieferung (von AN), Projektplan, Projektstatusbericht
Prüfer:
Abnahmeprotokoll
QS-Verantwortlicher:
QS-Bericht

E.1.19 Abnahme durchgeführt
In   dem  Entscheidungspunkt  Abnahme   durchgeführt  prüft   der   interne   Auftraggeber   das   entwickelte
(Teil-)System (Lieferung) und bestätigt dem internen Auftragnehmer die Abnahme.

Ein   detaillierter
Projektstatusbericht  dokumentiert   den   Projektfortschritt   und   der
Qualitätseigenschaften des Projekts.

 Projektplan  enthält   die   Planung   für   die   nächste  Projektfortschrittsstufe.   Der
 QS-Bericht  beschreibt   die

Es wird eine Projektfortschrittsentscheidung getroffen, um zum nächsten Entscheidungspunkt überzugehen.

Für den Fall, dass die Abnahme aufgrund mangelnder Qualität der Lieferung nicht ausgesprochen werden
kann, ergeben sich folgende Möglichkeiten:

1. Teilzahlungen   können   an   die   Abnahme   gebunden   sein.   Ohne   ausgesprochene   Abnahme   kann
vereinbart werden, dass diese Teilzahlungen für eine Iteration auf die nächste Iteration verschoben
werden. Die Arbeit läuft also weiter wie geplant, nur dass die Mängel in der folgenden Iteration
behoben werden müssen.

2.

Im Projekt wird die nötige Anzahl Entscheidungspunkte zurückgegangen und die Arbeit in Richtung
Abnahme wiederholt.

3. Das Projekt wird abgebrochen.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

E.1 Entscheidungspunkte

Zugeordnete Produkte

Projekteigner:
Projektfortschrittsentscheidung
Projektleiter:
Projektplan, Projektstatusbericht
QS-Verantwortlicher:
QS-Bericht

237

E.1.20 Systembetrieb freigegeben
Dieser Entscheidungspunkt kann sowohl vor, nach oder parallel zum Entscheidungspunkt Abnahme erklärt
erreicht werden.

Zu diesem Entscheidungspunkt muss die Betriebliche Freigabeerklärung vorliegen, die ein abzunehmendes
bzw.   fachlich   bereits   abgenommenes   System   für   den   betrieblichen   Einsatz   frei   gibt.   Sind   während   der
Prüfung   auf   Basis   der  Prüfspezifikation   Inbetriebnahme  betriebsverhindernde   Mängel   offensichtlich
geworden, sind diese im Prüfprotokoll Inbetriebnahme zu dokumentieren. Eine Freigabe kann in diesem Fall
nicht erklärt werden.

Zugeordnete Produkte

Betriebsverantwortlicher:
Betriebliche Freigabeerklärung
Projekteigner:
Projektfortschrittsentscheidung
Projektleiter:
Projektplan, Projektstatusbericht

E.1.21 Gesamtprojekt aufgeteilt
Im Entscheidungspunkt Gesamtprojekt aufgeteilt wird das Projekt auf der Basis der Skizze des Lebenszyklus
und   der   Gesamtsystemarchitektur  des   Produkts  Lastenheft   Gesamtprojekt  in   durchführbare   Teilprojekte
aufgeteilt.   Falls   sich   diese  Aufteilung   in  Teilprojekte   als   durchführbar   erweist,   wird   die   Festlegung   der
Teilprojekte im Projekthandbuch und im Projektplan eingebracht.

Es wird eine Projektfortschrittsentscheidung getroffen, um zum nächsten Entscheidungspunkt überzugehen.

Zugeordnete Produkte

Anforderungsanalytiker (AG):
Bewertung Lastenheft Gesamtprojekt, Lastenheft Gesamtprojekt
Projekteigner:
Projektfortschrittsentscheidung
Projektleiter:
Projekthandbuch, Projektplan, Projektstatusbericht
QS-Verantwortlicher:
QS-Bericht, QS-Handbuch

E.1.22 Gesamtprojektfortschritt überprüft
Auf der Basis aller Projektstatusbericht
 e   (von AN) der Teilprojekte wird eine Projektfortschrittsentscheidung
herbeigeführt, ob das Gesamtprojekt sich noch im Rahmen der im Projektplan gesetzten Plandaten befindet
und ob bzw. wie es fortgeführt werden soll.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


238

Zugeordnete Produkte

 Referenz Abläufe

Projekteigner:
Projektfortschrittsentscheidung
Projektleiter:
Projektplan, Projektstatusbericht, Projektstatusbericht (von AN)
QS-Verantwortlicher:
QS-Bericht

E.1.23 Projekt abgeschlossen
In dem Entscheidungspunkt Projekt abgeschlossen wird entschieden, ob das Projekt abgeschlossen wird.

Im   Falle   einer   positiven   Bewertung   bildet   der  Projektabschlussbericht  die   Grundlage   für   spätere
Analyseaufgaben. Um die Übergabe in den Wirkbetrieb zu ermöglichen und die dazugehörenden Regelungen
zwischen   Fach-   und   IT-Abteilung   zu   fixieren,   muss   zu   diesem   Zeitpunkt   auch   das   Produkt
Leistungsvereinbarung (SLA/OLA/UC) fertig gestellt werden.

Zugeordnete Produkte

Projekteigner:
Projektfortschrittsentscheidung
Projektleiter:
Leistungsvereinbarung (SLA/OLA/UC), Projektabschlussbericht,
Projektabschlussbericht (von AN)

E.2 Projektdurchführungsstrategien

E.2.1 AG-Projekt mit einem Auftragnehmer
Die Entscheidungspunkte der Projekttypvariante  AG-Projekt mit einem Auftragnehmer, sowie der Ablauf
sind in Abbildung 58 dargestellt.

Abbildung 58: Projekttypvariante AG-Projekt mit einem Auftragnehmer

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

E.2 Projektdurchführungsstrategien

239

Ablaufbausteine

Steuerung des Auftragnehmers im klassischen Softwareentwicklungsprojekt,
Abnahme als AG, Abnahme als AG mit Inbetriebnahme, Steuerung des
Auftragnehmers im agilen Softwareentwicklungsprojekt

E.2.2 AG-Projekt mit mehreren Auftragnehmern
Die   Entscheidungspunkte   der   Projekttypvariante  AG-Projekt   mit   mehreren   Auftragnehmern  sowie   der
Ablauf sind in Abbildung 59 dargestellt.

Abbildung 59: Projekttypvariante AG-Projekt mit mehreren Auftragnehmern

Ablaufbausteine

Steuerung des Auftragnehmers im klassischen Softwareentwicklungsprojekt,
Abnahme als AG, Abnahme als AG mit Inbetriebnahme, Steuerung des
Auftragnehmers im agilen Softwareentwicklungsprojekt

E.2.3 AG/AN-Projekt mit Entwicklung, Weiterentwicklung oder
Migration
Die Entscheidungspunkte der Projekttypvariante AG/AN-Projekt mit Entwicklung, Weiterentwicklung oder
Migration  sowie   der   Ablauf   eines   Entwicklungszyklus   sind   in  Abbildung   60  dargestellt.   Die
Projekttypvariante erlaubt, verschiedene Entwicklungsstrategien anzuwenden:

1.

inkrementelle Entwicklung

2. komponentenbasierte Entwicklung

3. prototypische Entwicklung

Die   Entscheidung   für   eine   Entwicklungsstrategie   wird   jedes   Mal   dann   getroffen,   nachdem   der
Entscheidungspunkt Iteration geplant eingeplant wird. Bestehen beispielsweise hohe Realisierungsrisiken, so
kann eine frühe Iteration mittels prototypischer Entwicklung durchgeführt werden.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland







240

 Referenz Abläufe

Abbildung 60: Projekttypvariante AG-AN-Projekt mit Entwicklung, Weiterentwicklung oder Migration

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

E.2 Projektdurchführungsstrategien

241

Ablaufbausteine

Steuerung des Auftragnehmers im klassischen Softwareentwicklungsprojekt,
Abnahme als AG, Inkrementelle Systementwicklung, Komponentenbasierte
Systementwicklung, Prototypische Systementwicklung, Unterauftrag, Abnahme
als AG mit Inbetriebnahme, Abnahme als AG/AN, Abnahme als AG/AN mit
Inbetriebnahme, Steuerung des Auftragnehmers im agilen
Softwareentwicklungsprojekt

E.2.4 AG/AN-Projekt mit Wartung und Pflege
Die Entscheidungspunkte der Projekttypvariante AG/AN-Projekt mit Wartung und Pflege sowie der Ablauf
der möglichen Entwicklungszyklen sind in Abbildung 61 dargestellt. Der Ablauf unterscheidet sich von der
Projekttypvariante  AG/AN-Projekt mit Entwicklung, Weiterentwicklung oder Migration  maßgeblich durch
die unterschiedlichen Einstiegspunkte in der Systementwicklung, die davon abhängen, wie umfassend die
durchzuführenden   Änderungen   am   System   sind.   Betroffen   sein   können   der   Gesamtsystementwurf,   der
Systementwurf oder der Feinentwurf.

Abbildung 61: Projekttypvariante AG-AN-Projekt mit Wartung und Pflege

Ablaufbausteine

Steuerung des Auftragnehmers im klassischen Softwareentwicklungsprojekt,
Abnahme als AG, Unterauftrag, Abnahme als AG mit Inbetriebnahme, Abnahme
als AG/AN, Abnahme als AG/AN mit Inbetriebnahme, Steuerung des
Auftragnehmers im agilen Softwareentwicklungsprojekt

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

242

 Referenz Abläufe

E.3 Ablaufbausteine

E.3.1 Abnahme als AG
Dieser Ablaufbaustein beschreibt den Abnahmeprozess der vom Auftragnehmer gelieferten Ergebnisse durch
den   Auftraggeber.   Die   Abnahme   erfolgt   auf   Basis   der   im  Lastenheft   (Anforderungen)  enthaltenen
Anforderungen.

E.3.2 Abnahme als AG/AN
Dieser Ablaufbaustein beschreibt den Abnahmeprozess der von einem internen Auftragnehmer gelieferten
Ergebnisse   durch   den  Auftraggeber.   Die  Abnahme   erfolgt   auf   Basis   der   im  Lastenheft   (Anforderungen)
enthaltenen Anforderungen.

E.3.3 Abnahme als AG/AN mit Inbetriebnahme
Dieser Ablaufbaustein erweitert den Ablaufbaustein Abnahme als AG/AN um einen Prozess für den Erhalt
der vom IT-Betrieb auszustellenden Freigabeerklärung.

E.3.4 Abnahme als AG mit Inbetriebnahme
Dieser Ablaufbaustein erweitert den Ablaufbaustein Abnahme als AG um einen Prozess für den Erhalt der
vom IT-Betrieb auszustellenden Freigabeerklärung.

E.3.5 Inkrementelle Systementwicklung
Eine   Entwicklungsstrategie,
(Gesamtsystementwurf)
Divide&Conquer-Prinzip immer weiter verfeinert bis SW-Spezifikation
SW-Architektur umgesetzt und integriert werden.

  bei   der   zunächst   das   Gesamtsystem   in   einem  Pflichtenheft
spezifiziert   wird.   Der   Systementwurf   wird   anschließend   nach   dem
 en    vorliegen, die dann anhand einer

Der Auftragnehmer entwirft, realisiert und liefert das System in einzelnen Stufen, welche auch  Inkrement
genannt werden. Jede dieser Stufen wird einzeln vom Auftraggeber abgenommen und entweder im Vorfeld
vertraglich vereinbart oder es werden zusätzliche Verträge über die Abwicklung ergänzender Inkremente
abgeschlossen. Bevor ein Inkrement an den Auftraggeber ausgeliefert wird, kann der Auftragnehmer intern
mehrere Iterationen durchlaufen.

Änderungen durch den Auftraggeber innerhalb eines Inkrements sind bei dieser Entwicklungsstrategie zu
vermeiden   und   sollten   über   das   Änderungsmanagement   im   folgenden   Inkrement   berücksichtigt   werden.
Wichtige  Änderungen, die beispielsweise die Architektur  des Systems  maßgeblich beeinflussen könnten,
sollten   dem   Auftragnehmer   so   früh   wie   möglich   mitgeteilt   werden.   Für   den   Auftraggeber   hat   diese
Vorgehensweise den Vorteil, dass er frühzeitig in den Besitz einer Vorstufe des Systems gelangt, die bereits
die wichtigsten Grundfunktionalitäten des Systems realisiert.

Diese Entwicklungsstrategie eignet sich vor allem dann, wenn die Anforderungen an das System als relativ
stabil eingeschätzt werden und technologische Risiken eher gering sind. Es können Fertigprodukte eingesetzt
werden, der Hauptanteil des Systems wird jedoch im Rahmen des Projekts erstellt.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


E.3 Ablaufbausteine

243

E.3.6 Komponentenbasierte Systementwicklung
Der Entwicklungsstrategie komponentenbasierte Entwicklung liegt die Idee zugrunde, dass das neue System
weitgehend durch Integration bestehender Systemelemente erstellt wird. Ein für die Integration vorgesehenes
Systemelement  (z.B.   ein   Segment   oder   eine   HW/SW-Einheit)   hat   eine   klar   definierte   Schnittstelle   nach
außen, kapselt Entwurf und Implementierung und kann mit anderen Systemelementen verbunden werden. Es
ist   sowohl   fachlich   als   auch   technisch   unabhängig   und   besitzt   eine   gewisse   Größe   (im   Sinne   eines
wirtschaftlichen Wertes).

Allgemein werden von einem Systemelement für die Integration folgende Eigenschaften verlangt:

➢ Verfügbarkeit klarer, sauber definierter Schnittstellen

➢ Kommunikation mit der Außenwelt (zum Beispiel mit anderen Komponenten) ausschließlich über

die definierten Schnittstellen

➢ Anpassung an bestimmte Anwendungsumgebungen (Customizing) nur über die Schnittstellen

➢ Realisierungsspezifika bleiben dem Benutzer verborgen (Blackbox-Sichtweise)

E.3.7 Prototypische Systementwicklung
Die  prototypische   Entwicklung
   basiert   auf   der   Erkenntnis,   dass   es   oft   nicht   möglich   ist,   die
Anforderungen an ein System vorab zu definieren. Außerdem stellt sie sicher, dass nichts spezifiziert wird,
was   sich   als   nicht   realisierbar   herausstellt.   Somit   wird   diese   Strategie   insbesondere   verwendet,   wenn
Realisierungsrisiken   im   Projekt   vorhanden   sind.   Änderungen   an   den  Anforderungen   werden   über   das
Problem- und Änderungsmanagement verwaltet.

 sstrategie

Typisch   für   diese   Entwicklungsstrategie   ist   darüber   hinaus   die   Präsenz   des   Auftraggebers   auf   der
Auftragnehmerseite   während   der   Entwicklung.   Dadurch   kann   der  Auftraggeber   Änderungswünsche   sehr
direkt übermitteln. Der Auftragnehmer entwirft, realisiert und liefert das System dann ähnlich wie bei der
Entwicklungsstrategie  inkrementelle Entwicklung  in einzelnen Stufen. Diese Stufen werden jede für sich
vom Auftraggeber abgenommen. Für den Auftraggeber hat diese Vorgehensweise den Vorteil, dass er bereits
frühzeitig   in   den   Besitz   eines   lauffähigen   Systems   gelangt,   das   die   wichtigsten   Grundfunktionalitäten
realisiert.   Ferner   ermöglicht   sie   eine   frühzeitige   Rückmeldung   durch   den   Auftraggeber,   die   die
Entwicklungsrisiken des Auftragnehmers minimiert.

E.3.8 Steuerung des Auftragnehmers im agilen
Softwareentwicklungsprojekt
Der Ablaufbaustein dient zur Steuerung des Auftragnehmers in einem agilen Softwareentwicklungsprojekt
nach Scrum. Die Entwicklung erfolgt in kurzen, aufeinanderfolgenden Zyklen (Sprints) mit einer Dauer von
jeweils maximal 4 Wochen.

Der   Baustein   umfasst   Entscheidungspunkte   zur  Abbildung   von   Start   und   Ende   der   Sprints   sowie   zur
regelmäßigen Überprüfung des Projektfortschritts innerhalb eines Sprints.

E.3.9 Steuerung des Auftragnehmers im klassischen
Softwareentwicklungsprojekt
Der   Ablaufbaustein   dient
in   einem   klassischen
Softwareentwicklungsprojekt   nach   V-Modell.   Jeder   Entwicklungszyklus   (Iteration)   kann   eine
unterschiedliche und beliebige Dauer aufweisen.

  zur   Steuerung   des   Auftragnehmers

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland



244

 Referenz Abläufe

Der   Baustein   umfasst   Entscheidungspunkte   für   die   Planung   der   Iterationen   und   zur   regelmäßigen
Überprüfung des Projektfortschritts innerhalb einer Iteration.

E.3.10 Unterauftrag
Bei größeren Projekten ist es bei einem Auftragnehmer- bzw. einem Auftraggeber/Auftragnehmer-Projekt
möglich,   einen   oder   mehrere   Unteraufträge   zu   vergeben.   Durch   die   Unterauftragsvergabe   nimmt   der
Auftragnehmer (bzw. der AG/AN) Aufgaben und Rolle des Auftraggebers wahr. Ein Auftragnehmer, bzw.
Auftraggeber/Auftragnehmer, wird dann als Unterauftraggeber bezeichnet, wenn er Teile des Systems selbst
als Auftraggeber weiter an einen  Unterauftragnehmer  vergibt, um den  Vertrag  (bzw.  Auftrag) mit seinem
Auftraggeber zu erfüllen. Demnach ist ein Unterauftragnehmer der Lieferant, der dem Unterauftraggeber ein
Systemelement bzw. Teilsystem bereitstellt (DIN EN ISO 8402). Die Projekte des Unterauftraggebers und
des   Unterauftragnehmers   werden   gemäß   dem   V-Modell
  und   durch   die
Auftraggeber-/Auftragnehmer-Schnittstelle miteinander verbunden. Für den Fall einer Unterauftragsvergabe
ist   festzulegen,   welche   Qualitätsvorgaben   für   den   Unterauftrag   gelten.   Diese   Vorgaben   sind   bei   der
Produkterstellung seitens des Unterauftragnehmers einzuhalten. Das Produkt Lastenheft (Anforderungen) ist
für den Unterauftraggeber nicht erforderlich zu erarbeiten. An dieser Stelle dienen die Produkte  Externes-
SW-Modul-Spezifikation und Externe-Einheit-Spezifikation als Vorgaben für den Unterauftragnehmer.

  abgewickelt

E.4 Ablaufindex
Modellelement

Abnahme als AG

Abnahme als AG/AN

Abnahme als AG/AN mit Inbetriebnahme

Abnahme als AG mit Inbetriebnahme

Abnahme durchgeführt

Abnahme erklärt

Typ

Ablaufbaustein

Ablaufbaustein

Ablaufbaustein

Ablaufbaustein

Entscheidungspunkt

Entscheidungspunkt

Seite

242

242

242

242

236

235

AG/AN-Projekt mit Entwicklung, Weiterentwicklung oder Migration Projektdurchführungsstr

239

AG/AN-Projekt mit Wartung und Pflege

AG-Projekt mit einem Auftragnehmer

AG-Projekt mit mehreren Auftragnehmern

Anforderungen festgelegt

Angebotsaufforderung erstellt

Ausschreibung freigegeben

Beauftragung erteilt

ategie

Projektdurchführungsstr
ategie

241

Projektdurchführungsstr
ategie

238

Projektdurchführungsstr
ategie

239

Entscheidungspunkt

Entscheidungspunkt

Entscheidungspunkt

Entscheidungspunkt

227

229

228

229

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

E.4 Ablaufindex

Modellelement

Einheit(en) entworfen

Einheit(en) realisiert

Gesamtprojekt aufgeteilt

Gesamtprojektfortschritt überprüft

Gesamtsystem entworfen

Inkrementelle Systementwicklung

Iteration geplant

Komponentenbasierte Systementwicklung

Lieferung durchgeführt

Produktvision entworfen

Projekt abgeschlossen

Projektfortschritt überprüft

Projekt genehmigt

Projekt initialisiert

Prototypische Systementwicklung

Sprint abgeschlossen

Sprint gestartet

Steuerung des Auftragnehmers im agilen
Softwareentwicklungsprojekt

Steuerung des Auftragnehmers im klassischen
Softwareentwicklungsprojekt

Systembetrieb freigegeben

System entworfen

System integriert

Unterauftrag

245

Typ

Seite

Entscheidungspunkt

Entscheidungspunkt

Entscheidungspunkt

Entscheidungspunkt

Entscheidungspunkt

Ablaufbaustein

Entscheidungspunkt

Ablaufbaustein

Entscheidungspunkt

Entscheidungspunkt

Entscheidungspunkt

Entscheidungspunkt

Entscheidungspunkt

Entscheidungspunkt

Ablaufbaustein

Entscheidungspunkt

Entscheidungspunkt

Ablaufbaustein

Ablaufbaustein

Entscheidungspunkt

Entscheidungspunkt

Entscheidungspunkt

Ablaufbaustein

232

233

237

237

231

242

230

243

234

228

238

235

226

226

243

234

234

243

243

237

231

234

244

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

246

 Referenz Tailoring

F Referenz Tailoring

F.1 Projekttypen und Projekttypvarianten

F.1.1 Systementwicklungsprojekt (AG)
Dieser   Projekttyp   befasst   sich   mit   V-Modell-Projekten   auf   der   Auftraggeberseite.   Bei   ihnen   muss   im
Projektverlauf ein Auftragnehmer bestimmt werden. Für die Beauftragung eines externen IT-Dienstleisters
wird zu diesem Zweck eine Ausschreibung erstellt und eines der eingegangenen Angebote ausgewählt. Die
Beauftragung eines IT-Dienstleisters des Bundes erfolgt ohne Ausschreibungs- und Vergabeverfahren auf
Basis einer Angebotsaufforderung. Der Auftragnehmer ist für die Systementwicklung zuständig und liefert
dem Auftraggeber ein System, welches dieser abnehmen muss.

Projektmerkmale

Ausgewählte
Vorgehensbausteine

Auftragnehmer, Entwicklungsmethode, Fertigprodukte, Informationssicherheit
und Datenschutz (AG), Betriebsübergabe (AG)

Projektmanagement, Projektmanagement (Bund), Qualitätssicherung,
Konfigurationsmanagement, Problem- und Änderungsmanagement,
Projektcontrolling, Wirtschaftlichkeitsbetrachtung, Vertragsschluss (AG),
Lieferung und Abnahme (AG)

F.1.1.1 AG-Projekt mit einem Auftragnehmer

Die   Projekttypvariante  AG-Projekt   mit   einem   Auftragnehmer  beschreibt   eine   Vorgehensweise   des
Projekttyps  Systementwicklungsprojekt (AG)  für die Vergabe eines Systementwicklungsprojekts an  einen
Auftraggeber.

Die   Vergabe   und   Durchführung   von   Systementwicklungsprojekten   beruht   auf   der   Grundidee,   dass   der
Auftraggeber die Notwendigkeit eines Systementwicklungsprojekts feststellt und das System nicht selbst
entwickelt bzw. entwickeln kann. Der Auftraggeber muss daher die Anforderungen an das benötigte System
festlegen. Die Entwicklung des Systems (oder einzelner Ausbaustufen) wird durch einen Auftragnehmer
durchgeführt.   Die   dabei   zu   erbringenden   Leistungen   werden   im  Anschluss   an   ein  Ausschreibungs-   und
Vergabeverfahren   in   einem  Vertrag  zwischen   dem  Auftraggeber   und   dem   erfolgreichen  Auftragnehmer
definiert.   Die   vom   Auftragnehmer   erbrachten   Leistungen   sind   durch   den   Auftraggeber   gemäß   der
vertraglichen Vereinbarung abzunehmen.

Wird die Systementwicklung durch einen IT-Dienstleister des Bundes erbracht, entfällt das Ausschreibungs-
und Vergabeverfahren. Stattdessen bildet der Auftrag die Grundlage der Zusammenarbeit.

Projektdurchführungsstr
ategie

Ausgewählte
Ablaufbausteine

AG-Projekt mit einem Auftragnehmer

Abnahme als AG

F.1.1.2 AG-Projekt mit mehreren Auftragnehmern

Die   Projekttypvariante  AG-Projekt   mit   mehreren   Auftragnehmern  beschreibt   eine   Vorgehensweise   des
Projekttyps Systementwicklungsprojekt (AG) für die Vergabe eines Systementwicklungsprojekts an mehrere
Auftraggeber.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

F.1 Projekttypen und Projekttypvarianten

247

Die   Projekttypvariante   beruht   auf   der   Grundidee,   dass   der   Auftraggeber   die   Notwendigkeit   eines
Systementwicklungsprojekts feststellt und das System nicht selbst entwickelt bzw. entwickeln kann und eine
Realisierung in mehreren Teilprojekten technische, organisatorische und wirtschaftliche Vorteile erwarten
lässt.   Es   müssen   daher   die  Anforderungen   an   das   Gesamtsystem   festlegt   werden.   Weiterhin   muss   eine
sinnvolle Aufteilung der Anforderungen auf der Basis einer Gesamtsystemarchitektur in Teilprojekte möglich
sein. Dabei ist stets ein Teilprojekt zu definieren, das die Integration der Ergebnisse der anderen Teilprojekte
beinhaltet.   Die   Entwicklung   des   Systems   (oder   einzelner  Ausbaustufen)   wird   in   mehreren  Teilprojekten
durch einen oder mehrere Auftragnehmer durchgeführt. Die in den Teilprojekten zu erbringenden Leistungen
werden nach einem Ausschreibungs- und Vergabeverfahren in Verträgen zwischen dem Auftraggeber und
den  erfolgreichen Auftragnehmern   definiert.   Die   von  den Auftragnehmern   erbrachten  Leistungen  in  den
Teilprojekten sind schließlich Gegenstand von Abnahmen durch den Auftraggeber.

Wird die Systementwicklung durch IT-Dienstleister des Bundes erbracht, entfällt das Ausschreibungs- und
Vergabeverfahren. Stattdessen bildet der Auftrag die Grundlage der Zusammenarbeit.

Einschränkung

Diese   Projekttypvariante   ist   nur   dann   sinnvoll   anwendbar,   wenn   der  Aufwand   für   die   Integration   der
Ergebnisse der einzelnen Teilprojekte die oben genannten Vorteile der Entwicklung in Teilprojekten nicht
übersteigt. Dies ist zum Beispiel im Rahmen einer Wirtschaftlichkeitsbetrachtung genau zu prüfen.

Projektdurchführungsstr
ategie

Ausgewählte
Vorgehensbausteine

Ausgewählte
Ablaufbausteine

AG-Projekt mit mehreren Auftragnehmern

Multi-Projektmanagement

Abnahme als AG

F.1.2 Systementwicklungsprojekt (AG/AN)
Dieser Projekttyp befasst sich mit V-Modell-Projekten, die keine (vertragliche) Trennung der Auftraggeber-
und Auftragnehmerseite  in  zwei  separate  Projekte  erfordern.  Dies  kann  gegeben sein,  wenn das  Projekt
entweder   in   einer   Behörde   als   "Eigenentwicklung"   durchgeführt   wird   oder   aber   zwar   mehrere
Organisationen beteiligt sind, diese jedoch bewusst in einem Projekt zusammenarbeiten. Im Unterschied zu
den getrennten Systementwicklungsprojekt (AG)  und Systementwicklungsprojekt (AN) entfallen somit das
Ausschreibungs-,   das   Vertragswesen   sowie   die   formale   Angebotserstellung.   Auch   eine   doppelte
Projektorganisation   mit   zwei   Projektleitern   ist   in   diesem   Projekt   nicht   erforderlich.   Die  Aufgaben   der
Auftraggeberseite können beispielsweise von einer Fachabteilung und die der Auftragnehmerseite von der
IT-Abteilung übernommen werden.

Projektmerkmale

Ausgewählte
Vorgehensbausteine

Fertigprodukte, Projektgegenstand, Benutzerschnittstelle, Informationssicherheit
und Datenschutz (AG/AN), Betriebsübergabe (AG/AN)

Projektmanagement, Projektmanagement (Bund), Qualitätssicherung,
Konfigurationsmanagement, Problem- und Änderungsmanagement,
Projektcontrolling, Wirtschaftlichkeitsbetrachtung, Anforderungsfestlegung,
Anforderungsfestlegung (Bund), Systemerstellung, Lieferung und Abnahme
(AG), Lieferung und Abnahme (AN)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

248

 Referenz Tailoring

F.1.2.1 AG/AN-Projekt mit Entwicklung, Weiterentwicklung oder Migration

Die Projekttypvariante AG/AN-Projekt mit Entwicklung, Weiterentwicklung oder Migration kommt nur für
Projekte des Projekttyps Systementwicklungsprojekt (AG/AN) in Betracht. Für ein Projekt ist in diesem Fall
keine  Trennung der Auftraggeber- und Auftragnehmerseite in zwei separate Projekte erforderlich. Infolge
dessen entfallen Ausschreibungs- und Vertragswesen sowie die Erstellung formaler Angebote. Auch ist eine
Organisation mit zwei Projektleiter nicht erforderlich.

Unterstützte Entwicklungsstrategien

Die   Projekttypvariante  AG/AN-Projekt   mit   Entwicklung,   Weiterentwicklung   oder   Migration   unterstützt
mehrere  Anwendungsszenarien:   Neuentwicklung,  Weiterentwicklung   und   Migration.   Generell   erfolgt   die
Entwicklung in dieser Projekttypvariante auf Basis von Anforderungen, die im Projekt zum Beispiel mithilfe
einer Fachabteilung ermittelt wurden. Stehen die Anforderungen zum Entscheidungspunkt  Anforderungen
festgelegt  fest,   kann   das   System   mithilfe   verschiedener   Vorgehensweisen   (sog.   Entwicklungsstrategien)
umgesetzt werden. Das V-Modell bietet für diese Projekttypvariante die folgenden Entwicklungsstrategien
an:

➢ inkrementelle Entwicklung

➢ komponentenbasierte Entwicklung

➢ prototypische Entwicklung

  (nur bei Verwendung des Projektmerkmals Prototypentwicklung )

Weitere Einsatzszenarien

Diese Projekttypvariante kann auch bei der Weiterentwicklung von Altsystemen verwendet werden. Über
eine Entwicklung hinaus, werden die Anforderungen an das neue (Teil-)System dokumentiert, die dann in
den Weiterentwicklungsprozess einfließen.

Wird ein System auf eine neue Umgebung migriert, beispielsweise auf eine neue Hardwareplattform oder
Laufzeitumgebung,   dann   ergibt   sich  gegebenenfalls   eine   andere   Grundlage   für   die  Anforderungen.   Dies
können   die   bei   der   Spezifikation   des   Gesamtsystems   (Gesamtsystem   entworfen)   im   Rahmen   der
Altsystemanalyse  ermittelten   bestehenden   Funktionalitäten,   Anforderungen   in   der   Änderungsstatusliste,
sowie neue Anforderungen des Anwenders sein. Eine vollständige Migration muss nicht immer erforderlich
sein. Bei einer Teilmigration verbleiben Teile des Altsystems auf ihrer ursprünglichen Plattform und das neue
(Teil-)System wird über Integrationstechnologien mit dem Altsystem verbunden.

Problem- und Änderungsmanagement

Das System wird in jeder Entwicklungsstrategie in Stufen entworfen, realisiert und ausgeliefert. Diese Stufen
werden  Inkrement
 e    genannt.   Jede   dieser   Stufen   wird   einzeln   abgenommen   und   ggf.   für   den   Betrieb
freigegeben.   Bevor   ein  Inkrement  ausgeliefert  wird,   kann der  Systemersteller  intern mehrere  Iterationen
durchlaufen. Jedes Inkrement beginnt mit dem Entscheidungspunkt  Iteration geplant. Änderungen an den
Anforderungen werden während der Entwicklung als  nachträgliche  Änderungen nur noch im Rahmen des
Problem-   und   Änderungsmanagements   erfasst.   Zum   Entscheidungspunkt  Iteration   geplant  werden   die
während des Inkrements gesammelten Änderungsforderungen betrachtet und in der Planung für das nächste
Inkrement berücksichtigt. Wichtige Änderungen, die beispielsweise die Architektur des Systems maßgeblich
beeinflussen könnten, sollten so früh wie möglich mitgeteilt werden. Diese Vorgehensweise hat den Vorteil,
dass der Anwender frühzeitig in den Besitz einer Vorstufe des Systems gelangt, die bereits die wichtigsten
Grundfunktionalitäten des Systems realisiert.

Projektdurchführungsstr
ategie

Projektmerkmale

Ausgewählte
Ablaufbausteine

AG/AN-Projekt mit Entwicklung, Weiterentwicklung oder Migration

Altsystem, Prototypentwicklung, Unterauftrag

Inkrementelle Systementwicklung, Komponentenbasierte Systementwicklung,
Abnahme als AG/AN

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland







F.1 Projekttypen und Projekttypvarianten

249

F.1.2.2 AG/AN-Projekt mit Wartung und Pflege

Die Projekttypvariante  AG/AN-Projekt mit Wartung und Pflege  kommt  nur für Projekte des Projekttyps
Systementwicklungsprojekt (AG/AN)  in Betracht. Für ein Projekt ist in diesem Fall  keine  Trennung der
Auftraggeber-   und  Auftragnehmerseite   in   zwei   separate   Projekte   erforderlich.   Infolge   dessen   entfallen
Ausschreibungs- und Vertragswesen sowie die Erstellung formaler Angebote. Auch ist eine Organisation mit
zwei Projektleitern nicht erforderlich.

Die   Projekttypvariante   erfasst   die   Situation,   dass   ein   bereits   in   der   Nutzung   befindliches   System   zu
adaptieren   bzw.   zu   ändern   ist,   indem   zum   Beispiel   Fehler   behoben,   neue  Technologien   eingeführt,   die
Erfüllung   nicht-funktionaler  Anforderungen   verbessert   oder   die   Funktionalität   modifiziert   oder   erweitert
werden   sollen.   Diese  Änderungsanforderungen  werden   zu   Beginn   des   Projekts   vom   Auftraggeber
vorgegeben. Zusätzliche Änderungsanforderungen, die bei der Projektdurchführung auftreten, sind nur über
das
  die
Änderungsanforderungen, führt die notwendigen Änderungen am System durch und liefert das modifizierte
System dann in  der  Regel  in mehreren  Iterationen.  Jede  dieser  Iterationen  wird einzeln vom Anwender
abgenommen.

 Problem-   und   Änderungsmanagement  möglich.

  Der   Systemersteller   analysiert

Projektdurchführungsstr
ategie

AG/AN-Projekt mit Wartung und Pflege

Projektmerkmale

Altsystem, Unterauftrag

Ausgewählte
Ablaufbausteine

Abnahme als AG/AN

F.2 Projektmerkmale

F.2.1 Auftragnehmer
Zur Erstellung des Systems kann als Auftragnehmer ein externer IT-Dienstleister oder ein IT-Dienstleister
des   Bundes   beauftragt   werden.   Für   die   Beauftragung   eines   externen   IT-Dienstleisters   wird   eine
Ausschreibung   erstellt   und   eines   der   eingegangenen  Angebote   ausgewählt.   Die   Beauftragung   eines   IT-
Dienstleisters   des   Bundes   erfolgt   ohne   Ausschreibungs-   und   Vergabeverfahren   auf   Basis   einer
Angebotsaufforderung.

Frage (im Projektassistenten)

Wird   zur   Erstellung   des   Systems   ein   externer   IT-Dienstleister   oder   ein   IT-Dienstleister   des   Bundes
beauftragt?

Antwort

Erläuterung

Externer IT-Dienstleister

IT-Dienstleister des Bundes

Zur Erstellung des Systems wird ein externer IT-Dienstleister beauftragt.
Ausgewählte Vorgehensbausteine: Vertragsschluss (mit externem IT-
Dienstleister)

Zur Erstellung des Systems wird ein IT-Dienstleister des Bundes beauftragt.
Ausgewählte Vorgehensbausteine: Vertragsschluss (mit IT-Dienstleister
des Bundes)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

250

 Referenz Tailoring

F.2.2 Entwicklungsmethode
Der   Auftraggeber   muss   festlegen,   welche   Entwicklungsmethode   beim   Auftragnehmer   zur   Anwendung
kommen soll.

Bei der  klassischen  Softwareentwicklung werden die umzusetzenden Anforderungen zu Projektbeginn in
Form eines vollständigen Lastenhefts festgelegt und anschließend vom Auftragnehmer umgesetzt.

Bei   der  agilen  Softwareentwicklung   werden   die   Anforderungen   zunächst   nur   grob   skizziert   und   im
Projektverlauf auf Grundlage regelmäßiger Zwischenergebnisse verfeinert und ergänzt. Dies erfordert eine
permanente Konkretisierung und Priorisierung der Anforderungen durch den Auftraggeber.

Frage (im Projektassistenten)

Welche   Entwicklungsmethode   (klassische   oder   agile   Softwareentwicklung)   soll   der   Auftragnehmer
einsetzen?

Antwort

Klassische SWE

Agile SWE

Erläuterung

Der Auftragnehmer soll als Entwicklungsmethode die klassische
Softwareentwicklung einsetzen.
Ausgewählte Vorgehensbausteine: Anforderungsfestlegung,
Anforderungsfestlegung (Bund)
Ausgewählte Ablaufbausteine: Steuerung des Auftragnehmers im
klassischen Softwareentwicklungsprojekt

Der Auftragnehmer soll als Entwicklungsmethode die agile
Softwareentwicklung einsetzen.
Ausgewählte Vorgehensbausteine: Agile SW-Entwicklung (AG)
Ausgewählte Ablaufbausteine: Steuerung des Auftragnehmers im agilen
Softwareentwicklungsprojekt

F.2.3 Fertigprodukte
Der Einsatz von Fertigprodukten erfordert frühzeitig in der Systementwicklung Maßnahmen zur Erfassung
der möglichen Systemelemente, die Kandidaten für Fertigprodukte sind. Zudem müssen die hierfür auf dem
Markt   existierenden   Lösungen   ermittelt   und   bewertet   werden.   Der   Einsatz   von   Fertigkomponenten   ist
besonders sinnvoll, wenn ein Projekt Komponenten beinhaltet, für die bereits viele Lösungen auf dem Markt
existieren.

Frage (im Projektassistenten)

Sollen, soweit sinnvoll und möglich, Fertigprodukte evaluiert und eingesetzt werden?

Antwort

Ja

Nein

Erläuterung

Der Einsatz von Fertigprodukten ist im Projekt erwünscht.
Ausgewählte Vorgehensbausteine: Evaluierung von Fertigprodukten

Der Einsatz von Fertigprodukten ist im Projekt nicht erwünscht.

F.2.4 Projektgegenstand
Der Projektgegenstand ist das Ergebnis, das im Projekt erarbeitet werden soll. Das Ergebnis kann dabei ein
Softwaresystem   sein   bzw.   eine   Integration   eines   neuen   (Teil-)Systems   in   eine   bereits   existierende
Infrastruktur.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

F.2 Projektmerkmale

251

Frage (im Projektassistenten)

Was ist der Entwicklungsgegenstand des Projekts?

Antwort

Software

Integration

Erläuterung

Ergebnis des Projekts ist eine Software.
Ausgewählte Vorgehensbausteine: SW-Entwicklung

Gegenstand des Projekts ist die Integration eines (Teil-)Systems in eine
bereits existierende Infrastruktur. Gegenstand der Integration ist Software.

F.2.5 Benutzerschnittstelle
Für   Systeme,   bei   denen   die   Benutzerschnittstelle   für   den   Projekterfolg   wesentlich   ist,   sind   besondere
analytische   Maßnahmen   durchzuführen  und  gestaltungstechnische  Vorgaben  zu   treffen.   Beispiele   hierfür
wären   Systeme,   die   aufgrund   der   hohen  zu   erwartenden   Nutzeranzahl   besonders   intuitiv   bedienbar   sein
müssen.

Frage (im Projektassistenten)

Ist die Benutzerschnittstelle ein Erfolgskriterium?

Antwort

Ja

Nein

Erläuterung

Die Benutzerschnittstelle ist für den Projekterfolg besonders wichtig.
Ausgewählte Vorgehensbausteine: Benutzbarkeit und Ergonomie

Die Benutzerschnittstelle ist für den Projekterfolg nicht besonders wichtig.

F.2.6 Altsystem
Das Projekt befasst sich mit der Weiterentwicklung und/oder Migration eines bestehenden (Alt-)Systems.
Der Schwerpunkt des Projekts liegt auf der Entwicklung zusätzlicher Funktionalitäten für ein existierendes
System oder dessen Ablösung.

Frage (im Projektassistenten)

Soll in diesem Projekt ein Altsystem migriert werden?

Antwort

Ja

Erläuterung

Das Projekt befasst sich mit der Weiterentwicklung und/oder Migration
eines Altsystems.
Ausgewählte Vorgehensbausteine: Weiterentwicklung und Migration von
Altsystemen

Nein

Altsysteme sind in diesem Projekt kein Betrachtungsgegenstand.

F.2.7 Prototypentwicklung
In   Projekten,   in   denen   zu   Beginn   nicht   alle   Anforderungen   festliegen,   bzw.   zur   Demonstration/zum
Nachweis von Realisierungsmöglichkeiten einer oder mehrere Prototypen erstellt werden sollen, muss dieses
Merkmal   mit   dem   Wert  Ja  belegt   werden.   Dies   hat   zur   Folge,   dass   dem   Projektleiter   mit   der

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

252

 Referenz Tailoring

Projektdurchführungsstrategie   eine   Entwicklungsstratgie   angeboten   wird,   in   der   zunächst   ohne
Spezifikation/Dokumentation schnell Prototypen realisiert werden können. Dieses Vorgehen ist als Vorstufe
z.B. für eine inkrementelle oder komponentenbasierte Entwicklung geeignet.

Frage (im Projektassistenten)

Sollen im Rahmen der Systementwicklung Prototypen erstellt werden?

Antwort

Ja

Nein

Erläuterung

Es wird die Entwicklungsstrategie Prototypische Systementwicklung zur
Verfügung gestellt, die ohne Dokumentationsaufwand die schnelle
Realisierung von Prototypen ermöglicht.
Ausgewählte Ablaufbausteine: Prototypische Systementwicklung

Es werden keine zusätzlichen Vorgehensbausteine oder Abläufe
eingebunden. Es stehen lediglich die standardmäßigen Elemente des
Projekttyps zur Verfügung.

F.2.8 Unterauftrag
Bei   AG/AN-Projekten   ist   es   möglich,   einen   oder   mehrere   Unteraufträge   zu   vergeben.   Die
Unterauftragnehmer (externe IT-Dienstleister oder IT-Dienstleister des Bundes) erstellen Teile des Systems
und liefern diese an das AG/AN-Projekt aus.

Frage (im Projektassistenten)

Sollen während der Systementwicklung Unteraufträge vergeben werden?

Antwort

Erläuterung

Ja (Externer IT-Dienstleister,
klassische SWE)

Ja (Externer IT-Dienstleister,
agile SWE)

Ja (IT-Dienstleister des
Bundes, klassische SWE)

In diesem Projekt sollen Unteraufträge an externe IT-Dienstleister vergeben
werden. Diese sollen als Entwicklungsmethode die klassische
Softwareentwicklung einsetzen.
Ausgewählte Vorgehensbausteine: Vertragsschluss (AG), Vertragsschluss
(mit externem IT-Dienstleister), Lieferung und Abnahme (AG)
Ausgewählte Ablaufbausteine: Steuerung des Auftragnehmers im
klassischen Softwareentwicklungsprojekt, Abnahme als AG, Unterauftrag

In diesem Projekt sollen Unteraufträge an externe IT-Dienstleister vergeben
werden. Diese sollen als Entwicklungsmethode die agile
Softwareentwicklung einsetzen.
Ausgewählte Vorgehensbausteine: Vertragsschluss (AG), Vertragsschluss
(mit externem IT-Dienstleister), Lieferung und Abnahme (AG)
Ausgewählte Ablaufbausteine: Abnahme als AG, Unterauftrag, Steuerung
des Auftragnehmers im agilen Softwareentwicklungsprojekt

In diesem Projekt sollen Unteraufträge an IT-Dienstleister des Bundes
vergeben werden. Diese sollen als Entwicklungsmethode die klassische
Softwareentwicklung einsetzen.
Ausgewählte Vorgehensbausteine: Vertragsschluss (AG), Vertragsschluss
(mit IT-Dienstleister des Bundes), Lieferung und Abnahme (AG)
Ausgewählte Ablaufbausteine: Steuerung des Auftragnehmers im
klassischen Softwareentwicklungsprojekt, Abnahme als AG, Unterauftrag

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

F.2 Projektmerkmale

253

Antwort

Erläuterung

Ja (IT-Dienstleister des
Bundes, agile SWE)

In diesem Projekt sollen Unteraufträge an IT-Dienstleister des Bundes
vergeben werden. Diese sollen als Entwicklungsmethode die agile
Softwareentwicklung einsetzen.
Ausgewählte Vorgehensbausteine: Vertragsschluss (AG), Vertragsschluss
(mit IT-Dienstleister des Bundes), Lieferung und Abnahme (AG)
Ausgewählte Ablaufbausteine: Abnahme als AG, Unterauftrag, Steuerung
des Auftragnehmers im agilen Softwareentwicklungsprojekt

Nein

In diesem Projekt sollen keine Unteraufträge vergeben werden.

F.2.9 Informationssicherheit und Datenschutz (AG)
Um die vom System verarbeiteten Daten und Datenflüsse zu schützen, muss der Auftraggeber Vorgaben zur
Informationssicherheit   und   zum   Datenschutz   festlegen.   Die  Checkliste   Informationssicherheit  enthält
verschiedene   Kriterien   und   Beispiele,   anhand   derer   der   Auftraggeber   die   Relevanz   von
Informationssicherheit und Datenschutz im Projekt bestimmen kann.

Frage (im Projektassistenten)

Müssen   im   Projekt   Aspekte   der   Informationssicherheit   (Security)   oder   des   Datenschutzes   (Privacy)
berücksichtigt werden?

Antwort

Ja

Nein

Erläuterung

Aspekte der Informationssicherheit und des Datenschutzes müssen in
diesem Projekt berücksichtigt werden.
Ausgewählte Vorgehensbausteine: Informationssicherheit und
Datenschutz, Informationssicherheit und Datenschutz (AG)

Aspekte der Informationssicherheit und des Datenschutzes müssen in
diesem Projekt nicht berücksichtigt werden.

F.2.10 Informationssicherheit und Datenschutz (AG/AN)
Um die vom System verarbeiteten Daten und Datenflüsse zu schützen, muss der Auftraggeber Vorgaben zur
Informationssicherheit   und   zum   Datenschutz   festlegen.   Die  Checkliste   Informationssicherheit  enthält
verschiedene   Kriterien   und   Beispiele,   anhand   derer   der   Auftraggeber   die   Relevanz   von
Informationssicherheit und Datenschutz im Projekt bestimmen kann.

Frage (im Projektassistenten)

Müssen   im   Projekt   Aspekte   der   Informationssicherheit   (Security)   oder   des   Datenschutzes   (Privacy)
berücksichtigt werden?

Antwort

Ja

Erläuterung

Aspekte der Informationssicherheit und des Datenschutzes müssen in
diesem Projekt berücksichtigt werden.
Ausgewählte Vorgehensbausteine: Informationssicherheit und
Datenschutz, Informationssicherheit und Datenschutz (AG),
Informationssicherheit und Datenschutz (AN)

Nein

Aspekte der Informationssicherheit und des Datenschutzes müssen in

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

254

Antwort

Erläuterung

diesem Projekt nicht berücksichtigt werden.

 Referenz Tailoring

F.2.11 Betriebsübergabe (AG)
Wird das System nach der Entwicklung in den IT-Betrieb überführt, muss der Auftraggeber Vorgaben zum
IT-Betrieb festlegen.

Frage (im Projektassistenten)

Wird das System nach der Entwicklung in den IT-Betrieb überführt?

Antwort

Ja

Erläuterung

Das System wird nach der Entwicklung in den IT-Betrieb überführt.
Ausgewählte Vorgehensbausteine: Betriebsübergabe (Bund),
Betriebsübergabe (AG)
Ausgewählte Ablaufbausteine: Abnahme als AG mit Inbetriebnahme

Nein

Das System wird nicht in den IT-Betrieb überführt.

F.2.12 Betriebsübergabe (AG/AN)
Wird das System nach der Entwicklung in den IT-Betrieb überführt, muss der Auftraggeber Vorgaben zum
IT-Betrieb festlegen.

Frage (im Projektassistenten)

Wird das System nach der Entwicklung in den IT-Betrieb überführt?

Antwort

Ja

Erläuterung

Das System wird nach der Entwicklung in den IT-Betrieb überführt.
Ausgewählte Vorgehensbausteine: Betriebsübergabe (Bund),
Betriebsübergabe (AG), Betriebsübergabe (AN)
Ausgewählte Ablaufbausteine: Abnahme als AG mit Inbetriebnahme,
Abnahme als AG/AN mit Inbetriebnahme

Nein

Das System wird nicht in den IT-Betrieb überführt.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

F.3 Vorgehensbausteine

255

F.3 Vorgehensbausteine

F.3.1 Projektmanagement

Zusätzliche Themen

Mitwirkungen

Lastenheft (Anforderungen):
Glossar
Pflichtenheft (Gesamtsystementwurf):
Glossar

Lenkungsausschuss:
Projektfortschrittsentscheidung
Projektleiter:
Projektfortschrittsentscheidung
Projekteigner:
Projekthandbuch, Projektplan

Gewählt bei

Immer (V-Modell-Kern)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

256

 Referenz Tailoring

F.3.2 Projektmanagement (Bund)

Zusätzliche Themen

Mitwirkungen

Projekthandbuch:
Organisation und Vorgaben zum Projektmanagement
Risikoliste:
Risikomatrix

Multi-Projektkoordination:
Projektfortschrittsentscheidung, Projektvorstudie, Projektauftrag
Personalvertretung:
Projekthandbuch, Projektauftrag

Gewählt bei

Immer (V-Modell-Kern)

F.3.3 Qualitätssicherung

Zusätzliche Themen

Mitwirkungen

Projektabschlussbericht:
Qualitätsbewertung
Projektstatusbericht:
Qualitätsbewertung

Projektleiter:
QS-Handbuch
QS-Verantwortlicher:
Projektabschlussbericht, Projektplan, Projektstatusbericht, Risikoliste
Qualitätsmanager:
QS-Handbuch

Gewählt bei

Immer (V-Modell-Kern)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

F.3 Vorgehensbausteine

257

F.3.4 Konfigurationsmanagement

Zusätzliche Themen

Mitwirkungen

Projekthandbuch:
Organisation und Vorgaben zum Konfigurationsmanagement

KM-Verantwortlicher:
Projektabschlussbericht, Projekthandbuch, Projektplan, Projektstatusbericht
Projektleiter:
Produktbibliothek

Gewählt bei

Immer (V-Modell-Kern)

F.3.5 Problem- und Änderungsmanagement

Zusätzliche Themen

Mitwirkungen

Projekthandbuch:
Organisation und Vorgaben zum Problem- und Änderungsmanagement
Projektstatusbericht:
Problem- und Änderungsstatistik

KM-Verantwortlicher:
Änderungsentscheidung, Problem-/Änderungsbewertung
Änderungsverantwortlicher:
Projektstatusbericht, Änderungsentscheidung
QS-Verantwortlicher:
Änderungsentscheidung, Problem-/Änderungsbewertung

Gewählt bei

Immer (V-Modell-Kern)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

258

 Referenz Tailoring

F.3.6 Projektcontrolling

Zusätzliche Themen

Projekthandbuch:
Organisation und Vorgaben zum Projektcontrolling

Gewählt bei

Projekttyp:
Systementwicklungsprojekt (AG), Systementwicklungsprojekt (AG/AN)

F.3.7 Wirtschaftlichkeitsbetrachtung

Mitwirkungen

Anforderungsanalytiker (AG):
WiBe (Fortschreibung)
Betriebsbeauftragter:
WiBe (Vorkalkulation)
Fachverantwortlicher:
WiBe (Vorkalkulation)
Multi-Projektkoordination:
WiBe (Vorkalkulation)

Gewählt bei

Projekttyp:
Systementwicklungsprojekt (AG), Systementwicklungsprojekt (AG/AN)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

F.3 Vorgehensbausteine

259

F.3.8 Vertragsschluss (AG)

Gewählt bei

Projekttyp:
Systementwicklungsprojekt (AG)
Projektmerkmal:
Unterauftrag (Ja (Externer IT-Dienstleister, klassische SWE); Ja (Externer IT-
Dienstleister, agile SWE); Ja (IT-Dienstleister des Bundes, klassische SWE); Ja
(IT-Dienstleister des Bundes, agile SWE))

F.3.9 Vertragsschluss (mit externem IT-Dienstleister)

Zusätzliche Themen

Projekthandbuch:
Vorgaben für das Projekthandbuch der Auftragnehmer, Organisation und
Vorgaben zur Vergabe von Entwicklungsleistungen
QS-Handbuch:
Vorgaben für das QS-Handbuch der Auftragnehmer

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

260

Mitwirkungen

Gewählt bei

 Referenz Tailoring

Anforderungsanalytiker (AG):
Kriterienkatalog, Leistungsbewertungsmatrix, Vergabeunterlagen
(Ausschreibung), Vertrag
Vergabestelle:
Beschaffungskonzeption, Kriterienkatalog, Leistungsbewertungsmatrix,
Eignungsbewertungsmatrix, Vergabeunterlagen (Ausschreibung), Vertrag,
Vertragszusatz
Projektleiter:
Kriterienkatalog, Leistungsbewertungsmatrix, Eignungsbewertungsmatrix,
Vergabeunterlagen (Ausschreibung), Vertrag
Projekteigner:
Kriterienkatalog, Leistungsbewertungsmatrix, Eignungsbewertungsmatrix,
Vergabeunterlagen (Ausschreibung)
Ausschreibungs- und Vertragsverantwortlicher:
Anforderungsbewertung

Projektmerkmal:
Auftragnehmer (Externer IT-Dienstleister), Unterauftrag (Ja (Externer IT-
Dienstleister, klassische SWE); Ja (Externer IT-Dienstleister, agile SWE))

F.3.10 Vertragsschluss (mit IT-Dienstleister des Bundes)

Zusätzliche Themen

Gewählt bei

Projekthandbuch:
Organisation und Vorgaben zur Beauftragung eines IT-Dienstleisters des Bundes

Projektmerkmal:
Auftragnehmer (IT-Dienstleister des Bundes), Unterauftrag (Ja (IT-Dienstleister
des Bundes, klassische SWE); Ja (IT-Dienstleister des Bundes, agile SWE))

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

F.3 Vorgehensbausteine

261

F.3.11 Anforderungsfestlegung

Mitwirkungen

Anwender:
Lastenheft (Anforderungen), Anforderungsbewertung, Abnahmeprotokoll
Projektleiter:
Lastenheft (Anforderungen), Anforderungsbewertung
Projekteigner:
Lastenheft (Anforderungen), Anforderungsbewertung
Fachverantwortlicher:
Lastenheft (Anforderungen), Anforderungsbewertung
Verfahrensverantwortlicher (Fachseite):
Lastenheft (Anforderungen), Anforderungsbewertung

Gewählt bei

Projekttyp:
Systementwicklungsprojekt (AG/AN)
Projektmerkmal:
Entwicklungsmethode (Klassische SWE)

F.3.12 Anforderungsfestlegung (Bund)
Der Vorgehensbaustein enthält keine Produkte.

Zusätzliche Themen

Projekthandbuch:
Organisation und Vorgaben zum Anforderungsmanagement
Lastenheft Gesamtprojekt:
Ausgangssituation und Zielsetzung, Funktionale Anforderungen, Nicht-
Funktionale Anforderungen, Skizze des Lebenszyklus und der
Gesamtsystemarchitektur, Lieferumfang, Abnahmekriterien
Lastenheft (Anforderungen):
Ausgangssituation und Zielsetzung, Funktionale Anforderungen, Nicht-
Funktionale Anforderungen, Skizze des Lebenszyklus und der
Gesamtsystemarchitektur, Lieferumfang, Abnahmekriterien

Mitwirkungen

Gewählt bei

Geschäftsprozessmanager:
Lastenheft (Anforderungen)

Projekttyp:
Systementwicklungsprojekt (AG/AN)
Projektmerkmal:
Entwicklungsmethode (Klassische SWE)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

262

 Referenz Tailoring

F.3.13 Multi-Projektmanagement

Zusätzliche Themen

Mitwirkungen

Projekthandbuch:
Teilprojekte
Projektstatusbericht:
Gesamtprojektfortschritt
Lastenheft (Anforderungen):
Anforderungsverfolgung zu den Anforderungen (Lastenheft Gesamtprojekt)

Anwender:
Bewertung Lastenheft Gesamtprojekt, Lastenheft Gesamtprojekt
Projektleiter:
Bewertung Lastenheft Gesamtprojekt, Lastenheft Gesamtprojekt
Projekteigner:
Bewertung Lastenheft Gesamtprojekt, Lastenheft Gesamtprojekt
Fachverantwortlicher:
Bewertung Lastenheft Gesamtprojekt, Lastenheft Gesamtprojekt

Gewählt bei

Projekttypvariante:
AG-Projekt mit mehreren Auftragnehmern

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

F.3 Vorgehensbausteine

263

F.3.14 Systemerstellung

Zusätzliche Themen

Projekthandbuch:
Organisation und Vorgaben zur Systemerstellung

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

264

Mitwirkungen

 Referenz Tailoring

Vergabestelle:
Externe Einheit, Make-or-Buy-Entscheidung
Projekteigner:
Make-or-Buy-Entscheidung
Prüfer:
Externe-Einheit-Spezifikation, Pflichtenheft (Gesamtsystementwurf),
Implementierungs-, Integrations- und Prüfkonzept System, Systemspezifikation
QS-Verantwortlicher:
Ausbildungsunterlagen, Pflichtenheft (Gesamtsystementwurf),
Implementierungs-, Integrations- und Prüfkonzept System,
Nutzungsdokumentation
Systemarchitekt:
Projekthandbuch, Projektplan, Änderungsentscheidung,
Problem-/Änderungsbewertung, Ausbildungsunterlagen, Pflichtenheft
(Gesamtsystementwurf), Make-or-Buy-Entscheidung, Nutzungsdokumentation,
Prüfspezifikation Systemelement
Systemintegrator:
Externe-Einheit-Spezifikation, Pflichtenheft (Gesamtsystementwurf),
Implementierungs-, Integrations- und Prüfkonzept System, Make-or-Buy-
Entscheidung, Prüfprotokoll Systemelement, Prüfprozedur Systemelement,
Prüfspezifikation Systemelement, Systemspezifikation, Abnahmeprotokoll,
Lieferung

Gewählt bei

Projekttyp:
Systementwicklungsprojekt (AG/AN)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

F.3 Vorgehensbausteine

265

F.3.15 SW-Entwicklung

Mitwirkungen

Vergabestelle:
Externes SW-Modul
Prüfer:
Externes-SW-Modul-Spezifikation, Implementierungs-, Integrations- und
Prüfkonzept SW, SW-Spezifikation
QS-Verantwortlicher:
Implementierungs-, Integrations- und Prüfkonzept SW
SW-Architekt:
Änderungsentscheidung, Problem-/Änderungsbewertung, Ausbildungsunterlagen,
Externe-Einheit-Spezifikation, Implementierungs-, Integrations- und Prüfkonzept
System, Make-or-Buy-Entscheidung, Nutzungsdokumentation, Prüfspezifikation
Systemelement, Systemarchitektur
SW-Entwickler:
Ausbildungsunterlagen, Nutzungsdokumentation, Prüfprotokoll Systemelement,
Datenbankentwurf, Externes-SW-Modul-Spezifikation, Implementierungs-,
Integrations- und Prüfkonzept SW, SW-Architektur, SW-Spezifikation
Systemarchitekt:
SW-Architektur
Systemintegrator:
SW-Architektur

Gewählt bei

Projektmerkmal:
Projektgegenstand (Software)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

266

 Referenz Tailoring

F.3.16 Agile SW-Entwicklung (AG)

Gewählt bei

Projektmerkmal:
Entwicklungsmethode (Agile SWE)

F.3.17 Evaluierung von Fertigprodukten

Zusätzliche Themen

Mitwirkungen

Projekttagebuch:
Erfahrungen mit Fertigprodukten
QS-Handbuch:
Vorgaben für die Prüfspezifikation von Fertigprodukten
Make-or-Buy-Entscheidung:
Evaluierung der Fertigprodukte

Anforderungsanalytiker (AG):
Marktsichtung für Fertigprodukte
Vergabestelle:
Marktsichtung für Fertigprodukte
Systemarchitekt:
Marktsichtung für Fertigprodukte
Systemintegrator:
Marktsichtung für Fertigprodukte

Gewählt bei

Projektmerkmal:
Fertigprodukte (Ja)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

F.3 Vorgehensbausteine

267

F.3.18 Benutzbarkeit und Ergonomie

Mitwirkungen

Anwender:
Anwenderaufgabenanalyse
Ergonomieverantwortlicher:
Externe-Einheit-Spezifikation, Pflichtenheft (Gesamtsystementwurf),
Nutzungsdokumentation, Prüfspezifikation Systemelement, Systemspezifikation,
Externes-SW-Modul-Spezifikation, SW-Spezifikation
Anforderungsanalytiker (AN):
Anwenderaufgabenanalyse
Technischer Autor:
Anwenderaufgabenanalyse

Gewählt bei

Projektmerkmal:
Benutzerschnittstelle (Ja)

F.3.19 Weiterentwicklung und Migration von Altsystemen

Mitwirkungen

Gewählt bei

Systemintegrator:
Migrationskonzept

Projektmerkmal:
Altsystem (Ja)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

268

 Referenz Tailoring

F.3.20 Informationssicherheit und Datenschutz

Zusätzliche Themen

Mitwirkungen

Gewählt bei

Projekthandbuch:
Organisation und Vorgaben zu Informationssicherheit und Datenschutz,
Organisation und Vorgaben zum Informationssicherheits-Managementsystem
Projektstatusbericht:
Sicherheitsrisiken
Abnahmeerklärung:
Bestätigung der Risikobehandlung

Informationssicherheitsverantwortlicher:
Projekthandbuch, Abnahmeerklärung
Datenschutzverantwortlicher:
Projekthandbuch

Projektmerkmal:
Informationssicherheit und Datenschutz (AG) (Ja), Informationssicherheit und
Datenschutz (AG/AN) (Ja)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

F.3 Vorgehensbausteine

269

F.3.21 Informationssicherheit und Datenschutz (AG)

Zusätzliche Themen

Mitwirkungen

Prüfspezifikation Inbetriebnahme:
Prüfkriterien für die Erweiterung der Vorgaben zur Informationssicherheit,
Prüfkriterien für die Erweiterung der Vorgaben zum Datenschutz
Betriebliche Freigabeerklärung:
Beurteilung des Systems aus Sicht der Informationssicherheit, Beurteilung des
Systems aus Sicht des Datenschutzes

Informationssicherheitsverantwortlicher:
Lastenheft Gesamtprojekt, Lastenheft (Anforderungen),
Schutzbedarfsfeststellung, Abnahmeprotokoll, Abnahmespezifikation
Datenschutzverantwortlicher:
Lastenheft Gesamtprojekt, Lastenheft (Anforderungen),
Schutzbedarfsfeststellung, Vorgaben zur Informationssicherheit,
Abnahmeprotokoll, Abnahmespezifikation
Informationssicherheitsbeauftragter:
Vorgaben zur Informationssicherheit
Datenschutzbeauftragter:
Vorgaben zum Datenschutz

Gewählt bei

Projektmerkmal:
Informationssicherheit und Datenschutz (AG) (Ja), Informationssicherheit und
Datenschutz (AG/AN) (Ja)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

270

 Referenz Tailoring

F.3.22 Informationssicherheit und Datenschutz (AN)

Zusätzliche Themen

Mitwirkungen

Systemarchitektur:
Informationssicherheits- und datenschutzkritische Systemelemente
SW-Architektur:
Informationssicherheits- und datenschutzkritische SW-Elemente

SW-Architekt:
Sicherheitskonzeption
Systemarchitekt:
Sicherheitskonzeption
Informationssicherheitsverantwortlicher:
Pflichtenheft (Gesamtsystementwurf), Systemarchitektur, SW-Architektur
Datenschutzverantwortlicher:
Pflichtenheft (Gesamtsystementwurf), Systemarchitektur, SW-Architektur,
Sicherheitskonzeption, Erweiterung der Vorgaben zur Informationssicherheit

Gewählt bei

Projektmerkmal:
Informationssicherheit und Datenschutz (AG/AN) (Ja)

F.3.23 Betriebsübergabe (Bund)

Mitwirkungen

Anwender:
Leistungsvereinbarung (SLA/OLA/UC)
Verfahrensverantwortlicher (Fachseite):
Leistungsvereinbarung (SLA/OLA/UC)
Verfahrensverantwortlicher (IT-Betrieb):
Leistungsvereinbarung (SLA/OLA/UC)
Verfahrensverantwortlicher (Weiterentwicklung):
Leistungsvereinbarung (SLA/OLA/UC)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

F.3 Vorgehensbausteine

Gewählt bei

Projektmerkmal:
Betriebsübergabe (AG) (Ja), Betriebsübergabe (AG/AN) (Ja)

271

F.3.24 Betriebsübergabe (AG)

Zusätzliche Themen

Projekthandbuch:
Organisation und Vorgaben zum IT-Betrieb

Mitwirkungen

Betriebsbeauftragter:
Vorgaben zum IT-Betrieb
Betriebsverantwortlicher:
Projekthandbuch, Lastenheft Gesamtprojekt, Lastenheft (Anforderungen),
Abnahmeprotokoll, Abnahmespezifikation
Verfahrensverantwortlicher (Fachseite):
Projektabschlussbericht
Verfahrensverantwortlicher (IT-Betrieb):
Projektabschlussbericht
Verfahrensverantwortlicher (Weiterentwicklung):
Projektabschlussbericht

Gewählt bei

Projektmerkmal:
Betriebsübergabe (AG) (Ja), Betriebsübergabe (AG/AN) (Ja)

F.3.25 Betriebsübergabe (AN)

Zusätzliche Themen

Systemarchitektur:
Auswirkungen auf den IT-Betrieb
SW-Architektur:
Auswirkungen auf den IT-Betrieb

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

272

Mitwirkungen

Gewählt bei

 Referenz Tailoring

Betriebsverantwortlicher:
Pflichtenheft (Gesamtsystementwurf), Systemarchitektur, SW-Architektur,
Sicherheitskonzeption

Projektmerkmal:
Betriebsübergabe (AG/AN) (Ja)

F.3.26 Lieferung und Abnahme (AG)

Mitwirkungen

Gewählt bei

Vergabestelle:
Abnahmeerklärung
Projektleiter:
Abnahmeerklärung
QS-Verantwortlicher:
Abnahmeerklärung
Ausschreibungs- und Vertragsverantwortlicher:
Abnahmeerklärung

Projekttyp:
Systementwicklungsprojekt (AG), Systementwicklungsprojekt (AG/AN)
Projektmerkmal:
Unterauftrag (Ja (Externer IT-Dienstleister, klassische SWE); Ja (Externer IT-
Dienstleister, agile SWE); Ja (IT-Dienstleister des Bundes, klassische SWE); Ja
(IT-Dienstleister des Bundes, agile SWE))

F.3.27 Lieferung und Abnahme (AN)

Zusätzliche Themen

Gewählt bei

QS-Handbuch:
Organisation und Vorgaben zur Qualitätssicherung der Auslieferung

Projekttyp:
Systementwicklungsprojekt (AG/AN)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

F.4 Tailoringindex

273

F.4 Tailoringindex
Modellelement

Typ

Seite

AG/AN-Projekt mit Entwicklung, Weiterentwicklung oder Migration Projekttypvariante

AG/AN-Projekt mit Wartung und Pflege

Agile SW-Entwicklung (AG)

AG-Projekt mit einem Auftragnehmer

AG-Projekt mit mehreren Auftragnehmern

Altsystem

Anforderungsfestlegung

Anforderungsfestlegung (Bund)

Auftragnehmer

Benutzbarkeit und Ergonomie

Benutzerschnittstelle

Betriebsübergabe (AG/AN)

Betriebsübergabe (AG)

Betriebsübergabe (AG)

Betriebsübergabe (AN)

Betriebsübergabe (Bund)

Entwicklungsmethode

Evaluierung von Fertigprodukten

Fertigprodukte

Informationssicherheit und Datenschutz

Informationssicherheit und Datenschutz (AG/AN)

Informationssicherheit und Datenschutz (AG)

Informationssicherheit und Datenschutz (AG)

Informationssicherheit und Datenschutz (AN)

Konfigurationsmanagement

Lieferung und Abnahme (AG)

Lieferung und Abnahme (AN)

Multi-Projektmanagement

Projekttypvariante

Vorgehensbaustein

Projekttypvariante

Projekttypvariante

Projektmerkmal

Vorgehensbaustein

Vorgehensbaustein

Projektmerkmal

Vorgehensbaustein

Projektmerkmal

Projektmerkmal

Projektmerkmal

Vorgehensbaustein

Vorgehensbaustein

Vorgehensbaustein

Projektmerkmal

Vorgehensbaustein

Projektmerkmal

Vorgehensbaustein

Projektmerkmal

Projektmerkmal

Vorgehensbaustein

Vorgehensbaustein

Vorgehensbaustein

Vorgehensbaustein

Vorgehensbaustein

Vorgehensbaustein

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

248

249

266

246

246

251

261

261

249

267

251

254

254

271

271

270

250

266

250

268

253

253

269

270

257

272

272

262

274

Modellelement

Problem- und Änderungsmanagement

Projektcontrolling

Projektgegenstand

Projektmanagement

Projektmanagement (Bund)

Prototypentwicklung

Qualitätssicherung

SW-Entwicklung

Systementwicklungsprojekt (AG/AN)

Systementwicklungsprojekt (AG)

Systemerstellung

Unterauftrag

Vertragsschluss (AG)

Vertragsschluss (mit externem IT-Dienstleister)

Vertragsschluss (mit IT-Dienstleister des Bundes)

Weiterentwicklung und Migration von Altsystemen

Wirtschaftlichkeitsbetrachtung

 Referenz Tailoring

Typ

Seite

Vorgehensbaustein

Vorgehensbaustein

Projektmerkmal

Vorgehensbaustein

Vorgehensbaustein

Projektmerkmal

Vorgehensbaustein

Vorgehensbaustein

Projekttyp

Projekttyp

Vorgehensbaustein

Projektmerkmal

Vorgehensbaustein

Vorgehensbaustein

Vorgehensbaustein

Vorgehensbaustein

Vorgehensbaustein

257

258

250

255

256

251

256

265

247

246

263

252

259

259

260

267

258

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

G Referenz Arbeitshilfen

275

G Referenz Arbeitshilfen

G.1 Methoden und Werkzeuge

G.1.1 Methodenreferenzen

G.1.1.1 Anforderungsanalyse

Ziel   der   Anforderungsanalyse   ist   die   Identifikation,   die   Beschreibung   und   die   Qualitätssicherung   von
Anforderungen. Die Anforderungsanalyse kann mit folgenden Methoden durchgeführt werden:

Anwendungsfall-Modellierung

Zielsetzung der Methode ist die Erfassung und Darstellung der aus Sicht von externen Bedienungseinheiten
(Akteure)   an   ein   System   gestellten   funktionalen  Anforderungen.   Die  Anforderungen   sind   in   Form   von
Anwendungsfällen,   den   "Use   Cases",   zu   beschreiben.   Ein   Anwendungsfall   kann   in   einer   Reihe   von
Szenarios   konkretisiert   werden.   Externe   Bedienungseinheiten   (z.B.   Mitarbeiter,
 Projektleiter  oder
Administrator)   repräsentieren  Rolle
 n  ,   die   von   konkreten   Personen,   Maschinen,   Computer-"Tasks"   oder
anderen Systemen eingenommen werden können.

Ein   Anwendungsfall   wird   durch   eine   Bedienungseinheit   ausgelöst.   Seine   Beschreibung   beinhaltet   die
Dialoge   beziehungsweise   Interaktionen,   die   zur   Bearbeitung   einer   Aufgabe   zwischen   dieser
Bedienungseinheit und dem System "gefordert" werden. Für die Beschreibung der Interaktionen wird eine
Folge von Aktionen und Ereignissen festgelegt, die von der initiierenden Bedienungseinheit, dem System
oder anderen Bedienungseinheiten ausgelöst werden. Es sind nur die Aktionen beziehungsweise Ereignisse
festzulegen, die aus der Sicht der Bedienungseinheit erkennbar sind, nicht aber Details, die beschreiben, wie
das System intern arbeiten soll.

Die   für   ein   System   spezifizierten   Anwendungsfälle   repräsentieren   in   ihrer   Gesamtheit   die
anwendungsorientierten, funktionalen Anforderungen an das System. Damit die Beschreibung vollständig ist,
sollten möglichst alle erkannten Anwendungsfälle in dieser Form spezifiziert werden.

Interviewtechnik

Eine   Möglichkeit   der   Anforderungsermittlung   ist   die   Interviewtechnik.   Hierbei   werden   die   künftigen
Anwender in einem vorgegebenen und formalisierten Verfahren befragt. Mit dieser Interviewtechnik soll es
möglich   sein,   unterschiedliche   Gruppen   zu   bilden   und   schwer   quantifizierbare,   quantifizierbare   und
ergänzende   Nutzenpotenziale   abzufragen.   Bei   einem   solchen   Vorgehen   ist   es   unerlässlich,   dass   für   die
Quantifizierung der Nutzenspotenziale alle betroffenen Bereiche einbezogen sind und aktiv mitwirken. Ohne
diese  Mitarbeit  lassen sich vorab zwar fiktive Werte annehmen,  diese können aber von den betroffenen
Bereichen   nachträglich   sehr   leicht   in   Frage   gestellt   werden.   Eine   definierte   Interviewmethode   ist   die
"Structured Hierarchical Interviewing for Requirement Analysis" (SHIRA). Sie setzt zu einem sehr frühen
Zeitpunkt   an.   SHIRA  versucht,   die   konkrete   Bedeutung  der   Produktattribute   wie   "einfach",   "innovativ",
"kontrollierbar" oder "eindrucksvoll" für ein mögliches Softwareprodukt zu verstehen.

Dialog Design Modellierung

Ziel der "Dialog Design Modellierung" ist es, die Struktur eines Nutzerdialogs mit Bildschirmmasken zu
modellieren.   Das   Layout   der   Bildschirmmasken   bleibt   hierbei   unberücksichtigt.   Die   Masken   können
lediglich typisiert werden (z.B. Typ: Eingabemaske).

Systemverhaltensmodelle

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


276

 Referenz Arbeitshilfen

Ziel der Erstellung von Systemverhaltensmodellen ist es, die Anforderungen an das dynamische Verhalten
eines Systems mittels eines Modells zu präzisieren. Besondere Beachtung finden hierbei der Einfluss von
(externen) Ereignissen auf das System sowie mögliche Nebenläufigkeiten innerhalb des Systems. Dieses
Modell   dient   insbesondere   dem  Abgleich   mit   den  Anforderungen   des  Anwenders   und   der   Präzisierung
bezüglich Vollständigkeit, Eindeutigkeit, etc.

Kosten-Nutzen-Analyse bei Anforderungen

Bei der Anforderungsanalyse wird häufig eine Kosten-Nutzen-Analyse zur Priorisierung der Anforderungen
durchgeführt. Hier bei handelt es sich um eine Untersuchung mit dem Ziel, eine Empfehlung auszusprechen,
ob der zu erwartende Nutzen der Realisierung einer Anforderung die zu erwartenden Kosten rechtfertigt.
Damit können Anforderungen nachgeordneter Bedeutung leichter eliminiert werden.

Einsatz von Kreativitätstechniken

Um der Heterogenität der verschiedenen Beteiligten in der Anforderungsermittlung erfolgreich begegnen zu
können, müssen manchmal ungewöhliche Wege gegangen werden. Kreativitätstechniken dienen dem Zweck,
dem   Denken   in   herkömmlichen   Bahnen   den   Rücken   zu   kehren   und   ungewöhnliche,   kreative   Ideen   zu
ermöglichen. Kreativitätstechniken eignen sich nicht für die Ermittlung einer detaillierten Beschreibung des
präzisen Verhaltens eines Systems. Statt dessen dienen sie dem Durchbrechen von Schranken, die die eigene
Denkweise und die Fremdartigkeit anderer Denkweisen der Anforderungsermittlung aufzwingen können.

Folgende Kreativitätstechniken können je nach Situation in Frage kommen:

➢ Brainstorming,

➢ Brainstorming paradox (es werden Ereignisse gesammtelt, die nicht erreicht werden sollen),

➢ Methode 6-3-5 (schriftliches Brainstorming: 6 Teilnehmer entwickeln jeweils 3 Ideen, diese werden

5 mal herumgereicht bis jeder Teilnehmer jede Karte einmal besessen hat),

➢ Wechsel   der   Perspektive   (jeder   Teilnehmer   betrachtet   das   Problem   aus   einer   unterschiedlichen,

vorher deefinierten Perspektive heraus),

➢ Walt   Disney  Methode   (Einteilung der  Teilnehmer   in die   Gruppen Träumer/Visionär,  Realist   und

Kritiker),

➢ Bionik/Bisoziation (finden von passenden Assoziationen zum Problem und Diskussion möglicher

Lösungsmöglichkeiten für das Analogon).

Einsatz von Beobachtungstechniken

Der Anwender weiß am besten darüber Bescheid, welche Aufgaben in seinem Tagesgeschäft anfallen und
wie sie bestritten werden können. Häufig zeigt sich jedoch, dass der Anwender aus verschiedenen Gründen
bewusst   oder   unbewusst   keine   passende   Beschreibung   seiner  Tätigkeiten  liefert.   Beobachtungstechniken
dienen   dem   Zweck,   dem  Anforderungsanalytiker   Einblick   in   die  Welt   des  Anwenders   zu   bieten.   Diese
Techniken   können   sehr   zeitaufwändig   sein,   allerdings   bieten   sie   das   Potential,   dass   der
Anforderungsanalytiker   die   anfallenden  Aufgaben   wirklich   verstehen   und   eigene  Anforderungen   an   ein
System zur Unterstützung dieser Aufgaben stellen kann.

Folgende Beobachtungstechniken können angewandt werden:

➢ Feldbeobachtung (der Anforderungsanalytiker beobachtet die Anwender bei seiner täglichen Arbeit),

➢ Apprenticing (der Anforderungsanalytiker erlernt die Tätigkeiten des Anwenders und wendet sie an).

Produkte

Lastenheft (Anforderungen), Externe-Einheit-Spezifikation, Pflichtenheft
(Gesamtsystementwurf), Systemspezifikation, Externes-SW-Modul-
Spezifikation, Projektvorstudie

Quellen

Coc00, Rup04

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

G.1 Methoden und Werkzeuge

G.1.1.2 Bewertungsverfahren

277

Im Rahmen von IT-Projekten ergibt sich immer öfter der Bedarf nach Verfahren, mit denen Vorgaben wie die
Anforderungen aus dem Lasten- oder Pflichtenheft oder die Evaluierung von Fertigprodukten nach möglichst
transparenten und nachvollziehbaren Kriterien qualitativ wie quantitativ bewertet werden können. Im Laufe
der letzten 10 Jahre haben sich hierfür einige Standardbausteine herauskristallisiert.

Weighted Scoring Model (WSM)

Einer dieser Standardbausteine ist das gewichtende Bewertungsmodell (WSM) [Schw04]. In einem ersten
Schritt   werden   hierbei   Bewertungskriterien   definiert,   die   dann   nach   Bedeutung   für   das   Gesamtsystem
gewichtet werden (z.B. essentiell, sehr wichtig, wichtig, nice-to-have, oder 10, 7, 5 oder 3 Punkte). In der
Evaluierung   wird   der   Erfüllungsgrad   der   einzelnen   Kriterien   festgehalten,   z.B.   70%.   Durch   die
Multiplikation des Erfüllungsgrades mit der Punktzahl pro Kriterium ergibt sich das Bewertungsresultat, z.B.
70%   *   7   Punkte   =   4,9   Punkte.   Die   Summe   aller   bewerteten   Kriterien   ergibt   die   Bewertung   des
Bewertungsgegenstands,   die   dann   mit   den   Ergebnissen   der   anderen   Punkte   verglichen   werden   kann.
Zusätzlich  können  noch  Mindestpunktzahlen  definiert   werden,   bei   deren  Unterschreiten  durch  sämtliche
Teilaspekte entsprechende Folgerungen für das Gesamtprojekt eintreten (wenn dies etwa für Fertigprodukte
ergibt,   dass   ein   Zukauf   keine   realistische   Möglichkeit   mehr   darstellt,   sondern   nur   noch   die
Individualentwicklung als gangbarer Weg bleibt).

Analytic Hierarchy Process (AHP)

Ähnlich ist das AHP-Verfahren, dass ebenfalls auf einer Entscheidungsmatrix beruht. Die Kriterien werden
in   Hierarchieebenen   der   Relevanz   entsprechend   angeordnet   und   paarweise   miteinander   verglichen   und
ausgewertet (s.u.a. Kon96).

Beiden Methoden, aber insbesondere dem AHP, ist das Risiko gemein, dass das Gesamtmodell durch falsche
Gewichtungen in sich inkonsistent wird und somit seine Aussagekraft verliert. Auch in Hinsicht auf den mit
der Evaluierung verbundenen Aufwand sollte also immer darauf geachtet werden, dass sich die Komplexität
des Modells in Grenzen hält.

Sonderfall COTS-Software

Ziel   der   Evaluierung   von   Standardsoftware   bzw.   Softwarekomponenten   ist   es,   Vergleichsmethoden   und
-kriterien zu finden und anzuwenden, die die Bewertung und Auswahl von Fertigprodukten ermöglichen.
Dies ist ein Thema, das seit etwa 1990 international diskutiert wird, seitdem zunehmend nicht mehr die
individuellen Systementwicklungen, sondern der Einsatz und die Integration von Standardapplikationen im
Vordergrund des kommerziellen IT-Einsatzes stehen.

Transaktionskostenanalyse

Generell wurde das Thema zunächst im Bereich der Industrieproduktion akut, aber bald auch für den IT-
Bereich übernommen: ist es kostengünstiger und effektiver, ein Teil- oder Endprodukt selbst zu fertigen oder
zuzukaufen?   Hierzu   wurde   die   Transaktionskostentheorie   (TCT)   [Wil75,  Wan02]   entwickelt,   die   die
einzelnen  Komponenten zunächst  danach bemisst,  wie  spezifisch  sie  für  den fraglichen Prozess  sind:  je
spezifischer, desto eher empfiehlt sich die Eigenproduktion und je weniger spezifisch, umso sinnvoller ist der
Zukauf. Zum zweiten werden die  Unwägbarkeiten, die Risiken, bewertet, gefolgt von der  Häufigkeit  des
Einsatzes und der Reputation des Anbieters als Kriterien für die Eigen- oder Fremdproduktion.

Zwischenzeitlich   entstand   eine   Vielzahl   von   Modellen,   die   Kombinationen   unterschiedlicher
Bewertungsverfahren propagieren [als kleine Auswahl s. Kon96 , PD99, LMTC01 , AF02].

Produkte

Quellen

Anforderungsbewertung, Make-or-Buy-Entscheidung, Marktsichtung für
Fertigprodukte, Projektvorstudie, Leistungsbewertungsmatrix

AF02, Kon96, LMTC01, PD99, Schw04, Wan02, Wil75

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

278

 Referenz Arbeitshilfen

G.1.1.3 Datenbankmodellierung

Die Datenbankmodellierung setzt sich dabei aus mehreren Teilmethoden zusammen:

ER-Modellierung:  Bei   der   Entity-Relationship-Modellierung   (ER-Modellierung)   wird   im   Rahmen   einer
vorgegebenen Aufgabenstellung ein Datenmodell erstellt, das sich im Allgemeinen allein an den fachlichen
Gegebenheiten   und   an   der   Sicht   der  Anwender,   nicht   an   der   IT-Realisierung,   orientiert.   Ziel   der   ER-
Modellierung ist es, die Objekte, die durch Daten in einem informationsverarbeitenden System repräsentiert
werden und ihre Beziehungen untereinander zu beschreiben. Die Erstellung eines ER-Modells erfolgt in
einer   Top-down-Vorgehensweise,   bei   der   in   jedem   Entwurfsschritt   detailliertere,   verfeinerte   Strukturen
entstehen. Das Darstellungsmittel der ER-Modellierung ist das ER-Diagramm. Ein ER-Diagramm besteht im
Wesentlichen aus:

➢ Der   Darstellung   von   Entitätstypen,   Beziehungstypen,   Kardinalitäten   durch   entsprechend

unterschiedliche grafische Symbole, und

➢ Der Angabe der Namen aller Entitätstypen und Beziehungstypen im Diagramm.

Data Navigation Modelling: Die Methode "Data Navigation Modelling" dient dazu, aus einem ER-Modell
eine   am   Datenbankmanagementsystem   ausgerichtete   Datenstruktur   zu   erstellen.   Insbesondere   für   die
Erstellung   leistungsfähiger,   hierarchischer   und   netzwerkartiger   Datenbankstrukturen   ist   Data   Navigation
Modelling hilfreich.

Normalisierung:  Ziel   der   "Normalisierung"   ist   die   Bildung   von   Datenstrukturen   (Entitätstypen   mit
Attributen), so dass gewisse Gesetzmäßigkeiten, sogenannte Normalisierungsregeln, eingehalten werden, die
unter anderem Folgendes bewirken:

➢ Elimination von Redundanzen,

➢ Elimination von Anomalien, die beim Einfügen, Löschen oder bei der Modifikation von Daten in

Datenstrukturen auftreten können.

Produkte

Quellen

Datenbankentwurf

KE04

G.1.1.4 Designverifikation

Ziel der Designverifikation ist es, mathematisch exakt nachzuweisen, dass die verfeinerte Spezifikation die
Anforderungen der Ausgangsspezifikation weiterhin erfüllt. Sie weist mit den Mitteln der formalen Logik
nach, dass eine formale Spezifikation (Feinspezifikation) die Verfeinerung einer Ausgangsspezifikation ist
und alle Anforderungen an die Ausgangsspezifikation ebenfalls erfüllt. Eine Spezifikation wird durch weitere
Detaillierung und Konkretisierung der Aussagen und Bedingungen verfeinert.

Die Designverifikation kann mit folgenden Methoden durchgeführt werden:

Software Architecture Analysis Method (SAAM)

SAAM   ist   eines   der   einfacheren   Verfahren   zur   szenariobasierten  Architekturbewertung,   das   als   erstes
publiziert   wurde.   SAAM   eignet   sich   zur   Untersuchung   von   Softwarearchitekturen   im   Hinblick   auf
Qualitätsattribute (qualitative Anforderungen) wie

➢ Modifizierbarkeit,

➢ Portierbarkeit,

➢ Erweiterbarkeit,

➢ Performance,

➢ Verlässlichkeit,

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

G.1 Methoden und Werkzeuge

279

aber   auch   zur   Evaluation   des   Funktionsumfangs   (funktionale  Anforderungen)   einer   Softwarearchitektur.
Grundsätzlich   werden   bei   einer   SAAM-Bewertung   Szenarios   entworfen,   priorisiert   und   den   von   ihnen
betroffenen Teilen der zu untersuchenden Softwarearchitektur zugeordnet. Bereits dies kann auf Probleme in
der Architektur hinweisen.

Architecture Tradeoff Analysis Method (ATAM)

Mit ATAM werden die Design-Entscheidungen der Architektur überprüft. Es wird überprüft, ob die Design-
Entscheidungen   die   Qualitätsanforderungen   in   zufrieden   stellender  Weise   unterstützen.   Die   Risiken   und
Kompromisse in der Architektur werden identifiziert und dokumentiert.

Der Prozess läuft in zwei Phasen ab. In der ersten Phase werden die notwendigen Bestandteile präsentiert.
Danach wird die Architektur untersucht und analysiert. In der zweiten Phase wird getestet, ob die Analyse
und die Untersuchung richtig und vollständig waren. Danach werden die Ergebnisse zusammengefasst.

Produkte

Quellen

Systemarchitektur, SW-Architektur

THE03

G.1.1.5 Geschäftsprozessmodellierung

Ziel der Geschäftsprozessmodellierung ist die Spezifikation von Geschäftsprozessen und deren Optimierung.
Die Geschäftsprozessmodellierung kann durch folgende Methoden durchgeführt werden:

Geschäftsprozessoptimierung

In einem Geschäftsprozess sollen die Ziele Dritter (Kunden, Bürger etc.) erfüllt werden und diese deshalb
auch zu Prozess-"Beteiligten" gemacht werden. Wesentliche Merkmale eines Geschäftsprozesses sind:

➢ die Kundenorientierung (hier sind auch verwaltungsinterne "Kunden" gemeint) und

➢ die Erreichung eines Nutzeneffekts (für den Kunden und die Organisation selbst).

Es gibt zwei grundsätzlich unterschiedliche Ansätze für die Geschäftsprozessoptimierung:

➢ der radikale Weg des Business (Process)Reengineering (BPR) nach Hammer und Champy und

➢ die behutsamere Vorgehensweise des Kontinuierlichen Verbesserungsprozesses (KVP).

Business Reengineering

Das Business Reengineering nach Hammer und Champy ist ein fundamentales Überdenken und radikales
Umgestalten   von   Unternehmen   oder   wesentlichen   Unternehmensprozessen.   Dabei   bedeutet   fundamental,
dass die Frage des "Was und Warum" vor dem "Wie" stehen muss. Außerdem soll sich die Reorganisation
nicht   nur   auf   Teilbereiche,   sondern   auf   das   ganze   Unternehmen   oder   zumindest   auf   die   wesentlichen
Unternehmensprozesse beziehen. "Radikal" bedeutet für Hammer und Champy, dass im Prinzip "ganz von
vorne" angefangen wird und bestehende Abläufe und Strukturen grundsätzlich in Frage zu stellen sind. Der
Ansatz   bietet   wichtige   Ideen,   Methoden   und   Denkanstöße,   die   auch   bei   allen   anderen   Formen   der
(Unternehmens-)Reorganisation von Bedeutung sind beziehungsweise sein können.

Kontinuierlicher Verbesserungsprozess (KVP)

Die Theorie des KVP ist die europäische Variante des so genannten japanischen Weges  (KAIZEN). Sie
beschreibt   eine   systematische   Vorgehensweise   zum   Erkennen   und   Beseitigen   von   Verschwendung   von
Ressourcen sowie zur Verbesserung der Arbeitsprozesse und des Arbeitsumfeldes. Nach dem Motto "Der
Weg   ist   das   Ziel"   setzt   KVP  auf   ständige   kleinere  Verbesserungen  der   Geschäftsprozesse   anstelle   einer
grundlegenden   Innovation   beziehungsweise   Reorganisation.   Das   unterscheidet   KVP   vom   BPR.   Die
Gemeinsamkeit mit dem BPR und damit das Neue gegenüber den herkömmlichen Organisationsverfahren ist
jedoch die Prozessorientierung und damit die Abkehr vom Funktionsdenken.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

280

 Referenz Arbeitshilfen

Der Ansatz des KVP ist weder revolutionär noch radikal, sondern hat sich aus langjährigen Erfahrungen
gebildet. Insofern ist der Ansatz wesentlich praxisorientierter als der des BPR und berücksichtigt in größerem
Maße die Probleme, die bei der Reorganisation von Unternehmensprozessen auftreten.

Anwendungsfall-Modellierung

Siehe entsprechender Absatz in Methodenreferenz Anforderungsanalyse

Produkte

Quellen

Lastenheft (Anforderungen), Projektvorstudie

BG03

G.1.1.6 Modellierung funktionaler Anforderungen (UML)

Die   Unified   Modeling   Language   (UML)   eignet   sich   insbesondere   für   die   Beschreibung   funktionaler
Anforderungen. Diese Methodenreferenz stellt dar, wie ein Ausschnitt der Modellierungssprache verwendet
werden   kann,   um   fachliche   Zusammenhänge   und   Systemverhalten   zu   modellieren.   Die   Modellierung
verwendet

➢ Anwendungsfalldiagramme,

➢ Aktivitätsdiagramme,

➢ Anwendungsfalltabellen (ergänzend zur UML) und

➢ Klassendiagramme.

Anwendungsfalldiagramm: Überblick über die Systemfunktionalität

Ein Anwendungsfalldiagramm gibt einen ersten Überblick über die Gesamtheit der Anwendungsfälle und
somit über die Definition des Systemverhaltens. Es  beschreibt, was  das  System ist, was  das System an
 en    das System interagiert. Ausgehend von den
Verhalten und Funktionalität umfasst und mit welchen Akteur
im   Anwendungsfalldiagramm   dargestellten   Anwendungsfällen   werden   diese   in   einem   weiteren   Schritt
ausführlicher beschrieben. Je nach Komplexität kann dies entweder textlich oder modellbasiert erfolgen.
Handelt   es   sich   um   nicht-komplexe   bzw.   nur   gering-komplexe   Anwendungsfälle,   ist   es   ausreichend,
Anwendungsfälle   mit   einer   kurzen   textlichen   Beschreibung   zu   versehen.   Ansonsten   sind   die   beiden
nachfolgend genannten Beschreibungsmöglichkeiten empfehlenswert.

Aktivitätsdiagramm: Detaillierung des Systemverhaltens

Zeichnen sich die Anwendungsfälle dahingegen als mittel bis stark komplex ab, ist es sinnvoll, diese mittels
Aktivitätsdiagrammen   näher   zu   erläutern.   Die   Aktivitätsdiagramme   vermitteln   auf   einen   Blick   und
ausdrucksstark, was der Normalablauf ist und wie Alternativabläufe aussehen, welche Vorbedingungen und
auslösende Ereignisse existieren. Eine optische Trennung zwischen System und Akteur ("Swimlane") kann
die Interaktion des Systems mit der Außenwelt noch übersichtlicher darstellen.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


G.1 Methoden und Werkzeuge

281

Anwendungsfalltabelle: Ergänzende Informationen

Informationen zu Priorität, Stakeholdern und dem Querbezug zu nicht-funktionalen Anforderungen können
nicht   unmittelbar   modelliert   werden.   Es   empfiehlt   sich,   für   jeden  Anwendungsfall   eine   Tabelle   nach
folgendem Muster zu hinterlegen:

Kurzbeschreibung

Hier erfolgt eine kurze und prägnante Beschreibung der Fachlichkeit des
Anwendungsfalls.

Vorbedingung / Auslösendes
Ereignis

Hier werden zum Einen die Voraussetzungen für den Anwendungsfall (der
Zustand, in dem sich das System vor Ausführung befindet) beschrieben und
zum Anderen die Ereignisse, die den Anwendungsfall auslösen.

Normalablauf

Hier erfolgt eine Beschreibung des Ablaufs des Anwendungsfalls, so wie er
sich im Normalfall (in der Mehrzahl der Fälle) verhält. Dabei wird der Ablauf
in einzelnen Schritten dargestellt.

Nachbedingung(en) /
Ergebnis

Hier werden zum Einen die Zustände, in dem sich das System nach
Ausführung des Anwendungsfalls befindet, und zum Anderen die Ergebnisse
für den Anwender angegeben.

Akteure

Priorität

Stakeholder

Alternativabläufe

Querbezug zu nicht-
funktionalen Anforderungen

Hier werden alle Akteure aufgeführt, die an dem Anwendungsfall in
irgendeiner Form beteiligt sind und somit mit dem beschriebenen
Anwendungsfall in Beziehung stehen.

Für die Angabe der Priorität wird aus der Prioritätenskala (siehe
Methodenreferenz Vom Lastenheft zum Kriterienkatalog im Teil
Methodenreferenzen des V-Modell XT Bund) genau eine festgelegt.

Gibt es für den hier beschriebenen Anwendungsfall konkrete Stakeholder
(über die Akteure hinaus), dann werden diese hier aufgeführt.

Hier erfolgt eine Beschreibung des Ablaufs des Anwendungsfalls, so wie er
sich in Sonder- bzw. Ausnahmefällen verhält. Dabei wird der Ablauf in
einzelnen Schritten dargestellt. Es können sich bei Alternativabläufen andere
Nachbedingungen bzw. Ergebnisse als im Normalablauf ergeben. Diese
werden dann hier angegeben.

Ist erkennbar, dass der hier beschriebene Anwendungsfall einen Querbezug
bzw. eine Abhängigkeit zu einer oder mehreren nicht-funktionalen
Anforderungen besitzt, so werden die davon betroffenen nicht-funktionalen
Anforderungen an dieser Stelle gelistet.

Klassendiagramm: Fachliches Datenmodell und fachliche Zusammenhänge

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

282

 Referenz Arbeitshilfen

Des   Weiteren   wird   für   datenzentrierte   Systeme   im   Rahmen   der   funktionalen  Anforderungen   ein   erstes
fachliches   Datenmodell   erstellt,   das   ggf.   Grundlage   eines   späteren   Datenbankentwurfs   oder   einer
objektorientierten Implementierung ist. Das fachliche Datenmodell des Systems leitet sich aus den Entitäten
und den fachlichen Zusammenhängen der Domäne ab. Die Dokumentation des fachlichen Datenmodells
erfolgt mit Klassendiagrammen. Zusätzlich zu der Diagrammdarstellung empfiehlt es sich – soweit diese
bereits bekannt sind – zusätzliche Informationen wie beispielsweise fachliche Attribute oder den Querbezug
zu funktionalen und nicht-funktionalen Anforderungen in einem Datenkatalog festzuhalten. Diese können je
nach eingesetztem Werkzeug bereits  im Modell  hinterlegt  werden oder aber im Lastenheft  textlich oder
tabellarisch ergänzt werden. Wichtig ist, dass die verwendeten Attribute und Datentypen (wenn sie überhaupt
angegeben sind) ausschließlich fachlicher Natur sind.

Produkte

Quellen

Lastenheft (Anforderungen)

PR09

G.1.1.7 Projektplanung und -steuerung

Ziel   der   Projektplanung   und   -steuerung   ist   die   Definition   von   Projekten   und   die   Überwachung   eines
zielgerichteten   Projektverlaufs.   Die   Projektplanung   und   -steuerung   kann   mit   folgenden   Methoden
durchgeführt werden:

Balkenplan- und Netzplantechnik

Ziel der Netzplantechnik ist die Terminplanung für Aktivitäten unter Berücksichtigung ihrer Abhängigkeiten.
Unter Abhängigkeiten versteht man beispielsweise, dass eine Aktivität erst starten darf, wenn eine andere
beendet ist.

Als   Notation   für   Projektpläne   wird   dabei   der   "Balkenplan"   verwendet.   Balkenpläne   existieren   in
unterschiedlichen Ausprägungen, als so genannter Vorgangsknotennetzplan, als Ereignisknotennetzplan oder
als Vorgangskantennetzplan. Moderne Werkzeuge für die Projektplanung integrieren diese unterschiedlichen
Notationen.

Als Anhaltspunkt für die Terminplanung bietet die Netzplantechnik unterschiedliche Berechnungsmethoden
an:   Bei   Eingabe   der  Abhängigkeiten   der  Aktivitäten   voneinander,   der  Aktivitätsdauern   sowie   frühester
beziehungsweise   spätester   Projektanfangs-   und   Projektendtermine   können   beispielsweise   kritische   Pfade
berechnet   werden.   Kritische   Pfade   sind   abhängige   Aktivitäten,   deren   Verzögerung   zu   einer
Gesamtverzögerung des Projektes führt.

Meilenstein-Trend-Analyse (MTA)

Eine MTA zeigt auf anschauliche Art die zu den verschiedenen Berichtszeitpunkten veränderte Einschätzung
von Plan-Werten und das veränderte Verhältnis von Plan- zu Ist-Werten.

Earned Value Verfahren (EVV)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

G.1 Methoden und Werkzeuge

283

Das   "Earned   Value   Verfahren"   stellt   grafisch   einen   Plan/Ist-Vergleich   der   Termin-   und   Kostensituation
bezogen   auf   den   Arbeitsfortschritt   in   einem   Projekt   dar.
  Es   vereint   Verfahren   der
Leistungsfortschrittsmessung mit der Kostenverfolgung und der Zeitkontrolle.

Im EVV-Diagramm werden drei verschiedene Sichten des Projektverlaufs einander gegenübergestellt:

➢ Soll: Budgetwert der geplanten Leistung,

➢ Ist: Ist-Wert der erbrachten Leistung,

➢ Leistung: Budgetwert der erbrachten Leistung.

Hieraus   werden   die   Wertabweichung   (Ist   minus   Leistung)   und   die   Leistungsabweichung   (Soll   minus
Leistung) an einem Stichtag ermittelt.

Kosten-Nutzenanalyse

Siehe Beschreibung zur Kosten-Nutzenanalyse .

Produkte

Quellen

Projektplan

Bal00, PMI

G.1.1.8 Prototyping

Protoyping ist eine Methode, um neue Systeme, Programme oder Informationsverwaltungssysteme zu testen
oder   zu   verfeinern.   Dazu   wird   ein   Modell   des   zu   testenden   Systems   erstellt   und   daran   Tests   oder
Untersuchungen durchgeführt.

Man spricht vom so genannten "Rapid Prototyping", wenn in rascher Folge immer wieder leicht verbesserte
Prototypen entwickelt werden, ohne lange einen "perfekten" Prototypen zu planen.

Beim  explorativen   Prototyping  wird   ein   Prototyp   als   Kommunikationsmedium   ("Vorzeigeprototyp")
entwickelt.   Im   direkten   Meinungsaustausch   mit   dem   Anwender   werden   anhand   des   Prototypen   die
Anwenderforderungen verfeinert, ergänzt und geklärt.

Produkte

Quellen

Systemarchitektur, Systemspezifikation, SW-Architektur, Projektvorstudie

Geb02, Mac99

G.1.1.9 Prozessanalyse

Die   Prozessanalyse   ist   die   Bewertung   von   organisationsspezifischen   Prozessen,   die   Identifikation   von
Fehlern   und   Schwachstellen   im   Entwicklungsprozess   und   die   Feststellung   von   Abweichungen   von
vorgegebenen   Standards,   Richtlinien   und   Vorgehensweisen.   Die   Prozessanalyse   kann   mit   folgenden
Methoden durchgeführt werden:

Assessment-Methoden:

Durch die Assessment-Methode werden Prozesse in einer Organisation bewertet. Dazu können verschiedene
Bewertungsmodelle und Methoden angewendet werden wie z.B.:

1. V-Modell XT Assessment

2. V-Modell XT Konformitätsprüfung

3. CMMI®:  CMMI®  (Capability  Maturity  Model  Integration)   stellt   eine   verbesserte  Version   des
Capability   Maturity   Modells   dar,   das   verschiedene   andere   Rahmenwerke   vereint,   die   von   dem
Software Engineering Institute erstellt wurden. CMMI® ermöglicht nicht nur die Unterstützung von

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland





284

 Referenz Arbeitshilfen

Software-Entwicklungsprozessen,   sondern   bezieht   sich   auch   auf   das   Risikomanagement   und   die
strukturierte Entscheidungsfindung. Es ermöglicht außerdem die effektive Integration von Aspekten
der menschlichen Möglichkeiten innerhalb der Softwareentwicklung.

ist

4. SPICE   (ISO   15504):  Das  SPICE  (  Software  Process  Improvement  Capability   dEtermination)
Projekt   ist   eine   internationale   Initiative   zur   Entwicklung   eines   Standards   für   Software-Prozess-
Assessments. Annähernd 40 Länder haben aktiv an der Entwicklung dieses Standards teilgenommen.
Sie wurde geleitet durch die Arbeitsgruppe 10 bei der ISO (ISO/IEC JTC1/SC7/WG10). Das SPICE
Projekt
  Projektinitialisierung,
Produktentwicklung,   Prüfungen,   Produktüberarbeitung,   Wissens-   und   Technologietransfer,
Abschluss.
  Prozessverbesserung   und
Leistungsbestimmung.   Die   übergeordneten   Ziele   des   Standards   sind   die   Förderung   von
vorhersehbarer   Produktqualität,   Verbesserung   zu   maximaler   Produktivität,   Förderung   eines
wiederholbaren Software Prozesses, ständige Prozessverbesserung durch periodische Prüfungen auf
Konsistenz.

in   sechs   zusammenhängende   Phasen   aufgeteilt:

  Standard   umfasst

  Prozessbewertung,

  Der

5. EFQM:  Die  EFQM-Methodik   (  European  Foundation   of  Quality  Management)   dient   der
ganzheitlichen Bewertung eines Unternehmens. Es können Prozesse nach EFQM beurteilt werden.
Die Aussagen sind aber meist qualitativer und nicht quantitativer Natur. Bei EFQM werden auch die
Schnittstellen   zu   nicht   entwicklungsrelevanten   Geschäftsprozessen   beurteilt.   Es   erfolgt   eine
Selbstbewertung   durch   die   Geschäftsverantwortlichen.   Ziel   ist   das   Erkennen   von   Stärken   und
Verbesserungspotentialen   durch   Verbesserungsmaßnahmen   und   erneute   Selbstbewertung   nach
beispielsweise   einem   Jahr.   Die   EFQM-Methodik   ist   aus   dem   TQM-Gedanken   (Total  Quality
Management) entstanden. Sie zwingt zur ganzheitlichen Betrachtung des Unternehmens, legt ein
allgemein akzeptiertes Business-Excellence-Modell zugrunde und bietet einen allgemein gültigen
Bewertungsmaßstab, beispielsweise eine europaweite Vergleichsmöglichkeit.

Fehler-Ursachen-Analyse (FUA)

Die FUA (oder Defect Causal Analysis) ist eine Methode, die Fehler im Produkt und Schwachstellen im
Erstellungsprozess   unmittelbar   nach   ihrem Auftreten   erfasst   und  einer   systematischen  Ursachen-Analyse
unterzieht.   Das   Resultat   sind   Vorschläge   für   Korrekturmaßnahmen,   die   den   Prozess   und   sein   Umfeld
betreffen. Die vorgeschlagenen Maßnahmen werden durch das Management geprüft und ihre Umsetzung
eingeleitet.   Nach   ihrer   Umsetzung   werden   die   Maßnahmen   erprobt   und   ihre   Wirksamkeit   gemessen.
Erfolgreiche Maßnahmen münden in Prozessverbesserungen, die in der Breite eingeführt werden.

Kategorien für die Fehlerursachen sind:

➢ Kommunikationsprobleme (z.B. Verantwortlichkeiten/Aufgaben im Projekt/Team nicht klar geregelt,
fehlende   Ansprechpartner   aufgrund   von   Absenzen   (Urlaub,   Fortbildung),   unzureichende
Kommunikation   zwischen   beteiligten   Komplexen   (SW/SW,   SW/HW,   Entwicklung/Kunde,
standortübergreifende Entwicklung),

➢ Umsetzungsprobleme (Tools, Zeitmanagement),

➢ mangelnder Überblick, fehlende Kenntnis (z.B. nicht verstandenes Design, fehlende Kenntnis der

Programmiersprache, etc.),

➢ Verfahrensprobleme (z.B. Prozess passt nicht zum Produkt, fehlende Mechanismen zur Behandlung

von Änderungsanforderungen, etc.),

➢ Probleme verursacht durch ungeplante Erweiterungen.

Audit

Ziel   des  Audits   ist   die   Feststellung   von  Abweichungen   von   vorgegebenen   Standards,   Richtlinien   und
Vorgehensweisen bei der Durchführung von Aktivitäten. Insbesondere ist es die Aufgabe eines Audits, auf
Verbesserungsmöglichkeiten   hinzuweisen.   Das   Prinzip   des   Audits   besteht   darin,   dass   ein   Team   unter
Führung eines Audit-Leiters die Durchführung von Aktivitäten anhand festgelegter Prüfkriterien prüft und

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland



G.1 Methoden und Werkzeuge

285

bewertet. Prüfungen und Bewertungen erfolgen durch die menschliche Urteilskraft und unter Anwendung der
Interviewtechnik. Je nach Umfang der Prüfung reicht es aus, das Audit nicht durch ein Team, sondern von
einer einzelnen Person durchführen zu lassen.

FMEA/FMECA

Zur Beschreibung von FMEA/FMECA siehe Fehler-/Zuverlässigkeitsanalyse.

Produkte

Quellen

G.1.1.10 Review

Prüfprotokoll

ANSI-Norm N45, Car02, Car93, Car98, CMMI®, DW88, EFQM, IEEE-STD
1028-1988, ISO DIS 10011, Kne03, Lev86, Phi86, SPICE, Sta95

Ein  Review  ist eine eingeplante, kritische, systematische und dokumentierte inhaltliche Überprüfung von
Arbeitsergebnissen am Ende von definierten Arbeitsschritten. Das Review ist gekennzeichnet durch eine
schriftlich festgehaltene, definierte Vorgehensweise. Im Review wird anhand von definierten Vorgaben (z.B.
Referenzdokumente,   Prüfkriterien)   geprüft.   Bei   der   Prüfung   werden   Hilfsmittel   (z.B.   Formulare   und
Checklisten)   verwendet   und   die   Ergebnisse   des   Reviews   werden   bewertet   und   in   einem   Protokoll
dokumentiert.   CMMI®   fordert   so   genannte  Peer   Reviews.   Darunter   versteht   man   Reviews   unter
Gleichgestellten, also sachkundigen Kollegen.

Ziele von Reviews sind:

➢ Prüfung von Ergebnissen anhand objektiver Prüfkriterien,

➢ frühzeitiges Entdecken und Beseitigen von Fehlern in Arbeitsergebnissen,

➢ Einhaltung von Richtlinien, Standards und sonstigen Vorgaben,

➢ Vermeidung der Wiederholung von in zurückliegenden Phasen erledigten Arbeiten,

➢ Minimierung der Kosten für die Fehlerbeseitigung,

➢ Gewinnung von Messdatentypen zur Bewertung der Qualität von Ergebnissen und des Prozesses,

➢ Aufdecken von Schwachstellen im Entwicklungsprozess,

➢ Erfahrungsgewinn als Basis für die zukünftige Vermeidung von Fehlern.

Der   Ablauf   von   Reviews   beginnt   mit   den   Vorarbeiten,   wozu   eine   Einführungsveranstaltung   (je   nach
Methode) und die Vorbereitung der Review-Sitzung (z.B. Termin- und Ortswahl) zählen. Anschließend wird
das Review nach einem vorher festgelegten Verfahren durchgeführt. Die dabei dokumentierten Fehler und
Verbesserungsvorschläge für das Review-Objekt (z.B. Dokument, Code, Zeichnung oder Prozess) werden
vom   Autor   des   Review-Objekts   nachgearbeitet.   Anschließend   kann   die   Freigabe   des   Review-Objekts
stattfinden.

Für die einzusetzenden Review-Verfahren gelten folgende Anforderungen:

➢ Der   Ablauf,   die   einzelnen   Schritte   sowie   die  Rolle

 n    und   deren   Aufgaben   sind   definiert   und

beschrieben.

➢ Alle  durchzuführenden Schritte  sind  geplant,  die  Verantwortlichkeiten und die  Prüfkriterien  sind

festgelegt.

➢ Die   Review-Ergebnisse   werden   aufgezeichnet,   Fehlerdaten   und   Aufwand   dokumentiert   und

ausgewertet.

Es existieren einige grundlegende Verfahren zum Review, die sich in ihrem Aufbau und Ablauf sowie in den
eingesetzten Rollen inklusive Aufgaben unterscheiden:

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


286

 Referenz Arbeitshilfen

➢ Bei Kommentartechnik-Verfahren (z.B. Stellungnahme) erfolgt die Überprüfung durch die Prüfer

separat, es findet keine Sitzung statt.

➢ Bei  Sitzungstechnik-Verfahren, wie Walkthrough, Peer Review oder 4-Augen-Prinzip, werden in

der Sitzung die in der Vorbereitung gefundenen Fehler durchgesprochen.

➢ Bei  Inspektionen, wie Intensiv-Inspektion von Code oder Dokumenten, werden die Inhalte der zu

untersuchenden Objekte systematisch durchgesprochen.

➢ Bei  Kombinierten Verfahren  werden verschiedene Verfahren aus schriftlichen Kommentaren und

Review-Sitzung kombiniert.

Methoden des Review:

Inspektion oder Walkthrough

Der Walkthrough ist eine formalisierte Review-Technik mit definiertem Vorgehen und Rollenverteilung in
der   Review-Sitzung.   Ziel   der   Review-Verfahren   Inspektion   oder   Walkthrough   ist   die   Identifikation
vorhandener   Fehler   beziehungsweise   fehlerträchtiger   Situationen,   sowie   die   Messung   der   Qualität.
Gegenstand des Review-Verfahrens ist der Programmquelltext (in Verbindung mit der Spezifikation), das
Dokument oder die Zeichnung.

Ein Walkthrough empfiehlt sich für Objekte von hoher Komplexität oder hoher Fehlerdichte. Die Review-
Teilnehmerzahl kann zwischen 3 und 7 Personen betragen. Mehr Teilnehmer verursachen in der Regel einen
zusätzlichen Aufwand,   dem  kein  zusätzlicher   Nutzen  in  Form  von mehr   gefundenen Fehlern entspricht;
zudem ist eine Sitzung mit 8 oder mehr Teilnehmern nicht mehr straff zu moderieren.

Die   Durchführung   eines   Walktroughs   oder   einer   Inspektion   eines   Dokuments,   eines   Codes   oder   einer
Zeichnung geschieht meist in einem Team von circa 4 Personen. Neben dem Ersteller gehören ein Moderator
und   Spezialisten   zum   Team.   Der   Ersteller   erläutert   die   Programmlogik   Anweisung   für   Anweisung
beziehungsweise das Dokument Satz für Satz. Die Teammitglieder stellen Fragen und identifizieren Fehler.
Die empfehlenswerte Dauer einer Sitzung ist circa 2 Stunden.

4-Augen-Prinzip

Das 4-Augen-Prinzip ist eine Sonderform des Walkthrough; durch die Teilnahme von nur 2 Personen soll der
Review-Aufwand   gering   gehalten   werden.   Um   aber   dennoch   eine   intensive   Prüfung   und   das   Finden
möglichst aller Fehler zu gewährleisten, sind bei dieser Technik die wahrzunehmenden Funktionen und die
Ablaufschritte   konkret   vorgegeben   sowie   mit   dem   Leser   eine   spezielle   Funktion   zusätzlich   vorgesehen.
Durch   die   geringere   Personenzahl   können   allerdings   auch   wichtige   Erfahrungen   und   Know-how   nicht
berücksichtigter Mitarbeiter verloren gehen.

Kombinierte Verfahren

In den Fällen, in denen möglichst viele Teilnehmer in das Review einbezogen werden sollen, wodurch aber
die maximal vorgesehene Teilnehmerzahl in einer Sitzung überschritten würde, ist eine Kombination zweier
Review-Techniken zweckmäßig. Dies ist z.B. gegeben, wenn das Review-Objekt aus vielen verschiedenen
Sichtweisen heraus betrachtet werden muss oder wenn sehr viele Stellen davon betroffen sind.

Die Kombination besteht einerseits aus der Abgabe schriftlicher Kommentare zum Review-Objekt durch
Mitarbeiter, die nicht an der Sitzung im Rahmen eines Walkthrough teilnehmen können oder sollen, und
andererseits   aus   einem Walkthrough.   In   einer   ersten  Phase   wird   das   Review-Objekt   von  allen  in   Frage
kommenden  Teilnehmern   geprüft,   um   möglichst   viele   Kommentare   einzuholen.   Daran   schließt   sich   ein
Walkthrough an, an dem nur ausgewählte Mitarbeiter (z.B. diejenigen, die vom Review-Objekt hauptsächlich
betroffen sind) oder nur die zum Sitzungstermin verfügbaren Mitarbeiter teilnehmen.

Produkte

Prüfprotokoll, Prüfspezifikation, Logistische Unterstützungsdokumentation,
Implementierungs-, Integrations- und Prüfkonzept SW

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

G.1 Methoden und Werkzeuge

287

Quellen

Bal00, FW90

G.1.1.11 Schätzmodelle

Schätzmodelle   bilden   die   Grundlage   für   eine   möglichst   objektive   und   realistische  Schätzung.   Das
angewandte   Verfahren   soll   eine   nachvollziehbare,   zuverlässige   und   genaue  Umfangschätzung  und
Aufwandsschätzung gewährleisten.

Zuerst müssen die Schätzobjekte festgelegt und möglichst genau charakterisiert werden. Auf der Basis der
Strukturierung des Projekts in überschaubare Teilaufgaben sind die Einflusskriterien für die Schätzung zu
ermitteln und zu bewerten. Dies betrifft Charakteristiken des Produkts, des Projekts, des Personals und der
Technologie. Es existieren sehr viele Schätzmodelle; allerdings ist kaum eines dieser Modelle allgemein
gültig, d.h. für unterschiedlichste Projekte, Systeme  und Unternehmen einsetzbar und zugleich für jeden
dieser Einsatzbereiche auch hinreichend zuverlässig und genau.

Im Folgenden werden einige gängige Methoden kurz vorgestellt:

Schätzformeln

Der  Aufwand   eines   Schätzobjektes   wird   mit   Hilfe   von   Formeln   berechnet,   die   auf   Erfahrungswerten
basieren.

➢ Function   Point  Analyse:   Hierbei   ist   das   betrachtete   SW-System   in   seine   Funktionsstruktur   zu
zerlegen. Für jede dieser Funktionen sind Transaktionen (Eingaben, Ausgaben oder Abfragen) und
Files (externer oder interner Datenbestand) zu zählen. Anschließend ist ein Funktionswert auf der
Basis der Komplexität der einzelnen Funktionen zu ermitteln. Mit Hilfe von Erfahrungskurven kann
aus diesem Funktionswert unter Berücksichtigung von definierten Einflussfaktoren auf den Aufwand
geschlossen werden.

➢ COCOMO:   COCOMO   wird   im   Umfeld   von   SW-Entwicklungen   eingesetzt   und   ermittelt   den
Aufwand   eines   Schätzobjektes   über   eine   Formel   aus   dem   geschätzten   Umfang   und   definierten
Einflussfaktoren.

➢ PRICE: PRICE umfasst eine Sammlung von Schätzmethoden, die nicht nur im SW- sondern auch

im HW-Umfeld eingesetzt werden können. Die SW-Variante ist COCOMO sehr ähnlich.

Expertenschätzung

Hier   sind   sowohl   der   Umfang   als   auch   der  Aufwand   der   Schätzobjekte   durch   Experten   abzuschätzen.
Schätzobjekte ergeben sich bei der  Umfangschätzung  aus der  Produktstruktur  , bei der Aufwandschätzung
aus der Projektstruktur des betrachteten Projekts. Bei jeder Expertenschätzung ist zumindest das 4-Augen-
Prinzip zu beachten, das heißt, der für das Schätzobjekt Verantwortliche schätzt den Umfang und Aufwand
und stimmt ihn mit einem erfahrenen Experten ab.

Eine spezielle und weit verbreitete Form der Expertenschätzung ist die Schätzklausur, an der 3-7 erfahrene
Schätzer   beteiligt   sind.   Diese   schätzen   unabhängig   voneinander   den   Umfang   und   Aufwand   der
Schätzobjekte,   diskutieren   die   Ursachen   größerer  Abweichungen  und   einigen   sich   auf   einen  gemeinsam
getragenen   Schätzwert.   Wesentliche   Annahmen   wie   Risiken   oder   Wiederverwendungsgrad   des
Schätzobjektes sind dabei zu dokumentieren. In der Abschlussdiskussion ist festzulegen, wie offene Punkte
geklärt werden. Es kann auch entschieden werden, die Schätzwerte durch eine Plausibilitätskontrolle mit
einer anderen Schätzmethode, zum Beispiel COCOMO oder Function Point Methode, zu überprüfen. Die
Schätzgenauigkeit hängt bei einer Schätzklausur wesentlich von der Erfahrung der beteiligten Schätzer ab.
Es ist deshalb wichtig, den geeigneten Personenkreis auszuwählen.

Prozentsatzmethode

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

288

 Referenz Arbeitshilfen

Bei der Prozentsatzmethode ist der Aufwand für einzelne Phasen beziehungsweise Aktivitäten mit Hilfe einer
Hochrechnung auf Basis durchschnittlicher oder empfohlener Anteile, so genannter Erfahrungswerte, vom
Gesamtaufwand zu bestimmen. Zum Beispiel werden 3% des Gesamtaufwands im Entwicklungsprojekt für
das Konfigurationsmanagement benötigt. Die Prozentsatzmethode ist nur für Grobschätzungen geeignet.

Produkte

Quellen

Schätzung

BF04, Bur03

G.1.1.12 Simulation

Ziel einer Simulation ist das Aufzeigen des Systemverhaltens unter dynamischen Aspekten. Die dynamischen
Auswirkungen   werden   durch   Einspielen   eines   operationellen   Szenarios   oder   durch   eine   Folge   von
Ereignissen   in   das   Modell   erzeugt   beziehungsweise   geschätzt.   Der   Einsatz   der   Simulationsmethode   ist
insbesondere zweckmäßig zur Bewertung folgender Eigenschaften:

➢ Erfüllung der Qualitätsanforderungen,

➢ Antwortverhalten für spezifische Eingabedaten,

➢ CPU-Nutzung,

➢ Speichernutzung/-kapazität,

➢ Erfüllung von Bedienungs-/Einsatzzeitzwängen,

➢ Mensch-Maschine-Zusammenspiel und Antwortverhalten.

Produkte

Quellen

Prüfprotokoll Systemelement

Hof97, Sch03

G.1.1.13 Systemanalyse

Das Ziel der Systemanalyse ist die Identifikation, Modellierung und Bewertung von Systemen. Es können
folgende Methoden verwendet werden:

Objektorientierte Analyse (OOA)

Die OOA kann mit den Mitteln der UML Methodenfamilie durchgeführt werden:

1. Anwendungsfall-Modellierung

Zielsetzung der Methode ist die Erfassung und Darstellung der aus Sicht von externen Bedienungseinheiten
("Aktoren") an ein System gestellten funktionalen Anforderungen. Die Anforderungen sind in Form von
Anwendungsfällen,   den   "Use   Cases",   zu   beschreiben.   Ein   Anwendungsfall   kann   in   einer   Reihe   von
Szenarios   konkretisiert   werden.   Externe   Bedienungseinheiten   (z.B.   Mitarbeiter,
 Projektleiter  oder
Administrator)   repräsentieren  Rolle
 n  ,   die   von   konkreten   Personen,   Maschinen,   Computer-"Tasks"   oder
anderen Systemen eingenommen werden können.

2. Klassen-/Objekt-Modellierung

Die Methode dient zur objektorientierten Systementwicklung. Diese erfordert die Modellierung von Klassen,
von   zugehörigen  Attributen   und   Operationen   sowie   der   Beziehungen   zwischen   den   Klassen.   Es   ist   die
Aufgabe   der   Klassenmodellierung,   die   statische   Klassenstruktur   in   Klassenmodellen   festzulegen.   Eine
Klasse ist in Bezug auf die Ausführung eines Systems statisch und definiert die Struktur und das Verhalten
ähnlicher Objekte. Objekte sind als Instanzen von Klassen zu modellieren.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


G.1 Methoden und Werkzeuge

289

Die Klassen-/Objektmodellierung kann in der objektorientierten Entwicklung sowohl während der Analyse-
als   auch   während   der   Entwurfsphase   eingesetzt   werden.  Während   der  Analyse   sind   die   Klassenstruktur
beziehungsweise die Objektstrukturen aus Nutzersicht zu modellieren, um auszudrücken, was ein System tut.
Im Entwurf sind diese Strukturen zu verfeinern, und es ist festzulegen, wie das System etwas tut.

Informationen

Bei der Klassenmodellierung sind Attribute zu verwenden, um identifizierende, beschreibende oder auch
referenzierende
  Durch   zusätzliche
Modellierungsmöglichkeiten,   wie   beispielsweise   die   Festlegung   von   Sichtbarkeiten,   die   Vergabe   von
Rollennamen, die Zuordnung von Einschränkungen ("constraints"), die Beschreibung abgeleiteter Attribute
und   die  Verwendung   von   Beziehungen   höherer   Ordnung,   können   die   Entwicklungsergebnisse   verfeinert
werden.

  Klasse   zu   modellieren.

in   einer

Die   Konzepte   der   Klassenmodellierung   können  auch  eingesetzt   werden,   um  die   statischen Aspekte   von
Schnittstellen von Klassen und Subsystemen und ihre Anwendung zu definieren. Die Teile von Klassen
(Attribute,   Operationen)   beziehungsweise   Subsystemen   (Klassen,   Beziehungen),   die   als   Schnittstellen
definiert werden sollen, können nochmals in eigenen Schnittstellenmodellen gekennzeichnet werden.

3. Interaktionsmodellierung

Die   Methode  dient   zur   objektorientierten Systementwicklung.  Zielsetzung  ist  es,  Interaktionen zwischen
Objekten   und   ihre   Reihenfolge   in   Interaktionsmodellen   zu   beschreiben.   Durch   Interaktionen   kann   das
Auftreten   von   Ereignissen   beziehungsweise   der   Austausch   von   Nachrichten   ausgedrückt   werden.   Die
Methode   kann   zur   Formalisierung   von   Szenarios   (Folgen   von   Ereignissen   und   das   damit   verbundene
Systemverhalten) und zur Modellierung des dynamischen Ablaufs von Operationen eingesetzt werden. Mit
Zeitliniendiagrammen   ("Sequence   Diagrams")   wird   dabei   das   Ziel   verfolgt,   schwerpunktmäßig   die
ablauforientierte Reihenfolge der Interaktionen zwischen den Objekten zu modellieren und zu visualisieren.
Um   die   Interaktionsbeziehungen   detaillierter   zu   modellieren   und   um   die   Softwarestruktur   zu   betonen,
werden vorwiegend Interaktionsgraphen ("Collaboration Diagrams") eingesetzt. Der für die Kommunikation
benötigte   Zeitaufwand   wird   in   der   Interaktionsmodellierung   nicht   direkt   betrachtet,   jedoch   können
Zeitbeschränkungen   modelliert   werden.   Nebenläufigkeiten   sind   abbildbar.   Durch   die   Modellierung   von
Signaturen,   synchronen   und   asynchronen   Abläufen,   Zeit-,   Ablauf-   und   Synchronisationsbedingungen,
Verzweigungen,   Iterationen,   Rekursionen   sowie   des   Erzeugens   und   Löschens   von   Objekten   können
Entwicklungsergebnissse verfeinert werden.

4. Aktivitätsdiagramme

Aktivitätsdiagramme   können   als   Konkretisierung   der   Anwendungsfälle   durch   Anlegen   von
Aktivitätsdiagrammen   in   Anwendungsfällen   angewendet   werden.   Damit   können   Abhängigkeiten,
nebenläufige   Prozesse,   Entscheidungs-/Verzweigungspunkte   dargestellt   werden.   Des   Weiteren   können
Aktivitätsdiagramme   als   eine   spezielle  Art   des   Zustandsdiagramms,   das   ausschließlich  Aktivitäten   und
Übergänge   zwischen   diesen   zeigt,   eingesetzt   werden.   Eine  Aktivität   ist   einem   Zustand   zugeordnet   und
repräsentiert eine andauernde interne Aktion.

5. Zustandsmodellierung

Zielsetzung der Zustandsmodellierung im objektorientierten Bereich ist die Modellierung des dynamischen
Verhaltens eines Systems. Wichtigstes Anwendungsgebiet ist die Modellierung des dynamischen Verhaltens
von   Objekten   signifikanter   ereignisgesteuerter   Klassen.   Solche   Klassen   spezifizieren   im   Allgemeinen
"aktive" Objekte.

Das   Verhalten   von   Objekten   einer   Klasse   ist   als   Lebenszyklus   zu   abstrahieren   und   wird   in   einem
Zustandsmodell   modelliert.   Das   Zustandsmodell   soll   alle   Zustände,   die   ein   Objekt   annehmen   kann,   die
möglichen Zustandsübergänge, die Ereignisse, die Zustandsübergänge bewirken können, die Bedingungen,
die neben den Ereignissen für einen Zustandswechsel erfüllt sein müssen, und die Aktionen, die infolge von
Zustandsübergängen auszuführen sind, definieren.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

290

 Referenz Arbeitshilfen

Mit den Zuständen werden Datenwerte, die die Attribute eines Objekts einer Klasse annehmen können, und
mögliche Verknüpfungen mit anderen Objekten festgelegt. Der Zustandsübergang, der für ein Objekt einer
Klasse in einer konkreten Situation eintritt, ist eindeutig durch den Zustand, in dem sich das Objekt aktuell
befindet, das eingetroffene Ereignis sowie spezifizierte Bedingungen bestimmt.

Ein Pfad in einem Zustandsmodell repräsentiert eine Folge von Ereignissen. Szenarios, die häufig während
der Analyse  zur Formulierung gewünschter Ereignisfolgen verwendet werden, müssen auf die Pfade der
spezifizierten Zustandsmodelle abbildbar sein.

Strukturierte Analyse (SA)

Die strukturierte Analyse besteht aus der Kombination der Methoden:

1. Datenflussmodellierung

Ziel   der   "Datenflussmodellierung"   ist   es,   die   Funktionsstruktur   eines   Systems   durch   die   kombinierte
Betrachtung von Funktionen und Daten zu präzisieren. Die  Datenflüsse  bilden hierbei die  Schnittstellen
zwischen den Funktionen. Die Datenflussmodellierung abstrahiert von den physikalischen Gegebenheiten
eines geplanten Systems.

In einem top-down-orientierten Vorgehen werden immer detailliertere Schichten des zukünftigen Systems
spezifiziert. Ausgangspunkt ist ein Übersichtsdiagramm („Kontextdiagramm“), das lediglich die Datenflüsse
des Systems von und zu seiner Umgebung wiedergibt. Bei der Verfeinerung des Datenflussmodells werden
die in der Funktionshierarchie identifizierten Funktionen durch ein Datenflussdiagramm der entsprechenden
Ebene verfeinert.

Ein   Datenflussdiagramm   einer   bestimmten   Hierarchie-Schicht   lässt   sich   als   ein   Zusammenspiel   von
Prozessen darstellen, die über Datenflüsse in Verbindung stehen. Eine Verfeinerung auf der Daten-Seite wird
stets in Abstimmung mit der entsprechenden Verfeinerung der Funktionshierarchie durchgeführt. Bei der
Modellierung der Datenflüsse kommt es darauf an, eine logische innere Struktur des geplanten Systems zu
finden, die stabil und unabhängig von Entwurfsentscheidungen und Hardware-Gegebenheiten ist.

2. Funktionsmodellierung

Die Funktionsmodellierung hat zum Ziel, schrittweise ein System zu zerlegen, beginnend bei der Sicht auf
die Hauptfunktion eines Systems über die Zwischenebenen bis zur Ebene elementarer Funktionen. Auf einer
Ebene   wird   jeweils   von   Details   der   darunter   liegenden   Ebene   abstrahiert.   Die   Teilfunktionen
zusammengenommen ergeben vollständig die aufgegliederte Funktion (Funktionshierarchie).

Formale Spezifikation

Die Formale Spezifikation ist eine Spezifikation nach strengen Regeln. Man unterscheidet zwei Klassen von
formaler Spezifikation: die abstrakte Spezifikation (implementierungsneutral, Blackbox-Sicht, algebraische
Spezifikation) und die modellbasierte Spezifikation, in der die Zustandsänderung des Systems aufgrund einer
oder   mehrer   Operationen   beschrieben   wird   (Beispiel   ist   die   Z-Spezifikation).  Ziel   einer   formalen
Spezifikation   ist   eine   knappe   und   präzise   Darstellung   mit   der   Möglichkeit,   diese   direkt   in   Code
umzuwandeln.   Eine   Verifikationsmöglichkeit   zur   Fehlererkennung   sowie   ein   Korrektheitsbeweis   des
Programms aufgrund der Spezifikation sind wünschenswert. Der Nachteil einer formalen Spezifikation ist
die schwere und aufwändige Erstellung, die nur wenige Entwickler/Projektleiter überhaupt beherrschen, die
Unverständlichkeit für den Kunden (d.h. sie kann nicht als Kommunikationsgrundlage verwendet werden)
sowie die Begrenzung auf einige funktionale Anforderungen (z.B. mathematische Berechnungen). Da eine
rein   formale   Spezifikation   kaum   realisierbar   erscheint,   ist   eine   Mischung   aus   formaler   und   halb-   oder
informaler Spezifikation das Optimum. Was formal spezifizierbar ist, soll damit beschrieben werden, der
Rest wird über eine andere Spezifikationsvariante behandelt.

Produkte

Externe-Einheit-Spezifikation, Pflichtenheft (Gesamtsystementwurf),
Systemspezifikation, Externes-SW-Modul-Spezifikation, SW-Spezifikation,
Projektvorstudie

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

G.1 Methoden und Werkzeuge

291

Quellen

BRL99, Mor99, You92

G.1.1.14 Systemdesign

Das Systemdesign kann sowohl

➢ objektorientiert,

➢ funktionsorientiert als auch

➢ formal spezifiziert werden.

Objektorientiert

Bei den objektorientierten Entwurfsmethoden können die gleichen Methoden aus der UML-Methodenfamilie
wie bei der Systemanalyse eingesetzt werden.

Funktionsorientiert

Die Methode des Strukturierten Entwurfs (Structured Design) wird hauptsächlich in Verbindung mit der
Strukturierten   Analyse   durchgeführt.   Die   Methode   stammt   aus   den   siebziger   Jahren   und   wird   heute
schwerpunktmäßig   noch   für   die   Pflege   von   Altsystemen   verwendet.   Strukturierter   Entwurf   ist   eine
Entwurfsmethode, die zu einer Softwarearchitektur führt, die aus funktionalen Modulen besteht. Die Struktur
der Architektur ist ein Baum oder ein azyklisches Netz. Die Beschreibung erfolgt durch Strukturdiagramme.
Die Methode wird sowohl zum Grobentwurf als auch zum Feinentwurf der Software angewandt. Ziel der
Methode im Grobentwurf ist es, sowohl die übergeordneten Steuerungsabläufe als auch die eigentlichen
Verarbeitungsfunktionen in Form einer Modulhierarchie zu strukturieren.

Formale Spezifikation

Zur Beschreibung siehe Systemanalyse.

Produkte

G.1.1.15 Test

Implementierungs-, Integrations- und Prüfkonzept System, Systemarchitektur,
SW-Architektur

Ziel   des   "Testens"   ist   das   Aufdecken   von   Fehlern   sowie   der   Nachweis   der   Erfüllung   spezifizierter
Anforderungen.

Man unterscheidet zwischen verschiedenen Strukturtests, Whitebox-Tests und Blackbox-Tests.

Bei   Strukturtests   wird   in   Kenntnis   des   inneren  Aufbaus   getestet.   Eine   wesentliche  Rolle  spielen   hier
Überdeckungsmaße (Coverage), die angebenen wie intensiv die Struktur getestet wurde.

Blackbox Tests werden ohne Kenntnis des inneren Aufbaus in Hinblick auf die Anforderungen durchgeführt.
Hier gibt es unterschiedliche Ziele und Testarten wie:

➢ Funktionstest,

➢ Volumentest,

➢ Stress-, Performancetest,

➢ Ressourcentest,

➢ Recoverytest,

➢ Usability Test,

➢ Systemtest,

➢ Regressionstest.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

292

Produkte

 Referenz Arbeitshilfen

Implementierungs-, Integrations- und Prüfkonzept System, Prüfspezifikation
Systemelement, Prüfprotokoll Systemelement, Logistische
Unterstützungsdokumentation, Implementierungs-, Integrations- und Prüfkonzept
SW

Quellen

Bal00, Tha02

G.1.1.16 Vom Lastenheft zum Kriterienkatalog

Hinweis:  Die   vorliegende   Methodenreferenz   bezieht   sich   insbesondere   auf   Projekte,   bei   denen   der
Auftragnehmer   mit   einer   (öffentlichen   oder   nicht-öffentlichen)   Ausschreibung   oder   einem   (offenen   oder
nicht-offenen) Verfahren ermittelt wird.

Für die Entwicklung eines IT-Systems ergeben sich für den Auftraggeber bereits vor Vertragsschluss zwei
wichtige Aufgaben:

➢ Er muss die Anforderungen an das System möglichst genau spezifizieren, um selbst zu wissen, was
das   System  leisten   muss   und   um   dieses  Wissen   auch   für   die   Entwickler   (beim Auftragnehmer)
festzuschreiben.

➢ Er muss einen Kriterienkatalog (als Teil der Leistungsbewertungsmatrix) erstellen, auf Basis dessen
die Bieter ihre Angebote erstellen. Da sich der Vertrag als Zuschlag auf ein Angebot ergibt, muss der
Auftraggeber also sicher stellen, dass sich die definierten Anforderungen auch in den Angeboten der
Bieter wiederfinden.

Während   die   erste   Aufgabe   zum   Software   und   Systems   Engineering   gehört   und   einen   erfahrenen
Anforderungsanalytiker (AG) benötigt, ist die zweite Aufgabe Teil des Vergabeprozesses und benötigt einen
erfahrenen Ausschreibungs- und Vertragsverantwortlichen. Im Folgenden wird eine Methode beschrieben,
die den Weg von den definierten Anforderungen über eine Anforderungsbewertung hin zum Kriterienkatalog
aufzeigt.   Die   Methode   eignet   sich   für   alle   Arten   von   Anforderungen   und   Lastenhefte,   also   sowohl
funktionale   als   auch   nicht-funktionale,   textbasierte   und   modellbasierte,   präzise   und   schwammige.   Die
Methode gliedert sich in die Anforderungsbewertung, die anschließende Überarbeitung, die Strukturierung
eines Kriterienkatalogs und die Ableitung von einzelnen Kriterien.

Bewertung der Anforderungen

Ausgangspunkt ist eine fertig gestellte Version des Lastenhefts. Die Bewertung der Anforderungen besitzt
zwei  Aspekte:   Einerseits   ist   sie   eine   zusätzliche   Qualitätssicherung   für   die   definierten  Anforderungen,
andererseits werden dabei die Anforderungen durch die Brille des zukünftigen Auftragnehmers betrachtet.

Um dieses zu bewerten muss zunächst klar sein, welche Bewertungskriterien dafür herangezogen werden:

Die Priorität (Prio) beschreibt, wie wichtig die Umsetzung der Anforderung für die Gesamtfunktionalität des
Systems bzw. für den Erfolg des Projekts ist. Idealerweise sollte sie bereits im Lastenheft definiert sein und
hier nur übernommen werden müssen. Mögliche Werte sind hier:

Muss (m)

Soll (s)

Könnte (k)

Eine solche Anforderung muss vom System umgesetzt werden, um den Projekterfolg (z.B.
gesetzlichen Auftrag) nicht zu gefährden.

Eine solche Anforderung sollte wenn möglich (finanzierbar, realisierbar) umgesetzt werden.
Für die Umsetzung gilt aber das Gebot der Wirtschaftlichkeit.

Eine solche Anforderung beschreibt einen Zusatznutzen, der beispielsweise die Akzeptanz
der Benutzer erhöht. Eine solche Anforderung sollte umgesetzt werden, sofern dies möglich
und kostengünstig oder kostenneutral erfolgen kann.

Unnötig (u)

Eine unnötige Anforderung sollte überhaupt nicht umgesetzt werden, in keinem Fall sollte

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

G.1 Methoden und Werkzeuge

293

für die Umsetzung einer solchen Anforderung Geld aufgewendet werden.

Die Genauigkeit (Gen) beschreibt, wie präzise die Anforderung beschrieben ist. Mögliche Werte sind hier:

Sehr präzise
(sp)

weitgehend
klar (wk)

schwammig/
offen (so)

Eine solche Anforderung ist vollständig beschrieben und lässt keinen
Interpretationsspielraum. Dies bedeutet insbesondere, dass das Systemverhalten unter allen
Umständen beschrieben ist (z.B. auch Ausnahmen, Fehlerfälle, Alternativwege), dass die
handelnden Akteure klar sind und dass die verwendeten und verarbeiteten Daten(-strukturen)
klar beschrieben sind. Sehr präzise Anforderungsbeschreibungen lassen sich insbesondere
durch die Verbindung von Modellen (z.B. UML), strukturierten Texten (siehe Rupp) und
mathematischen Ausdrücken (z.B. OCL) erreichen.

Eine solche Anforderung erfüllt nicht die oben genannten Anforderungen einer sehr präzisen
Anforderung, dennoch ist mit gesundem Menschenverstand klar, wie die Anforderung
verstanden werden soll. Es sind nicht alle Fehler- oder Ausnahmefälle beschrieben.

Eine solche Anforderung ist unklar, besitzt offene Punkte oder hohen
Interpretationsspielraum, z.B. "Das System muss ergonomisch sein", "Das System muss
performant arbeiten", etc. Manchmal können Anforderungen nur sehr schwammig
beschrieben werden, denn eine präzise Beschreibung benötigt zu viel Aufwand.

Die  Verbindlichkeit   (Verb)  der   Beschreibung   legt   fest,   in   welchem   Verhältnis   die   Realisierung   einer
Anforderung zu ihrer  Beschreibung steht.  Diese  Information ist als Ergänzung zur Genauigkeit wichtig:
Beispielsweise kann das Systemverhalten im Lastenheft (Anforderungen) zwar sehr präzise beschrieben sein,
es stellt sich jedoch heraus, dass die Umsetzung davon auch abweichen darf. Wie die Priorität sollte sich
auch die Verbindlichkeit aus dem Lastenheft ableiten lassen. Mögliche Werte sind hier:

Genau so
(gs)

Diese Verbindlichkeit bedeutet, dass das Verhalten des entwickelten Systems exakt dem in
den Anforderungen spezifizierten Systemverhalten entsprechen muss. Diese Verbindlichkeit
ist nur sinnvoll, sofern die Anforderung sehr präzise oder weitgehend klar ist.

so oder
ähnlich (soä)

Diese Verbindlichkeit bedeutet, dass das Verhalten des entwickelten Systems von der
definierten Anforderung abweichen darf. Dies ist sinnvoll, sofern eine Anforderung
schwammig oder (wie eingangs beschrieben) "überpräzise" beschrieben ist.

Die  Realisierbarkeit   (Real)  beschreibt   die   grundsätzliche   theoretische   und   technische   Möglichkeit,   die
Anforderung umzusetzen. Mögliche Werte sind hier:

realisierbar
(r)

unrealisierbar
(ur)

Die Anforderung ist sowohl theoretisch als auch mit den Mitteln der aktuellen Technik
umsetzbar.

Die Anforderung ist nicht umsetzbar. Insbesondere die Grenzen der Physik und der
Berechenbarkeit können dazu führen, dass eine Anforderung in diese Kategorie fällt.
Beispiele hierfür sind die Definition von Reaktionsgeschwindigkeiten innerhalb eines global
verteilten Systems oder auch die Suche nach optimalen Lösungen zu NP-harten Problem
(z.B. Problem des Handlungsreisenden).

unklar (uk)

Es ist nicht klar, ob eine solche Anforderung realisierbar ist.

Die Finanzierbarkeit (Fin) beschreibt, ob die Umsetzung der Anforderung unverhältnismäßig teuer ist, oder
gar das kalkulierte Projektbudget sprengt. Mögliche Werte sind hier:

finanzierbar
(f)

unfinanzierba
r (uf)

Die Anforderung ist im Rahmen des Projektbudgets finanzierbar und erzeugt im Vergleich zu
den anderen Anforderungen keine unverhältnismäßigen Mehrkosten.

Die Anforderung sprengt das Projektbudget oder stellt eine unverhältnismäßige Verteuerung
der Entwicklungskosten dar. Gerade überzogene nicht-funktionale Anforderungen (sehr

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

294

 Referenz Arbeitshilfen

kleine Reaktionszeit, sehr hohe Ausfallsicherheit, etc.) können die Entwicklungskosten
enorm verteuern.

unklar (uk)

Es ist nicht schätzbar, wie viel die Umsetzung der Anforderung kosten wird.

Hinweis: Die Finanzierbarkeit lässt sich in der Regel nicht anhand einer Anforderung ausdrücken, sondern
ergibt sich aus den wechselseitigen Abhängigkeiten aller Anforderungen. Die hier getroffenen Aussagen sind
deshalb sehr vereinfachend. Eine präzisere Beschreibung würde aber den Rahmen sprengen.

Auf Basis der vorgestellten Kriterien bewertet der Anforderungsanalytiker (AG) die einzelnen Bestandteile
des  Produkts  Lastenheft  (Anforderungen),  was  beispielhaft  in der  folgenden Tabelle  dargestellt  wird.   Je
nachdem, ob die Anforderungen als Prosa, strukturierter Text oder Modell verfasst sind, eignen sich als
Bewertungseinheit   Textabschnitte,   Kapitel,   einzelne   Anforderungen   oder   Modelldiagramme.   Die
Untergliederung  (vertikal)   soll   zumindest   so  feingranular   erfolgen,   dass   sich  für   die   einzelnen  Kriterien
eindeutige Werte ergeben: Besitzt also beispielsweise ein beschreibender Text teilweise die Priorität Muss
und   teilweise   die   Priorität   Soll,   so   wird   er   nach   diesem   Kriterium   aufgeteilt   und   benötigt   somit   zwei
Tabellenzeilen.

Überarbeitung der Anforderungen

Auf   Basis   der  Bewertungsergebnisse  überarbeitet   der   Anforderungsanalytiker   (AG)   zunächst   die
Anforderungen.   Dabei   beachtet   er   insbesondere   die   in   der   folgenden  Tabelle   gegebenen   Hinweise.   Die
zweite Spalte ist beispielweise folgendermaßen zu verstehen:

Anforderungen mit der Priorität Muss oder Soll, die schwammig/offen formuliert sind, bergen das Risiko,
dass wichtige Bestandteile der Systemfunktionalität falsch verstanden werden und sollten daher überarbeitet
und präzisiert werden.

Prio  Gen  Verb  Real  Fin

Risiko

Empfehlung

Dokument wird unnötig aufgebläht. entfernen

u

*

m, s

so

m

*

*

*

*

*

*

*

*

uk

*

Wichtige Bestandteile werden
falsch verstanden.

Niemand kann das System
realisieren.

m

*

*

*

uk

Die Angebote übersteigen den
Finanzrahmen.

überarbeiten und präzisieren

entweder so ändern, dass die
Anforderung realisierbar ist, oder
Priorität herabstufen

entweder so ändern, dass die
Anforderung finanzierbar ist, oder
Priorität herabstufen

*

*

*

*

*

*

ur

*

Unnötige Aufwände werden zur
Realisierung investiert.

realisierbar umformulieren oder
streichen

*

uf

Die Angebote übersteigen den
Finanzrahmen.

finanzierbar umformulieren oder
streichen

Struktur des Kriterienkatalogs

Die   Struktur   des   Kriterienkatalogs   ist   prinzipiell   frei   wählbar.   Je   mehr   sich   die   Struktur   jedoch   an   der
Themenstruktur der Produkte  Lastenheft (Anforderungen),  Projekthandbuch  und  QS-Handbuch  orientiert,
desto   leichter   gelingt   die   Zuordnung   zwischen   den   dort   definierten   Inhalten   und   dem   Kriterienkatalog.
Folgende   Tabelle   zeigt   ein   Beispiel,   wie   der   Kriterienkatalog   in   Kriterienhauptgruppen   (teilweise   mit
Untergruppen) untergliedert werden kann:

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

G.1 Methoden und Werkzeuge

295

Kriterienhauptgruppe

Kriteriengruppe

Kriterium

Verständnis von Ausgangssituation und
Zielsetzung

Funktionale Anforderungen

Nicht-Funktionale Anforderungen

Gesamtsystemarchitektur und Lebenszyklus

Lieferung und Abnahme

Projektmanagement (Vorgaben für das
Projekthandbuch)

Qualitätssicherung (Vorgaben für das QS-
Handbuch)

Ableitung von Kriterien

Schnittstellen und Akteure

Funktionalität

Datenmodell

Funktionalität

Zuverlässigkeit

Benutzbarkeit

Effizienz

Änderbarkeit

Übertragbarkeit

Randbedingungen

Unabhängig davon, ob die Anforderungen wie im vorangegangenen Abschnitt überarbeitet wurden, muss der
Ausschreibungs- und Vertragsverantwortliche aus dem  Lastenheft (Anforderungen)  einen Kriterienkatalog
ableiten und die einzelnen Kriterien, die Kriteriengruppen und Kriterienhauptgruppen gewichten. Dabei kann
er   sich   ebenfalls   auf   die   Ergebnisse   der   Anforderungsbewertung   stützen,   die   sich   ggf.   durch   die
Überarbeitung   der   Anforderungen   verändert   haben.   Grundsätzlich   sollte   der   Ausschreibungs-   und
Vertragsverantwortliche dabei folgende Regeln beachten:

➢ Genau   die   Anforderungen,   die   finanzierbar,   realisierbar   und   nicht   unnötig   sind,   sollten   im

Kriterienkatalog durch entsprechende Kriterien (Fragen an den Bieter) abgedeckt werden.

➢ Die Zuordnung von Anforderungen und Kriterien ist dabei flexibel: Beispielsweise kann sich ein B-
Kriterium auf mehrere Anforderungen beziehen oder eine Anforderung kann durch ein B- und ein A-
Kriterium umgesetzt werden.

➢ Die Gewichtung eines B-Kriteriums sollte sich daran orientieren, wie viele Anforderungen durch

dieses B-Kriterium abgedeckt werden, und welche Priorität diese besitzen.

Die nachfolgende Tabelle dient als Hilfestellung für die Ableitung von Kriterien und die Überprüfung des
Kriterienkatalog. Die letzte Zeile ist beispielsweise wie folgt zu verstehen:

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

u

*

*

*

*

m

m

*

*

*

*

*

sp,
wk

sp,
wk

296

 Referenz Arbeitshilfen

Eine realisierbare und finanzierbare Anforderung mit Könnte-Priorität sollte keinesfalls Gegenstand eines
A-Kriteriums sein. Dagegen ist es sinnvoll, die Umsetzung vom Bieter durch ein niedrig gewichtetes B-
Kriterium zu erfragen.

Prio  Gen  Verb  Real  Fin

Hinweise für Aufstellung von Kriterien

*

*

*

*

*

*

ur

*

uk

*

*

uf

*

Keine Berücksichtigung im Kriterienkatalog

Keine Berücksichtigung im Kriterienkatalog

Keine Berücksichtigung im Kriterienkatalog

Keinesfalls durch A-Kriterium abdecken; ggf. als optionales Kriterium;
Hinweis in Kriterien, dass Realisierbarkeit unklar ist

*

uk

Keinesfalls durch A-Kriterium abdecken; ggf. als optionales Kriterium;
Hinweis in Kriterien, dass Finanzierbarkeit unklar ist

gs

r

soä

r

m, s

s

*

s

k

sp,
wk

*

*

*

r

r

r

f

f

f

f

f

A-Kriterium, das die Umsetzung der Anforderung wie beschrieben
zusichert * (siehe unten)

A-Kriterium (siehe oben); zusätzlich hoch gewichtetes B-Kriterium

Kein A-Kriterium; hoch gewichtetes B-Kriterium; Frage nach der
genauen Umsetzung stellen; Erwartungshaltung möglichst flexibel
gestalten

Kein A-Kriterium; hoch gewichtetes B-Kriterium

Keinesfalls als A-Kriterium abdecken; niedrig gewichtetes B-Kriterium

* = Theoretisch ist damit sichergestellt, dass die Anforderung wie beschrieben umgesetzt wird. Allerdings
können   sich   durch   die   alleinige   Umsetzung   als   A-Kriterium   Verzerrungen   in   der   Ermittlung   des
Leistungsumfangs ergeben, da das Erfüllen eines A-Kriterium nicht in die Leistungsbewertung mit eingeht.

Produkte

Quellen

Anforderungsbewertung, Kriterienkatalog

Rup04, UfAB

G.1.2 Werkzeugreferenzen

G.1.2.1 Anforderungsmanagement

Im Verlauf eines Projekts ist es notwendig, neue Anforderungen zu erfassen, gegebenenfalls aus anderen
Dokumenten zu importieren, zu ändern und zu verwalten. Bei einer großen Anzahl von Anforderungen ist
dies   nur   werkzeuggestützt   möglich.   Die   Werkzeuge   zum   Anforderungsmanagement   sollten   folgende
Aufgaben erfüllen:

➢ Erfassen der Anforderungen,

➢ Aufbau   und   Verwaltung   von   Anforderungsstrukturen   (z.B.   hierarchische   und   lose   Strukturen,

Verweis auf die zugehörige Testanforderung),

➢ Verfeinerung von Anforderungen,

➢ Verwalten der Historie,

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

G.1 Methoden und Werkzeuge

297

➢ Beobachtung   und   Überwachung   (Tracking)   von   Anforderungen   (um   z.B.   festzustellen,   ob   die
Anforderung bereits bearbeitet worden ist oder wie lange die Bearbeitung der Anforderung dauerte),

➢ Auswerten,   Nachvollziehen   und   Rückverfolgen   (Tracing)   der   Anforderungen   (z.B.   auf

Entwurfsobjekte und Testfälle),

➢ Unterstützung   der   Auswirkungsanalyse   (wie   hoch   wird   der   Aufwand   sein,   wenn   sich   eine

Anforderung verändert und welche weiteren Anforderungen sind davon betroffen),

➢ Datenbankgestützte   Verwaltung   der   Anforderungen,

  nach   Möglichkeit   in   mehreren

Datenbankplattformen,

➢ Attribute von  Anforderungen festlegen  (z.B. Priorität, Bearbeitungsstatus, Kosten der Umsetzung,

Bearbeiter, etc.).

Produkte

G.1.2.2 Compiler

Lastenheft (Anforderungen), Externe-Einheit-Spezifikation, Pflichtenheft
(Gesamtsystementwurf), Implementierungs-, Integrations- und Prüfkonzept
System, Systemspezifikation, Externes-SW-Modul-Spezifikation

Ein Compiler (auch Kompilierer oder Übersetzer) ist ein Computerprogramm, das ein in einer Quellsprache
geschriebenes   Programm   in   ein   semantisch   äquivalentes   Programm   einer   Zielsprache   umwandelt.
Üblicherweise   handelt   es   sich   dabei   um   die   Übersetzung   eines   von   einem   Programmierer   in   einer
Programmiersprache geschriebenen Quelltextes in Assemblersprache oder Maschinensprache.

In der Regel erzeugt ein Compiler kein direkt fertiges, ausführbares Programm, sondern eine Objekt-Datei.
Eine oder mehrere Objekt-Dateien können mit einem Link-Programm zu einem ausführbaren Programm
verbunden   werden,   selbst   wenn   sie   in   verschiedenen   Sprachen   oder   gar   von   einem  Assembler   erstellt
wurden. Die Kompilation ist ein einmaliger Vorgang, muss also nicht für jeden Durchlauf des Programms
erneut vorgenommen werden, weil die "Übersetzung" gespeichert wird.

Produkte

Implementierungs-, Integrations- und Prüfkonzept SW

G.1.2.3 Fehler-/Änderungsmanagement

Werkzeuge   zur   Unterstützung   des   Fehler-   und   Änderungsmanagements   (Change   Request   Management)
sollen

➢ Problem-/Änderungsmeldungen erfassen,

➢ die Meldungen hinsichtlich Dringlichkeit und Auswirkung einstufen,

➢ den Stand und Status der Fehlerbearbeitung wiedergeben (Änderungskontrolle und Statusreporting).

Häufig   sind   die   Werkzeuge   zum   Fehler-/Änderungsmanagement   mit   den   Werkzeugen   des
Konfigurationsmanagements kombiniert, manchmal aber auch separat.

Produkte

Änderungsentscheidung, Änderungsstatusliste, Problem-/Änderungsbewertung,
Problemmeldung/Änderungsantrag

G.1.2.4 GUI-Werkzeug

Software-Ergonomie   behandelt   die  Aspekte   der   Gestaltung   von   Benutzerschnittstellen   (Graphical   User-
Inteface, kurz GUI genannt). Mittels des GUI-Werkzeuges wird das Design der grafischen Oberfläche einer
Software, der Schnittstelle zwischen Mensch und Maschine, vorgenommen. GUI-Design kennzeichnet das,
was der Anwender der Software zu sehen bekommt, was also über ihr schlichtes Funktionieren hinausgeht.
Besonderes Augenmerk gilt hier der menschlichen Wahrnehmung und Informationsverarbeitung. Während

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

298

 Referenz Arbeitshilfen

des GUI-Designs wird die Benutzerschnittstelle gestaltet und getestet. Dieser Entwicklungsabschnitt umfasst
die Definition von Benutzeraktionen (der Handlungsmöglichkeiten des Benutzers), die Repräsentation der
Systemfunktionalität und das Feedback.

Produkte

Mensch-Maschine-Schnittstelle (Styleguide)

G.1.2.5 Integrierte Entwicklungsumgebung

Eine integrierte Entwicklungsumgebung ist eine durchgängige Plattform für die Entwicklung und den Test
von Software. Meistens wird synonym der englische Begriff verwendet: Integrated Design Environment oder
Integrated   Development   Environment,   abgekürzt   IDE.   IDEs   können   funktional   zu   einer   Gruppe
zusammengefasst werden und verfügen in der Regel über folgende Komponenten:

➢ Text-Editor,

➢ Compiler und/oder Interpreter,

➢ Linker/Binder,

➢ Testhilfsmittel (Debugger).

Meist verfügen die IDEs über eine gemeinsame Datenbasis und erlauben unter einer einheitlichen, grafisch
bedienbaren Oberfläche zu arbeiten. Damit lassen sich häufig vorkommende Arbeitsschritte automatisieren
und der Wechsel zwischen einzelnen Programmen (z.B. Editor/Compiler/Linker oder Debugger/Editor) ist
nicht  mehr  offensichtlich. Umfangreichere  IDEs können darüber hinaus  weitere hilfreiche Komponenten
besitzen, wie zum Beispiel eine Versionsverwaltung, Projektverwaltung oder die Möglichkeit der einfachen
Erstellung von GUIs.

Produkte

Externe-Einheit-Spezifikation, Pflichtenheft (Gesamtsystementwurf),
Implementierungs-, Integrations- und Prüfkonzept System, Systemspezifikation,
Externes-SW-Modul-Spezifikation, Migrationskonzept

G.1.2.6 KM-Werkzeug

Transparenz   und   Nachvollziehbarkeit   sind  zentrale  Anforderungen  im  Projektalltag.   Hierzu  dienen  KM-
Werkzeug
 e  . Das bedeutet, dass während der gesamten Lebensdauer des Softwareprodukts dessen Aufbau und
Bestandteile ständig überschaubar und kontrollierbar gehalten werden müssen. Im einfachsten Fall wird dies
auf   dem   Dateisystem   gemacht.   Sinnvoller   ist   die   Verwendung   spezieller   Werkzeuge,   die   die   geordnete
Ablage   unterstützen.   Zusammenhänge   und   Unterschiede   zwischen   früheren   Konfigurationen   und   der
aktuellen Konfiguration müssen mit Hilfe des KM-Werkzeuges jederzeit erkennbar sein. Ferner muss mit
Hilfe   des   KM-Werkzeuges   sichergestellt   werden,   dass   jederzeit   sowohl   auf   die   aktuelle   wie   auch   auf
vorausgegangene Versionen zurückgegriffen werden kann. Es gibt einige Open-Source-Werkzeuge zur KM-
Verwaltung, die Mehrzahl der Werkzeuge ist jedoch proprietär.

Typische Eigenschaften von KM-Systemen sind:

➢ Versionskontrolle,

➢ Variantenkontrolle,

➢ Build-Management,

➢ Änderungsmanagement und Abhängigkeitskontrolle (Dependency Tracking),

➢ Problembehandlung (Bug Tracking),

➢ Dokumentationskontrolle, Distributionskontrolle, etc.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


G.1 Methoden und Werkzeuge

299

Produkte

Produktbibliothek, Produktkonfiguration, Implementierungs-, Integrations- und
Prüfkonzept System, Implementierungs-, Integrations- und Prüfkonzept SW

G.1.2.7 Konstruktion/Simulation

CAE/CAD-Werkzeuge für den digitalen Schaltungsentwurf verfügen meist über folgende Funktionen:

➢ der Entwurf der Schaltung in Form eines Schaltplans,

➢ die Verifizierung der Funktion,

➢ die Simulation unter verschiedenen Toleranz-Bedingungen,

➢ die Erstellung von Gehäuse und Bauteilbibliotheken,

➢ die Überführung des Schaltplans in ein Layout,

➢ die Erstellung von Belichtungsmasken für die Produktion,

➢ die Ableitung von produktionswichtigen Daten wie etwa Stücklisten und Prüfplänen.

Diesem verwandt ist das Design von programmierbaren Bausteinen wie Gate Arrays, GALs und anderen
Typen   programmierbarer   Logik   (PLDs).   Als   Spezialfall   der   CAD-Entwicklung   sind   Programme   für
Simulationen nach der Finite-Elemente-Methode zu bezeichnen.

Produkte

Implementierungs-, Integrations- und Prüfkonzept System, Logistische
Unterstützungsdokumentation, Externes-SW-Modul-Spezifikation

G.1.2.8 Modellierungswerkzeug

Modellierung ist eine zentrale Aufgabe in vielen Bereichen der Softwaretechnik, z.B. bei der Ermittlung von
Anforderungen, der Strukturierung von Anwendungsbereichen und bei der Erstellung von Software- und
Prozess-Architekturen.   Dabei   helfen   Modellierungswerkzeuge.   Sie   bilden   die   Methoden   ab,
schwerpunktmäßig   die   UML-basierten   Modellierungstechniken   oder   die   konventionell   strukturieren
Methoden.

Modellierungswerkzeuge können Bestandteil einer integrierten Entwicklungsumgebung (IDE) sein oder als
reines stand-alone Modellierungswerkzeug existieren.

Mit   Hilfe   grafischer   Modellbildungswerkzeuge   ist   es   möglich,   auch   ohne   große   Detailkenntnisse   und
zunächst   unter   Verzicht   auf   in   Formeln   gegossene   Bezüge   Simulationsmodelle   am   Bildschirm   zu
konstruieren. Dabei wird das Modell interaktiv als Wirkungsnetz am Bildschirm erzeugt, indem Symbole für
die Elemente Zustandsgrößen, Änderungsgrößen, Funktionen und Konstanten einer Palette entnommen und
im Drag-and-Drop-Verfahren mit der Maus auf dem Bildschirm verknüpft werden.

Produkte

Externe-Einheit-Spezifikation, Pflichtenheft (Gesamtsystementwurf),
Implementierungs-, Integrations- und Prüfkonzept System, Systemarchitektur,
Systemspezifikation, Externes-SW-Modul-Spezifikation, SW-Architektur, SW-
Spezifikation

G.1.2.9 Projektplanung

Werkzeuge zur Projektplanung unterstützen die zeitliche Planung durchzuführender Aktivitäten und ihrer
Abhängigkeiten sowie die Ressourcenplanung. Weiterhin können die folgenden Aspekte unterstützt werden:

➢ die Überwachung von Meilensteinen,

➢ die Projektsteuerung über Arbeitsaufträge und

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

300

 Referenz Arbeitshilfen

➢ die quantitative Projektplanung und -kontrolle (Aufwand, Kosten und Zeit, Plan-/Ist-Vergleich).

Produkte

Projektplan, Schätzung

G.1.2.10 Tailoring/Projektinitialisierung

Werkzeuge zum Tailoring und zur Projektinitialisierung im Rahmen eines V-Modell-Projekts unterstützen
den Projektleiter bei der Durchführung des Tailorings. Sie implementieren den in TK09 beschriebenen und
im V-Modell XT Projektassistenten als Referenzimplementierung hinterlegten Tailoringalgorithmus, der das
projektspezifische   V-Modell   auf   Basis   der  Auswahl   eines   Projekttyps,   einer   Projekttypvariante   und   der
Belegung der Projektmerkmale berechnet. Darüber hinaus unterstützt das Werkzeug bei der Ableitung eines
  Meilensteinplans   auf   der   Basis   der   im   Tailoring   berechneten
initialen   Projekt-   bzw.
Projektdurchführungsstrategie und befolgt dabei die in  BF10  hinterlegten Konsistenzregeln. Idealerweise
kann   das   Werkzeug   vorgehensmodellkonforme   Produktvorlagen   im   Corporate   Design   der   jeweiligen
Organisation   generieren,   den   Projektleiter   bei   der   Ressourcenplanung   und   Produktinstanzierung   unter
Beachtung der erzeugenden Produktabhängigkeiten unterstützen. Die beiden letztgenannten Punkte werden
durch den Projektassistenten nicht unterstützt.

Produkte

Projekthandbuch, Projektplan

G.1.2.11 Tools zum IT-Grundschutz

Das BSI stellt eine Übersicht alternativer Tool-Lösungen bereit, welche die BSI-Standards umsetzen und bei
der Erstellung, Verwaltung und Fortschreibung von Sicherheitskonzepten unterstützen.

Produkte

Quellen

Sicherheitskonzeption

IT-Grundschutz

G.1.2.12 V-Modell XT Projektassistent

Der V-Modell XT Projektassistent unterstützt den  Projektleiter  bei der initialen Anpassung des V-Modells
(Tailoring) und erzeugt das projektspezifische V-Modell. Der Projektassistent bietet im Anschluss an das
Tailoring folgende Funktionen an:

➢ Export einer Prozessdokumentation des projektspezifischen V-Modells in verschiedenen Formaten
(PDF, HTML). Diese Dokumentation entspricht im Aussehen der Dokumentation des gesamten V-
Modells, enthält jedoch nur die Inhalte, die nach dem Tailoring für das Projekt noch relevant sind.

➢ Export   von  Produktvorlagen  (siehe  Teil  Vorlagen)   im  Umfang   wie   er   im  projektspezifischen V-
Modell festgelegt wird. Die Produktvorlagen sind auf die Inhalte des projektspezifischen V-Modells
so angepasst, dass sie nur noch Themen enthalten, die für das Projekt relevant sind. Ferner sind auch
nur noch solche Rollen in den Vorlagen referenziert, die aufgrund des Tailorings zu besetzen sind.
Beim   Produktvorlagenexport   können   zu   Produkten   auch   verschiedene   Mustertexte   ausgewählt
werden, die beim Export in die einzelnen Vorlagen integriert werden. Der Produktvorlagenexport
kann in den Formaten OpenOffice.org (ODT) und Microsoft Word (DOC) erfolgen.

➢ Export eines initialen Projektplans und den Formaten CSV, Gantt-Project sowie Microsoft Project
200x-XML.   Dieser   Projektplan   wird   auf   Grundlage   der   im   Tailoring   ermittelten
Projektdurchführungsstrategie   erstellt   und   enthält   nach   dem   Export   alle   geplanten
Entscheidungspunkte als Meilensteine, denen die wesentlichen Vorgänge und ggf. initiale Rollen
zugeordnet sind.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

G.1 Methoden und Werkzeuge

301

Der Projektassistent unterstützt außerdem die Bereitstellung von Kopiervorlagen, die unabhängig von V-
Modell-Inhalten Vorlagen für Produkte bereit stellen. Kopiervorlagen können auch in Formaten vorliegen,
die durch den Vorlagenexport nicht erzeugt werden, also z.B. Microsoft Excel.

Produkte

Quellen

Projekthandbuch, Projektplan

4Ever

G.1.2.13 WiBe-Kalkulator

Der  WiBe-Kalkulator  unterstützt  die Bewertung durch die  Bereitstellung eines  Kriterienkatalogs für alle
Module, Möglichkeiten zur Auswahl passender Kriterien und zur Erfassung der projektspezifischen Werte.
Er   erleichtert   die   Gesamtbeurteilung   des   Projekts   durch   aggregierte   Darstellungen   der   erfassten   Daten.
Außerdem können mit ihm verschiedene Alternativen berechnet werden.

Die Software ist auf der Webseite des Beauftragten der Bundesregierung für Informationstechnik (BfIT) zu
beziehen.

Produkte

Quellen

WiBe (Vorkalkulation), WiBe (Fortschreibung)

WiBe

G.2 Produktvorlagen

G.2.1 Grundsätzliches zu Produktvorlagen
Dieses Kapitel beantwortet die grundlegenden Fragen zu Produktvorlagen:

➢ Was sind Produktvorlagen und wozu werden sie gebraucht?

➢ Für welche Produkte existieren Produktvorlagen?

➢ Woher bekommt man Produktvorlagen?

G.2.1.1 Sinn und Zweck

Eine Produktvorlage ist ein Dokument (in den Formaten ODT oder DOC), das alle für einen konkreten
Produkttyp  relevanten   Inhalte   des  V-Modells   (Produktname,  Disziplin,   verantwortliche   und   mitwirkende
Rolle
 n    sowie   Produkt-   und   Themenbeschreibungen)   enthält.   Sofern   für   einen   Produkttyp,   d.h.   für   die
einzelnen   Themen   des   Produkttyps,   bereits   Mustertexte   erstellt   wurden,   können   diese   ebenfalls   in   die
Produktvorlage übernommen werden.

Sämtliche   der   zuvor   genannten Inhalte  finden  sich  in  der  Referenz  Produkte  bzw.  der  im XML-Format
gespeicherten Mustertexte-Datei. Bei der Erstellung eines Produktexemplar
 s   müsste der Autor demnach die
gewünschten   Daten   aus   der   V-Modell-Referenz   und   der   XML-Datei   kopieren   und   in   sein   Dokument
einfügen. Mit Hilfe der dazugehörigen Produktvorlage wird ein entsprechend den im V-Modell definierten
Themen gegliedertes Dokument bereitgestellt, das diese Informationen bereits beinhaltet. Zudem folgen alle
angebotenen Produktvorlagen einem einheitlichen Layout.

G.2.1.2 Vorlagen nicht für alles

Für jedes V-Modell-Produkt, das als Dokument realisiert wird, existiert eine dazugehörige Produktvorlage.
Einzige Ausnahme bilden hierbei verschiedene Dokumente der  Auftraggeber-/Auftragnehmer-Schnittstelle,
wie z.B. der Vertrag. Dieser existiert sowohl beim Auftraggeber (als Vertrag) als auch beim Auftragnehmer

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland



302

 Referenz Arbeitshilfen

(als Vertrag (von AG)). Da diese Dokumente jedoch nicht doppelt erstellt, sondern als Datei, Brief oder Fax
über   die  Auftraggeber-/Auftragnehmer-Schnittstelle  ausgetauscht   werden,   existiert   entsprechend  nur   eine
Produktvorlage.

Darüber hinaus sind im V-Modell Produkte enthalten, die nicht in Form von Dokumenten verwendet werden,
wie  z.B.  Systemelemente,  Produkte  des Typs  SW-Modul,  die  Produktbibliothek  oder  die  Lieferung.  Für
derartige Produkte wird ebenfalls keine Produktvorlage bereitgestellt.

Produktvorlagen (Kurzform)

Die zuvor beschriebenen Produktvorlagen enthalten neben den im V-Modell definierten Themen eine Reihe
weiterer   Gliederungspunkte,   wie   beispielsweise   ein   Änderungs-   oder   Prüfverzeichnis.   Für   einige   der   zu
erstellenden Produkte (z.B. Besprechungsdokumente) sind diese jedoch irrelevant. Aus diesem Grund besteht
die Möglichkeit anstelle der vollständigen Produktvorlage eine Kurzform der Vorlage zu generieren. Diese
beinhaltet   ausschließlich   die   durch   das   V-Modell   vorgegebene   Themenstruktur   sowie   eine   kurze
Beschreibung des Produkts (Name, Autor, ...).

Kopiervorlagen

Für   einige   Produkte   enthält   das  V-Modell   auch  sogenannte  externe   Kopiervorlagen.   Dies   sind Vorlagen
(Dokumente),   die   nicht   aus   den   Inhalten   des   V-Modells   erzeugt   werden   und   die   generierten   Vorlagen
ergänzen.   Kopiervorlagen  sind  darüber   hinaus   nicht   auf   die   Exportformate   ODT  oder   DOC   beschränkt.
Somit können den Anwendern z.B. auch Tabellen- oder Präsentationsvorlagen angeboten werden.

G.2.1.3 Bezugswege

Prinzipiell existieren zwei Möglichkeiten, Produktvorlagen zu verwenden.

Ausgelieferte Produktvorlagen

Im   Lieferumfang   des   V-Modells   finden   sich   alle   verfügbaren   Produktvorlagen   im   ODT-Format.   Diese
Vorlagen   sind   nicht   auf   ein   konkretes   Projekt   zugeschnitten,   sondern   enthalten   alle   gemäß   V-Modell
möglichen Inhalte. So existiert beispielsweise in der Produktvorlage für das Projekthandbuch das Thema
Organisation und Vorgaben zu Informationssicherheit und Datenschutz unabhängig davon, ob im konkreten
Projekt der Vorgehensbaustein Informationssicherheit und Datenschutz (AG) ausgewählt wurde oder nicht.
In diesem Fall muss die Produktvorlage durch das Löschen des entsprechenden Kapitels an das konkrete
Projekt angepasst werden.

Selbst generierte Produktvorlagen

Mit   dem   V-Modell   steht   auch   der   V-Modell   Projektassistent   zur   Verfügung.   Mit   dem   V-Modell
Projektassistenten   können   projekt-   und   organisationsspezifische   Produktvorlagen   generiert   werden.   So
können   beispielsweise   eigene   Projektlogos,
  organisationsspezifische   Formatierungen   oder
Dateiablageinformationen   in   die   Produktvorlagen   aufgenommen   werden.   Des   Weiteren   besteht   die
Möglichkeit, die Produktvorlagen entsprechend dem projektspezifischen Tailoring zu generieren.

G.2.2 Inhalt und Aufbau der generierten Produktvorlagen
Das folgende Kapitel beschreibt den Inhalt und den Aufbau der Produktvorlagen.

G.2.2.1 Titelseite

Die Titelseite enthält die wichtigsten Informationen über das Produktexemplar. Dies sind der Produktname
und die entsprechende Disziplin, gefolgt von weiteren Informationen, die vom Produktverantwortlichen bei
der initialen Erstellung des Produktexemplars aktualisiert werden sollten.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

G.2 Produktvorlagen

303

Abbildung 62: Beispiel für die Titelseite einer Systemspezifikation

G.2.2.2 Weitere Produktinformationen

Dieser   Abschnitt   der   Produktvorlage   beinhaltet   weitere   V-Modell-spezifische   Informationen   über   das
Produkt.

Unter  Mitwirkend  finden sich alle Rollen, die gemäß V-Modell bei der Erstellung des Produktexemplars
mitwirken können. Sofern eine Rolle an der Erstellung beteiligt ist, ist vor der Rollenbezeichnung der Name
des Mitarbeiters anzugeben, der diese Rolle wahrnimmt. Rollen, die im konkreten Fall nicht beteiligt sind,
verbleiben mit der Kennzeichnung "nicht beteiligt". Sofern eine im Lieferumfang des V-Modells enthaltene
Produktvorlage verwendet wird, sind Rollen, die aufgrund des Tailorings nicht im Projekt vorkommen, zu
löschen.

Unter Erzeugung finden sich alle erzeugenden Produktabhängigkeiten, durch die der vorliegende Produkttyp
erzeugt werden kann. Dabei sind folgende drei Fälle zu unterscheiden:

1. Das Produkt ist ein initiales Produkt oder ein externes Produkt. In diesem Fall gibt es keine erzeugende
Produktabhängigkeit.

2. Es existiert genau eine erzeugende Produktabhängigkeit, durch die der vorliegende Produkttyp erzeugt
werden kann. In diesem Fall sind der Name und das Thema des Quell-Produkttyps sowie der Dateiname des
konkreten Quell-Produktexemplars anzugeben.

3. Es existieren mehrere erzeugende Produktabhängigkeiten, durch die der vorliegende Produkttyp erzeugt
werden kann. Für ein konkretes Produktexemplar trifft jedoch immer nur eine der Alternativen zu. Die nicht
zutreffenden Alternativen sind zu löschen.  Für  die  verbleibende  Produktabhängigkeit  ist  wie  in Punkt  2
beschrieben zu verfahren.

Abbildung  63  und  Abbildung   64  zeigen   den Abschnitt  Weitere   Produktinformationen  am  Beispiel   einer
Systemspezifikation.

Abbildung 63: Der Abschnitt "Weitere Produktinformationen" in einer Produktvorlage

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

304

 Referenz Arbeitshilfen

Abbildung 64: Der Abschnitt "Weitere Produktinformationen" in einem konkreten Produktexemplar

G.2.2.3 Änderungs- und Prüfverzeichnis

Um die Erstellung des Dokuments nachvollziehbar zu machen, ist es wichtig, das  Änderungsverzeichnis
gewissenhaft   zu   pflegen.  Auch   die   Prüfungen   des   Dokuments   müssen   nachvollziehbar   sein.   Zu   diesem
Zweck ist für jede Prüfung ein entsprechender Eintrag anzulegen - unabhängig davon, ob es sich um eine
Eigenprüfung oder um eine Prüfung durch eine eigenständige Qualitätssicherung handelt.

Die genauen Vorgaben für die Erstellung von Einträgen in diesen Tabellen werden im Projekthandbuch im
Kapitel Organisation und Vorgaben zum Konfigurationsmanagement festgelegt.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

G.2 Produktvorlagen

305

Abbildung 65: Änderungs- und Prüfverzeichnis in einem Beispieldokument

G.2.2.4 Einleitung

Unter Einleitung sollte dargestellt werden, welche Rolle das vorliegende Dokument innerhalb des Projekts
einnimmt. Dies umfasst die Gründe für die Existenz des Dokuments sowie die Ziele, die mit der Erstellung
des Dokuments verfolgt werden. Ein beispielhafter Text für die Einleitung wird standardmäßig hinterlegt und
kann entsprechend angepasst werden.

G.2.2.5 Themen

Die gemäß des Tailorings für das jeweilige Produkt relevanten Themen werden als Kapitel in das Dokument
eingefügt und sind entsprechend zu bearbeiten.

Je   nach   Auswahl   im   Projektassistenten   beinhalten   die   Themen   bereits   die   im   V-Modell   hinterlegten
Themenbeschreibungen bzw. Mustertexte. Die Themenbeschreibungen dienen nur als Hilfestellung für die
Erarbeitung der Inhalte und sollten daher vor der Fertigstellung des Dokuments gelöscht werden.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

306

 Referenz Arbeitshilfen

G.2.2.6 Vorgaben zur Prüfung des Dokumentes

Dieser Teil ist lediglich als Informationsquelle und Hilfestellung für den oder die Bearbeiter und  Prüfer des
Dokuments gedacht. Mit der Fertigstellung des Dokumentes kann der Text gelöscht werden.

In dem Text wird nochmals festgehalten, welche inhaltlichen Abhängigkeiten zwischen dem vorliegenden
Produkt   und   anderen  Produkte  bestehen.   Diese   müssen   geprüft   werden,   bevor   das   vorliegende
Produktexemplar in den Zustand fertig gestellt überführt werden kann.

Ganz wichtig ist dabei, dass sich diese Informationen auf der Ebene von Produkttyp
 en    bewegen. Das heißt
zum Beispiel, dass eine Systemspezifikation für ein konkretes Segment nicht mit allen im Projekt erstellten
SW-Spezifikation
 en
innerhalb des betroffenen Segments.

 en    konsistent zu halten ist, sondern nur zu den SW-Spezifikation

 en    für die  SW-Einheit

G.2.3 Übersicht über Produktvorlagen

G.2.3.1 Anbahnung und Organisation

Typ

Beschreibung

Externe Kopiervorlage

Externe Kopiervorlage

Checkliste Informationssicherheit
URI: https://itzbund.de/SharedDocs/Downloads/DE/VMXTBund/08_CL-
Informationssicherheit.xlsx?__blob=publicationFile

Informationssicherheits-Navigator
URI: https://itzbund.de/SharedDocs/Downloads/DE/VMXTBund/10_IS-
Navigator.pdf?__blob=publicationFile

Generierte Produktvorlage

Projektauftrag(.odt|.doc)

Generierte Produktvorlage

Projekthandbuch(.odt|.doc)

Generierte Produktvorlage

Projektvorstudie(.odt|.doc)

G.2.3.2 Planung und Steuerung

Typ

Beschreibung

Externe Kopiervorlage

Aufgabenliste
URI:
https://itzbund.de/SharedDocs/Downloads/DE/VMXTBund/11_Aufgabenli
ste.xls?__blob=publicationFile

Generierte Produktvorlage

Projektfortschrittsentscheidung(.odt|.doc)

Generierte Produktvorlage

Projektplan(.odt|.doc)

Generierte Produktvorlage

Schätzung(.odt|.doc)

G.2.3.3 Risikomanagement

Typ

Beschreibung

Externe Kopiervorlage

Risikoliste

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland





G.2 Produktvorlagen

307

Typ

Beschreibung

URI:
https://itzbund.de/SharedDocs/Downloads/DE/VMXTBund/13_Risikoliste.
xls?__blob=publicationFile

Generierte Produktvorlage

Risikoliste(.odt|.doc)

G.2.3.4 Problem- und Änderungsmanagement

Typ

Beschreibung

Externe Kopiervorlage

Änderungsstatusliste
URI:
https://itzbund.de/SharedDocs/Downloads/DE/VMXTBund/12_Aenderung
sstatusliste.xls?__blob=publicationFile

Generierte Produktvorlage

Problem-Änderungsbewertung(.odt|.doc)

Generierte Produktvorlage

ProblemmeldungÄnderungsantrag(.odt|.doc)

Generierte Produktvorlage

Änderungsentscheidung(.odt|.doc)

Generierte Produktvorlage

Änderungsstatusliste(.odt|.doc)

G.2.3.5 Qualitätssicherung

Typ

Beschreibung

Generierte Produktvorlage

Abnahmeprotokoll(.odt|.doc)

Generierte Produktvorlage

Abnahmespezifikation(.odt|.doc)

Generierte Produktvorlage

Nachweisakte(.odt|.doc)

Generierte Produktvorlage

Prüfprotokoll(.odt|.doc)

Generierte Produktvorlage

Prüfprotokoll Inbetriebnahme(.odt|.doc)

Generierte Produktvorlage

Prüfprotokoll Systemelement(.odt|.doc)

Generierte Produktvorlage

Prüfprozedur Systemelement(.odt|.doc)

Generierte Produktvorlage

Prüfspezifikation(.odt|.doc)

Generierte Produktvorlage

Prüfspezifikation Inbetriebnahme(.odt|.doc)

Generierte Produktvorlage

Prüfspezifikation Systemelement(.odt|.doc)

Generierte Produktvorlage

QS-Handbuch(.odt|.doc)

G.2.3.6 Messung und Analyse

Typ

Beschreibung

Generierte Produktvorlage

Kennzahlenauswertung(.odt|.doc)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

308

 Referenz Arbeitshilfen

G.2.3.7 Berichtswesen

Typ

Beschreibung

Generierte Produktvorlage

Besprechungsdokument(.odt|.doc)

Generierte Produktvorlage

Projektabschlussbericht(.odt|.doc)

Generierte Produktvorlage

Projektstatusbericht(.odt|.doc)

Generierte Produktvorlage

Projekttagebuch(.odt|.doc)

Generierte Produktvorlage

QS-Bericht(.odt|.doc)

G.2.3.8 Systemanalyse

Typ

Beschreibung

Externe Kopiervorlage

Externe Kopiervorlage

Checkliste für das Interview zur Schutzbedarfsfeststellung
URI: https://itzbund.de/SharedDocs/Downloads/DE/VMXTBund/09_CL-
Schutzbedarfsfeststellung.pdf?__blob=publicationFile

Lastenheft (ITZBund)
URI:
https://itzbund.de/SharedDocs/Downloads/DE/VMXTBund/14_Lastenheft
_ITZBund.docx?__blob=publicationFile

Generierte Produktvorlage

Altsystemanalyse(.odt|.doc)

Generierte Produktvorlage

Anforderungsbewertung(.odt|.doc)

Generierte Produktvorlage

Anwenderaufgabenanalyse(.odt|.doc)

Generierte Produktvorlage

Bewertung Lastenheft Gesamtprojekt(.odt|.doc)

Generierte Produktvorlage

Lastenheft (Anforderungen)(.odt|.doc)

Generierte Produktvorlage

Lastenheft Gesamtprojekt(.odt|.doc)

Generierte Produktvorlage

Make-or-Buy-Entscheidung(.odt|.doc)

Generierte Produktvorlage

Marktsichtung für Fertigprodukte(.odt|.doc)

Generierte Produktvorlage

Schutzbedarfsfeststellung(.odt|.doc)

Generierte Produktvorlage

Vorgaben zum Datenschutz(.odt|.doc)

Generierte Produktvorlage

Vorgaben zur Informationssicherheit(.odt|.doc)

G.2.3.9 Systementwurf

Typ

Beschreibung

Generierte Produktvorlage

Datenbankentwurf(.odt|.doc)

Generierte Produktvorlage

Erweiterung der Vorgaben zum Datenschutz(.odt|.doc)

Generierte Produktvorlage

Erweiterung der Vorgaben zur Informationssicherheit(.odt|.doc)

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

G.2 Produktvorlagen

309

Typ

Beschreibung

Generierte Produktvorlage

Implementierungs-, Integrations- und Prüfkonzept SW(.odt|.doc)

Generierte Produktvorlage

Implementierungs-, Integrations- und Prüfkonzept System(.odt|.doc)

Generierte Produktvorlage

Mensch-Maschine-Schnittstelle (Styleguide)(.odt|.doc)

Generierte Produktvorlage

Migrationskonzept(.odt|.doc)

Generierte Produktvorlage

Pflichtenheft (Gesamtsystementwurf)(.odt|.doc)

Generierte Produktvorlage

SW-Architektur(.odt|.doc)

Generierte Produktvorlage

Sicherheitskonzeption(.odt|.doc)

Generierte Produktvorlage

Systemarchitektur(.odt|.doc)

G.2.3.10 Systemspezifikation

Typ

Beschreibung

Generierte Produktvorlage

Externe-Einheit-Spezifikation(.odt|.doc)

Generierte Produktvorlage

Externes-SW-Modul-Spezifikation(.odt|.doc)

Generierte Produktvorlage

SW-Spezifikation(.odt|.doc)

Generierte Produktvorlage

Systemspezifikation(.odt|.doc)

G.2.3.11 Logistikelemente

Typ

Beschreibung

Generierte Produktvorlage

Ausbildungsunterlagen(.odt|.doc)

Generierte Produktvorlage

Nutzungsdokumentation(.odt|.doc)

G.2.3.12 IT-Organisation und Betrieb

Typ

Beschreibung

Generierte Produktvorlage

Betriebliche Freigabeerklärung(.odt|.doc)

Generierte Produktvorlage

Erweiterung der Vorgaben zum IT-Betrieb(.odt|.doc)

Generierte Produktvorlage

Leistungsvereinbarung (SLAOLAUC)(.odt|.doc)

Generierte Produktvorlage

Vorgaben zum IT-Betrieb(.odt|.doc)

G.2.3.13 Ausschreibungswesen (Vergabeakte)

Typ

Beschreibung

Externe Kopiervorlage

Bewertungsmatrix (Muster, Microsoft Excel)
URI:
https://itzbund.de/SharedDocs/Downloads/DE/VMXTBund/01_Bewertung

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

310

Typ

Externe Kopiervorlage

Externe Kopiervorlage

Externe Kopiervorlage

Externe Kopiervorlage

Externe Kopiervorlage

Externe Kopiervorlage

 Referenz Arbeitshilfen

Beschreibung

smatrix.xls?__blob=publicationFile

EVB-IT Erstellungsvertrag (Word)
URI:
https://itzbund.de/SharedDocs/Downloads/DE/VMXTBund/04_Vertragsmu
ster.docx?__blob=publicationFile

EVB-IT Systemvertrag (Word)
URI:
https://itzbund.de/SharedDocs/Downloads/DE/VMXTBund/07_Systemvert
rag.docx?__blob=publicationFile

Ergänzende Vertragsbedingungen für die Erstellung bzw. Anpassung von
Software (EVB-IT Erstellung)
URI:
https://itzbund.de/SharedDocs/Downloads/DE/VMXTBund/03_AGB_Erste
llung.pdf?__blob=publicationFile

Ergänzende Vertragsbedingungen für die Erstellung eines IT-Systems
(EVB-IT System)
URI:
https://itzbund.de/SharedDocs/Downloads/DE/VMXTBund/06_AGB_Syst
emvertrag.pdf?__blob=publicationFile

Nutzungshinweise EVB-IT System
URI:
https://itzbund.de/SharedDocs/Downloads/DE/VMXTBund/05_Nutzungshi
nweise.pdf?__blob=publicationFile

UfAB 2018 Bewertungsmatrix (Excel)
URI:
https://itzbund.de/SharedDocs/Downloads/DE/VMXTBund/02_Bewertung
smatrix_UfAB.xls?__blob=publicationFile

G.2.3.14 Vertragswesen

Typ

Beschreibung

Externe Kopiervorlage

Externe Kopiervorlage

Externe Kopiervorlage

EVB-IT Erstellungsvertrag (Word)
URI:
https://itzbund.de/SharedDocs/Downloads/DE/VMXTBund/04_Vertragsmu
ster.docx?__blob=publicationFile

EVB-IT Systemvertrag (Word)
URI:
https://itzbund.de/SharedDocs/Downloads/DE/VMXTBund/07_Systemvert
rag.docx?__blob=publicationFile

Ergänzende Vertragsbedingungen für die Erstellung bzw. Anpassung von
Software (EVB-IT Erstellung)
URI:

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

G.2 Produktvorlagen

311

Typ

Beschreibung

Externe Kopiervorlage

Externe Kopiervorlage

https://itzbund.de/SharedDocs/Downloads/DE/VMXTBund/03_AGB_Erste
llung.pdf?__blob=publicationFile

Ergänzende Vertragsbedingungen für die Erstellung eines IT-Systems
(EVB-IT System)
URI:
https://itzbund.de/SharedDocs/Downloads/DE/VMXTBund/06_AGB_Syst
emvertrag.pdf?__blob=publicationFile

Nutzungshinweise EVB-IT System
URI:
https://itzbund.de/SharedDocs/Downloads/DE/VMXTBund/05_Nutzungshi
nweise.pdf?__blob=publicationFile

Generierte Produktvorlage

Vertrag(.odt|.doc)

Generierte Produktvorlage

Vertragszusatz(.odt|.doc)

G.2.3.15 Lieferung und Abnahme

Typ

Beschreibung

Generierte Produktvorlage

Abnahmeerklärung(.odt|.doc)

G.3 V-Modell XT Projektassistent
Das Tailoring wird durch den V-Modell XT Projektassistenten unterstützt. Dieser bietet dem Projektleiter
folgende Funktionen:

➢ der Anpassung des V-Modells auf die Anforderungen des Projekts

➢ der Erzeugung einer projektspezifischen Dokumentation des V-Modells

➢ der initialen, groben Planung von Entscheidungspunkten

➢ der Erzeugung von Produktvorlagen (siehe auch Produktvorlagen)

Der Projektassistent führt schrittweise durch die einzelnen Stufen der projektspezifischen Anpassung und
hilft insbesondere bei der Erstellung des Anwendungsprofils. Dieses bezieht nur solche Teile des gesamten
V-Modells   mit   ein,   die   für   das   Projekt   erforderlich  sind.   Nicht   benötigte  Teile   werden   im  Rahmen   des
Tailorings   entfernt   (siehe   auch  FH+09).   Damit   erfüllt   der   Projektassistent   die   wesentlichen   in   der
Werkzeugreferenz Tailoring/Projektinitialisierung genannten Anforderungen.

G.3.1 Tailoring
Der Prozess zum Tailoring erfolgt in drei Schritten.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

312

 Referenz Arbeitshilfen

Abbildung 66: Auswahl von Projekttyp und Projekttypvariante im Projektassistenten

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

G.3 V-Modell XT Projektassistent

313

Abbildung 67: Festlegen des Anwendungsprofils mit Projektmerkmalen

Diese werden durch Reiter im Projektassistenten abgebildet:

1. Reiter 1 - Projekttyp

○ Zuerst   muss   einer   der   verfügbaren  Projekttyp

 en     ausgewählt   werden.   Dieser   gibt   eine   Reihe

verschiedener Vorgehensbausteine und Projektmerkmale vor.

○ Als   nächstes   muss   eine   der   verfügbaren  Projekttypen   und   Projekttypvarianten  ausgewählt
werden.   Jeder   Projekttyp   bieten   mindestens   eine   Projekttypvariante   an,   die   weitere
Vorgehensbausteine   und   Projektmerkmale   vorgeben   kann.   Die   Projekttypvariante   legen
gleichzeitig auch den Ablauf in Form einer Projektdurchführungsstrategie fest (Abbildung 66).

2. Reiter 2 - Anwendungsprofil

○ Nachdem Projekttyp und Projekttypvariante ausgewählt wurden, können die  Projektmerkmale
auf   dem   Reiter   Anwendungsprofil   mit   Werten   belegt   werden.   Der   Wertebereich   jedes
Projektmerkmals   ist   vorgegeben   und   es   befindet   sich   eine   kurze   Erläuterung   des
Projektmerkmals   in   einem  Tooltip,   der   erscheint,   wenn   man   kurz   mit   der   Maus   über   dem
Projektmerkmal   verharrt.   Je   nach   Wertebelegung   werden   dem   Projekt   weitere
Vorgehensbausteine  hinzugefügt oder auch Ergänzungen an der Projektdurchführungsstrategie
vorgenommen (Abbildung 67).

○ Die   Auswahl   der   Werte   der  Projektmerkmale

ist   zu   begründen.   Somit   ist   jederzeit
nachvollziehbar,   warum   ein   bestimmter   Wert   gewählt   wurde.   Die   Begründung   wird   in   die
Vorlage des Produkts Projekthandbuch übernommen.

3. Reiter 3 - Vorgehensbausteine

○ Auf diesem Reiter ist die Auswahl der Vorgehensbausteine zusammengefasst, die für das Projekt
relevant   sind.   Ferner   wird   für   die   ausgewählte   Projekttypvariante   angezeigt,   welche   dafür
bereitgestellten   Vorgehensbausteine   nicht   in   das   projektspezifische   V-Modell   aufgenommen
wurden (Abbildung 68).

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland


314

 Referenz Arbeitshilfen

Abbildung 68: Übersicht über die Vorgehensbausteine

G.3.2 Meilensteinplanung
Nach   der
  durch   die   Projekttypvariante   eine
Projektdurchführungsstrategie   zur   Verfügung,   die   für   die   Erstellung   eines   initialen   Meilenstein-   bzw.
Projektplans verwendet werden kann.

  projektspezifischen   Anpassung   steht

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

G.3 V-Modell XT Projektassistent

315

Abbildung 69: Planung mit dem Projektassistenten

Dazu   ist   im   linken   Teil   des   Projektassistenten   die   Schaltfläche  Planung  zu   wählen,   woraufhin   eine
Arbeitsfläche   angezeigt   wird   (Abbildung   69),   in   der   die  Entscheidungspunkte  gemäß   der   Vorgabe   der
Projektdurchführungsstrategie eingeplant werden können.

Ein Mausklick in die Arbeitsfläche legt den ersten Entscheidungspunkt  Projekt genehmigt  an und versieht
diesen mit einem Datum. Nach einem Doppelklick auf das Datum öffnet sich ein Kalender und ermöglicht
die Festlegung eines neuen Termins. Wird mit einem einfachen Klick nur der Entscheidungspunkt gewählt,
erscheint im rechten unteren Bereich des Symbols ein "+". Wird dieses angeklickt, stellt der Projektassistent
eine   Liste   der   nächsten  möglichen   Entscheidungspunkte,   sowie  freie   Meilensteine  dar.   Die   angebotenen
Entscheidungspunkte   entsprechen   den   Vorgaben   der   Projektdurchführungsstrategie.   Freie   Meilensteine
können   immer   eingetragen   werden.   Sie   eignen   sich   zur   Einplanung   von   Terminen   oder
Zwischenmeilensteinen,   die   zwar   bei   der   Planung   bereits   bekannt,   jedoch   nicht   durch   die
Projektdurchführungsstrategie   abgedeckt   sind.   Beim   Auswählen   eines   Entscheidungspunkts   mit   einem
einfachen Mausklick erscheint ein "x" im rechten oberen Bereich. Dieses dient dazu, den aktuellen  und alle
folgenden Entscheidungspunkte aus dem Plan zu entfernen.

Bei   Projektdurchführungsstrategien,   die   Verzweigungen   im   Projektablauf   vorsehen   (z.B.   innerhalb   der
Projekttypvariante  AG/AN-Projekt   mit   Entwicklung,   Weiterentwicklung   oder   Migration),   können   auch
parallele   Abläufe  geplant   werden.   Der   Projektassistent   zeigt   dann   im   Folgenden   auch   an,   zu   welchen
anderen Entscheidungspunkten die parallelen Abläufe wieder zusammengeführt werden können.

Der Projektassistent überprüft die Planung auf Konsistenz und damit, ob alle Entscheidungspunkte in einer
korrekten Reihenfolge sind und ob alle geöffneten Parallelabläufe wieder ordnungsgemäß zusammengeführt
wurden.   Im   Falle   einer   Inkonsistenz,   wird   eine   entsprechende   Fehlermeldung   im   Kopf   des
Bearbeitungsformulars angezeigt.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

316

 Referenz Arbeitshilfen

G.3.3 Vorlagengenerierung
Sobald eine Projektdurchführungsstrategie nach dem Tailoringprozess feststeht, kann diese für die Erstellung
von Produktvorlagen und Verwendung von Kopiervorlagen eingesetzt werden.

Dazu   ist   im   linken   Teil   des   Projektassistenten   die   Schaltfläche  Vorlagen  zu   wählen,   woraufhin   eine
Arbeitsfläche angezeigt wird (Abbildung 70). Hier ist die Liste aller Produkte aufgeführt, die für das Projekt
relevant sind, sofern kein Haken bei  Auch Elemente zeigen, die für das Projekt nicht relevant sind  gesetzt
wurde.

Die   vorgeschlagene  Auswahl   an   Produkten   und   Textbausteinen   kann   übernommen   oder   nach   Belieben
geändert   werden.   Änderungen   können   durch   Auswählen   der   Buttons   (Alle/Keine/Nur   Initiale
Produktvorlagen; Alle/Keine Themenbeschreibungen; Alle/Keine Mustertexte (sofern vorhanden)) oder über
selektives   Anklicken   der   Checkboxen   vorgenommen   werden.   Mustertexte   sind   Text-Vorlagen   für   die
Ausgestaltung von Themen, Unterthemen und Zusatzthemen. Der Button  Vorlagen erzeugen  am Ende der
Seite startet den Generierungsvorgang und legt alle selektierten Vorlagen im angegebenen Exportverzeichnis
ab.   Bei   der   Generierung   der  Produktvorlagen  kann   eines   der   Exportformate   gewählt   werden.   Die
Kopiervorlagen sind an das Dateiformat der jeweiligen Vorlage gebunden. Das Exportverzeichnis kann über
den Button „Ändern“ gewechselt werden.

Abbildung 70: Vorlagen mit dem Projektassistenten

G.3.4 Export
Nach Abschluss der projektspezifischen Anpassung und der initialen Planung kann das projektspezifische V-
Modell exportiert werden.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

G.3 V-Modell XT Projektassistent

317

Es dient hierbei als Quelle für verschiedene Exporte:

Abbildung 71: Export der Prozessdokumentation

➢ Prozessdokumentation:   Über   die   Schaltfläche  Tailoring  wird   die   Tailoringansicht   für   die
projektspezifische   Anpassung   gewählt.   Im   unteren   Bereich   befindet   sich   ein   Feld,   das   den
Exportpfad enthält. Mithilfe der Schaltfläche  Ändern kann dieser Pfad angepasst werden. Über die
Schaltfläche  V-Modell exportieren... gelangt man zu einem Dialog (Abbildung 71), der den Export
der verschiedenen Teile der Prozessdokumentation in den Exportformaten HTML, PDF und ODT
ermöglicht.

➢ Projektplan: Im unteren Bereich des Planungsformulars befindet sich ein Feld, das den Exportpfad
für den Projektplan enthält. Mithilfe der Schaltfläche  Ändern  kann dieser Pfad angepasst werden.
Über die Schaltfläche  Projektplan exportieren...  gelangt man zu einem Dialog, der den Export des
Projektplans in den Formaten Gantt-Project, Text (CSV) und XML (Microsoft Project 2003 und
höher) ermöglicht.

➢ Produktvorlagen:   Der   Projektassistent   unterstützt   auch   die   Erzeugung   von   Produktvorlagen   auf
Basis   des   projektspezifischen   V-Modells.   Im   Kapitel  Vorlagengenerierung  werden   das   dazu
erforderliche Vorgehen sowie weitere Hintergrundinformationen zu Vorlagen beschrieben.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

318

 Referenz Arbeitshilfen

G.4 Arbeitshilfenindex
Modellelement

Abnahmeerklärung(.odt|.doc)

Abnahmeprotokoll(.odt|.doc)

Abnahmespezifikation(.odt|.doc)

Altsystemanalyse(.odt|.doc)

Änderungsentscheidung(.odt|.doc)

Änderungsstatusliste

Änderungsstatusliste(.odt|.doc)

Anforderungsanalyse

Anforderungsbewertung(.odt|.doc)

Anforderungsmanagement

Anwenderaufgabenanalyse(.odt|.doc)

Aufgabenliste

Ausbildungsunterlagen(.odt|.doc)

Besprechungsdokument(.odt|.doc)

Betriebliche Freigabeerklärung(.odt|.doc)

Bewertung Lastenheft Gesamtprojekt(.odt|.doc)

Typ

Generierte
Produktvorlage

Generierte
Produktvorlage

Generierte
Produktvorlage

Generierte
Produktvorlage

Generierte
Produktvorlage

Seite

311

307

307

308

307

Externe Kopiervorlage

307

Generierte
Produktvorlage

Methodenreferenz

Generierte
Produktvorlage

Werkzeugreferenz

Generierte
Produktvorlage

307

275

308

296

308

Externe Kopiervorlage

306

Generierte
Produktvorlage

Generierte
Produktvorlage

Generierte
Produktvorlage

Generierte
Produktvorlage

309

308

309

308

Bewertungsmatrix (Muster, Microsoft Excel)

Externe Kopiervorlage

309

Bewertungsverfahren

Methodenreferenz

277

Checkliste für das Interview zur Schutzbedarfsfeststellung

Externe Kopiervorlage

308

Checkliste Informationssicherheit

Compiler

Externe Kopiervorlage

306

Werkzeugreferenz

297

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

G.4 Arbeitshilfenindex

Modellelement

Datenbankentwurf(.odt|.doc)

Datenbankmodellierung

Designverifikation

319

Typ

Generierte
Produktvorlage

Methodenreferenz

Methodenreferenz

Seite

308

278

278

Ergänzende Vertragsbedingungen für die Erstellung bzw. Anpassung
von Software (EVB-IT Erstellung)

Externe Kopiervorlage

310

Ergänzende Vertragsbedingungen für die Erstellung bzw. Anpassung
von Software (EVB-IT Erstellung)

Externe Kopiervorlage

310

Ergänzende Vertragsbedingungen für die Erstellung eines IT-Systems
(EVB-IT System)

Externe Kopiervorlage

310

Ergänzende Vertragsbedingungen für die Erstellung eines IT-Systems
(EVB-IT System)

Externe Kopiervorlage

311

Erweiterung der Vorgaben zum Datenschutz(.odt|.doc)

Erweiterung der Vorgaben zum IT-Betrieb(.odt|.doc)

Erweiterung der Vorgaben zur Informationssicherheit(.odt|.doc)

EVB-IT Erstellungsvertrag (Word)

EVB-IT Erstellungsvertrag (Word)

EVB-IT Systemvertrag (Word)

EVB-IT Systemvertrag (Word)

Externe-Einheit-Spezifikation(.odt|.doc)

Externes-SW-Modul-Spezifikation(.odt|.doc)

Fehler-/Änderungsmanagement

Geschäftsprozessmodellierung

GUI-Werkzeug

Implementierungs-, Integrations- und Prüfkonzept SW(.odt|.doc)

Generierte
Produktvorlage

Generierte
Produktvorlage

Generierte
Produktvorlage

308

309

308

Externe Kopiervorlage

310

Externe Kopiervorlage

310

Externe Kopiervorlage

310

Externe Kopiervorlage

310

Generierte
Produktvorlage

Generierte
Produktvorlage

Werkzeugreferenz

Methodenreferenz

Werkzeugreferenz

Generierte
Produktvorlage

309

309

297

279

297

309

309

Implementierungs-, Integrations- und Prüfkonzept System(.odt|.doc) Generierte

Informationssicherheits-Navigator

Integrierte Entwicklungsumgebung

Produktvorlage

Externe Kopiervorlage

306

Werkzeugreferenz

298

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

320

Modellelement

Kennzahlenauswertung(.odt|.doc)

KM-Werkzeug

Konstruktion/Simulation

Lastenheft (Anforderungen)(.odt|.doc)

Lastenheft (ITZBund)

Lastenheft Gesamtprojekt(.odt|.doc)

Leistungsvereinbarung (SLAOLAUC)(.odt|.doc)

Make-or-Buy-Entscheidung(.odt|.doc)

Marktsichtung für Fertigprodukte(.odt|.doc)

Mensch-Maschine-Schnittstelle (Styleguide)(.odt|.doc)

Migrationskonzept(.odt|.doc)

Modellierung funktionaler Anforderungen (UML)

Modellierungswerkzeug

Nachweisakte(.odt|.doc)

Nutzungsdokumentation(.odt|.doc)

Nutzungshinweise EVB-IT System

Nutzungshinweise EVB-IT System

Pflichtenheft (Gesamtsystementwurf)(.odt|.doc)

Problem-Änderungsbewertung(.odt|.doc)

ProblemmeldungÄnderungsantrag(.odt|.doc)

Projektabschlussbericht(.odt|.doc)

Projektauftrag(.odt|.doc)

 Referenz Arbeitshilfen

Typ

Generierte
Produktvorlage

Werkzeugreferenz

Werkzeugreferenz

Generierte
Produktvorlage

Seite

307

298

299

308

Externe Kopiervorlage

308

Generierte
Produktvorlage

Generierte
Produktvorlage

Generierte
Produktvorlage

Generierte
Produktvorlage

Generierte
Produktvorlage

Generierte
Produktvorlage

Methodenreferenz

Werkzeugreferenz

Generierte
Produktvorlage

Generierte
Produktvorlage

308

309

308

308

309

309

280

299

307

309

Externe Kopiervorlage

310

Externe Kopiervorlage

311

Generierte
Produktvorlage

Generierte
Produktvorlage

Generierte
Produktvorlage

Generierte
Produktvorlage

Generierte

309

307

307

308

306

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

G.4 Arbeitshilfenindex

Modellelement

321

Typ

Seite

Projektfortschrittsentscheidung(.odt|.doc)

Projekthandbuch(.odt|.doc)

Projektplan(.odt|.doc)

Projektplanung

Projektplanung und -steuerung

Projektstatusbericht(.odt|.doc)

Projekttagebuch(.odt|.doc)

Projektvorstudie(.odt|.doc)

Prototyping

Prozessanalyse

Prüfprotokoll(.odt|.doc)

Prüfprotokoll Inbetriebnahme(.odt|.doc)

Prüfprotokoll Systemelement(.odt|.doc)

Prüfprozedur Systemelement(.odt|.doc)

Prüfspezifikation(.odt|.doc)

Prüfspezifikation Inbetriebnahme(.odt|.doc)

Prüfspezifikation Systemelement(.odt|.doc)

QS-Bericht(.odt|.doc)

QS-Handbuch(.odt|.doc)

Produktvorlage

Generierte
Produktvorlage

Generierte
Produktvorlage

Generierte
Produktvorlage

Werkzeugreferenz

Methodenreferenz

Generierte
Produktvorlage

Generierte
Produktvorlage

Generierte
Produktvorlage

Methodenreferenz

Methodenreferenz

Generierte
Produktvorlage

Generierte
Produktvorlage

Generierte
Produktvorlage

Generierte
Produktvorlage

Generierte
Produktvorlage

Generierte
Produktvorlage

Generierte
Produktvorlage

Generierte
Produktvorlage

Generierte
Produktvorlage

306

306

306

299

282

308

308

306

283

283

307

307

307

307

307

307

307

308

307

Review

Methodenreferenz

285

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

322

Modellelement

Risikoliste

Risikoliste(.odt|.doc)

Schätzmodelle

Schätzung(.odt|.doc)

Schutzbedarfsfeststellung(.odt|.doc)

Sicherheitskonzeption(.odt|.doc)

Simulation

SW-Architektur(.odt|.doc)

SW-Spezifikation(.odt|.doc)

Systemanalyse

Systemarchitektur(.odt|.doc)

Systemdesign

Systemspezifikation(.odt|.doc)

Tailoring/Projektinitialisierung

Test

Tools zum IT-Grundschutz

 Referenz Arbeitshilfen

Typ

Seite

Externe Kopiervorlage

306

Generierte
Produktvorlage

Methodenreferenz

Generierte
Produktvorlage

Generierte
Produktvorlage

Generierte
Produktvorlage

Methodenreferenz

Generierte
Produktvorlage

Generierte
Produktvorlage

Methodenreferenz

Generierte
Produktvorlage

Methodenreferenz

Generierte
Produktvorlage

Werkzeugreferenz

Methodenreferenz

Werkzeugreferenz

307

287

306

308

309

288

309

309

288

309

291

309

300

291

300

UfAB 2018 Bewertungsmatrix (Excel)

Externe Kopiervorlage

310

Vertrag(.odt|.doc)

Vertragszusatz(.odt|.doc)

V-Modell XT Projektassistent

Vom Lastenheft zum Kriterienkatalog

Vorgaben zum Datenschutz(.odt|.doc)

Vorgaben zum IT-Betrieb(.odt|.doc)

Generierte
Produktvorlage

Generierte
Produktvorlage

Werkzeugreferenz

Methodenreferenz

Generierte
Produktvorlage

Generierte
Produktvorlage

311

311

300

292

308

309

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

G.4 Arbeitshilfenindex

Modellelement

Vorgaben zur Informationssicherheit(.odt|.doc)

WiBe-Kalkulator

323

Typ

Generierte
Produktvorlage

Seite

308

Werkzeugreferenz

301

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

324

 Anhang

H Anhang

H.1 Glossar
Begriff

Akteur

Aktivität

Aktivitätsexemplar

Aktivitätsstruktur

Aktivitätstyp

Anforderungscontrolling

Anwendungsprofil

Arbeitspaket

Erläuterung

Akteure (externe Beteiligte außerhalb des Systems) sind an Anwendungs-
bzw. Geschäftsfällen beteiligt. Es muss zwischen primären und sekundären
Akteuren unterschieden werden. Ein primärer Akteur ist derjenige, der
einen Anwendungs- bzw. Geschäftsfall auslöst (z.B. ein Kunde, der eine
bestimmte Dienstleistung vom fachlichen System erwartet). Bei dem
Kunden kann es sich um einen "echten" Kunden handeln oder auch z.B. um
Abteilungen oder andere (fachliche) Systeme. Ein sekundärer Akteur sind
Personen oder Systeme, die zur externen Unterstützung für die Umsetzung
von Anwendungs- bzw. Geschäftsfällen benötigt werden.

Man unterscheidet zwischen Aktivitätstyp und Aktivitätsexemplar. Im V-
Modell-Kontext bezeichnet der Begriff Aktivität im Allgemeinen einen
Aktivitätstyp.

Unter einem Aktivitätsexemplar versteht man die konkrete Ausprägung
eines Aktivitätstyp
Software-Einheit.

 s  , zum Beispiel die Realisierung einer bestimmten

Unter dem Begriff Aktivitätsstruktur versteht man die Menge der
Aktivitätsexemplar

 e   eines Projekts und deren Zusammenhänge.

Ein Aktivitätstyp (im Folgenden kurz als "Aktivität" bezeichnet) beschreibt
Aktivitätsexemplar
 e  , die während eines Entwicklungsprozesses ausgeführt
werden können.
Aktivitäten sind Bestandteil genau einer Disziplin und damit stets einem
Vorgehensbaustein zugeordnet. Jedes Produkt wird einer es bearbeitenden
Aktivität zugeordnet. Aktivitäten verändern also Produkte. Produkte, die in
einer Aktivität nur als Eingabe dienen, werden nicht explizit einer Aktivität
zugeordnet. Bei Fertigstellung eines Produkts ist dieses im Produktzustand
fertig gestellt und die dem Produkt zugeordneten
Fertigstellungsbedingungen gelten.

Das Anforderungscontrolling unterstützt bei der Identifikation der unter
Kosten- und Nutzungsgesichtspunkten besten Umsetzungsalternative einer
Anforderung.

Ein Anwendungsprofil stellt die Wertbelegung der einzelnen
Projektmerkmal
Anwendungsprofils findet ein erstes Tailoring statt.

 e   im konkreten Projekt dar. Anhand dieses

Ein Arbeitspaket ist eine projektspezifische inhaltliche Gruppierung von
Aktivitätsexemplar
 en   .
Beispielsweise können Aktivitätsexemplar
Konfigurationsmanagement zu einem Arbeitspaket zusammengefasst
werden, da unter Umständen keine terminliche Planung dieser

 e   aus dem

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland







H.1 Glossar

325

Begriff

Erläuterung

Architektur

Auftraggeber

Auftraggeber-/Auftragnehmer-
Schnittstelle

Auftragnehmer

Datenschutz

Datenschutz-
Grundverordnung

Disziplin

dynamisches Tailoring

Entscheidungspunkt

Aktivitätsexemplare im Einzelnen erfolgen muss.

Architektur ist der Oberbegriff für die Produkte Systemarchitektur und SW-
Architektur.

Unter einem Auftraggeber wird der Kunde im Rahmen einer
Vertragssituation verstanden, also der Empfänger eines vom Auftragnehmer
bereitgestellten Produkt

 s   (DIN EN ISO 8402).

Die Auftraggeber-/Auftragnehmer-Schnittstelle beschreibt explizit, welche
 e   zwischen dem Auftraggeber- und dem Aufragnehmer-V-Modell-
Produkt
Projekt ausgetauscht werden. Diese Produkte werden
 e   genannt.
Schnittstellenprodukt

Unter einem Auftragnehmer wird der Lieferant im Rahmen einer
Vertragssituation verstanden, also die Organisation, die dem Auftraggeber
ein Produkt bereitstellt (DIN EN ISO 8402).

Aufgabe des Datenschutzes ist es, den Einzelnen davor zu schützen, dass er
durch den Umgang mit seinen personenbezogenen Daten in seinem
Persönlichkeitsrecht beeinträchtigt wird. (Quelle:
Bundesdatenschutzgesetz)

VERORDNUNG (EU) 2016/679 DES EUROPÄISCHEN PARLAMENTS
UND DES RATES vom 27. April 2016 zum Schutz natürlicher Personen
bei der Verarbeitung personenbezogener Daten, zum freien Datenverkehr
und zur Aufhebung der Richtlinie 95/46/EG (Datenschutz-
Grundverordnung)

 e   und Aktivität

 en    des V-Modell

 s   sind hierarchisch strukturiert.

Die Produkt
Auf der obersten Ebene befinden sich Disziplinen. Eine Disziplin ist eine
Gruppierung einer Menge von inhaltlich eng zusammenhängenden
Produkten und der Aktivitäten, die die enthalten Produkte erstellen. Jedes
Produkt ist genau einer Disziplin fest zugeordnet. Darüber hinaus existieren
Querschnittsdisziplinen, die orthogonal zu den Disziplinen stehen und
denen Produkte nur "lose" zugeordnet werden. Beispielsweise ist das
Produkt Logistische Berechnungen und Analysen einerseits der Disziplin
Systemanalyse fest zugeordnet, andererseits aber auch Teil der
Querschnittsdisziplin Logistikkonzeption. Querschnittsdisziplinen finden
sich ausschließlich im Kapitel Inhalte des V-Modell XT, dienen aber nicht
zur Gruppierung in den Referenzteilen.

Dynamisches Tailoring ist das Tailoring, das nach der Projektinitialisierung
und damit während der Projektlaufzeit durchgeführt wird, also nach dem
Entscheidungspunkt Projekt initialisiert.

In einem Entscheidungspunkt wird über das Erreichen einer
Projektfortschrittsstufe entschieden. Diese Entscheidung wird auf Basis der
zum Entscheidungspunkt vorzulegenden, fertig gestellt
getroffen
Die Reihenfolge, in welcher die Entscheidungspunkte im Rahmen eines
Projekts durchlaufen werden müssen, wird in der
Projektdurchführungsstrategie festgelegt.

 en    Produkt

 e

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland









326

Begriff

Entwicklung, inkrementell

Entwicklung,
komponentenbasierte

Entwicklung, prototypische

 Anhang

Erläuterung

 en    vorliegen, die dann anhand einer SW-

Eine Entwicklungsstrategie, bei der zunächst das Gesamtsystem in einem
Pflichtenheft (Gesamtsystementwurf) spezifiziert wird. Der Systementwurf
wird anschließend nach dem Divide&Conquer-Prinzip immer weiter
verfeinert bis SW-Spezifikation
Architektur umgesetzt und integriert werden.
Der Auftragnehmer entwirft, realisiert und liefert das System in einzelnen
Stufen, welche auch Inkrement genannt werden. Jede dieser Stufen wird
einzeln vom Auftraggeber abgenommen und entweder im Vorfeld
vertraglich vereinbart oder es werden zusätzliche Verträge über die
Abwicklung ergänzender Inkremente abgeschlossen. Bevor ein Inkrement
an den Auftraggeber ausgeliefert wird, kann der Auftragnehmer intern
mehrere Iterationen durchlaufen.
Änderungen durch den Auftraggeber innerhalb eines Inkrements sind bei
dieser Entwicklungsstrategie zu vermeiden und sollten über das
Änderungsmanagement im folgenden Inkrement berücksichtigt werden.
Wichtige Änderungen, die beispielsweise die Architektur des Systems
maßgeblich beeinflussen könnten, sollten dem Auftragnehmer so früh wie
möglich mitgeteilt werden. Für den Auftraggeber hat diese Vorgehensweise
den Vorteil, dass er frühzeitig in den Besitz einer Vorstufe des Systems
gelangt, die bereits die wichtigsten Grundfunktionalitäten des Systems
realisiert.
Diese Entwicklungsstrategie eignet sich vor allem dann, wenn die
Anforderungen an das System als relativ stabil eingeschätzt werden und
technologische Risiken eher gering sind. Es können Fertigprodukte
eingesetzt werden, der Hauptanteil des Systems wird jedoch im Rahmen
des Projekts erstellt.

Der Entwicklungsstrategie komponentenbasierte Entwicklung liegt die Idee
zugrunde, dass das neue System weitgehend durch Integration bestehender
Systemelemente erstellt wird. Ein für die Integration vorgesehenes
Systemelement (z.B. ein Segment oder eine HW/SW-Einheit) hat eine klar
definierte Schnittstelle nach außen, kapselt Entwurf und Implementierung
und kann mit anderen Systemelementen verbunden werden. Es ist sowohl
fachlich als auch technisch unabhängig und besitzt eine gewisse Größe (im
Sinne eines wirtschaftlichen Wertes).
Allgemein werden von einem Systemelement für die Integration folgende
Eigenschaften verlangt:

➢ Verfügbarkeit klarer, sauber definierter Schnittstellen
➢ Kommunikation mit der Außenwelt (zum Beispiel mit anderen
Komponenten) ausschließlich über die definierten Schnittstellen
➢ Anpassung an bestimmte Anwendungsumgebungen (Customizing)

nur über die Schnittstellen

➢ Realisierungsspezifika bleiben dem Benutzer verborgen (Blackbox-

Sichtweise)

Die prototypische Entwicklung
  basiert auf der Erkenntnis, dass es
oft nicht möglich ist, die Anforderungen an ein System vorab zu definieren.
Außerdem stellt sie sicher, dass nichts spezifiziert wird, was sich als nicht
realisierbar herausstellt. Somit wird diese Strategie insbesondere

 sstrategie

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland




H.1 Glossar

327

Begriff

Erläuterung

verwendet, wenn Realisierungsrisiken im Projekt vorhanden sind.
Änderungen an den Anforderungen werden über das Problem- und
Änderungsmanagement verwaltet.
Typisch für diese Entwicklungsstrategie ist darüber hinaus die Präsenz des
Auftraggebers auf der Auftragnehmerseite während der Entwicklung.
Dadurch kann der Auftraggeber Änderungswünsche sehr direkt
übermitteln. Der Auftragnehmer entwirft, realisiert und liefert das System
dann ähnlich wie bei der Entwicklungsstrategie inkrementelle Entwicklung
in einzelnen Stufen. Diese Stufen werden jede für sich vom Auftraggeber
abgenommen. Für den Auftraggeber hat diese Vorgehensweise den Vorteil,
dass er bereits frühzeitig in den Besitz eines lauffähigen Systems gelangt,
das die wichtigsten Grundfunktionalitäten realisiert. Ferner ermöglicht sie
eine frühzeitige Rückmeldung durch den Auftraggeber, die die
Entwicklungsrisiken des Auftragnehmers minimiert.

Entwicklungsstandards für IT-
Systeme des Bundes

siehe V-Modell.

erzeugende
Produktabhängigkeit

Externe Einheit

siehe Produktabhängigkeit, erzeugende.

Unter dem Produkt Externe Einheit versteht man Systemelemente, die nicht
innerhalb des Projekts entwickelt werden. Bei einem Produkt vom Typ
Externe Einheit kann es sich um ein Fertigprodukt, eine Beistellung des
Auftraggebers, ein im Vorfeld entwickeltes System oder Segment, welches
wiederverwendet wird, ein Nachbarsystem oder das Ergebnis eines
Unterauftrags handeln. Eine Externe Einheit kann sowohl HW- als auch
SW-Anteile umfassen.

externes HW-Modul

siehe HW-Modul, externes.

externes Produkt

siehe Produkt, externes.

externes SW-Modul

siehe SW-Modul, externes.

fertig gestellt

Funktionssicherheit

HW-Element

 s  , das fertig gestellt ist. Für
Definiert einen Produktzustand eines Produkt
diesen Begriff "fertig gestellt" wird häufig auch der Begriff "freigegeben"
oder auch "gültig" verwendet. Dieser Produktzustand wird in der
Produktbibliothek gesetzt.

Die Funktionssicherheit steht für die Verfahrens- oder Betriebssicherheit
sowie für Zuverlässigkeit, Fehlertoleranz und Korrektheit. Dieser Zustand
ergibt sich aus Maßnahmen, durch die das Risiko eines Personen-, Sach-
oder immateriellen Schadens auf einen annehmbaren Wert begrenzt ist.

Der Begriff HW-Element ist ein Oberbegriff, der in der Hierarchie der
Systemelement
bezeichnen kann: HW-Einheit, HW-Komponente, HW-Modul und Externes
HW-Modul.

 e   alle Systemelemente ab der Ebene der HW-Einheit

HW-Modul, externes

Unter dem Produkt Externes HW-Modul versteht man Systemelemente
(HW-Module, HW-Komponenten), die nicht innerhalb des Projekts
entwickelt werden. Ein Externes HW-Modul ist ein selbständig

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland



328

Begriff

 Anhang

Erläuterung

beschreibbares Funktionselement. Dabei kann es sich um ein Fertigprodukt,
eine Beistellung des Auftraggebers, eine im Vorfeld entwickelte
Komponente, die wiederverwendet wird, ein Nachbarsystem oder das
Ergebnis eines Unterauftrags handeln.

in Bearbeitung

Definiert einen Produktzustand eines Produkt
befindet. Dieser Produktzustand wird in der Produktbibliothek gesetzt.

 s  , das sich in der Bearbeitung

Informationssicherheit

Informationssicherheits-
Managementsystem

Informationsverbund

Informationssicherheit beschreibt den Zustand, der die Verfügbarkeit, die
Integrität, die Verbindlichkeit und die Vertraulichkeit von Informationen
gewährleistet. Dieser Zustand ergibt sich aus technischen Maßnahmen
sowie aus Maßnahmen personeller, materieller (beinhaltet baulich-
technische Maßnahmen) und organisatorischer Art.

Ein Informationssicherheits-Managementsystem (ISMS) ist ein
Rahmenwerk zur Etablierung und Fortführung eines kontinuierlichen
Prozesses zur Planung, Lenkung und Kontrolle der Konzepte und
Aufgaben, die auf die Wahrung der Ziele der Informationssicherheit in
einer Organisation gerichtet sind. Die internationale Norm für ISMS ist der
Standard ISO/IEC 27001. Das Bundesamt für Sicherheit in der
Informationstechnik (BSI) stellt im Rahmen des IT-Grundschutzes den
dazu kompatiblen BSI-Standard 200-1 bereit. Dieser wird ergänzt von den
BSI-Standards 200-2 zur IT-Grundschutz-Vorgehensweise und 200-3 zum
Risikomanagement sowie dem IT-Grundschutz-Kompendium mit seinen
konkreten Anforderungen.

Der Geltungsbereich eines IT-Sicherheitskonzepts wird als
Informationsverbund bezeichnet und stellt detailliert den Bereich dar, für
den das Sicherheitskonzept umgesetzt werden soll. Ein
Informationsverbund kann sich somit auf Fachaufgaben, Geschäftsprozesse
oder Organisationseinheiten beziehen. Er umfasst alle infrastrukturellen,
organisatorischen, personellen und technischen Komponenten, die der
Aufgabenerfüllung in diesem Anwendungsbereich der
Informationsverarbeitung dienen. Der Informationsverbund muss so
festgelegt sein, dass die betrachteten Geschäftsprozesse und Informationen
diesem Bereich vollständig zugeordnet werden können. Die
Abhängigkeiten aller sicherheitsrelevanten Prozesse sind zu
berücksichtigen. Die Schnittstellen zu den anderen Bereichen müssen klar
definiert werden, so dass der Informationsverbund in der
Gesamtorganisation eine sinnvolle Mindestgröße einnimmt.

inhaltliche
Produktabhängigkeit

siehe Produktabhängigkeit, inhaltliche.

initiales Produkt

siehe Produkt, initiales.

Inkrement

Bei einer Projektdurchführungsstrategie AN-Projekt mit Entwicklung,
Weiterentwicklung oder Migration wird der zu erstellende SW-/HW-
Gegenstand in einer stufenweisen Vorgehensweise entwickelt. Die
Entwicklung findet in Iteration
aufeinanderfolgend entwickelt. Jedes Inkrement ist inhaltlich weitgehend
unabhängig von den anderen Inkrementen, so dass mit jeder Fertigstellung
 s   bei der Lieferung ein lauffähiges System zur Verfügung
eines Inkrement

 en    statt, d.h. die Stufen werden

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland




H.1 Glossar

329

Begriff

Erläuterung

inkrementelle Entwicklung

siehe Entwicklung, inkrementell.

steht. Ein Inkrement kann Gegenstand einer Iteration sein.

Integrität

Iteration

komponentenbasierte
Entwicklung

konkludente Abnahme

Konsistenz

Konventionsabbildung

Messdatentyp

Integrität ist der Zustand, der unbefugte und unzulässige Veränderungen
von Informationen und an IT-Systemen oder -Komponenten ausschließt.

Eine Iteration bezeichnet einen einzelnen Entwicklungszyklus bei der
Systemerstellung. Eine iterative Vorgehensweise bringt periodisch
wiederkehrende ähnliche Aufgaben der Systementwicklung mit sich, bei
denen der Gegenstand in jeder Iteration entweder ein anderer ist (z.B.
Entwicklung unterschiedlicher Teilsysteme in aufeinanderfolgenden
Inkrement
 en    überarbeitet
werden (z.B. die schrittweise Verfeinerung und Ausgestaltung von
Systemen).

 en   ) oder in aufeinander folgenden Iteration

siehe Entwicklung, komponentenbasierte.

Die konkludente Abnahme (lat. concludere "folgern", "einen Schluss
ziehen") wird oft auch "stille Abnahme" genannt und erfolgt aufgrund von
schlüssigem Handeln des Auftraggebers. Hierunter fällt beispielsweise die
Bezahlung oder die Nutzung des Systems.
Wenn das System aus Sachzwängen heraus trotz bestehender Mängel in
Betrieb genommen werden muss, sollte zuvor sichergestellt sein, dass sich
daraus keine Abnahme ableiten lässt. Die EVB-IT schließen die
konkludente Abnahme explizit aus.

Ein Produkt, das in den Zustand fertig gestellt überführt werden soll, wird
im Rahmen einer Eigenprüfung und gegebenenfalls einer eigenständigen
Qualitätssicherungauf Konsistenz hinsichtlich seiner relevante
Produktabhängigkeit

 en    geprüft.

 en    stellen den Bezug des V-Modell

Konventionsabbildung
(Quasi-)Standards, Normen und Vorschriften dar.
Eine Konventionsabbildung setzt dazu die Begriffe, die in der Konvention
definiert sind, in Beziehung zu dem Begriffssystem des V-Modells.

 s   zu aktuellen

Jeder Messdatentyp beschreibt ein Maß, das direkt ermittelt wird (z.B.
durch Zählen von Fehlern, Zählen von Stunden, Messen einer Dauer), und
als konkret gemessener Wert (Messdatum) in die Ermittlung einer Metrik
eingeht. Synonyme für Messdatentypen sind Basisdaten bzw. Messgrößen.
Messdatentypen

➢ sind absolute Werte,
➢ werden durch Messen an Projekt, Produkt oder Prozess gewonnen,
➢ können sich z.B. auf Zeitpunkte, Phasen, Produkte,

Organisationsbereiche beziehen.

Messdatentypen können auch "weich" sein, d.h. sie ergeben sich aus
informellen Erhebungen und individuellen Einschätzungen, z.B.
Risikowahrscheinlichkeit gering/mittel/hoch.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland






330

Begriff

Erläuterung

Messdatentypen

siehe Messdatentyp.

 Anhang

Methodenreferenz

Metrik

Eine Methodenreferenz beschreibt eine Klasse von Methoden, die zur
Durchführung von Aktivitäten beziehungsweise Erstellung von Produkte
verwendet werden können.

Synonym: Kennzahlen
Eine Metrik beschreibt ein quantitatives Maß für eine Eigenschaft eines
Projekts, eines Produkt

 s   oder eines Prozesses.

➢ Metriken werden aus Messdatentypen oder anderen Metriken

abgeleitet (z.B. Formeln, Prozentsätzen, Gegenüberstellungen).

➢ Ein Messdatentyp kann auch eine Metrik sein.

Mitarbeiterentwicklungsplan

Synonym für Ausbildungsplan

Mitwirkender

Multi-Projektmanagement

Nichtabstreitbarkeit

Non-disclosure-agreement

Organisationsrolle

Mit dem Begriff Mitwirkender werden solche Rolle
Verantwortlichen zur Bearbeitung eines Produkt
konsultiert werden sollten.

 n   bezeichnet, die vom

 s   einbezogen bzw.

Multi-Projektmanagement bezeichnet im Allgemeinen die Koordination
mehrerer Projekte innerhalb einer Organisation. Es wird meist noch feiner
differenziert in strategisches und operatives Multi-Projektmanagement.
Strategisches Multi-Projektmanagement beschäftigt sich mit der Auswahl
und Priorisierung von Projekten und der Definition eines Projektportfolios.
Operatives Projektmanagement beschäftigt sich mit der
projektübergreifenden Planung und Steuerung und der
Ressourcenzuordnung zwischen den einzelnen Projekten und wird im V-
Modell durch die Rolle Multi-Projektkoordination repräsentiert.
Darüber hinaus kennt das V-Modell den Vorgehensbaustein Multi-
Projektmanagement. Dieser kümmert sich allerdings um die gleichzeitige
Zusammenarbeit mit mehreren (organisationsfremden) Auftragnehmern
und entspricht eher einer Losbildung bei der Vergabe.

Nichtabstreitbarkeit (auch: Verbindlichkeit) ist ein weiteres Schutzziel der
Informationssicherheit. Sie fordert, dass kein unzulässiges Abstreiten
durchgeführter Handlungen möglich ist, und kann bspw. durch
elektronische Signaturen erreicht werden.

Ein Non-disclosure-agreement ist eine Verschwiegenheitsvereinbarung,
welche das Stillschweigen über Verhandlungen, Verhandlungsergebnisse
oder vertrauliche Unterlagen festschreibt. Der Verpflichtete stimmt zu, ihm
zugänglich gemachte Informationen geheim zu halten.

Eine Rolle kann einer Rollenkategorie zugeordnet werden.
Organisationsrollen sind auch außerhalb der Lebenszeit des Projektes
besetzt. Es sind solche Rollen, die in der Organisation unabhängig vom
konkreten Projektkontext bestehen, und einen institutionalisierten
Verantwortungsbereich innehaben. Sie werden im V-Modell XT
berücksichtigt, da sie Verantwortung für wichtige, projektübergreifende
Produkte haben können.

Penetrationstest

Ein Penetrationstest prüft, ob ein unautorisiertes Eindringen in ein System /

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland




H.1 Glossar

331

Begriff

Erläuterung

Privacy by default

Privacy by design

Produkt

Produkt, externes

Produkt, initiales

Produktabhängigkeit

Netzwerk möglich ist. Da dies grundsätzlich illegal ist, bedarf es für solche
Tests genauer Vorgaben zum erlaubten Vorgehen der Penetrationstester.

Rechtsgrundlage: Artikel 25 Absatz 2 DSGVO
"Privacy by default" bedeutet datenschutzfreundliche Voreinstellungen.
Systeme sollen so voreingestellt sein, dass "grundsätzlich nur
personenbezogene Daten, deren Verarbeitung für den jeweiligen
bestimmten Verarbeitungszweck erforderlich ist, verarbeitet werden".

Rechtsgrundlage: Artikel 25 Absatz 1 DSGVO
"Privacy by Design" bedeutet, den Datenschutz von vorneherein in die
Gesamtkonzeption einzubeziehen und Systeme so zu konzipieren und zu
konstruieren, dass der Umfang der verarbeiteten personenbezogenen Daten
minimiert wird.

Man unterscheidet zwischen Produkttyp und Produktexemplar. Welche
Bedeutung der Begriff Produkt hat, ist vom jeweiligen Kontext abhängig.
Nicht nur das zu erstellende System, sondern alle Dokumente,
Prüfprotokolle, SW-Module, kurz: Erzeugnisse, werden im V-Modell XT
als Produkttyp (häufig auch nur als Produkt) bezeichnet.

 e   (z.B. Externe Einheit, Externes HW-Modul

Externe Produkte sind Produkt
oder Externes SW-Modul), die außerhalb des V-Modell-Projekt
werden können. Für externe Produkte gibt das V-Modell XT
verantwortliche Rolle
Aktivität

 en    angegeben.

 n   an. Es werden aber nicht zu jedem externen Produkt

 s   erstellt

Der Begriff initiales Produkt steht für ein Produkt, das in jedem Fall und
genau einmal erstellt werden muss.

 en   . Dabei kann eine Produktabhängigkeit

Eine Produktabhängigkeit beschreibt eine Konsistenzbedingung zwischen
zwei oder mehreren Produkt
sowohl innerhalb eines Vorgehensbaustein
verschiedener Vorgehensbausteine bestehen.
Man unterscheidet erzeugende Produktabhängigkeit, strukturelle
Produktabhängigkeit und inhaltliche Produktabhängigkeit. Alle diese Arten
von Produktabhängigkeiten können relevante Produktabhängigkeit sein.

 s   als auch zwischen Produkte

Produktabhängigkeit,
erzeugende

Produktabhängigkeit,
inhaltliche

Produktabhängigkeit,
relevante

Eine erzeugende Produktabhängigkeit beschreibt, dass in einem oder
mehreren Ausgangsprodukten die Bedingungen beziehungsweise Regeln
festgelegt werden, unter denen eines oder mehrere Zielprodukte erzeugt
werden müssen.

Eine inhaltliche Produktabhängigkeit beschreibt den inhaltlichen
Zusammenhang mehrerer Produkt
ist beispielsweise gegeben, wenn eine Änderung an einem Produkt eine
Änderung eines weiteren Produkts nach sich zieht.

 e  . Eine inhaltliche Produktabhängigkeit

Eine Produktabhängigkeit ist relevant im Bezug auf ein betrachtetes
Produkt, genau dann wenn sie - in den im Rahmen des Tailoring
ausgewählten Vorgehensbaustein
Produkt enthält und - mindestens ein anderes Produkt in der

 en    enthalten ist und - das betrachtete

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland









332

Begriff

Produktabhängigkeit,
strukturelle

Erläuterung

Produktabhängigkeit den Zustand fertig gestellt hat.

 Anhang

Strukturelle Produktabhängigkeit
Beziehungen zueinander. So gibt es beispielsweise eine strukturelle
Produktabhängigkeit, die aussagt, dass eine SW-Einheit aus SW-
Komponente

 en    gliedern Produkte und setzen sie in

 n   besteht.

Produkte

siehe Produkt.

Produktexemplar

Produktstruktur

Produkttyp

Produktversion

Produktzustand

Produktzustandsmodell

Projekt

Unter einem Produktexemplar versteht man die konkrete Ausprägung eines
Produkttyps, zum Beispiel ein bestimmtes Dokument. Für ein konkretes
Beispiel siehe Produkttyp.

Unter dem Begriff Produktstruktur versteht man die Menge der
Produktexemplar

 e   eines Projekts und deren Zusammenhänge.

Ein Produkttyp beschreibt in allgemeiner Weise Produktexemplare, die
während eines Entwicklungsprozesses entstehen können.
Z.B. beschreibt das Produkt (genauer: der Produkttyp)
Besprechungsdokument alle im Projekt erstellten Besprechungsdokumente.
Ein konkretes Besprechungsprotokoll ist ein Produktexemplar des
Produkttyps Besprechungsdokument.

Eine Produktversion ist ein identifizierbarer und reproduzierbarer
Bearbeitungsstand eines Produktartefaktes. Eine Produktversion hat genau
einen Produktzustand.

 e   besitzen einen Produktzustand, der durch Aktivität

 en    verändert
Produkt
werden kann. Man unterscheidet zwischen den drei Produktzuständen in
Bearbeitung, vorgelegt und fertig gestellt.

Ein Produktzustandsmodell beschreibt den Zustand eines Produkts zu
einem bestimmten Zeitpunkt. Jedes Produkt besitzt einen Produktzustand.
Im V-Modell wird mindestens zwischen den Zuständen in Bearbeitung,
vorgelegt und fertig gestellt unterschieden. Der Zustand eines Produktes
wird spätestens mit der erfolgreichen Beendigung der bearbeitenden
Aktivität neu ermittelt.

Unter einem Projekt versteht man gemäß der IPMA eine einmalige
Gesamtheit von koordinierten Aktivitäten mit bestimmten Anfangs- und
Endpunkten, die von einer Person oder Organisation mit dem Ziel
durchgeführt werden, bestimmte Termin-, Kosten- und Leistungsziele zu
erreichen.

Projektabschnitt

Ein Projektabschnitt bezeichnet den Zeitraum zwischen zwei aufeinander
folgenden Entscheidungspunkt

 en   .

Projektdurchführungsstrategie Die Projektdurchführungsstrategie legt die Reihenfolge fest, in der die für
 e   durchlaufen werden müssen.
das Projekt relevanten Entscheidungspunkt
Sie bestimmt sich anhand der Auswahl einer Projekttypvariante und der
Belegung aller bedingter Projektmerkmal

 e  .

Projektfortschrittsstufe

Eine Projektfortschrittsstufe kennzeichnet einen Zeitpunkt im Projekt, an
dem eine gewisse Entscheidung getroffen wird und somit ein

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland









H.1 Glossar

333

Begriff

Erläuterung

Projektabschnitt beendet wird. Eine Projektfortschrittsstufe wird daher
immer erreicht, wenn ein Entscheidungspunkt erfolgreich durchlaufen
wird.

Projektmerkmal

Projektrolle

 e   charakterisiert. Jedes

Ein Projekt wird durch mehrere Projektmerkmal
Projektmerkmal wird zur Erstellung eines Anwendungsprofil
Wert belegt, der aus einer Menge von möglichen Wertbelegungen
ausgewählt werden muss. Beispiele für Projektmerkmale sind
Informationssicherheit und Datenschutz (AG) oder Projektgegenstand. Ob
ein Projektmerkmal im Tailoring vom V-Modell-Anwender belegt werden
muss, hängt davon ab, ob es durch den gewählten Projekttyp oder die
gewählte Projekttypvariante bedingt ist.

 s   mit einem

Eine Rolle kann einer Rollenkategorie zugeordnet werden. Projektrollen
sind nur zur Lebenszeit des Projektes besetzt. Es sind alle Rollen, die im
Projekt sind und dort (inhaltlich) arbeiten. Sie übernehmen Verantwortung
für V-Modell Produkte, i.d.R. auf Anweisung des Projektleiters oder wirken
bei der Erstellung verschiedener Produkte mit, bzw. sind an
Entscheidungsprozessen beteiligt.

projektspezifische Anpassung
des V-Modells

siehe Tailoring.

projektspezifisches V-Modell

siehe Tailoring-Ergebnis.

Projektsponsor

Projektstakeholder

Als Projektsponsor (engl. Project Sponsor) wird im engeren Sinne diejenige
Person oder Entität verstanden, die die finanziellen Mittel für das Projekt
zur Verfügung stellt. Im weiteren Sinne werden alle Personen als
Projektsponsor bezeichnet, die dem Projekt positiv gegenüberstehen und
dieses unterstützen. Die Art der Unterstützung kann dabei ganz
unterschiedlich sein, beispielsweise politische Unterstützung,
Bereitstellung von Mitarbeitern und Ressourcen oder auch durch positive
Berichterstattung in der Presse.

Projektstakeholder sind alle Personen oder Gruppen, die ein berechtigtes
Interesse am Verlauf oder Ergebnis eines Projekts besitzen. Dabei ist es
unerheblich, ob dieses Interesse positiv oder negativ ist, ob die
Personen/Gruppen also ein Interesse am Gelingen oder am Scheitern des
Projekts haben. Typische Stakeholder (Aufzählung nicht abschließend) sind
der Projektleiter und die Projektteammitglieder, die Anwender des
erstellten Systems, der Projektauftraggeber sowie die Projektsponsor
Multiplikatoren.

 en    und

Projektstufe

Eine Projektstufe bezeichnet die Zeitspanne zwischen zwei
(Teil-)Lieferungen eines Auftragnehmers.

Projekttyp

Im V-Modell wird zwischen drei Projekttyp

 en    unterschieden:

➢ Systementwicklungsprojekt eines Auftraggebers,
➢ Systementwicklungsprojekt eines Auftragnehmers,
➢ Systementwicklungsprojekt eines Auftraggebers mit

Auftragnehmer in der gleichen Organisation (ohne Vertrag).
Ein Projekttyp legt grob fest, welche Vorgehensbausteine, Projektmerkmale

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland





334

Begriff

Projekttypvariante

 Anhang

Erläuterung

und Anforderungen an die Projektdurchführungsstrategie für alle Projekte
dieses Typs gelten. Für jeden dieser Projekttypen bietet das V-Modell
mindestens eine Projekttypvariante an.
Der Projekttyp legt auch eine Mindestmenge an Projektmerkmalen fest, die
im Tailoring mit einem Wert belegt werden müssen.

Eine Projekttypvariante gestaltet einen Projekttyp aus. Die Wahl der
Projekttypvariante bestimmt im Tailoring letztlich die Auswahl der
Vorgehensbaustein
Projektdurchführungsstrategie), die ergänzend zum Projekttyp
hinzugenommen werden.

 e   und Abläufe (Bestandteile der

 e  , Projektmerkmal

prototypische Entwicklung

siehe Entwicklung, prototypische.

Querschnittsdisziplin

siehe Disziplin.

Referenzmodell

Das V-Modell XT Referenzmodell definiert die für die Konformität
erforderlichen Inhalte und Beziehungen, die in einem konformen Prozess
mindestens abgedeckt sein müssen.

relevante Produktabhängigkeit siehe Produktabhängigkeit, relevante.

Restrisiko

Risikoklasse

Risikomaß

Risikoschaden

Im Risikomanagement bezeichnet man das nach Umsetzung
entsprechender Gegenmaßnahmen verbleibende Risiko als Restrisiko.

Risikoklasse
 n   ermöglichen eine Priorisierung der potentiellen Risiken. Sie
werden individuell in einer Organisation oder in einem Projekt festgelegt.
Risikoklassen erleichtern die Entscheidung darüber, ob und welche
Maßnahmen als Reaktion auf Risiken auszuwählen sind. Im Bereich des
Risikomanagements orientieren sich Risikoklassen häufig an dem
Risikomaß und dem Projektvolumen.Typische Risikoklassen sind z. B.

➢ Tolerierbar: das Risikomaß ist geringer als 0,1% des

Projektvolumens,

➢ Unerwünscht: das Risikomaß ist größer als 0,1% und geringer als

1% des Projektvolumens,

➢ Kritisch: das Risikomaß ist größer als 1% und geringer als 10% des

Projektvolumens,

➢ Katastrophal: das Risikomaß ist größer als 10% des

Projektvolumens.

Im Risikomanagement bezeichnet das Risikomaß den mit der
Risikowahrscheinlichkeit gewichteten Risikoschaden.
Risikomaß = Risikowahrscheinlichkeit * Risikoschaden

Der Risikoschaden ist der geschätzte Schaden, der im Schadensfall mit
einem Risiko im Projekt verbunden ist. Die möglichen Schäden werden in
Geldeinheiten (z.B. in T) dargestellt. Nicht in Geldeinheiten zu beziffernde
Schäden (z.B. Imageverlust) sind über Hilfsgrößen weitestgehend zu
monetarisieren, z.B. Imageverlust führt zu einem Umsatzverlust in
Geldeinheiten.

Risikowahrscheinlichkeit

Die Risikowahrscheinlichkeit ist die geschätzte oder berechnete

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland




H.1 Glossar

Begriff

Rolle

Rollenkategorie

335

Erläuterung

Wahrscheinlichkeit, mit der ein Risiko eintritt.

Eine Rolle ist die Beschreibung einer Menge von Aufgaben und
Verantwortlichkeiten im Rahmen eines Projekts und einer Organisation.
Durch die Festlegung von Rollen wird die Unabhängigkeit des V-Modell
von organisatorischen und projektspezifischen Rahmenbedingungen
erreicht. Die Zuordnung von Organisationseinheiten und Personen zu den
Rollen erfolgt zu Beginn eines Projekts. Dabei kann eine Person mehrere
Rollen besetzen, es kann aber auch eine Rolle durch mehrere Personen
besetzt werden.

 s

Jede Rolle kann einer Rollenkategorie zugeordnet sein: entweder
Projektrolle oder Organisationsrolle. Das Ordnungskriterium ist somit die
Projektlebenszeit.

Safety

Siehe Funktionssicherheit.

Schnittstellenprodukt

Schnittstelle zwischen V-
Modell-Projekten

Schutzbedarf

Schutzziele

 en    von Auftraggeber und Auftragnehmer

Als Schnittstellenprodukt bezeichnet man ein Produkt, welches zwischen
den V-Modell-Projekt
ausgetauscht wird. Die Schnittstellenprodukte sind in der
Auftraggeber-/Auftragnehmer-Schnittstelle festgelegt. Für die Erstellung
des Produkte ist entweder der Auftraggeber oder der Auftragnehmer
verantwortlich. Im V-Modell-Projekt des jeweils anderen Projektpartners
taucht das Produkt dann unter gleichem Namen, allerdings mit dem Zusatz
"(von AG)" bzw. "(von AN)" auf.

siehe Auftraggeber-/Auftragnehmer-Schnittstelle.

Schutzbedarf beschreibt die Kritikalität der Verletzung von Schutzzielen,
die gemeinsam mit den Schutzzielen zu definieren sind. Der Schutzbedarf
wird in Stufen je nach Kritikalität angegeben, oft abgestuft als normal,
hoch und sehr hoch.

Die gemeinsamen Schutzziele von Informationssicherheit und Datenschutz
sind Verfügbarkeit, Integrität und Vertraulichkeit. Darüber hinaus hat der
Datenschutz die Schutzziele Datensparsamkeit, Transparenz,
Nichtverkettbarkeit und Intervenierbarkeit.

Secure Software Development
Life Cycle

siehe Security by design.

Security

Siehe Informationssicherheit.

Security by design

Rechtsgrundlage: Artikel 32 DSGVO
"Security by Design" bedeutet, Informationssicherheit als explizite
Anforderung in den Entwicklungsprozess aufzunehmen sowie
ganzheitliche Sicherheitsmaßnahmen von der Initialisierung an zu
berücksichtigen, umzusetzen und zu testen. Security by Design ist keine
Technik, sondern eine Sicherheitsmaßnahme, die den Entwicklungsprozess
begleitet und oft als Secure Software Development Lifecycle (SSDLC)
bezeichnet wird. Die Maßnahmen ergänzen den herkömmlichen
Softwareentwicklungsprozess und sollen eine integrierte und nachhaltige

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland



336

Begriff

Segment

Sicherheit

Sicherheitsstufe

Erläuterung

Sicherheit der entwickelten Software zur Folge haben.

 Anhang

Ein Segment ist ein wesentlicher Teil eines System
Hierarchie-Ebene unterhalb des System
Teils des System
unterteilt werden.

 s  . Segment

 s   dar. Es ist die Realisierung eines

 e   können hierarchisch in weitere Segment

 e

 s   und stellt eine

Die Sicherheit umfasst die Begriffe Funktionssicherheit (Safety),
Informationssicherheit (Security) und Datenschutz.
Funktionssicherheit steht hierbei für die Verfahrens- oder
Betriebssicherheit. Dieser Zustand ergibt sich aus Maßnahmen, durch die
das Risiko eines Personen-, Sach- oder immateriellen Schadens auf einen
annehmbaren Wert begrenzt ist.
Informationssicherheit beschreibt hingegen den Zustand, der die
Verfügbarkeit, die Integrität, die Verbindlichkeit und die Vertraulichkeit von
Informationen beim Einsatz von IT gewährleistet. Dieser Zustand ergibt
sich aus Maßnahmen in der Informationstechnik sowie aus Maßnahmen
personeller, materieller und organisatorischer Art. Dabei ist

➢ Verfügbarkeit der Zustand, der die erforderliche Nutzbarkeit von
Informationen sowie IT-Systemen und -Komponenten sicherstellt;

➢ Integrität der Zustand, der unbefugte und unzulässige

Veränderungen von Informationen und an IT-Systemen oder
Komponenten ausschließt;

➢ Verbindlichkeit der Zustand, in dem geforderte oder zugesicherte

Eigenschaften oder Merkmale von Informationen und
Übertragungsstrecken sowohl für die Nutzer verbindlich
feststellbar als auch Dritten gegenüber beweisbar sind;

➢ Vertraulichkeit der Zustand, der unbefugte

Informationsgewinnung/-beschaffung ausschließt.

Die Aufgabe des Datenschutzes ist es, den Einzelnen davor zu schützen,
dass er durch den Umgang mit seinen personenbezogenen Daten in seinem
Persönlichkeitsrecht beeinträchtigt wird. (Quelle: BDSG)

Eine Sicherheitsstufe bezeichnet eine Stufe, die den Betrachtungseinheiten
(physikalisch System / -elemente bzw. logisch Funktionen / -ketten)
zugeordnet wird und die ein diskretes Maß darstellt

➢ für die potentielle Gefährdung (nach außen) von Personen, Umwelt
oder Gütern beim Betrieb oder bei Verlust der Verfügbarkeit
(Ausfall, Nichterreichbarkeit etc.) bzw. Fehlverhalten eben dieser
Betrachtungseinheit und

➢ für die Bedrohung des Systems (von außen) während des Betriebes

durch Angriffe auf diese Betrachtungseinheit mit der Zielrichtung
Spionage, Sabotage, Manipulation etc. in Kombination mit der
Sensitivität (dem Wert) der zu schützenden Informationen, mit
denen die Betrachtungseinheit umgeht (be- / verarbeiten,
übertragen, speichern).

Neben den bekannten Gefahren, die von Ausfall bzw. Fehlverhalten
ausgehen, kann alleine schon der Betrieb eines Systems eine Gefährdung
hervorrufen: Sowohl ein Kraftfahrzeug als auch ein Raketenwerfer oder ein

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland






H.1 Glossar

337

Begriff

Erläuterung

Röntgengerät gefährden aufgrund von Bauprinzip und Funktionsweise
schon beim fehlerfreien Betrieb Bedienpersonal, unbeteiligte Dritte und
Umwelt.
Die Sensitivität von Informationen kann sowohl von Gesetzen
(Datenschutzgesetz etc.) oder amtlichen Regelungen (Geheimschutz u. a.)
festgelegt sein, als sich auch aus dem Geschäftsbetrieb ergeben (z. B.
Kontodaten bei Banken oder Versicherungen, Patentverwaltung bei einem
Forschungsunternehmen). Es geht dabei immer um den Schutz (hoher)
materieller oder immaterieller Werte gegen (signifikante) Risiken
(Manipulation, Missbrauch, Spionage etc.).

Akronym für Specific (spezifisch), Measurable (messbar), Accepted
(akzeptiert), Realistic (realisierbar), Timely (terminierbar). Im
Projektmanagement ist SMART ein Kriterium zur eindeutigen Definition
von Zielen.

Bei der agilen Softwareentwicklung nach Scrum wird das System in
kurzen, aufeinanderfolgenden Zyklen (Sprints) entwickelt. Ein Sprint ist
immer auf eine Dauer von 1 bis maximal 4 Wochen begrenzt und endet mit
der Erstellung eines Inkrements.

SMART

Sprint

Standard-Datenschutzmodell Das Standard-Datenschutzmodell (SDM) ist eine Methode, mit der die

statisches Tailoring

stellt fertig

strukturelle
Produktabhängigkeit

SW-Element

SW-Modul, externes

Übereinstimmung von Anforderungen des Datenschutzrechts und
technisch-organisatorischen Funktionen personenbezogener Verfahren
überprüfbar wird. Sie wurde von der Konferenz der
Datenschutzbeauftragten des Bundes und der Länder (DSBK) Ende 2016
verabschiedet.

Statisches Tailoring ist das Tailoring, das im Rahmen der
Projektinitialisierung durchgeführt wird, also bis zum Entscheidungspunkt
Projekt initialisiert.

Eine Aktivität stellt ein Produkt fertig. Ein Aktivitätsexemplar ist erst dann
abgeschlossen, wenn sich das zugehörige Produktexemplar im
Produktzustand fertig gestellt befindet.

siehe Produktabhängigkeit, strukturelle.

Der Begriff SW-Element ist ein Oberbegriff, der in der Hierarchie der
Systemelement
bezeichnen kann: SW-Einheit, SW-Komponente, SW-Modul und Externes
SW-Modul.

 e   alle Systemelemente ab der Ebene der SW-Einheit

 e  , SW-Komponente

 n  ), die nicht innerhalb des Projekts

Unter dem Produkt Externes SW-Modul versteht man Systemelemente
(SW-Modul
entwickelt werden. Ein Externes SW-Modul ist ein selbständig
beschreibbares Funktionselement. Dabei kann es sich um ein Fertigprodukt,
eine Beistellung des Auftraggebers, eine im Vorfeld entwickelte
Komponente, die wiederverwendet wird, ein Nachbarsystem oder das
Ergebnis eines Unterauftrags handeln.

System

Das System ist ein einheitliches Ganzes mit der Fähigkeit, vorgegebene

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland




338

Begriff

Systemelement

Tailoring

Tailoring-Ergebnis

Test

Testfall

Thema

Themen

Trigger

Unterauftraggeber

 Anhang

Erläuterung

Forderungen oder Ziele zu befriedigen und stellt den zwischen
Auftraggeber und Auftragnehmer vereinbarten Auftragsgegenstand dar. Das
System besteht aus Beschreibungen und/oder Realisierungen von
Hardware, Software und/oder logistischen Elementen.

Der Begriff Systemelement ist ein Oberbegriff, der alle Elemente, die im
Rahmen der Systemerstellung zu realisieren sind, bezeichnen kann. Im
Einzelnen sind dies System, Segment, Externe Einheit, HW-Einheit, SW-
Einheit, HW-Komponente, SW-Komponente, HW-Modul und SW-Modul.

 s   nicht nur das "Wegschneiden" von

Über die wörtliche Bedeutung des englischen Begriffs hinaus bedeutet
Tailoring im Kontext des V-Modell
Teilen, sondern auch das "Anpassen" des V-Modells. Die Anpassung des V-
Modells an ein konkretes Projekt erfolgt im Normalfall über Hinzunehmen
 en   . Anpassungen innerhalb von
von Vorgehensbaustein
Vorgehensbausteinen sind als Ausnahmefall anzusehen. Zusätzlich zur
Auswahl der Vorgehensbausteine werden dabei die
Projektdurchführungsstrategie
Vorgehensbausteine und der Projektdurchführungsstrategie bildet die
Festlegung des Projekttyp
 s   und die Auswahl einer Projekttypvariante.
Je nach Projektfortschritt wird zwischen

 n   ermittelt. Die Basis für die Auswahl der

➢ statisches Tailoring

 , das heißt Tailoring während der

Projektinitialisierung und

➢ dynamisches Tailoring

 , das heißt Tailoring im weiteren

Projektverlauf

unterschieden.

Das Tailoring-Ergebnis legt den Projekttyp, die im Projekt zu
verwendenden Vorgehensbaustein
 e   und die Projektdurchführungsstrategie
sowie deren Kombination fest. Das Tailoring-Ergebnis ist das Resultat des
Tailoring

 s   (statisches Tailoring, oder dynamisches Tailoring).

 n

Testen wird als spezielle Form der Prüfung verstanden, bei der das
Ausführungsverhalten von SW-Element

 en    einer Prüfung unterzogen wird.

Ein Testfall ist die spezielle Form eines Prüffalls, mit dem das
 en    geprüft werden soll.
Ausführungsverhalten von SW-Element

Ein Thema ist eindeutig einem Produkt zugeordnet, das seinerseits aus
beliebig vielen Themen bestehen kann. Ein Thema ist inhaltlicher Natur
und in sich abgeschlossen. Die Themen eines Produkts sind als eine
Aufzählung der wesentlichen Inhalte des Produkts zu verstehen.

siehe Thema.

Ein Trigger beschreibt ein Ereignis, das eine Aktivität auslöst. Trigger
werden beispielsweise im Rahmen der Planung und Durchführung von
Maßnahmen zur Risikovermeidung und -minderung verwendet.

Ein Auftragnehmer wird als Unterauftraggeber bezeichnet, wenn er Teile
des Vertragsgegenstands selbst als Auftraggeber weiter an einen
Unterauftragnehmer vergibt, um den Vertrag mit seinem Auftraggeber zu

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland












H.1 Glossar

Begriff

Unterauftragnehmer

Validierung

Verantwortlicher

Verifizierung

V-Modell

339

Erläuterung

erfüllen.

Unter einem Unterauftragnehmer ist der Lieferant im Rahmen einer
Vertragssituation bezeichnet, also die Organisation, die dem
Unterauftraggeber ein Systemelement bzw. Teilsystem bereitstellt (DIN EN
ISO 8402).

Die Validierung erbringt anhand des Systems (oder eines Prototyps) den
Nachweis, dass die definierten Anforderungen die Anwenderwünsche
korrekt wiedergeben. Die Validierung kann negativ verlaufen, selbst wenn
das System den gestellten Anforderungen entspricht: In diesem Fall haben
sich entweder die Wünsche der Anwender in der Zwischenzeit verändert
oder die Anforderungsdefinition war fehlerhaft.

 n   bezeichnet, die für

 s   verantwortlich sind und dort festgehaltene

Mit dem Begriff Verantwortlicher werden solche Rolle
die Inhalte eines Produkt
Entscheidungen zu tragen haben. Bei der Erstellung übernimmt der
Verantwortliche die tragende Rolle bei der Koordination und Verteilung der
Arbeit und bei der Verfolgung des Produktzustands.
Verantwortlich für ein externes Produkt ist jene Rolle, die es in Empfang
nimmt, sowie für die Distribution zur weiteren Verwendung im Rahmen des
Projekts zuständig ist.

Die Verifizierung erbringt den Nachweis, dass ein System eine bestehende
Spezifikation erfüllt. Meist wird das System "im aufsteigenden Ast des Vs"
durch einen Test gegen die bestehende Spezifikation verifiziert.

Das V-Modell ist ein Leitfaden zum Planen und Durchführen von
Entwicklungsprojekten unter Berücksichtigung des gesamten
Systemlebenszyklus. Dabei definiert das V-Modell die in einem Projekt zu
erstellenden Ergebnisse und beschreibt die konkreten Vorgehensweisen,
mittels derer diese Ergebnisse erarbeitet werden. Darüber hinaus legt das V-
Modell die Verantwortlichkeiten der einzelnen Projektbeteiligten fest.

V-Modell, weiterentwickeltes Für die Pflege und Weiterentwicklung des V-Modell

 s   wird ein zweistufiges

Verfahren definiert. In vergleichsweise kurzen Abständen, die den
Innovationszyklen der Informationstechnologie gerecht werden, kann das
V-Modell geändert und erweitert werden.
Dazu wird entsprechend der Erstellung eines organisationsspezifischen
Vorgehensmodells ein weiterentwickeltes V-Modell, beziehungsweise Teile
eines weiterentwickelten V-Modells, erarbeitet. Diese Änderungs- und
Weiterentwicklungsvorschläge werden der Änderungskonferenz des V-
Modells (Äko) vorgelegt. Die Äko entscheidet dann über die Übernahme
der Änderungen in das V-Modell. Änderungen und Erweiterungen können
dabei nur Vorgehensbaustein
Entscheidungspunkt
betreffen.
Änderungen, die über diesen Rahmen hinausgehen, wie zum Beispiel
Änderungen an den vorliegenden Grundkonzepten des V-Modell XT, fallen
in die zweite Stufe des Verfahrens. Derartige Änderungen müssen durch
einen gesonderten Review- und Abstimmungsprozess mit den V-Modell-
Anwender

 n   im Rahmen eines Fortschreibungsprojektes durchgeführt

 e  , Projektdurchführungsstrategie

 e   und Konventionsabbildung

 e  , Projektmerkmal

 en

 n  ,

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland










340

Begriff

V-Modell-Anwender

V-Modell-Kern

 Anhang

Erläuterung

werden.

Als V-Modell-Anwender werden Personen bezeichnet, die sich mit der
Durchführung von V-Modell-Projekt
 en    beschäftigen, also in V-Modell-
Projekten involviert sind.

Der V-Modell-Kern bildet die Basis jedes Anwendungsprofil
Menge von Vorgehensbaustein
Projekt Projekt verwendet werden müssen.

 en    fest, die in jedem V-Modell-konformes

 s  . Er legt eine

V-Modell-konformer Prozess Ein Prozess wird als V-Modell-konform bezeichnet, wenn er bzgl.

Beschreibungstechniken, Ergebnissen und Abläufen den
Qualitätsansprüchen des V-Modell XT entspricht. Die erwarteten
Ergebnisse und die Anforderungen an die Abläufe werden durch das V-
Modell XT Referenzmodell bestimmt. Der Nachweis der V-Modell®XT
Konformität erfolgt im Rahmen einer V-Modell XT Konformitätsprüfung.

V-Modell-konformes Projekt

V-Modell-Projekt

V-Modell-Referenz

Ein Projekt wird als V-Modell-konform bezeichnet, wenn es mindestens die
Vorgehensbaustein
jede relevante Produktabhängigkeit im Rahmen der Entwicklung
berücksichtigt.

 e   des V-Modell-Kern

 s   beinhaltet sowie

 e   und Produkt

Unter einem V-Modell-Projekt versteht man ein Projekt, das V-Modell-
konformes Projekt durchgeführt wird.

 en   , Rolle

 e  , Aktivität

 n   usw. ändern sich nicht. Sie werden jedoch im

 s  . Die Beschreibungen und Beziehungen der einzelnen

Eine V-Modell-Referenz definiert eine bestimmte Gruppierung der Inhalte
des V-Modell
Produkt
Rahmen ihrer Abhängigkeiten neu gruppiert und bei Bedarf verkürzt
dargestellt. Für verschiedene Anwendungszwecke und Anwender können
so angepasste Darstellungen der gleichen Inhalte bereitgestellt werden.
V-Modell-Referenzen werden in der Druckversion des V-Modells in den
unterschiedlichen Teilen des V-Modells umgesetzt.

V-Modell XT

Der Namenszusatz "XT" zu V-Modell steht für "extreme tailoring", oder
aber für "extendable".

V-Modell XT Assessment

V-Modell XT
Konformitätsprüfung

Das V-Modell XT Assessment überprüft, ob ein V-Modell-konformer
Prozess einer Organisation auch wirklich angewendet wird. Es liefert damit
den bei einer V-Modell XT Konformitätsprüfung fehlenden Praxisteil.
Nach erfolgreichem Abschluss eines Assessments wird das Zertifikat "V-
Modell XT Pur" (vgl. Zertifizierungsprogramm) vergeben.

Das Ziel einer V-Modell XT Konformitätsprüfung ist es, die V-Modell®XT
Konformität eines vom (Standard-)V-Modell XT abweichenden Prozesses
zu überprüfen. Falls der Prozess V-Modell XT konform ist, darf er in
Absprache mit dem Auftraggeber an Stelle des V-Modell XT in Projekten
eingesetzt werden, in denen V-Modell XT gefordert ist.
Bei der Konformitätsprüfung wird anhand eines Fragenkatalogs überprüft,
ob der betrachtete Prozess bzgl. Beschreibungstechniken, Ergebnissen und
Abläufen den Qualitätsansprüchen des V-Modell XT entspricht. Die
erwarteten Ergebnisse und die Anforderungen an die Abläufe werden durch
das V-Modell XT Referenzmodell bestimmt.

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland











H.1 Glossar

341

Begriff

Erläuterung

V-Modell XT ORG

Vorgehensbaustein

vorgelegt

Vorprojekt

Weit e.V.

Das V-Modell XT ORG umfasst den bis zur Version 2.0 im Standardmodell
enthaltenen Projekttyp Einführung und Pflege eines
organisationsspezifischen Vorgehensmodells. Seit der Version 2.1 wird das
V-Modell XT ORG als eigenständiges Modell bereitgestellt.

 s  . Das V-Modell ist aus

 en    zusammengesetzt. Ein Vorgehensbaustein fasst

Die modulare Einheit des V-Modell
Vorgehensbaustein
unterschiedliche Aktivitätsbausteine zu einer modularen Einheit zusammen.
Indirekt sind ihm somit auch Produkt
eindeutig fortlaufenden Aktivität
Aktivitäten zugeordnet sind.

 e   zugeordnet, da diese wiederum
 en    beziehungsweise fertig stellenden

Definiert einen Produktzustand eines Produkt
 s  , das zur Prüfung durch
unabhängige Qualitätssicherung vorgelegt wird. Je nach Ergebnis der
Prüfung wird der nachfolgende Produktzustand in der Produktbibliothek
gesetzt.

Bei großen Projekten wird oft vor der eigentlichen Projektdurchführung
eine Projektvorstudie durchgeführt, die ggf. so umfangreich sein kann, dass
sie selbst im Rahmen eines Projekts durchgeführt wird. Dieses
vorgeschaltete Vorstudien-Projekt wird oft auch einfach als Vorprojekt
bezeichnet.

Der Weit e.V. ist ein eingetragener Verein, dessen Hauptanliegen die Pflege
und Weiterentwicklung des V-Modells ist. Der Weit e.V. ist direkt aus dem
V-Modell XT Entwicklungsprojekt "Weit" hervorgegangen und 2008
gegründet worden. In diesem Verein sind Vertreter der Behörden, der
Industrie sowie der Hochschulen vertreten.

weiterentwickeltes V-Modell

siehe V-Modell, weiterentwickeltes.

Werkzeugreferenz

Eine Werkzeugreferenz beschreibt eine Klasse von Werkzeugen, die zur
Durchführung von Aktivitäten beziehungsweise Erstellung von Produkte
verwendet werden können.

H.2 Abkürzungen
Kürzel

Begriff

ABE

AG

Äko

Abnahme erklärt

Auftraggeber

Änderungskonferenz des V-Modells

A-Kriterium

Ausschlusskriterium (siehe UfAB)

AN

ANF

ARC

BfIT

Auftragnehmer

Anforderungen festgelegt

Architektur

Der Beauftragte der Bundesregierung für Informationstechnik

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland






342

Kürzel

B-Kriterium

BSI

BVB

COTS

DIN

DSGVO

EP

EVB-IT

FEA

FPGA

GOTS

GWB

HHM

HW

IEC

IIPK

IIPK

IPMA

ISMS

ISO

IT

LFD

NDA

OLA

PDS

PHB

PJA

PJB

PJD

 Anhang

Begriff

Bewertungskriterium (siehe UfAB)

Bundesamt für Sicherheit in der Informationstechnik

Besondere Vertragsbedingungen für die Beschaffung von DV-Leistungen

Commercial off the shelf

Deutsche Industrienorm

Datenschutz-Grundverordnung

Entscheidungspunkt

Ergänzende Vertragsbedingungen für die Beschaffung von
Informationstechnik bzw. informationstechnischen (Dienst-)Leistungen

Einheit(en) entworfen

Field-Programmable Gate Array

Government off the shelf

Gesetz für Wettbewerbsbeschränkungen

Haushaltsmittel

Hardware

International Engineering Consortium

Implementierungs-, Integrations- und Prüfkonzept

Implementierungs-, Integrations- und Prüfkonzept

International Project Management Association

Informationssicherheits-Managementsystem

International Organization for Standardization

Informationstechnik

Lieferung durchgeführt

Non-disclosure-agreement

Operational Level Agreement

Projektdurchführungsstrategie

Projekthandbuch

Ausschreibung freigegeben

Beauftragung erteilt

Projekt initialisiert

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

H.2 Abkürzungen

343

Kürzel

PJG

PJS

QSHB

SER

SLA

SSDLC

SW

SYE

SYI

SYS

UC

UfAB

UML

VB

VDE

VgV

VOB

VOL

Begriff

Projekt genehmigt

Projekt abgeschlossen

QS-Handbuch

Einheit(en) realisiert

Service Level Agreement

Secure Software Development Life Cycle

Software

System entworfen

System integriert

Gesamtsystem entworfen

Underpinning Contract

Unterlage für die Ausschreibung und Bewertung von IT-Leistungen

Unified Modeling Language

Vorgehensbaustein

Verein deutscher Elektrotechniker

VergabeVerordnung

Verdingungsordnung für Bauleistungen

Verdingungsordnung für Lieferleistungen

H.3 Literaturverzeichnis
Quellenverweis
Kürzel

4Ever

4Ever XML Framework, SourceForge, Online:
http://sourceforge.net/projects/fourever

AECMA Simplified English

AF02

ANSI-Norm N45

Bal00

Aircraft European Contractors Manufacturers Association: ASD Simplified
Technical English Website: http://www.simplifiedenglish-aecma.org, Stand:
15.04.2015

Carina Alves, Anthony Finkelstein: Challenges in COTS Decision-Making:
A Goal-DrivenRequirements Engineering Perspective, Proceedings of
SEKE 2002, 789 - 794

ANSI-Norm N45. 2.10.1973, American National Standard Institute,
//global.ihs.com

Helmuth Balzert: Lehrbuch der Software-Technik. Software-Management,
Software-Qualitätssicherung, Unternehmensmodellierung. Spektrum

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

344

Kürzel

BDSG

BF04

BF10

BG03

BGG

BIT13

BPersVG

BRL99

Bur03

Car02

Car93

Car98

CMMI®

Coc00

DIN 31051

DIN 51052

 Anhang

Quellenverweis

akademischer Verlag. 2000

Bundesdatenschutzgesetz, online: http://www.gesetze-im-
internet.de/bdsg_1990/

Manfred Bundschuh, Axel Fabry: Aufwandschätzung von IT-Projekten,
mitp-Verlag Bonn, 2. Auflage, 2004

Klaus Bergner, Jan Friedrich. Using project procedure diagrams for
milestone planning. New Modeling Concepts for Today’s Software
Processes. Springer Berlin Heidelberg, 2010. 88-99.

Eva Best, Martin Weth Gabler, Geschäftsprozesse optimieren Der Leitfaden
für erfolgreiche Reorganisation, captitum, 2003

Gesetz zur Gleichstellung behinderter Menschen, online:
http://www.gesetze-im-internet.de/bgg/

BITKOM (2013): Agiles Software Engineering Made in Germany, Online:
https://www.bitkom.org/Bitkom/Publikationen/Agiles-Software-
Engineering-Made-in-Germany.html

Bundespersonalvertretungsgesetz, online: http://www.gesetze-im-
internet.de/bpersvg/

G. Booch, J. Rumbaugh, L. Jacobson, Das UML Benutzerhandbuch, Bonn
1999

Manfred Burghardt: Projektmanagement; Publicis MCD Verlag, München,
6. Auflage, 2003

Carnegie Mellon University: CMMI®-SE for Systems Engineering,
Software Engineering, and Integrated Product and Process Development
(CMMI®-SE/SW/IPPD, V1.1, Staged) © 2002 by Carnegie Mellon
University

David N. Card, Defect-Causal Analysis Drives Down Error Rates, IEEE
Software, July 1993

David N. Card, Learning from Our Mistakes with Defect Causal Analysis,
IEEE Software, January - February 1998

CMMI® - Capability Maturity Model Integration, Carnegie Mellon,
Software Engineering Institute, Pittsburgh, USA, Webseite:
http://www.sei.cmu.edu/CMMI, Stand: 15.04.2015

Alistair Cockburn: Writing Effective Use Cases, Collection Editor, The
Crystal Collection for Software Professionals, Addison-Wesley, 2000,
ISBN 0-201-70225-8

Deutsches Institut für Normung e.V.: DIN 31051 2003-06: Grundlagen der
Instandhaltung. Beuth Verlag, Berlin 2003.

Deutsches Institut für Normung e.V.: DIN 31052 (06/81) Instandhaltung:
Inhalt und Aufbau von Instandhaltungsanleitungen. Beuth Verlag, Berlin

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

H.3 Literaturverzeichnis

345

Kürzel

DIN EN 13306

DIN EN 9241

DIN EN IEC 61508

DW88

Ebe02

EFQM

Quellenverweis

1981.

Deutsches Institut für Normung e.V.: DIN EN 13306:2001: Begriffe der
Instandhaltung, dreisprachige Fassung EN 13306:2001. Beuth Verlag,
Berlin 2001.

DIN (Deutsches Institut für Normung e.V.):
DIN EN ISO 9241 "Ergonomische Anforderungen für Bürotätigkeiten mit
Bildschirmgeräten", Teil 10: Grundsätze der Dialoggestaltung Der
Bildschirmarbeitsplatz ; Softwareentwicklung mit DIN EN 9241

CENELEC, Funktionale Sicherheit sicherheitsbezogener
elektrischer/elektronischer/programmierbarer elektronischer Systeme, Dez.
2001

M. S. Deutsch, R. Willis: Software Quality Engineering, Prentice-Hall,
Englewood Cliffs, NJ, 1988

Otto Eberhard, Gefährdungsanalyse mit FMEA, Expert Verlag, 2002

EFQM, Brussels Representativ Office, Avenue des Pleiades 15, 1200
Brussels, Belgium, Webseite: http://www.efqm.org, Stand: 15.04.2015,
EFQM Framework for Cooperate Responsibility, ISBN 90-5236-480-x

FDA 21c FR11

Food and Drug Administration (FDA), Guidance for Industry, Part 11,
Electronic Records; Electronic Signatures, 2003

FH+09

FW90

Geb02

Hof97

Friedrich, J., Hammerschall, U., Kuhrmann, M., Sihling, M.: Das V-Modell
XT. Springer, Informatik im Fokus, 2. Auflage, 2009.

D. Freedman, G. Weinberg: Handbook of Walkthroughs, Inspections, and
Technical Reviews; Dorset House Publishing, 1990

Andreas Gebhardt, Rapid Prototyping, Hanser Fachbuch 2002

Josef Hoffmann, MATLAB und SIMULINK. Beispielorientierte
Einführung in die Simulation dynamischer Systeme, Addison-Wesley 1997

IEEE-STD 1028-1988

IEEE-STD 1028-1988, IEEE Standard for Software Reviews and Audits,
1998, Webseite: http://www.ieee.org, Stand: 15.04.2015

ISO/IEC 12119

ISO/IEC 12207

ISO/IEC 15288

ISO 13407

ISO (International Organization for Standardization) / IEC ( International
Electrotechnical Commission) 12119: "Information technology - Software
packages - Quality requirements and testing."

ISO (International Organization for Standardization) / IEC ( International
Electrotechnical Commission) 12207: "Information Technology—Software
Life-Cycle Processes"

ISO (International Organization for Standardization) / IEC ( International
Electrotechnical Commission) 15288: "Systems engineering -- System life
cycle processes"

ISO (International Organization for Standardization) 13407: "Human
centered design processes for interactive systems"

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

346

Kürzel

ISO 15408

ISO 9001:2000

ISO DIS 10011

IT-Grundschutz

ITIL

ITSEC

IuK-Mindestanforderungen-
2011

KE04

Kne03

Kon96

Lev86

LMTC01

Mac99

Mor99

Mot06

NPSI

 Anhang

Quellenverweis

BSI, Gemeinsame Kriterien für die Prüfung und Bewertung der Sicherheit
von Informationstechnik / Common Criteria for Information Technology
Security Evaluation (CC), Version 2.1, 1999

ISO (International Organization for Standardization) 9001:2000: "Quality
management systems -- Requirements"

ISO DIS 10011: "Guidelines for Auditing Quality Systems", 1989

Bundesamt für Sicherheit in der Informationstechnik, IT-Grundschutz
(Online: www.bsi.bund.de)

Information Technology Infrastructure Library, Webseite:
https://www.axelos.com/best-practice-solutions/itil, Stand 15.04.2015

BSI, "Information Technology Security Evaluation Criteria – ITSEC",
1998, Webseite:
https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Zertifizierung/IT
Sicherheitskriterien/itsec-dt_pdf.htm, Stand: 15.04.2015

Mindestanforderungen der Rechnungshöfe des Bundes und der Länder zum
Einsatz der Informations- und Kommunikationstechnik – Leitlinien und
gemeinsame Maßstäbe für IuK-Prüfungen – (IuK-Mindestanforderungen
2011); Stand November 2011; Online:
https://www.bundesrechnungshof.de/de/veroeffentlichungen/broschueren/m
indestanforderungen-der-rechnungshoefe-des-bundes-und-der-laender-zum-
einsatz-der-informations-und-kommunikationstechnik/view

Alfons Kemper, Andre Eickler, Datenbanksysteme, Oldenbourg Verlag,
2004

Ralf Kneuper, CMMI®, Verbesserung von Softwareprozessen mit
Capability Maturity Model Integration; dpunkt.verlag, 2003 Heidelberg

Jyrki Kontio: A Case Study in Applying a Systematic Method for COTS
Selection, Proceedings of ICSE-18 (1996), 201-209

N. G. Leveson: Software Safety: What, Why and How, ACM Computing
Surveys Vol 18 No 2, June 1986

Patricia Lawlis, Kathryn Mark, Deborah Thomas, Terry Courtheyn: A
Formal Process for Evaluating COTS-Software Products, Computer, (May
2001), 58-63

Michael Macht, Ein Vorgehensmodell für den Einsatz von Rapid
Prototyping, Herbert Utz Verlag, 1999

Jörn Mordau, Die Integration formaler Methoden zur Spezifikation von
Informationssystemen, Verlag Kovac, 1999

Motzel, Erhard (2006): Projektmanagement Lexikon. Begriffe der
Projektwirtschaft von ABC-Analyse bis Zwei-Faktoren-Theorie. Weinheim:
WILEY-VCH.

http://www.bmi.bund.de/SharedDocs/Downloads/DE/Themen/OED_Verwa

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

H.3 Literaturverzeichnis

347

Kürzel

Quellenverweis

PD99

Phi86

PMI

PR09

PSP

RD02

Rup04

SAGA

SaSch75

Sch03

Schw04

SKB14

SPICE

Sta95

Tha02

ltung/Informationsgesellschaft/Nationaler_Plan_Schutz_Informationsinfras
trukturen.html

Jose M. Padillo, Moustapha Diaby: A multiple-criteria decision
methodology for the make-or-buy problem, International Journal of
Production Research, 1999, 37(14), 3203-3229

Ronald T. Philips, An Approach to Software Causal Analysis and Defect
Extinction, IBM Corporation, 1986

Project Management Institute; “A Guide to the Project Management Body
of Knowledge” (2000 Edition), Newtown Square, Pennsylvania USA,
December 2003

Pohl, K., Rupp, C.: Basiswissen Requirements Engineering, Aus- und
Weiterbildung zum "Certified Professional for Requirements Engineering"
Foundation Level nach IREB-Standard. dpunkt.verlag 1. Auflage, 2009.

Humphrey, Watts S. (November 2000): The Personal Software Process
(PSP). Carnegie Mellon Software Engineering Institute. Pittsburgh.
(CMU/SEI-2000-TR-022). Online verfügbar unter
http://www.sei.cmu.edu/reports/00tr022.pdf, zuletzt geprüft am 21.11.2009.

Chris Rupp, Jürgen Dallner. Mustergültige Anforderungen.
OBJEKTspektrum Nr. 3. 2001

Chris Rupp, SOPHIST GROUP, Requirements-Engineering und
Management. Professionelle, iterative Anforderungsanalyse für die Praxis,
3. neu bearbeitete Auflage Hanser Fachbuch, 2004

Die Beauftragte der Bundesregierung für Informationstechnik, SAGA,
Online: www.cio.bund.de.

Jerome H. Saltzer, Michael D. Schroeder, The Protection of Information in
Computer Systems, Proceedings of the IEEE 63.9, 1975, S. 1278-1308

E. Scherf, Modellbildung und Simulation dynamischer Systeme,
Oldenbourg, 2003

Kathy Schwalbe: Information Technology Project Management, Thomson,
3. Aufl. 2004

Schmidt, Kalkoven, Böni (2014): Scrum, Kanban, V-Modell XT - was
bringt Erfolg? Online: http://www.cio.de/scrum/2944862/

Software Process Improvement Capability dEtermination (ISO 15504)
Das SPICE (Software Process Improvement Capability dEtermination)
Projekt ist eine internationale Initiative zur Entwicklung eines Standards
für Software Prozess Assessments. Die Entwicklung wurde geleitet durch
die Arbeitsgruppe 10 bei der ISO (ISO/IEC JTC1/SC7/WG10).

D. H. Stamatis, Failure Mode and Effect Analysis, Hardcover Published
1995, ISBN 087389300x

Georg E. Thaller, Software-Test, Heise, 2002

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

348

Kürzel

THE03

TK09

TKK09

UfAB

VOL/A

Wan02

WiBe

Wil75

You92

 Anhang

Quellenverweis

Thiel, S.; Hein, A.; Engelhardt, H.; "Tool Support for Scenario-Based
Architecture Evaluation", ICSE 2003 Workshop: Workshop on Software
Requirements to Architectures, Portland, USA, May 2003

Ternité, Thomas, Marco Kuhrmann. Das V-Modell XT 1.3 Metamodell.
Forschungsbericht TUM-I0905, Technische Universität München 214
(2009).

Toutenburg, H., Knöfel, P., Kreuzmair, I.: Six Sigma. Springer, 2. Auflage,
2009.

Unterlage für die Ausschreibung und Bewertung von IT-Leistungen, (in der
jeweils aktuellen Version), Webseite: http://www.cio.bund.de/Web/DE/IT-
Beschaffung/UfAB/ufab_node.html, Stand: 25.04.2018

Vergabe- und Vertragsordnung für Leistungen, Teil A, Abschnitt 1:
Bestimmungen für die Vergabe von Leistungen (VOL/A); Ausgabe 2012
Online: https://www.bmwi.de/BMWi/Redaktion/PDF/V/vol-a-abschnitt-
1,property=pdf,bereich=bmwi2012,sprache=de,rwb=true.pdf

E.T.G Wang: Transaction attributes and software outsourcing success: an
empirical investigation of transaction cost theory, Info Systems Journal
2002, (12) 153-181

Der Beauftragte der Bundesregierung für Informationstechnik,
Wirtschaftlichkeitsbetrachtungen (WiBe 5.0), Online: www.cio.bund.de

O.E. Williamson: Markets and Hierarchies, Free Press New York 1975

Edward Yourdon, Moderne Strukturierte Analyse. Standardwerk zur
modernen Systemanalyse, VMI Buch AG, 1992

V-Modell XT Bund (Version: 2.3), ©2019 Bundesrepublik Deutschland

