[![](//upload.wikimedia.org/wikipedia/commons/thumb/3/3a/V-Modell.svg/500px-V-Modell.svg.png)](/wiki/Datei:V-Modell.svg)Phasen des V-Modells über Zeit und Detaillierung

Das **V-Modell** ist ein [Vorgehensmodell](/wiki/Vorgehensmodell_\(Software\) "Vorgehensmodell \(Software\)") bzw. Prozessreferenzmodell[1], welches ursprünglich für die Softwareentwicklung konzipiert wurde. Ähnlich dem [Wasserfallmodell](/wiki/Wasserfallmodell "Wasserfallmodell") organisiert es den [Softwareentwicklungsprozess](/wiki/Softwaretechnik "Softwaretechnik") in Phasen. Zusätzlich zu diesen Entwicklungsphasen definiert das V-Modell auch das Vorgehen zur Qualitätssicherung ([Testen](/wiki/Softwaretest "Softwaretest")), indem den einzelnen Entwicklungsphasen Testphasen gegenübergestellt werden. Auf der linken Seite wird mit einer funktionalen/fachlichen Spezifikation begonnen, die immer tiefer detailliert zu einer technischen Spezifikation und Implementierungsgrundlage ausgebaut wird. In der Spitze erfolgt die [Implementierung](/wiki/Implementierung "Implementierung"), die anschließend auf der rechten Seite gegen die entsprechenden Spezifikationen der linken Seite getestet wird. So entsteht bildlich das namensgebende „V“, welches die einzelnen Entwicklungsebenen ihren jeweiligen Testebenen gegenüberstellt.

Zum V-Modell im Allgemeinen werden in der Literatur die Anzahl der Phasen und auch deren Bezeichnungen unterschiedlich dargestellt, jedoch immer mit 1:1-Gegenüberstellung von Entwurfs- und Teststufen.

Die Prozesse des V-Modells werden mit einem Prozessbewertungsmodell, z. B. nach ISO 33000-Familie bewertet. Eine Umsetzung der Norm ist die [Automotive SPICE](/wiki/Automotive_SPICE "Automotive SPICE").

Das V-Modell ist nicht zu verwechseln mit dem [Verfügbarkeitsmodell](/w/index.php?title=Verf%C3%BCgbarkeitsmodell_\(Transportsysteme\)&action=edit&redlink=1 "Verfügbarkeitsmodell \(Transportsysteme\) \(Seite nicht vorhanden\)") (auch abgekürzt als "V-Modell").[2][3]

## Geschichte

[[Bearbeiten](/w/index.php?title=V-Modell&veaction=edit&section=1 "Abschnitt bearbeiten: Geschichte") | [Quelltext bearbeiten](/w/index.php?title=V-Modell&action=edit&section=1 "Quellcode des Abschnitts bearbeiten: Geschichte")]

Vorgeschlagen wurde dieses Vorgehen zuerst von dem US-amerikanischen Softwareingenieur [Barry Boehm](/wiki/Barry_Boehm "Barry Boehm") im Jahre 1979 und basiert auf dem [Wasserfallmodell](/wiki/Wasserfallmodell "Wasserfallmodell"): Die Phasenergebnisse sind bindende Vorgaben für die nächsttiefere [Projektphase](/wiki/Projektphase "Projektphase"). Der linke, nach unten führende Ast für die Spezifizierungsphasen schließt mit der Realisierungsphase ab. Eine Erweiterung gegenüber dem Wasserfallmodell sind die zeitlich nachfolgenden Testphasen, die im rechten, nach oben führenden Ast dargestellt werden. Den spezifizierenden Phasen stehen jeweils testende Phasen gegenüber, was in der Darstellung ein charakteristisches „V“ ergibt, das dem Modell auch den Namen gab.[4] Diese Gegenüberstellung soll zu einer möglichst hohen [Testabdeckung](/wiki/Testabdeckung "Testabdeckung") führen, weil die [Spezifikationen](/wiki/Spezifikation "Spezifikation") der jeweiligen Entwicklungsstufen die Grundlage für die Tests ([Testfälle](/wiki/Testfall "Testfall")) in den entsprechenden [Teststufen](/wiki/Softwaretest#Teststufen "Softwaretest") sind.

## Anwendungen

[[Bearbeiten](/w/index.php?title=V-Modell&veaction=edit&section=2 "Abschnitt bearbeiten: Anwendungen") | [Quelltext bearbeiten](/w/index.php?title=V-Modell&action=edit&section=2 "Quellcode des Abschnitts bearbeiten: Anwendungen")]

### IT-Entwicklungsprojekte

[[Bearbeiten](/w/index.php?title=V-Modell&veaction=edit&section=3 "Abschnitt bearbeiten: IT-Entwicklungsprojekte") | [Quelltext bearbeiten](/w/index.php?title=V-Modell&action=edit&section=3 "Quellcode des Abschnitts bearbeiten: IT-Entwicklungsprojekte")]

Das allgemeine V-Modell ist die Grundlage von Entwicklungsstandards wie z. B. dem [V-Modell (Entwicklungsstandard)](/wiki/V-Modell_\(Entwicklungsstandard\) "V-Modell \(Entwicklungsstandard\)") der öffentlichen Hand in Deutschland.

### Das V-Modell in der Entwicklung mechatronischer Systeme

[[Bearbeiten](/w/index.php?title=V-Modell&veaction=edit&section=4 "Abschnitt bearbeiten: Das V-Modell in der Entwicklung mechatronischer Systeme") | [Quelltext bearbeiten](/w/index.php?title=V-Modell&action=edit&section=4 "Quellcode des Abschnitts bearbeiten: Das V-Modell in der Entwicklung mechatronischer Systeme")]

[![](//upload.wikimedia.org/wikipedia/commons/thumb/f/f0/V-Modell_VDI-VDE-2206_Nov2021.png/250px-V-Modell_VDI-VDE-2206_Nov2021.png)](/wiki/Datei:V-Modell_VDI-VDE-2206_Nov2021.png)V-Modell nach VDI/VDE 2206 aus dem Jahr 2021

Spätestens seit 2004 wird das V-Modell auch allgemeiner in Entwicklungsprozessen verwendet. So empfiehlt die Richtlinie VDI/VDE 2206 das V-Modell als Teil der „Entwicklungsmethodik für [mechatronische](/wiki/Mechatronik "Mechatronik") Systeme“. Hintergrund ist dabei die zunehmende Integration von [mechanischen](/wiki/Mechanik "Mechanik"), [elektrischen](/wiki/Elektrizit%C3%A4t "Elektrizität") und [informationstechnischen](/wiki/Software "Software") Komponenten in mechatronischen Systemen und die damit verbundene Steigerung der Komplexität[5].

Ausgangspunkt ist dabei meist eine konkrete Anforderung bzw. eine Anforderungsliste in Form eines Entwicklungsauftrags. Diese Anforderungen stellen zugleich den Maßstab dar, nach dem das spätere Produkt zu bewerten ist. Im Systementwurf wird die Gesamtfunktion des Systems bzw. des späteren Produktes in Teilfunktionen zerlegt. Sind die Teilfunktionen ermittelt erfolgt die Konkretisierung des Lösungskonzeptes meist getrennt in den einzelnen Fachdisziplinen (Domänen). Die konkreten Lösungen der einzelnen Disziplinen werden im Rahmen der Systemintegration zu einem Gesamtsystem verbunden und ihr Zusammenwirken untersucht. Fortlaufend wird dabei im Zuge der Eigenschaftsabsicherung der jetzige Entwurf gegen die spezifizierten Anforderungen geprüft, dadurch wird sichergestellt, dass die gewünschten Eigenschaften mit den tatsächlichen Eigenschaften übereinstimmen. Der gesamte Prozess kann dabei durch rechnergestützte Modellierung und Simulation unterstützt werden. Ergebnis eines durchlaufenen Zyklus des V-Modells ist das „Produkt“, wobei es sich hierbei um einen bestimmten Reifegrad (Funktionsmuster, [Prototyp](/wiki/Prototyp_\(Technik\) "Prototyp \(Technik\)"), Vorserienmuster etc.) des geplanten Endproduktes handeln kann. Das V-Modell stellt also einen iterativen Prozess dar, der sich schrittweise der endgültigen Lösung annähert und je nach Komplexität des Endproduktes vielfach durchlaufen wird.[6]

### Das V-Modell als Datenstruktur

[[Bearbeiten](/w/index.php?title=V-Modell&veaction=edit&section=5 "Abschnitt bearbeiten: Das V-Modell als Datenstruktur") | [Quelltext bearbeiten](/w/index.php?title=V-Modell&action=edit&section=5 "Quellcode des Abschnitts bearbeiten: Das V-Modell als Datenstruktur")]

Neben der Funktion als Prozessmodell kann das V-Modell auch die Grundlage für die [Datenstruktur](/wiki/Datenstruktur "Datenstruktur") in der Entwicklung übernehmen. Dabei werden die verschiedenen Artefakte der Entwicklung auf dem V positioniert: Links oben die Anforderungen, bis zur Mitte unten zur Implementierung und auf dem rechten Arm die dazugehörigen [Verifizierungs- und Validierungs](/wiki/Verifizierung_und_Validierung "Verifizierung und Validierung")-Artefakte. Eine [Rückverfolgbarkeit (engl. "Traceability")](/wiki/R%C3%BCckverfolgbarkeit_\(Anforderungsmanagement\) "Rückverfolgbarkeit \(Anforderungsmanagement\)") zwischen den Artefakten unterstützt das Arbeiten mit den Artefakten. Diese Umsetzung ist in den gängigen [Anforderungsmanagementwerkzeugen](/wiki/Anforderungsmanagement-Software "Anforderungsmanagement-Software") üblich[7].

## Weiterentwicklung

[[Bearbeiten](/w/index.php?title=V-Modell&veaction=edit&section=6 "Abschnitt bearbeiten: Weiterentwicklung") | [Quelltext bearbeiten](/w/index.php?title=V-Modell&action=edit&section=6 "Quellcode des Abschnitts bearbeiten: Weiterentwicklung")]

Auf Basis von Erfahrungen aus der industriellen Anwendung und dem technologischen Fortschritt wurde seither eine Vielzahl von Weiterentwicklungen des V-Modells publiziert[8]. Durch Hinwendung zu [agilen Methoden](/wiki/Agile_Methoden "Agile Methoden"), [Concurrent-Engineering](/wiki/Simultaneous_Engineering "Simultaneous Engineering")-Prozessen und die zeitgleiche Relevanz des [Systems Engineerings](/wiki/Systems_Engineering "Systems Engineering") wurde das V-Modell um 2000 beispielsweise zum _W-Modell_ weiterentwickelt.[9] Mit einer vorgezogenen Testphase und der Einbindung von [Simulationsprozessen](/wiki/Simulationsbasierte_Optimierung "Simulationsbasierte Optimierung") und statistischen Methoden zur Fehlervermeidung greift das W-Modell Maßnahmen auf, die zur Parallelisierung von Arbeitsschritten genutzt werden können.[10] Es dient damit als Möglichkeit, agile Ansätze in klassische Arbeitsumfelder einzubetten.[11] Der Begriff findet vorrangig im deutschsprachigen Raum Verwendung.

Die Richtlinie VDI 2206 wurde im VDI in den Jahren 2014 bis 2021 von dem Fachausschuss 4.10 „Interdisziplinäre Produktentstehung“ der VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik überarbeitet und im November 2021 veröffentlicht. Hierbei wurden auf Basis einer Schwachstellenanalyse[12] der hohen Interdisziplinarität, Komplexität und Heterogenität moderner Systeme[13] Rechnung getragen und das V-Modell erneuert. Die Entwicklungen moderner Produkte, die neben einem mechanischen, häufig elektronischen sowie möglichen Software-Anteile mit einer Verbindung zum [Internet der Dinge](/wiki/Internet_der_Dinge "Internet der Dinge") und Dienste umfassen kann, angepasst. Es existieren neben der neuen Richtlinie VDI/VDE 2206 „Entwicklung mechatronischer und cyber-physischer Systeme“ weitere wissenschaftliche Veröffentlichungen[5]. Zentral war die Erneuerung des Bildes des V-Modells, das zum Download zur Verfügung steht, siehe bei den **Weblinks**.

## Weblinks

[[Bearbeiten](/w/index.php?title=V-Modell&veaction=edit&section=7 "Abschnitt bearbeiten: Weblinks") | [Quelltext bearbeiten](/w/index.php?title=V-Modell&action=edit&section=7 "Quellcode des Abschnitts bearbeiten: Weblinks")]

![](//upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Commons-logo.svg/20px-Commons-logo.svg.png)

**[Commons : V-Modell](https://commons.wikimedia.org/wiki/Category:V-models?uselang=de)** – Sammlung von Bildern, Videos und Audiodateien

  * [_Richtlinie VDI/VDE 2206 "Entwicklung mechatronischer und cyber-physischer Systeme"._](https://www.vdi.de/richtlinien/programme-zu-vdi-richtlinien/vdi-2206) In: _VDI._ Abgerufen am 16. November 2022.
  * V-Modell VDI/VDE 2206 Deutsch ([PDF](https://www.vdi.de/fileadmin/pages/vdi_de/redakteure/richtlinien/dateien/VDI_2206_V-Modell_de.pdf))
  * V-model VDI/VDE 2206 English ([PDF](https://www.vdi.de/fileadmin/pages/vdi_de/redakteure/richtlinien/dateien/VDI_2206_V-model_en.pdf))

## Siehe auch

[[Bearbeiten](/w/index.php?title=V-Modell&veaction=edit&section=8 "Abschnitt bearbeiten: Siehe auch") | [Quelltext bearbeiten](/w/index.php?title=V-Modell&action=edit&section=8 "Quellcode des Abschnitts bearbeiten: Siehe auch")]

  * [Liste von Softwareentwicklungsprozessen](/wiki/Liste_von_Softwareentwicklungsprozessen "Liste von Softwareentwicklungsprozessen")
  * [V-Modell (Entwicklungsstandard)](/wiki/V-Modell_\(Entwicklungsstandard\) "V-Modell \(Entwicklungsstandard\)")

## Literatur

[[Bearbeiten](/w/index.php?title=V-Modell&veaction=edit&section=9 "Abschnitt bearbeiten: Literatur") | [Quelltext bearbeiten](/w/index.php?title=V-Modell&action=edit&section=9 "Quellcode des Abschnitts bearbeiten: Literatur")]

### Fachbücher

[[Bearbeiten](/w/index.php?title=V-Modell&veaction=edit&section=10 "Abschnitt bearbeiten: Fachbücher") | [Quelltext bearbeiten](/w/index.php?title=V-Modell&action=edit&section=10 "Quellcode des Abschnitts bearbeiten: Fachbücher")]

  * Paul Alpar, Rainer Alt, Frank Bensberg, Peter Weimann: Anwendungsorientierte Wirtschaftsinformatik: Strategische Planung, Entwicklung und Nutzung von Informationssystemen. Springer Fachmedien Wiesbaden, Wiesbaden 2019, [ISBN 978-3-658-25580-0](/wiki/Spezial:ISBN-Suche/9783658255800), S. 347 ff., [doi](/wiki/Digital_Object_Identifier "Digital Object Identifier"):[10.1007/978-3-658-25581-7](https://doi.org/10.1007/978-3-658-25581-7).
  * Kai Borgeest: Elektronik in der Fahrzeugtechnik: Hardware, Software, Systeme und Projektmanagement. Springer Fachmedien Wiesbaden, Wiesbaden 2021, [ISBN 978-3-658-23663-2](/wiki/Spezial:ISBN-Suche/9783658236632), [doi](/wiki/Digital_Object_Identifier "Digital Object Identifier"):[10.1007/978-3-658-23664-9](https://doi.org/10.1007/978-3-658-23664-9).
  * Jan Friedrich, Marco Kuhrmann, Marc Sihling, Ulrike Hammerschall: Das V-Modell XT (= Informatik im Fokus). Springer Berlin Heidelberg, Berlin, Heidelberg 2008, [ISBN 978-3-540-76403-8](/wiki/Spezial:ISBN-Suche/9783540764038), [doi](/wiki/Digital_Object_Identifier "Digital Object Identifier"):[10.1007/978-3-540-76404-5](https://doi.org/10.1007/978-3-540-76404-5).
  * Thomas Grechenig, Mario Bernhart, Roland Breiteneder, Karin Kappel: _Softwaretechnik._ Pearson Studium, München u. a. 2010, [ISBN 978-3-86894-007-7](/wiki/Spezial:ISBN-Suche/9783868940077), [S. 375](https://books.google.de/books?id=RcSvlD2-QQ0C&pg=PA375&hl=de).
  * Ernest Wallmüller: _Software-Qualitätsmanagement in der Praxis._ 2\. völlig überarbeitete Auflage. Hanser Verlag, München u. a. 2001, [ISBN 3-446-21367-8](/wiki/Spezial:ISBN-Suche/3446213678), [S. 131](https://books.google.de/books?id=BdWJuc7i0QEC&pg=PA131&hl=de).
  * Fabian Wolf: Fahrzeuginformatik: Eine Einführung in die Software- und Elektronikentwicklung aus der Praxis der Automobilindustrie. Springer Fachmedien Wiesbaden, Wiesbaden 2018, [ISBN 978-3-658-21223-0](/wiki/Spezial:ISBN-Suche/9783658212230), [doi](/wiki/Digital_Object_Identifier "Digital Object Identifier"):[10.1007/978-3-658-21224-7](https://doi.org/10.1007/978-3-658-21224-7).

### Historische Werke und Klassiker

[[Bearbeiten](/w/index.php?title=V-Modell&veaction=edit&section=11 "Abschnitt bearbeiten: Historische Werke und Klassiker") | [Quelltext bearbeiten](/w/index.php?title=V-Modell&action=edit&section=11 "Quellcode des Abschnitts bearbeiten: Historische Werke und Klassiker")]

  * Tom DeMarco, Timothy R. Lister (Hrsg.): Software state-of-the-art: selected papers. Dorset House Pub, New York, N.Y 1990, [ISBN 978-0-932633-14-9](/wiki/Spezial:ISBN-Suche/9780932633149) ([archive.org](https://archive.org/details/softwarestateoft0000unse)).

## Einzelnachweise

[[Bearbeiten](/w/index.php?title=V-Modell&veaction=edit&section=12 "Abschnitt bearbeiten: Einzelnachweise") | [Quelltext bearbeiten](/w/index.php?title=V-Modell&action=edit&section=12 "Quellcode des Abschnitts bearbeiten: Einzelnachweise")]

  1. ↑ G. Müller-Ettrich: System Development with V-Model and UML. In: The Unified Modeling Language. Physica-Verlag HD, Heidelberg 1998, [ISBN 978-3-7908-1105-6](/wiki/Spezial:ISBN-Suche/9783790811056), S. 238–249, [doi](/wiki/Digital_Object_Identifier "Digital Object Identifier"):[10.1007/978-3-642-48673-9_16](https://doi.org/10.1007/978-3-642-48673-9_16) (englisch, [springer.com](https://link.springer.com/chapter/10.1007/978-3-642-48673-9_16) [abgerufen am 29. November 2023]).
  2. ↑ [_BMDV - Das V-Modell (Verfügbarkeitsmodell)._](https://www.bmdv.bund.de/SharedDocs/DE/Artikel/StB/oepp-geschaeftsmodelle-v-modell.html) [Bundesministerium für Digitales und Verkehr](/wiki/Bundesministerium_f%C3%BCr_Digitales_und_Verkehr "Bundesministerium für Digitales und Verkehr"), 2023, abgerufen am 29. November 2023.
  3. ↑ Johannes Fottner, Stefan Galka, Sebastian Habenicht, Eva Klenk, Ingolf Meinhardt, Thorsten Schmidt: Allgemeine Grundlagen für die Planung von Transportsystemen. In: Planung von innerbetrieblichen Transportsystemen. Springer Berlin Heidelberg, Berlin, Heidelberg 2022, [ISBN 978-3-662-63972-6](/wiki/Spezial:ISBN-Suche/9783662639726), S. 77–120, [doi](/wiki/Digital_Object_Identifier "Digital Object Identifier"):[10.1007/978-3-662-63973-3_4](https://doi.org/10.1007/978-3-662-63973-3_4) ([springer.com](https://link.springer.com/10.1007/978-3-662-63973-3_4) [abgerufen am 29. November 2023]).
  4. ↑ [_Fragen und Antworten._](https://www.cio.bund.de/SharedDocs/faq-liste/Webs/CIO/DE/digitaler_wandel_fragen_antworten.html?nn=18094882) Bundesministerium des Innern und für Heimat, 2023, abgerufen am 29. November 2023.
  5. ↑ a b Iris Graessler, Julian Hentze: The new V-Model of VDI 2206 and its validation. In: at - Automatisierungstechnik. Band 68, Nr. 5, 1. Mai 2020, [ISSN](/wiki/Internationale_Standardnummer_f%C3%BCr_fortlaufende_Sammelwerke "Internationale Standardnummer für fortlaufende Sammelwerke") [2196-677X](https://zdb-katalog.de/list.xhtml?t=iss%3D%222196-677X%22&key=cql), S. 312–324, [doi](/wiki/Digital_Object_Identifier "Digital Object Identifier"):[10.1515/auto-2020-0015](https://doi.org/10.1515/auto-2020-0015) ([degruyter.com](https://www.degruyter.com/document/doi/10.1515/auto-2020-0015/html) [abgerufen am 5. Januar 2022]).
  6. ↑ Verein Deutscher Ingenieure (Hrsg.): VDI 2206 - Entwicklungsmethodik für mechatronische Systeme. Beuth Verlag GmbH.
  7. ↑ SE-Trends: [Was ist eigentlich das V-Modell?](https://www.se-trends.de/was-ist-eigentlich-das-v-modell/)
  8. ↑ Iris Graessler, Julian Hentze, Tobias Bruckmann: V-MODELS FOR INTERDISCIPLINARY SYSTEMS ENGINEERING. In: DS 92: Proceedings of the DESIGN 2018 15th International Design Conference. 2018, S. 747–756, [doi](/wiki/Digital_Object_Identifier "Digital Object Identifier"):[10.21278/idc.2018.0333](https://doi.org/10.21278/idc.2018.0333) ([designsociety.org](https://www.designsociety.org/publication/40489/V-MODELS+FOR+INTERDISCIPLINARY+SYSTEMS+ENGINEERING) [abgerufen am 5. Januar 2022]).
  9. ↑ A. Spillner: [_From V-model to W-model. Establishing the Whole Test Process._](https://www.tib.eu/de/suchen/id/BLCP:CN039119328/From-V-model-to-W-model-Establishing-the-Whole/) In: _Leibniz-Informationszentrum Technik und Naturwissenschaften Universitätsbibliothek._ Technische Informationsbibliothek (TIB) Hannover, 2000, abgerufen am 18. Juni 2019 (englisch).
  10. ↑ Reiner Anderl, Roland Nattermann, Thomas Rollmann: [_Das W-Modell. Systems Engineering in der Entwicklung aktiver Systeme._](https://d-nb.info/1019526661/34) In: _Katalog der Deutschen Nationalbibliothek._ Technische Universität Darmstadt. Fachgebiet Datenverarbeitung in der Konstruktion, abgerufen am 18. Juni 2019.
  11. ↑ A. Spillner: [_Das W-Modell. Vorteile der agilen Prozesse in einem konservativen Umfeld nutzen._](https://www.gi-hb-ol.de/uta/gi-rg/WModellSpillner.pdf) In: _Gesellschaft für Informatik. Regionalgruppe Bremen Oldenburg._ Hochschule Bremen, 13. Mai 2003, abgerufen am 18. Juni 2019.
  12. ↑ Gräßler I, Hentze J, Yang X. Eleven Potentials for mechatronic V-model. In: _Production Engineering and Management, 6th International Conference, Band 01/2016_. Vol 01/2016. Lemgo: Ostwestfalen-Lippe University of Applied Sciences ; 2016:257-268.
  13. ↑ Gräßler I. A New V-Model for Interdisciplinary Product Engineering. In: Technische Universität Ilmenau, Marketing Division, ed. _59th IWK. Ilmenau Scientific Colloquium_. Technische Universität Ilmenau; 2017:1-6.

![](https://de.wikipedia.org/wiki/Special:CentralAutoLogin/start?useformat=desktop&type=1x1&usesul3=1)

Abgerufen von „[https://de.wikipedia.org/w/index.php?title=V-Modell&oldid=258803524](https://de.wikipedia.org/w/index.php?title=V-Modell&oldid=258803524)“
