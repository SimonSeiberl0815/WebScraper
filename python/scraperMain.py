from sys import modules

import scraperTermin as sc
import csv
import pandas as pd
import genAi as ga

class Studiengang_For_Csv:
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
        """
        Export a list of Termin objects to a CSV file.

        Parameters:
        terms (list of Termin): The terms to export.
        filename (str): The name of the CSV file to create.
        """
        # Ensure there are termin objects to export
        if not termins:
            raise ValueError("No terms to export.")

        # Get fieldnames from the first termin object
        fieldnames = termins[0].to_dict().keys()

        # Write to CSV
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()  # Write the header row
            for termin in termins:
                writer.writerow(termin.to_dict())

    @staticmethod
    def export_to_excel(termins, filename):
        """
        Export a list of Termin objects to an Excel file.

        Parameters:
        terms (list of Termin): The terms to export.
        filename (str): The name of the Excel file to create.
        """
        # Ensure there are termin objects to export
        if not termins:
            raise ValueError("No terms to export.")

        # Convert list of Termin objects to list of dictionaries
        termin_dicts = [termin.to_dict() for termin in termins]

        # Create a pandas DataFrame
        df = pd.DataFrame(termin_dicts)

        # Write DataFrame to an Excel file
        df.to_excel(filename, index=False, engine='openpyxl')

class Termin_for_csv:
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
        """
        Export a list of Termin objects to a CSV file.

        Parameters:
        terms (list of Termin): The terms to export.
        filename (str): The name of the CSV file to create.
        """
        # Ensure there are termin objects to export
        if not termins:
            raise ValueError("No terms to export.")

        # Get fieldnames from the first termin object
        fieldnames = termins[0].to_dict().keys()

        # Write to CSV
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()  # Write the header row
            for termin in termins:
                writer.writerow(termin.to_dict())

    @staticmethod
    def export_to_excel(termins, filename):
        """
        Export a list of Termin objects to an Excel file.

        Parameters:
        terms (list of Termin): The terms to export.
        filename (str): The name of the Excel file to create.
        """
        # Ensure there are termin objects to export
        if not termins:
            raise ValueError("No terms to export.")

        # Convert list of Termin objects to list of dictionaries
        termin_dicts = [termin.to_dict() for termin in termins]

        # Create a pandas DataFrame
        df = pd.DataFrame(termin_dicts)

        # Write DataFrame to an Excel file
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
        """
        Export a list of Course objects to a CSV file.

        Parameters:
        courses (list of Course): The courses to export.
        filename (str): The name of the CSV file to create.
        """
        # Ensure there are courses to export
        if not datalist:
            raise ValueError("No courses to export.")

        # Get fieldnames from the first course object
        fieldnames = datalist[0].to_dict().keys()



        # Write to CSV
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()  # Write the header row
            for data in datalist:
                writer.writerow(data.to_dict())


    @staticmethod
    def export_to_excel(datalist, filename):
        """
        Export a list of Lva_for_csv objects to an Excel file.

        Parameters:
        lvas (list of Lva_for_csv): The LVA objects to export.
        filename (str): The name of the Excel file to create.
        """
        # Ensure there are Lvas to export
        if not datalist:
            raise ValueError("No Lvas to export.")

        # Convert list of Lva_for_csv objects to list of dictionaries
        data_dicts = [data.to_dict() for data in datalist]

        # Create a pandas DataFrame
        df = pd.DataFrame(data_dicts)

        # Write DataFrame to an Excel file
        df.to_excel(filename, index=False, engine='openpyxl')



class Lva_for_csv:
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
        """
        Convert the Course object to a dictionary.

        Returns:
        dict: A dictionary representation of the Course object.
        """
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
        """
        Export a list of Course objects to a CSV file.

        Parameters:
        courses (list of Course): The courses to export.
        filename (str): The name of the CSV file to create.
        """
        # Ensure there are courses to export
        if not courses:
            raise ValueError("No courses to export.")

        # Get fieldnames from the first course object
        fieldnames = courses[0].to_dict().keys()



        # Write to CSV
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()  # Write the header row
            for course in courses:
                writer.writerow(course.to_dict())


    @staticmethod
    def export_to_excel(lvas, filename):
        """
        Export a list of Lva_for_csv objects to an Excel file.

        Parameters:
        lvas (list of Lva_for_csv): The LVA objects to export.
        filename (str): The name of the Excel file to create.
        """
        # Ensure there are Lvas to export
        if not lvas:
            raise ValueError("No Lvas to export.")

        # Convert list of Lva_for_csv objects to list of dictionaries
        lva_dicts = [lva.to_dict() for lva in lvas]

        # Create a pandas DataFrame
        df = pd.DataFrame(lva_dicts)

        # Write DataFrame to an Excel file
        df.to_excel(filename, index=False, engine='openpyxl')


def write_csv(studiengangNr):
    #sc.scrapStudiengang('https://studienhandbuch.jku.at/index.php')
    studiengang = sc.get_studiengang(studiengangNr)
    studiengaenge = sc.get_all_studiengaenge()
    #sc.scrapLva(studiengang)
    termin_objects = []
    termins = sc.get_all_termine_studiengang(studiengang.skz)
    for termin in termins:

        termin_object = Termin_for_csv(
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


    kurse = sc.get_all_kurse_studiengang(studiengang.skz)
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


    lvas = sc.get_all_lvas_studiengang(studiengang.skz)
    lva_objects = []

    for lva in lvas:
        print('lva: '+lva)
        lva_object = Lva_for_csv(
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

        # Add to the list of Lva_for_csv objects
        lva_objects.append(lva_object)

    Studiengang_For_Csv.export_to_csv(studiengaenge, "Studiengaenge.csv")
    Studiengang_For_Csv.export_to_excel(studiengaenge, "Studiengaenge.xlsx")
    Lva_for_csv.export_to_csv(lva_objects, f"{studiengang.skz}Lvas.csv")
    Lva_for_csv.export_to_excel(lva_objects, f"{studiengang.skz}Lvas.xlsx")
    Kurs_for_csv.export_to_csv(kurs_objects,f"{studiengang.skz}Kurse.csv")
    Kurs_for_csv.export_to_excel(kurs_objects, f"{studiengang.skz}Kurse.xlsx")
    Termin_for_csv.export_to_csv(termin_objects, f"{studiengang.skz}Termine.csv")
    Termin_for_csv.export_to_excel(termin_objects, f"{studiengang.skz}Termine.xlsx")


def main():
    #scraper.srap
    #writeCsv('33526')
    #modul = sc.get_modul('526GLWNEWI13')
    #print(modul)
    #sc.post_modul(modul)
    #sc.scrapSingleModul('https://studienhandbuch.jku.at/175403')
    #sc.summerize_modul('526GLWNEWI13')
    #modul = sc.get_modul('526GLWNEWI13')
    #print(modul)
    #print(studiengang)
    #sc.scrapModul(studiengang)
    #modules = sc.get_all_modules()
    #for modul in modules:
    #    print(modul)
    #print(sc.get_modul('526GLWNEWI13'))
    #sc.scrapLva(studiengang)
    #sc.scrapSingleLva('https://studienhandbuch.jku.at/175410')
    #sc.get_skz('https://studienhandbuch.jku.at/175403')
    #sc.scrapKurs('526GLWNEWIU14')
    #sc.scrap_termin()
    #lva = sc.get_lva('526GLWNDAMV14')
    #print(lva)
    #sc.scrapKurs(lva)
    #kurs = sc.get_kurs('250.711')
    #print(kurs)
    #termin = sc.scrap_termin(kurs)
    lvas = sc.get_all_lvas()
    for lva in lvas:

        sc.scrapKurs(lva)
    kurse = sc.get_all_kurse()
    for kurs in kurse:
        sc.scrap_termin(kurs)

if __name__ == "__main__":
    main()