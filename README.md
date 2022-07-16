# PySparen

Ein Python-Skript, dass das Planen von Finanzen mit Krediten und Bausparern erleichtern soll. Der Quellcode ist, soweit möglich auf deutsch geschrieben.

Die Darstellung der Pläne basiert auf den HTML-Rendering-Fähigkeiten von Jupyter und `tabulate`.

## Verwendung

Am besten benutzt mein ein Jupyter-Notebook und importiert alles aus pysparen:
```
from pysparen import *
```

Dann definiert man Variablen, die `Eigenkapital`, `Einkommen`, `Ausgaben`, `Kredit`e und `Bausparer` repräsentieren, indem man Objekte mit entsprechendem Namen erstellt.
Zu jedem dieser von `Finanzelement` abgeleiteten Klassen gibt es die Funktion `zeige`, die einem einen Plan ausgibt.
Alle `zeige`-Funktionen geben standardmäßig eine HTML-Tabelle zurück, die von aktuellen Jupyter-Versionen direkt gerendert dargestellt wird.

Mehrer Finanzelemente können in einem `Finanzplan` kombiniert werden. Auch die Klasse `Finanzierungsplan` bietet eine `zeige`-Methode an, die alle relevanten Informationen auflistet.

## Beispiel
```
from pysparen import *

eigenkapital = Eigenkapital(name = "Eigenkapital",
                            kapital_euro = 1000,
                            start = Monat(22,7))

einkommen = Einkommen(name = "Eink.",
                      einkommen_euro = 1500,
                      laufzeit = Monat(4,3),
                      start = Monat(22,7))

ausgabe = Ausgaben(name = "Ausgabe",
                   kosten_euro = 500,
                   start = Monat(24,6))

bauspar = Bausparer(name = 'Bausparer',
                    bausparsumme_euro = 10_000,
                    effektiver_jahreszins_ab_zuteilung_prozent = 1.04,
                    mindestsparguthaben_prozent = 45,
                    sparzeit = Monat(10,10), 
                    tilgungsdauer = Monat(7,1),
                    abschlussgebühr_prozent = 1.4,
                    jahresentgelt_euro = 19,
                    sofortaufzahlung_euro=50,
                    start = Monat(22,8))

kredit = Kredit(name = 'Kredit',
                kreditsumme_euro = 3000,
                effektiver_jahreszins_prozent = 5,
                laufzeit = Monat(15,0),
                volltilger = True,
                start = bauspar.start + bauspar.sparzeit - Monat(15,0) + 1)

finanzplan = Finanzierungsplan([eigenkapital, einkommen, ausgabe, bauspar, kredit])
finanzplan.zeige(monate_zusammenfassen=12)
```
