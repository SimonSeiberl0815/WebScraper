from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
import time
from datetime import datetime
import scraperKurs as Sck

class Termin:
    def __init__(self,terminKey,kursnummer,tag, datum, start, ende, dauer, raum, leiter, studiengang):
        self.terminKey = terminKey
        self.kursnummer = kursnummer
        self.tag = tag
        self.datum = datum
        self.start = start
        self.ende = ende
        self.dauer = dauer
        self.raum = raum
        self.leiter = leiter
        self.studiengang = studiengang

    @classmethod
    def from_dict(cls, data):
        return cls(
            terminKey=data.get('terminKey'),
            kursnummer=data.get('kursnummer'),
            tag=data.get('tag'),
            datum=data.get('datum'),
            start=data.get('start'),
            ende=data.get('ende'),
            dauer=data.get('dauer'),
            raum=data.get('raum'),
            leiter=data.get('leiter'),
            studiengang=data.get('studiengang')
        )
    # Method to convert object to dictionary
    def to_dict(self):
        return {
            'terminKey': self.terminKey,
            'kursnummer': self.kursnummer,
            'tag': self.tag,
            'datum': self.datum,
            'start': self.start,
            'ende': self.ende,
            'dauer': self.dauer,
            'raum': self.raum,
            'leiter': self.leiter,
            'studiengang': self.studiengang
        }

    # String representation of the object
    def __str__(self):
        return (
            f"TerminKey={self.terminKey}\n"
            f"Kursnummer={self.kursnummer}\n"
            f"Tag={self.tag}\n"
            f"datum={self.datum}\n"
            f"start={self.start}\n"
            f"ende={self.ende}\n"
            f"dauer={self.dauer}\n"
            f"raum={self.raum}\n"
            f"leiter={self.leiter}\n"
            f"studiengang={self.studiengang}\n"
        )

def scrap_termin(kurs : Sck.Kurs):
    driver = webdriver.Chrome()
    url = kurs.url
    driver.get(url)
    time.sleep(5)
    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, "lxml")
    table1 = soup.find("table", class_='subinfo')
    table = table1.find("table", {"width": "100%", "align": "center", "cellspacing": "1",
                                  "cellpadding": "3", "border": "0", "summary": True})

    trs = table.findAll('tr')
    result = []
    for tr in trs:
        td = tr.findAll('td')
        if len(td) == 4:
            result.append(td)
    for i in result:
        tag = re.sub(r"[^a-zA-Z0-9.:]", "", i[0].text)
        datum = re.sub(r"[^a-zA-Z0-9.:]", "",i[1].text)
        datumDate = convert_to_serializable_date(datum)
        uhrzeit = re.sub(r"[^a-zA-Z0-9.:]", "",i[2].text)
        startDate, endeDate = convert_to_serializable_time(uhrzeit)
        startTime = datetime.strptime(startDate, "%H:%M:%S").time()
        endeTime = datetime.strptime(endeDate, "%H:%M:%S").time()
        raum = re.sub(r"[^a-zA-Z0-9.:]", "", i[3].text)
        dummy_date = datetime(2000, 1, 1)
        start_datetime = datetime.combine(dummy_date, startTime)
        end_datetime = datetime.combine(dummy_date, endeTime)
        dauer = ((end_datetime - start_datetime).total_seconds()) /60
        kursnummer = kurs.kursnummer
        leiter = kurs.leiter
        studiengang = kurs.studiengang
        terminKey = kursnummer+'/'+datumDate+'/'+startDate+'/'+ studiengang
        termin = Termin(terminKey=terminKey,kursnummer=kursnummer,tag=tag,datum=datumDate,start=startDate,ende=endeDate,dauer=dauer,raum=raum,leiter=leiter,studiengang=studiengang)
        post_termin(termin)

def post_termin(termin: Termin):
    url = 'http://localhost:8080/termin'
    data = termin.to_dict()
    response = requests.post(url, json=data)
    print(termin.terminKey+' : '+str(response.status_code))

def get_all_termine():
    url = "http://localhost:8080/termin"
    response = requests.get(url)
    if response.status_code == 200:
        termine = response.json()
        print(f"getAllTermin: {response.status_code}")
        return [Termin.from_dict(term) for term in termine]
    else:
        print(f"Error: {response.status_code}")
        return None

def get_all_termine_studiengang(studiengang):
    url = f"http://localhost:8080/termin/studiengang/{studiengang}"
    response = requests.get(url)

    if response.status_code == 200:
        termine = response.json()
        print(f"getAllTermine{studiengang}: {response.status_code}")
        return [Termin.from_dict(termin) for termin in termine]
    else:
        print(f"Error: {response.status_code}")
        return None

def split_date(time_string):
    start_time = time_string[:5]  # First 5 characters: "12:00"
    end_time = time_string[5:]
    return start_time, end_time

def convert_to_serializable_date(datum):
    return datetime.strptime(datum, "%d.%m.%y").date().isoformat()

def convert_to_serializable_time(uhrzeit):
    start, ende = split_date(uhrzeit)
    start_time = datetime.strptime(start, "%H:%M").time().isoformat()
    ende_time = datetime.strptime(ende, "%H:%M").time().isoformat()
    return start_time, ende_time

def getNumberOfTermine(kursnummer):
    url = f'http://localhost:8080/termin/{kursnummer}/termine/count'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:

        print(f"Failed to fetch Modul with ID {id}: {response.status_code}")
        return None




