from bs4 import BeautifulSoup
import requests
import re
import time
from enum import Enum
import scraperStudiengang as Scs
import scraperModul as Scm
import compress_decompress as Cd
import genAi as ga

class Lva:
    def __init__(self,lvanummer, name,typ, studiengang, modul,etcs, verantwortlicher,jahr,stunden,universitaet, url, vorraussetzungen=None, ziele=None, inhalte=None, beurteilung=None, lehrmethoden=None, sprache=None, literatur=None):
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
        self.url = url
        self.vorraussetzungen = vorraussetzungen
        self.ziele = ziele
        self.inhalte = inhalte
        self.beurteilung = beurteilung
        self.lehrmethoden = lehrmethoden
        self.sprache = sprache
        self.literatur = literatur


    def to_dict(self):
        return {
            'lvanummer': self.lvanummer,
            'name': self.name,
            'typ': self.typ,
            'studiengang': self.studiengang,
            'modul': self.modul,
            'etcs': self.etcs,
            'verantwortlicher': self.verantwortlicher,
            'jahr': self.jahr,
            'stunden': self.stunden,
            'universitaet': self.universitaet,
            'url': self.url,
            'vorraussetzungen': self.vorraussetzungen,
            'ziele': self.ziele,
            'inhalte': self.inhalte,
            'beurteilung': self.beurteilung,
            'lehrmethoden': self.lehrmethoden,
            'sprache': self.sprache,
            'literatur': self.literatur

        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            lvanummer=data.get('lvanummer'),
            name=data.get('name'),
            typ=data.get('typ'),
            studiengang=data.get('studiengang'),
            modul=data.get('modul'),
            etcs=data.get('etcs'),
            verantwortlicher=data.get('verantwortlicher'),
            jahr=data.get('jahr'),
            stunden=data.get('stunden'),
            universitaet=data.get('universitaet'),
            url=data.get('url'),
            vorraussetzungen=Cd.decompress_string(data.get('vorraussetzungen')),
            ziele=Cd.decompress_string(data.get('ziele')),
            inhalte=Cd.decompress_string(data.get('inhalte')),
            beurteilung=Cd.decompress_string(data.get('beurteilung')),
            lehrmethoden=Cd.decompress_string(data.get('lehrmethoden')),
            sprache=Cd.decompress_string(data.get('sprache')),
            literatur=Cd.decompress_string(data.get('literatur'))

        )

    def __str__(self):
        return (
            f"LVA-Nummer: {self.lvanummer}\n"
            f"Name: {self.name}\n"
            f"Typ: {self.typ}\n"
            f"Studiengang: {self.studiengang or 'N/A'}\n"
            f"Modul: {self.modul}\n"
            f"ETCS: {self.etcs}\n"
            f"Verantwortlicher: {self.verantwortlicher}\n"
            f"Jahr: {self.jahr}\n"
            f"Stunden: {self.stunden}\n"
            f"Universitaet: {self.universitaet}\n"
            f"URL: {self.url}\n"
            f"Voraussetzungen: {self.vorraussetzungen or 'N/A'}\n"
            f"Ziele: {self.ziele or 'N/A'}\n"
            f"Inhalte: {self.inhalte or 'N/A'}\n"
            f"Beurteilung: {self.beurteilung or 'N/A'}\n"
            f"Lehrmethoden: {self.lehrmethoden or 'N/A'}\n"
            f"Sprache: {self.sprache or 'N/A'}\n"
            f"Literatur: {self.literatur or 'N/A'}\n"

        )

def scrap_lva(studiengang : Scs.Studiengang):
    url = studiengang.url
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    data = soup.findAll('a',href=True,class_='currlist')

    for datapoint in data:
        scrap_single_lva(datapoint['href'])

def scrap_single_lva(url):
    td_map = {
        'Anmeldevoraussetzungen': 'vorraussetzungen',
        'Ziele': 'ziele',
        'Lehrinhalte': 'inhalte',
        'Beurteilungskriterien' : 'beurteilung',
        'Lehrmethoden' : 'lehrmethoden',
        'Abhaltungssprache' : 'sprache',
        'Sonstige Informationen': 'infos',
        'Literatur': 'literatur'
    }
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')

    heading = soup.find('h3').text
    lvanummer, typ, name = split_lva(heading)
    if match_enum(typ):
        name = typ +' '+name
        typ = get_course_type(typ)
        studiengang = get_skz(url).strip()
        modul = get_modulnr(url)
        if modul != None:
            modul = modul.strip()
        subject = soup.find('tr',class_='darkcell')
        td_subject = subject.find_all('td')
        etcs = td_subject[0].text.strip()
        jahr = td_subject[1].text.strip()
        verantwortlicher = td_subject[3].text.strip()
        stunden = td_subject[4].text.strip()
        universitaet = td_subject[5].text.strip()
        lva = Lva(lvanummer=lvanummer,name = name,typ=typ,studiengang=studiengang,modul=modul,etcs=etcs,verantwortlicher=verantwortlicher,jahr=jahr,stunden=stunden,universitaet=universitaet,url=url)

        tableMod = soup.find('table',style=lambda s: s and
                                                     "width: 100%" in s and
                                                     "border-spacing: 0px" in s and
                                                     "border-collapse: collapse" in s)
        rows = tableMod.find_all('tr')
        for row in rows:
            if row:
                tds = row.find_all('td')
                if len(tds) == 2:
                    first_td = tds[0]
                    # Check if the text in the first <td> matches any key in the dictionary
                    if first_td.get_text(strip=True) in td_map:
                        second_td = tds[1]
                        # Dynamically assign the second <td> value to the correct attribute in the object
                        attribute_name = td_map[first_td.get_text(strip=True)]
                        compressed_value = Cd.compress_string(second_td.get_text(strip=True))
                        setattr(lva, attribute_name, compressed_value)
        post_lva(lva)
        summarize_lva(lvanummer)
        time.sleep(50)




def post_lva(lva: Lva):
    url = 'http://localhost:8080/lva'
    data = lva.to_dict()
    response = requests.post(url, json=data)
    print(lva.lvanummer+' : '+str(response.status_code))

def get_lva(id):
    url = f'http://localhost:8080/lva/{id}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"getLva: {response.status_code}")
        return Lva.from_dict(data)
    else:
        print(f"Failed to fetch Modul with ID {id}: {response.status_code}")
        return None

def get_all_lvas():
    url = "http://localhost:8080/lva"
    response = requests.get(url)

    if response.status_code == 200:
        lvas = response.json()
        print(f"getAllLvas: {response.status_code}")
        return [Lva.from_dict(lv) for lv in lvas]
    else:
        print(f"Error: {response.status_code}")
        return None
def get_all_lvas_studiengang(studiengang):
    url = f"http://localhost:8080/lva/studiengang/{studiengang}"
    response = requests.get(url)

    if response.status_code == 200:
        lvas = response.json()
        print(f"getAllLvas{studiengang}: {response.status_code}")
        return [Lva.from_dict(lv) for lv in lvas]
    else:
        print(f"Error: {response.status_code}")
        return None

#summarize lva with genAi script
def summarize_lva(id):
    lva = get_lva(id)
    modulnummer = lva.modul
    modul = Scm.get_modul(str(modulnummer)) if lva.modul is not None else None
    if lva.vorraussetzungen.startswith('Siehe') and modul:
        vorraussetzungen = modul.voraussetzungen
    else:
        vorraussetzungen = ga.get_course_summary(lva.vorraussetzungen,'requirements')

    lva.vorraussetzungen=Cd.compress_string(vorraussetzungen)

    if lva.ziele.startswith('Siehe') and modul:
        ziele = modul.ziele
    else:
        ziele = ga.get_course_summary(lva.ziele,'goals')
    lva.ziele = Cd.compress_string(ziele)
    if lva.inhalte.startswith('Siehe') and modul:
        inhalte = modul.lerninhalte
    else:
        inhalte = ga.get_course_summary(lva.inhalte,'topics')
    lva.inhalte = Cd.compress_string(inhalte)

    if lva.lehrmethoden.startswith('Siehe') and modul:
        lva.lehrmethoden = Cd.compress_string(modul.infos)

    else:
        lva.lehrmethoden = Cd.compress_string(ga.get_course_summary(lva.lehrmethoden,'methods'))

    if lva.literatur.startswith('Siehe') and modul:
        literatur = modul.books
    else:
        literatur = ga.get_course_summary(lva.literatur,'books (author, title)')
    lva.literatur = Cd.compress_string(literatur)

    lva.sprache= Cd.compress_string(lva.sprache)
    lva.beurteilung = Cd.compress_string(lva.beurteilung)
    post_lva(lva)

#splits lva heading in lvanummer, typ und name
def split_lva(input_string):
    match = re.match(r'\[\s*(.*?)\s*\]\s*([A-Z]{2})\s*(.*)', input_string)
    if match:
        content_in_brackets = match.group(1)
        two_char_string = match.group(2)
        rest_of_string = match.group(3)
        return content_in_brackets, two_char_string, rest_of_string
    return None, None, None

#enum for different lva types
class CourseTypeEnum(Enum):
    VL = "VL"  # Vorlesung
    UE = "UE"  # Uebung
    PR = "PR"  # Praktikum
    SE = "SE"  # Seminar
    PS = "PS"  # Proseminar
    KS = "KS"  # Kurs
    KV = "KV"  # Kombinierte Lva

#get String representation for lva zype
def get_course_type(two_char_string):
    try:
        match = CourseTypeEnum[two_char_string]
        if match == CourseTypeEnum.VL:
            return "Vorlesung"
        elif match == CourseTypeEnum.UE:
            return "Uebung"
        elif match == CourseTypeEnum.PR:
            return "Praktikum"
        elif match == CourseTypeEnum.SE:
            return "Seminar"
        elif match == CourseTypeEnum.PS:
            return "Proseminar"
        elif match == CourseTypeEnum.KS:
            return "Kurs"
        elif match == CourseTypeEnum.KV:
            return "Kombinierte Lva"
        else:
            return "Unknown course type"
    except KeyError:
        return "Invalid two-character string"

#boolean to check if valid lva
def match_enum(two_char_string):
    try:
        CourseTypeEnum[two_char_string]
        return True
    except KeyError:
        return False
#navigates along the bread-crumb-trail to match every Lva with a Studienkennzahl
def get_skz(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    skz = soup.find('li',class_='bread-crumb-trail').find('a')
    return scrap_skz(skz['href'])

def scrap_skz(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text,'lxml')
    heading = soup.find('h3').text
    match = re.search(r"\(UK (\d+)/(\d+)\)", heading)

    if match:
        numbers = match.group(1) + match.group(2)
        return numbers
    else:
        return None

#navigates along the bread-crumb-trail to match Lvas with a Moduls
def get_modulnr(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    modulnumbers = soup.findAll('li',class_='bread-crumb-trail')
    modulnr = modulnumbers[-1].find('a') if modulnumbers else None
    return scrap_modulnr(modulnr['href'])

def scrap_modulnr(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    heading = soup.find('h3').text
    match = re.search(r"\[([^\]]+)\]\s+(\w+)", heading)

    if match:
        bracket_content = match.group(1)  # Content inside the brackets
        first_word = match.group(2)      # First word from the rest of the string
        if first_word == 'Modul':
            return bracket_content
        else:
            return None
    else:
        return None