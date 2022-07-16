from tabulate import tabulate

class Zeigeparameter:
    def __init__(self,tablefmt=None,zeige_monat=None,zeige_tilgung=None,zeige_zinsen=None,zeige_monatliche_belastung=None,zeige_restschuld=None,zeige_ausschüttung=None,zeige_kosten=None,zeige_einnahmen=None,zeige_besondere_kosten=None,zeige_monatliche_differenz=None,zeige_guthaben=None,zeige_ereignisse=None):
        self.tablefmt = tablefmt
        self.zeige_monat = zeige_monat
        self.zeige_tilgung = zeige_tilgung
        self.zeige_zinsen = zeige_zinsen
        self.zeige_monatliche_belastung = zeige_monatliche_belastung
        self.zeige_restschuld = zeige_restschuld
        self.zeige_ausschüttung = zeige_ausschüttung
        self.zeige_kosten = zeige_kosten
        self.zeige_einnahmen = zeige_einnahmen
        self.zeige_besondere_kosten = zeige_besondere_kosten
        self.zeige_monatliche_differenz = zeige_monatliche_differenz
        self.zeige_guthaben = zeige_guthaben
        self.zeige_ereignisse = zeige_ereignisse

    def standard(self):
        self.tablefmt="html"
        self.zeige_monat=True
        self.zeige_tilgung=False
        self.zeige_zinsen=False
        self.zeige_monatliche_belastung=False
        self.zeige_restschuld=False
        self.zeige_ausschüttung=False
        self.zeige_kosten=False
        self.zeige_einnahmen=False
        self.zeige_besondere_kosten=False
        self.zeige_monatliche_differenz=False
        self.zeige_guthaben=False
        self.zeige_ereignisse=True
        return self

    def update(self, other):
        if None != other.tablefmt:
            self.tablefmt = other.tablefmt
        if None != other.zeige_monat:
            self.zeige_monat = other.zeige_monat
        if None != other.zeige_tilgung:
            self.zeige_tilgung = other.zeige_tilgung
        if None != other.zeige_zinsen:
            self.zeige_zinsen = other.zeige_zinsen
        if None != other.zeige_monatliche_belastung:
            self.zeige_monatliche_belastung = other.zeige_monatliche_belastung
        if None != other.zeige_restschuld:
            self.zeige_restschuld = other.zeige_restschuld
        if None != other.zeige_ausschüttung:
            self.zeige_ausschüttung = other.zeige_ausschüttung
        if None != other.zeige_kosten:
            self.zeige_kosten = other.zeige_kosten
        if None != other.zeige_einnahmen:
            self.zeige_einnahmen = other.zeige_einnahmen
        if None != other.zeige_besondere_kosten:
            self.zeige_besondere_kosten = other.zeige_besondere_kosten
        if None != other.zeige_monatliche_differenz:
            self.zeige_monatliche_differenz = other.zeige_monatliche_differenz
        if None != other.zeige_guthaben:
            self.zeige_guthaben = other.zeige_guthaben
        if None != other.zeige_ereignisse:
            self.zeige_ereignisse = other.zeige_ereignisse
        return self      

class Monat:
    def __init__(self, jahr: int, monat: int):
        self.jahr = jahr
        self.monat = monat

        self.normalisieren()
    
    def normalisieren(self):
        while self.monat > 12:
            self.monat -= 12
            self.jahr += 1
        while self.monat <= 0:
            self.monat += 12
            self.jahr -= 1
    
    def __add__(self, monat_or_monate):
        if isinstance(monat_or_monate, Monat):
            return Monat(self.jahr + monat_or_monate.jahr, self.monat + monat_or_monate.monat)
        else:
            return Monat(self.jahr, self.monat + monat_or_monate)
    
    def __le__(self, other):
        return self.__int__() <= other.__int__()

    def __ge__(self, other):
        return other <= self

    def __lt__(self, other):
        return not (other <= self)
    
    def __gt__(self, other):
        return other < self
    
    def __eq__(self, other):
        return (self <= other) and (other <= self)
    
    def __ne__(self, other):
        return not self == other

    def __int__(self):
        return 12*self.jahr + self.monat

    def __sub__(self, monat_or_monate):
        if isinstance(monat_or_monate, Monat):
            monat = monat_or_monate
            return Monat(self.jahr - monat.jahr, self.monat - monat.monat)
        else:
            return Monat(self.jahr, self.monat - monat_or_monate)

    def __str__(self):
        return f"{self.jahr}-{self.monat:02}"

class Monatsbereich:
    def __init__(self, beginn:Monat, laufzeit:Monat):
        self.beginn = beginn
        self.laufzeit = laufzeit
    
    def __iter__(self):
        self.zähler = self.beginn
        return self

    def __next__(self):
        if self.zähler < self.beginn + self.laufzeit:
            self.zähler += 1
            return self.zähler - 1
        else:
            raise StopIteration


class Plan:
    def __init__(self, besondere_einnahmen_euro=[], besondere_ausgaben_euro=[], regelmäßige_einnahmen_euro=[], regelmäßige_ausgaben_euro=[], monat=[]):
        self.monat = monat.copy()
        self.besondere_einnahmen_euro = besondere_einnahmen_euro.copy()
        self.besondere_ausgaben_euro = besondere_ausgaben_euro.copy()
        self.regelmäßige_einnahmen_euro = regelmäßige_einnahmen_euro.copy()
        self.regelmäßige_ausgaben_euro = regelmäßige_ausgaben_euro.copy()


class Elementplan:
    def __init__(self):
        self.monat = []
        self.tilgung_euro = []
        self.zinsen_euro = []
        self.restschuld_euro = []
        self.ausschüttung_euro = []
        self.kosten_euro = []
        self.besondere_kosten_euro = []
        self.einnahmen_euro = []
        self.ereignisse = []
    
    def füge_monat_hinzu(self, monat, tilgung_euro, zinsen_euro, restschuld_euro, ausschüttung_euro, kosten_euro, besondere_kosten_euro, einnahmen_euro, ereignisse):
        self.monat.append(monat)
        self.tilgung_euro.append(tilgung_euro)
        self.zinsen_euro.append(zinsen_euro)
        self.restschuld_euro.append(restschuld_euro)
        self.ausschüttung_euro.append(ausschüttung_euro)
        self.kosten_euro.append(kosten_euro)
        self.besondere_kosten_euro.append(besondere_kosten_euro)
        self.einnahmen_euro.append(einnahmen_euro)
        self.ereignisse.append(ereignisse)

    def füge_leere_monate_am_anfang_hinzu(self, anzahl):
        monat = self.monat[0]
        neue_monate = []
        for index in range(anzahl):
            monat = monat - 1
            neue_monate.append(monat)
        neue_monate.reverse()
        self.monat = neue_monate + self.monat
        self.tilgung_euro = [0.]*anzahl + self.tilgung_euro
        self.zinsen_euro = [0.]*anzahl + self.zinsen_euro
        self.restschuld_euro = [0.]*anzahl + self.restschuld_euro
        self.ausschüttung_euro = [0.]*anzahl + self.ausschüttung_euro
        self.kosten_euro = [0.]*anzahl + self.kosten_euro
        self.besondere_kosten_euro = [0.]*anzahl + self.besondere_kosten_euro
        self.einnahmen_euro = [0.]*anzahl + self.einnahmen_euro
        self.ereignisse = [[]]*anzahl + self.ereignisse

    def füge_leere_monate_am_ende_hinzu(self, anzahl):
        monat = self.monat[-1]
        neue_monate = []
        for index in range(anzahl):
            monat = monat + 1
            neue_monate.append(monat)
        self.monat = self.monat + neue_monate
        self.tilgung_euro = self.tilgung_euro + [0.]*anzahl
        self.zinsen_euro = self.zinsen_euro + [0.]*anzahl
        self.restschuld_euro = self.restschuld_euro + [0.]*anzahl
        self.ausschüttung_euro = self.ausschüttung_euro + [0.]*anzahl
        self.kosten_euro = self.kosten_euro + [0.]*anzahl
        self.besondere_kosten_euro = self.besondere_kosten_euro + [0.]*anzahl
        self.einnahmen_euro = self.einnahmen_euro + [0.]*anzahl
        self.ereignisse = self.ereignisse + [[]]*anzahl

    @staticmethod
    def zusammenfassen(anzahl, liste, funktion):
        ausgabe = []
        for index in range(0, len(liste), anzahl):
            ausgabe.append(funktion(liste[index:min(index+anzahl,len(liste))]))
        return ausgabe

    @staticmethod
    def zusammenfassen_durchschnitt(anzahl, liste):
        return Elementplan.zusammenfassen(anzahl, liste, lambda x: sum(x)/len(x))

    @staticmethod
    def zusammenfassen_summe(anzahl, liste):
        return Elementplan.zusammenfassen(anzahl, liste, lambda x: sum(x))

    @staticmethod
    def zusammenfassen_ende(anzahl, liste):
        return Elementplan.zusammenfassen(anzahl, liste, lambda x: x[-1])

    @staticmethod
    def zusammenfassen_join(anzahl, liste):
        return Elementplan.zusammenfassen(anzahl, liste, lambda x: ", ".join(x))

    @staticmethod
    def zusammenfassen_monat(anzahl, liste):
        if anzahl == 1:
            return liste
        else:
            return Elementplan.zusammenfassen(anzahl, liste, lambda x: x[0].__str__() + " - " + x[-1].__str__())

    def zeige(self, monate_zusammenfassen=1, zeigeparameter=Zeigeparameter().standard()) -> str:
        if monate_zusammenfassen == 1:
            durchschnitt = ""
        else:
            durchschnitt = "⌀ "
        output = {}

        Monat = Elementplan.zusammenfassen_monat(monate_zusammenfassen, self.monat)
        Ausschüttung_euro = Elementplan.zusammenfassen_summe(monate_zusammenfassen, self.ausschüttung_euro)
        Besondere_Kosten_euro = Elementplan.zusammenfassen_summe(monate_zusammenfassen, self.besondere_kosten_euro)
        Einnahmen_euro = Elementplan.zusammenfassen_durchschnitt(monate_zusammenfassen, self.einnahmen_euro)
        Zinsen_euro = Elementplan.zusammenfassen_durchschnitt(monate_zusammenfassen, self.zinsen_euro)
        Fixkosten_euro = Elementplan.zusammenfassen_durchschnitt(monate_zusammenfassen, self.kosten_euro)
        Tilgung_euro = Elementplan.zusammenfassen_durchschnitt(monate_zusammenfassen, self.tilgung_euro)
        Belastung_euro = [sum(x) for x in zip(Tilgung_euro, Zinsen_euro, Fixkosten_euro)]
        Monatliche_Differenz_euro = [haben - soll for (haben,soll) in zip(Einnahmen_euro,Belastung_euro)]
        alle_gesamten_differenzen_euro = [haben_mtl + haben_bes - zinsen - tilgung - kosten - soll_bes for (haben_mtl,haben_bes,zinsen,tilgung,kosten,soll_bes) in zip(self.einnahmen_euro,self.ausschüttung_euro,self.zinsen_euro,self.tilgung_euro,self.kosten_euro,self.besondere_kosten_euro)]
        total = 0.
        alle_guthaben_euro = [total := total + wert for wert in alle_gesamten_differenzen_euro]
        Guthaben_euro = Elementplan.zusammenfassen_ende(monate_zusammenfassen, alle_guthaben_euro)
        Restschuld_euro = Elementplan.zusammenfassen_ende(monate_zusammenfassen, self.restschuld_euro)
        Ereignis = map(lambda x: ", ".join(x), Elementplan.zusammenfassen(monate_zusammenfassen, self.ereignisse, lambda xss: [x for xs in xss for x in xs]))

        if zeigeparameter.zeige_monat:
            output["Monat"] = Monat
        if zeigeparameter.zeige_ausschüttung:
            output["Ausschüttung/€"] = Ausschüttung_euro
        if zeigeparameter.zeige_besondere_kosten:
            output["Bes. Kosten/€"] = Besondere_Kosten_euro
        if zeigeparameter.zeige_einnahmen:
            output[durchschnitt+"Einnahmen/€"] = Einnahmen_euro
        if zeigeparameter.zeige_monatliche_belastung:
            output[durchschnitt+"Belastung/€"] = Belastung_euro
        if zeigeparameter.zeige_monatliche_differenz:
            output[durchschnitt+"Differenz lfd. Kosten/€"] = Monatliche_Differenz_euro
        if zeigeparameter.zeige_zinsen:
            output[durchschnitt+"Zinsen/€"] = Zinsen_euro
        if zeigeparameter.zeige_kosten:
            output[durchschnitt+"Fixkosten/€"] = Fixkosten_euro
        if zeigeparameter.zeige_tilgung:
            output[durchschnitt+"Tilgung/€"] = Tilgung_euro
        if zeigeparameter.zeige_restschuld:
            output["Restschuld/€"] = Restschuld_euro
        if zeigeparameter.zeige_guthaben:
            output["Guthaben/€"] = Guthaben_euro
        if zeigeparameter.zeige_ereignisse:
            output["Ereignis"] = Ereignis
        return tabulate(output, headers='keys', floatfmt=".2f", tablefmt=zeigeparameter.tablefmt)

class Finanzelement:
    def __init__(self, laufzeit:Monat, name:str = "Finanzelement", start:Monat = Monat(0,1)) -> None:
        self.name = name
        self.start = start
        self.laufzeit = laufzeit

    @staticmethod
    def berechne_tilgung_volltilger(kreditlaufzeit: Monat, effektiver_jahreszins_prozent: float) -> float:
        tilgung_prozent = effektiver_jahreszins_prozent/((effektiver_jahreszins_prozent/100 / 12 + 1)**kreditlaufzeit.__int__() - 1)
        return tilgung_prozent
    
    def berechne_plan(self):
        plan = Elementplan()
        vorherige_restschuld_euro = self.berechne_initiale_restschuld_euro()

        for monat in Monatsbereich(self.start, self.laufzeit):
            self.berechne_nächsten_monat(monat, vorherige_restschuld_euro, plan)
            vorherige_restschuld_euro = plan.restschuld_euro[-1]
        
        return plan
    
    def zeige(self, monate_zusammenfassen = 1, zeigeparameter = Zeigeparameter()):
        zeigeparameter = Zeigeparameter().standard().update(zeigeparameter)
        return self.berechne_plan().zeige(monate_zusammenfassen=monate_zusammenfassen, zeigeparameter=zeigeparameter)


class Kredit(Finanzelement):
    def __init__(self, laufzeit, kreditsumme_euro, effektiver_jahreszins_prozent, tilgungsfreie_anlaufzeit=Monat(0,0), volltilger=False, tilgung_prozent=None, name="Kredit", start=Monat(0,1)):
        Finanzelement.__init__(self, laufzeit=laufzeit, name=name, start=start)
        self.kreditsumme_euro = kreditsumme_euro
        self.effektiver_jahreszins_prozent = effektiver_jahreszins_prozent
        self.tilgungsfreie_anlaufzeit = tilgungsfreie_anlaufzeit
        if volltilger:
            self.tilgung_prozent = self.berechne_tilgung_volltilger(self.laufzeit - self.tilgungsfreie_anlaufzeit, self.effektiver_jahreszins_prozent)
        elif tilgung_prozent != None:
            self.tilgung_prozent = tilgung_prozent
        else:
            raise RuntimeError("Es muss entweder volltilger=True oder tilgung_prozent angegeben werden.")
        
        self.berechne_parameter()

    def berechne_parameter(self):
        self.berechne_monatliche_belastung_euro()
        self.berechne_monatliche_belastung_tilgungsfreie_anlaufzeit_euro()
    
    def berechne_monatliche_belastung_euro(self):
        self.monatliche_belastung_euro = self.kreditsumme_euro * (self.tilgung_prozent + self.effektiver_jahreszins_prozent)/100 / 12
    
    def berechne_monatliche_belastung_tilgungsfreie_anlaufzeit_euro(self):
        self.monatliche_belastung_tilgungsfreie_anlaufzeit_euro = self.kreditsumme_euro * (self.effektiver_jahreszins_prozent)/100 / 12

    def berechne_initiale_restschuld_euro(self):
        return self.kreditsumme_euro
    
    def berechne_nächsten_monat(self, monat, vorherige_restschuld_euro, plan:Elementplan):
        tilgung_euro = 0.
        zinsen_euro = 0.
        restschuld_euro = 0.
        ausschüttung_euro = 0.
        kosten_euro = 0.
        besondere_kosten_euro = 0.
        ereignisse = []

        monatliche_belastung_euro = 0.

        if monat == self.start:
            ereignisse.append("Beginn " + self.name)
            ausschüttung_euro += self.kreditsumme_euro
        if monat+1 == self.start + self.tilgungsfreie_anlaufzeit:
            ereignisse.append("Ende tilgungfr. Anlaufz. " + self.name)
        if monat < self.start + self.tilgungsfreie_anlaufzeit:
            monatliche_belastung_euro += self.monatliche_belastung_tilgungsfreie_anlaufzeit_euro
        else:
            monatliche_belastung_euro += self.monatliche_belastung_euro
            tilgung_euro += self.monatliche_belastung_euro - vorherige_restschuld_euro*self.effektiver_jahreszins_prozent/100 / 12

        zinsen_euro += monatliche_belastung_euro - tilgung_euro
        restschuld_euro += vorherige_restschuld_euro - tilgung_euro

        if monat+1 == self.start + self.laufzeit:
            besondere_kosten_euro += restschuld_euro
            ereignisse.append("Ende " + self.name)

        plan.füge_monat_hinzu(monat=monat,
                              tilgung_euro=tilgung_euro,
                              zinsen_euro=zinsen_euro,
                              restschuld_euro=restschuld_euro,
                              ausschüttung_euro=ausschüttung_euro,
                              kosten_euro=kosten_euro,
                              besondere_kosten_euro=besondere_kosten_euro,
                              einnahmen_euro=0.,
                              ereignisse=ereignisse)


    def zeige(self,monate_zusammenfassen=1, zeigeparameter=Zeigeparameter()):
        zeigeparameter = Zeigeparameter(zeige_ausschüttung=True,zeige_tilgung=True,zeige_monatliche_belastung=True,zeige_restschuld=True,zeige_zinsen=True).update(zeigeparameter)
        return Finanzelement.zeige(self,monate_zusammenfassen=monate_zusammenfassen,zeigeparameter=zeigeparameter)

class Bausparer(Finanzelement):
    def __init__(self, bausparsumme_euro, effektiver_jahreszins_ab_zuteilung_prozent, mindestsparguthaben_prozent, sparzeit, tilgungsdauer, abschlussgebühr_prozent, jahresentgelt_euro, sofortaufzahlung_euro=0., name="Bausparer", start=Monat(0,1)):
        self.bausparsumme_euro = bausparsumme_euro
        self.effektiver_jahreszins_ab_zuteilung_prozent = effektiver_jahreszins_ab_zuteilung_prozent
        self.mindestsparguthaben_prozent = mindestsparguthaben_prozent
        self.sparzeit = sparzeit
        self.tilgungsdauer = tilgungsdauer
        self.abschlussgebühr_prozent = abschlussgebühr_prozent
        self.jahresentgelt_euro = jahresentgelt_euro
        self.sofortaufzahlung_euro = sofortaufzahlung_euro

        Finanzelement.__init__(self, laufzeit=self.sparzeit + self.tilgungsdauer, name=name, start=start)
    
        self.mindestsparsumme_euro = self.mindestsparguthaben_prozent/100 * self.bausparsumme_euro

    def berechne_initiale_restschuld_euro(self):
        return self.abschlussgebühr_prozent/100 * self.bausparsumme_euro - self.sofortaufzahlung_euro
    
    def berechne_nächsten_monat(self, monat, vorherige_restschuld_euro, plan:Elementplan):
        tilgung_euro = 0.
        zinsen_euro = 0.
        restschuld_euro = 0.
        ausschüttung_euro = 0.
        kosten_euro = 0.
        ereignisse = []

        monatliche_belastung_euro = 0.

        in_sparphase = (monat < self.start + self.sparzeit)

        if in_sparphase:
            if monat == self.start:
                ereignisse.append("Beginn " + self.name)
            tilgung_euro += (self.mindestsparsumme_euro + vorherige_restschuld_euro) / (self.start + self.sparzeit - monat).__int__()
            kosten_euro += self.jahresentgelt_euro/12
        else:
            # Tilgungsphase
            ist_ausschüttung = (monat == self.start + self.sparzeit)
            if ist_ausschüttung:
                ereignisse.append("Zuteilung " + self.name)
                ausschüttung_euro = self.bausparsumme_euro
                vorherige_restschuld_euro += self.bausparsumme_euro
                self.kreditsumme_euro = vorherige_restschuld_euro
                self.tilgung_prozent = Finanzelement.berechne_tilgung_volltilger(self.tilgungsdauer, self.effektiver_jahreszins_ab_zuteilung_prozent)
                self.monatliche_belastung_euro = self.kreditsumme_euro * (self.tilgung_prozent + self.effektiver_jahreszins_ab_zuteilung_prozent)/100 / 12
            monatliche_belastung_euro += self.monatliche_belastung_euro
            tilgung_euro += self.monatliche_belastung_euro - vorherige_restschuld_euro*self.effektiver_jahreszins_ab_zuteilung_prozent/100 / 12
            zinsen_euro += monatliche_belastung_euro - tilgung_euro

        restschuld_euro += vorherige_restschuld_euro - tilgung_euro

        if monat == self.start + self.sparzeit + self.tilgungsdauer - 1:
            ereignisse.append("Ende " + self.name)

        plan.füge_monat_hinzu(monat=monat,
                              tilgung_euro=tilgung_euro,
                              zinsen_euro=zinsen_euro,
                              restschuld_euro=restschuld_euro,
                              ausschüttung_euro=ausschüttung_euro,
                              kosten_euro=kosten_euro,
                              besondere_kosten_euro=0.,
                              einnahmen_euro=0.,
                              ereignisse=ereignisse)

    def zeige(self,monate_zusammenfassen=1, zeigeparameter=Zeigeparameter()):
        zeigeparameter = Zeigeparameter(zeige_kosten=True,zeige_ausschüttung=True,zeige_tilgung=True,zeige_monatliche_belastung=True,zeige_restschuld=True,zeige_zinsen=True).update(zeigeparameter)
        return Finanzelement.zeige(self,monate_zusammenfassen=monate_zusammenfassen,zeigeparameter=zeigeparameter)


class Einkommen(Finanzelement):
    def __init__(self, einkommen_euro, laufzeit, name="Einkommen", start=Monat(0,1)):
        Finanzelement.__init__(self,name=name, start=start, laufzeit=laufzeit)
        self.einkommen_euro = einkommen_euro

    def berechne_initiale_restschuld_euro(self):
        return 0.
    
    def berechne_nächsten_monat(self, monat, vorheriges_restschuld_euro, plan:Elementplan):
        ereignisse = []
        einnahmen_euro = 0.
        ausschüttung_euro = 0.
        if self.laufzeit == Monat(0,1):
            ereignisse.append(self.name)
            ausschüttung_euro += self.einkommen_euro
        else:
            if monat == self.start:
                ereignisse.append("Beginn " + self.name)
            if monat == self.start + self.laufzeit - 1:
                ereignisse.append("Ende " + self.name)
            einnahmen_euro += self.einkommen_euro

        plan.füge_monat_hinzu(monat=monat,
                              tilgung_euro=0.,
                              zinsen_euro=0.,
                              restschuld_euro=0.,
                              ausschüttung_euro=ausschüttung_euro,
                              kosten_euro=0.,
                              einnahmen_euro=einnahmen_euro,
                              besondere_kosten_euro=0.,
                              ereignisse=ereignisse)

    def zeige(self,monate_zusammenfassen=1, zeigeparameter=Zeigeparameter()):
        zeigeparameter = Zeigeparameter(zeige_ausschüttung=True,zeige_einnahmen=True).update(zeigeparameter)
        return Finanzelement.zeige(self,monate_zusammenfassen=monate_zusammenfassen,zeigeparameter=zeigeparameter)



class Ausgaben(Finanzelement):
    def __init__(self, kosten_euro, name="Ausgaben", start=Monat(0,1), laufzeit=Monat(0,1)):
        Finanzelement.__init__(self,name=name, start=start, laufzeit=laufzeit)
        self.kosten_euro = kosten_euro

    def berechne_initiale_restschuld_euro(self):
        return 0.
    
    def berechne_nächsten_monat(self, monat, vorherige_restschuld_euro, plan:Elementplan):
        ereignisse = []
        kosten_euro = 0.
        besondere_kosten_euro = 0.
        if self.laufzeit != Monat(0,1):
            kosten_euro += self.kosten_euro
            if monat == self.start:
                ereignisse.append("Beginn " + self.name)
            if monat == self.start + self.laufzeit - 1:
                ereignisse.append("Ende " + self.name)
        else:
            besondere_kosten_euro += self.kosten_euro
            if monat == self.start:
                ereignisse.append(self.name)

        plan.füge_monat_hinzu(monat=monat,
                              tilgung_euro=0.,
                              zinsen_euro=0.,
                              restschuld_euro=0.,
                              ausschüttung_euro=0.,
                              kosten_euro=kosten_euro,
                              besondere_kosten_euro=besondere_kosten_euro,
                              einnahmen_euro=0.,
                              ereignisse=ereignisse)

    def zeige(self,monate_zusammenfassen=1, zeigeparameter=Zeigeparameter()):
        zeigeparameter = Zeigeparameter(zeige_kosten=True,zeige_besondere_kosten=True).update(zeigeparameter)
        return Finanzelement.zeige(self,monate_zusammenfassen=monate_zusammenfassen,zeigeparameter=zeigeparameter)



class Eigenkapital(Finanzelement):
    def __init__(self, kapital_euro, name="Eigenkapital", start=Monat(0,1)):
        Finanzelement.__init__(self,name=name, start=start, laufzeit=Monat(0,1))
        self.kapital_euro = kapital_euro

    def berechne_initiale_restschuld_euro(self):
        return 0.
    
    def berechne_nächsten_monat(self, monat, vorherige_restschuld_euro, plan:Elementplan):
        ereignisse = []
        if monat == self.start:
            ereignisse.append(self.name)

        plan.füge_monat_hinzu(monat=monat,
                              tilgung_euro=0.,
                              zinsen_euro=0.,
                              restschuld_euro=0.,
                              ausschüttung_euro=self.kapital_euro,
                              kosten_euro=0.,
                              besondere_kosten_euro=0.,
                              einnahmen_euro=0.,
                              ereignisse=ereignisse)

    def zeige(self,monate_zusammenfassen=1, zeigeparameter=Zeigeparameter()):
        zeigeparameter = Zeigeparameter(zeige_ausschüttung=True).update(zeigeparameter)
        return Finanzelement.zeige(self,monate_zusammenfassen=monate_zusammenfassen,zeigeparameter=zeigeparameter)


class Finanzierungsplan:
    def __init__(self, liste_finanzelemente):
        self.liste_finanzelemente = liste_finanzelemente
    
    def berechne_start_und_ende(self):
        self.start = self.liste_finanzelemente[0].start
        self.ende = self.liste_finanzelemente[0].start + self.liste_finanzelemente[0].laufzeit
        for finanzelement in self.liste_finanzelemente:
            if finanzelement.start < self.start:
                self.start = finanzelement.start
            if finanzelement.start + finanzelement.laufzeit > self.ende:
                self.ende = finanzelement.start + finanzelement.laufzeit

    @staticmethod
    def flatten(xss):
        return [x for xs in xss for x in xs]

    def berechne_plan(self):
        self.berechne_start_und_ende()
        self.pläne = {}
        for finanzelement in self.liste_finanzelemente:
            self.pläne[finanzelement]:Elementplan = finanzelement.berechne_plan()
            self.pläne[finanzelement].füge_leere_monate_am_anfang_hinzu((finanzelement.start - self.start).__int__())
            self.pläne[finanzelement].füge_leere_monate_am_ende_hinzu((self.ende -  (finanzelement.start + finanzelement.laufzeit)).__int__())
        self.plan:Elementplan = Elementplan()
        for monat in Monatsbereich(self.start, self.ende - self.start):
            self.plan.füge_monat_hinzu(monat=monat,
                tilgung_euro = sum([self.pläne[finanzelement].tilgung_euro[(monat-self.start).__int__()] for finanzelement in self.liste_finanzelemente]),
                zinsen_euro = sum([self.pläne[finanzelement].zinsen_euro[(monat-self.start).__int__()] for finanzelement in self.liste_finanzelemente]),
                restschuld_euro = sum([self.pläne[finanzelement].restschuld_euro[(monat-self.start).__int__()] for finanzelement in self.liste_finanzelemente]),
                ausschüttung_euro = sum([self.pläne[finanzelement].ausschüttung_euro[(monat-self.start).__int__()] for finanzelement in self.liste_finanzelemente]),
                kosten_euro = sum([self.pläne[finanzelement].kosten_euro[(monat-self.start).__int__()] for finanzelement in self.liste_finanzelemente]),
                besondere_kosten_euro = sum([self.pläne[finanzelement].besondere_kosten_euro[(monat-self.start).__int__()] for finanzelement in self.liste_finanzelemente]),
                einnahmen_euro = sum([self.pläne[finanzelement].einnahmen_euro[(monat-self.start).__int__()] for finanzelement in self.liste_finanzelemente]),
                ereignisse = Finanzierungsplan.flatten([self.pläne[finanzelement].ereignisse[(monat-self.start).__int__()] for finanzelement in self.liste_finanzelemente])
                )
        return self.plan

    def zeige(self, monate_zusammenfassen=1, tablefmt="html"):
        self.berechne_plan()
        return self.plan.zeige(monate_zusammenfassen,Zeigeparameter(tablefmt=tablefmt,zeige_monatliche_belastung=True,zeige_ausschüttung=True,zeige_einnahmen=True,zeige_besondere_kosten=True,zeige_monatliche_differenz=True,zeige_guthaben=True))