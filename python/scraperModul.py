from bs4 import BeautifulSoup
import requests
import re
import time
import scraperStudiengang as Scs
import compress_decompress as Cd
import genAi as ga

class Modul:
    def __init__(self, modulnummer, name, studiengang, url, voraussetzungen=None, ziele=None, lerninhalte=None, infos=None, books=None):
        self.modulnummer = modulnummer
        self.name = name
        self.studiengang = studiengang
        self.url = url
        self.voraussetzungen = voraussetzungen
        self.ziele = ziele
        self.lerninhalte = lerninhalte
        self.infos = infos
        self.books = books

    @classmethod
    def from_dict(cls, data):
        return cls(
            modulnummer=data.get('modulnummer'),
            name=data.get('name'),
            studiengang=data.get('studiengang'),
            url=data.get('url'),
            voraussetzungen=Cd.decompress_string(data.get('vorraussetzungen')),
            ziele=Cd.decompress_string(data.get('ziele')),
            lerninhalte=Cd.decompress_string(data.get('lerninhalte')),
            infos=Cd.decompress_string(data.get('infos')),
            books=Cd.decompress_string(data.get('books'))
        )

    def to_dict(self):
        return {
            'modulnummer': self.modulnummer,
            'name': self.name,
            'vorraussetzungen': self.voraussetzungen,
            'ziele': self.ziele,
            'lerninhalte': self.lerninhalte,
            'infos': self.infos,
            'studiengang': self.studiengang,
            'books': self.books,
            'url': self.url
        }
    def __str__(self):
        return (
            f"Modulnummer: {self.modulnummer}\n"
            f"Name: {self.name}\n"
            f"Studiengang: {self.studiengang or 'N/A'}\n"
            f"URL: {self.url}\n"
            f"Voraussetzungen: {self.voraussetzungen}\n"
            f"Ziele: {self.ziele or 'N/A'}\n"
            f"Lerninhalte: {self.lerninhalte or 'N/A'}\n"
            f"Infos: {self.infos or 'N/A'}\n"
            f"Books: {self.books or 'N/A'}"
        )

#scrap all Module for a Studiengang
def scrap_modul(studiengang: Scs.Studiengang):
    url = studiengang.url
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    data = soup.findAll('a',href=True,class_='currlist')
    for datapoint in data:
        scrap_single_modul(datapoint['href'])

#scrap a Modul
#moduls ar not allways equal in the web source function only assigns what is there
def scrap_single_modul(url):
    td_map = {
        'Anmeldevoraussetzungen': 'voraussetzungen',
        'Ziele': 'ziele',
        'Lehrinhalte': 'lerninhalte',
        'Sonstige Informationen': 'infos',
        'Literatur': 'books'
    }
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')

    heading = soup.find('h3').text
    modulnummer, name = split_modul(heading)
    if name.startswith('Modul'):
        studiengang = get_skz(url)
        modul = Modul(modulnummer=modulnummer,name = name,studiengang=studiengang,url=url)

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
                        setattr(modul, attribute_name, compressed_value)
        post_modul(modul)
        summarize_modul(modulnummer)
        time.sleep(60)



def post_modul(modul: Modul):
    url = 'http://localhost:8080/modul'
    data = modul.to_dict()
    response = requests.post(url, json=data)
    print(modul.modulnummer+ ' : ' + str(response.status_code))

def get_modul(id):
    url = f'http://localhost:8080/modul/{id}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return Modul.from_dict(data)
    else:
        print(f"Failed to fetch Modul with ID{id}: {response.status_code}")
        return None

def get_all_modules():
    url = "http://localhost:8080/modul"
    response = requests.get(url)

    if response.status_code == 200:
        modules = response.json()
        return [Modul.from_dict(mod) for mod in modules]
    else:
        print(f"Error: {response.status_code}")
        return None

def get_all_modules_studiengang(studiengang):
    url = f"http://localhost:8080/modul/studiengang/{studiengang}"
    response = requests.get(url)

    if response.status_code == 200:
        module = response.json()
        print(response.status_code)
        return [Modul.from_dict(modul) for modul in module]
    else:
        print(f"Error: {response.status_code}")
        return None

#navigates along the bread-crumb-trail to match every Modul with a Studienkennzahl
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

#split Modul heading into modulnummer and name
def split_modul(input_string):
    match = re.match(r'\[\s*(.*?)\s*\]\s*(.*)', input_string)

    if match:
        return match.group(1), ' '.join(match.group(2).split())
    return None, None

#summarize modul with genAi script
def summarize_modul(id):
    modul = get_modul(id)
    modul.voraussetzungen = Cd.compress_string(ga.get_course_summary(modul.voraussetzungen,'requirements'))
    modul.ziele = Cd.compress_string(ga.get_course_summary(modul.ziele,'goals'))
    modul.lerninhalte = Cd.compress_string(ga.get_course_summary(modul.lerninhalte,'topics'))
    text = modul.infos
    split_pattern = r"(Lehrmethoden:)(.*?)(Literatur:)(.*)"
    match = re.search(split_pattern, text, re.DOTALL)
    if match:
        lehrmethoden = match.group(2).strip()
        literatur = match.group(4).strip()
        modul.infos = Cd.compress_string(ga.get_course_summary(lehrmethoden,'methods'))
        modul.books = Cd.compress_string(ga.get_course_summary(literatur,'books (author, title)'))
    else:
        modul.infos = None
    post_modul(modul)