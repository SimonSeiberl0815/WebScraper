import scraperKurs as Sck
import scraperLva as Scl
import scraperTermin as Sct
import scraperStudiengang as Scs
import scraperModul as Scm
import csv
import pandas as pd

import os



class StudiengangCsv:
    def __init__(self,skz, name, level, url):
        self.skz = skz
        self.name = name
        self.level = level
        self.url = url

    def to_dict(self):
        return {
            'skz': self.skz,
            'name': self.name,
            'level': self.level,
            'url': self.url
        }
    @staticmethod
    def export_to_csv(termins, filename):
        if not termins:
            raise ValueError("No terms to export.")

        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        fieldnames = termins[0].to_dict().keys()

        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for termin in termins:
                writer.writerow(termin.to_dict())

    @staticmethod
    def export_to_excel(termins, filename):
        if not termins:
            raise ValueError("No terms to export.")

        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        termin_dicts = [termin.to_dict() for termin in termins]
        df = pd.DataFrame(termin_dicts)
        df.to_excel(filename, index=False, engine='openpyxl')

class TerminCsv:
    def __init__(self, kursnummer, tag, datum, start, ende, dauer, raum, leiter, studiengang):
        self.kursnummer = kursnummer
        self.tag = tag
        self.datum = datum
        self.start = start
        self.ende = ende
        self.dauer = dauer
        self.raum = raum
        self.leiter = leiter
        self.studiengang = studiengang

    def to_dict(self):
        return {
            "kursnummer": self.kursnummer,
            "tag": self.tag,
            "datum": self.datum,
            "start": self.start,
            "ende": self.ende,
            "dauer": self.dauer,
            "raum": self.raum,
            "leiter": self.leiter,
            "studiengang": self.studiengang,
        }

    @staticmethod
    def export_to_csv(termins, filename):
        if not termins:
            raise ValueError("No terms to export.")

        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        fieldnames = termins[0].to_dict().keys()

        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()  # Write the header row
            for termin in termins:
                writer.writerow(termin.to_dict())

    @staticmethod
    def export_to_excel(termins, filename):
        if not termins:
            raise ValueError("No terms to export.")

        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        termin_dicts = [termin.to_dict() for termin in termins]

        df = pd.DataFrame(termin_dicts)

        df.to_excel(filename, index=False, engine='openpyxl')

class Kurs_for_csv:
    def __init__(self, kursnummer, lva,name, leiter, studiengang ):
        self.kursnummer = kursnummer
        self.lva = lva
        self.name = name
        self.leiter = leiter
        self.studiengang = studiengang

    def to_dict(self):
        return {
            "kursnummer": self.kursnummer,
            "lva": self.lva,
            "name": self.name,
            "leiter": self.leiter,
            "studiengang": self.studiengang,
        }

    @staticmethod
    def export_to_csv(datalist, filename):
        if not datalist:
            raise ValueError("No courses to export.")

        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        fieldnames = datalist[0].to_dict().keys()

        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()  # Write the header row
            for data in datalist:
                writer.writerow(data.to_dict())


    @staticmethod
    def export_to_excel(datalist, filename):
        if not datalist:
            raise ValueError("No courses to export.")

        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        data_dicts = [data.to_dict() for data in datalist]

        df = pd.DataFrame(data_dicts)

        df.to_excel(filename, index=False, engine='openpyxl')



class LvaCsv:
    def __init__(self,lvanummer,name,typ, studiengang, modul, etcs, verantwortlicher, jahr, stunden, universitaet,vorraussetzungen,ziele, inhalte, lehrmethoden, sprache, literatur):
        self.lvanummer = lvanummer
        self.name = name
        self.typ = typ
        self.studiengang = studiengang
        self.modul = modul
        self.etcs = etcs
        self.verantwortlicher = verantwortlicher
        self.jahr = jahr
        self.stunden = stunden
        self.universitaet = universitaet
        self.vorraussetzungen = vorraussetzungen
        self.ziele = ziele
        self.inhalte = inhalte
        self.lehrmethoden = lehrmethoden
        self.sprache = sprache
        self.literatur = literatur


    def to_dict(self):
        return {
            "lvanummer": self.lvanummer,
            "name": self.name,
            "typ": self.typ,
            "studiengang": self.studiengang,
            "modul": self.modul,
            "etcs": self.etcs,
            "verantwortlicher": self.verantwortlicher,
            "jahr": self.jahr,
            "stunden": self.stunden,
            "universitaet": self.universitaet,
            "vorraussetzungen": self.vorraussetzungen,
            "ziele": self.ziele,
            "inhalte": self.inhalte,
            "lehrmethoden": self.lehrmethoden,
            "sprache": self.sprache,
            "literatur": self.literatur,
        }

    @staticmethod
    def export_to_csv(courses, filename):
        if not courses:
            raise ValueError("No courses to export.")

        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        fieldnames = courses[0].to_dict().keys()

        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()  # Write the header row
            for course in courses:
                writer.writerow(course.to_dict())


    @staticmethod
    def export_to_excel(lvas, filename):
        if not lvas:
            raise ValueError("No Lvas to export.")

        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        lva_dicts = [lva.to_dict() for lva in lvas]

        # Create a pandas DataFrame
        df = pd.DataFrame(lva_dicts)

        # Write DataFrame to an Excel file
        df.to_excel(filename, index=False, engine='openpyxl')


def write_csv(studiengangNr):

    studiengang = Scs.get_studiengang(studiengangNr)
    studiengaenge = Scs.get_all_studiengaenge()

    termin_objects = []
    termins = Sct.get_all_termine_studiengang(studiengang.skz)
    for termin in termins:

        termin_object = TerminCsv(
            kursnummer=termin.kursnummer,
            tag=termin.tag,
            datum=termin.datum,
            start=termin.start,
            ende=termin.ende,
            dauer=termin.dauer,
            raum=termin.raum,
            leiter=termin.leiter,
            studiengang=termin.studiengang
        )
        termin_objects.append(termin_object)


    kurse = Sck.get_all_kurse_studiengang(studiengang.skz)
    kurs_objects = []
    for kurs in kurse:
        kurs_object = Kurs_for_csv(
            kursnummer = kurs.kursnummer,
            lva = kurs.lva,
            name= kurs.name,
            leiter = kurs.leiter,
            studiengang = kurs.studiengang
        )
        kurs_objects.append(kurs_object)


    lvas = Scl.get_all_lvas_studiengang(studiengang.skz)
    print(studiengang.skz)
    print(Scl.get_all_lvas_studiengang(studiengang.skz))
    lva_objects = []

    for lva in lvas:
        lva_object = LvaCsv(
            lvanummer=lva.lvanummer,
            name=lva.name,
            typ=lva.typ,
            studiengang=lva.studiengang,
            modul=lva.modul,
            etcs=lva.etcs,
            verantwortlicher=lva.verantwortlicher,
            jahr=lva.jahr,
            stunden=lva.stunden,
            universitaet=lva.universitaet,
            vorraussetzungen=lva.vorraussetzungen,  # Use the resolved value
            ziele=lva.ziele,
            inhalte=lva.inhalte,
            lehrmethoden=lva.lehrmethoden,
            sprache=lva.sprache,
            literatur=lva.literatur,
        )

        # Add to the list of LvaCsv objects
        lva_objects.append(lva_object)

    StudiengangCsv.export_to_csv(studiengaenge, "exports/Studiengaenge.csv")
    StudiengangCsv.export_to_excel(studiengaenge, "exports/Studiengaenge.xlsx")
    LvaCsv.export_to_csv(lva_objects, f"exports/{studiengang.skz}/{studiengang.skz}Lvas.csv")
    LvaCsv.export_to_excel(lva_objects, f"exports/{studiengang.skz}/{studiengang.skz}Lvas.xlsx")
    Kurs_for_csv.export_to_csv(kurs_objects,f"exports/{studiengang.skz}/{studiengang.skz}Kurse.csv")
    Kurs_for_csv.export_to_excel(kurs_objects, f"exports/{studiengang.skz}/{studiengang.skz}Kurse.xlsx")
    TerminCsv.export_to_csv(termin_objects, f"exports/{studiengang.skz}/{studiengang.skz}Termine.csv")
    TerminCsv.export_to_excel(termin_objects, f"exports/{studiengang.skz}/{studiengang.skz}Termine.xlsx")


def main():
    #Scs.scrap_studiengang()
    skz = "033526"
    studiengang=Scs.get_studiengang(skz)

    Scm.scrap_modul(studiengang)
    Scl.scrap_lva(studiengang)
    lvas = Scl.get_all_lvas_studiengang(skz);
    print(lvas)
    for lva in lvas:
        Sck.scrap_kurs(lva)
    kurse = Sck.get_all_kurse_studiengang(skz)
    for kurs in kurse:
        Sct.scrap_termin(kurs)

    write_csv(skz)
if __name__ == "__main__":
    main()