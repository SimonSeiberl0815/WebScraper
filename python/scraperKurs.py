from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import scraperLva as Scl
count = 0

class Kurs:
    def __init__(self, kursnummer, lva,name, leiter,url, studiengang ):
        self.kursnummer = kursnummer
        self.lva = lva
        self.name = name
        self.leiter = leiter
        self.url = url
        self.studiengang = studiengang

    def to_dict(self):
        """
        Converts the Kurs object into a dictionary.
        """
        return {
            "kursnummer": self.kursnummer,
            "lva": self.lva,
            "name": self.name,
            "leiter": self.leiter,
            "url": self.url,
            "studiengang": self.studiengang,
        }

    @classmethod
    def from_dict(cls, data):
        """
        Creates a Kurs object from a dictionary.
        """
        return cls(
            kursnummer=data.get("kursnummer"),
            lva=data.get("lva"),
            name=data.get("name"),
            leiter=data.get("leiter"),
            url=data.get("url"),
            studiengang=data.get("studiengang"),
        )

    def __str__(self):
        """
        Returns a string representation of the Kurs object.
        """
        return (
            f"Kursnummer: {self.kursnummer}\n"
            f"Lva: {self.lva}\n"
            f"Name: {self.name}\n"
            f"Leiter: {self.leiter}\n"
            f"Url: {self.url}\n"
            f"Studiengang: {self.studiengang}\n"
        )
def scrap_kurs(lva : Scl.Lva):
    lvanummer = lva.lvanummer
    studiengang = lva.studiengang
    driver = webdriver.Chrome()

    # Open the URL
    url = (
        f"https://www.kusss.jku.at/kusss/coursecatalogue-searchlvareg.action?sortParam0courses=lvaName&asccourses=true&showFilters=false&abhart=all&lvasearch={lvanummer}&direct=true&lvaName=&organisationalHint=&lastname=&firstname=&lvaNr=&klaId=&type=all&curriculumContentKey=all&orgid=Alle&language=all&day=all&timefrom=all&timeto=all&room=all"
    )
    driver.get(url)

    # Wait for the JavaScript to load
    time.sleep(5)  # Adjust based on website load time

    # Extract content from the rendered page
    html = driver.page_source

    # Close the driver
    driver.quit()

    soup = BeautifulSoup(html, "lxml")
    table = soup.find("table", {"width": "100%", "border": "0", "cellspacing": "1", "cellpadding": "3"})
    result = []
    if table:
        for tr in table.find_all("tr"):  # Find all rows in the table
            row_data = []
            tds = tr.find_all("td")

            if len(tds) >= 4:
                a_tag = tds[0].find("a")
                if a_tag:
                    kursnummer = a_tag.text.strip()
                    url = "https://www.kusss.jku.at/kusss/"+a_tag['href']
                else:
                    kursnummer = None
                    url = None

                name = tds[1].text.strip() if len(tds) > 1 else None
                leiter = tds[4].text.strip() if len(tds) > 3 else None
                row_data = [kursnummer, name, url, leiter]
                if row_data:
                    result.append(row_data)

    for row in result:
        kursnummer, name, url, leiter = row
        kurs = Kurs(kursnummer=kursnummer, lva=lvanummer, name=name, leiter=leiter, url=url, studiengang=studiengang)
        post_kurs(kurs)


def post_kurs(kurs: Kurs):
    url = 'http://localhost:8080/kurs'
    data = kurs.to_dict()
    response = requests.post(url, json=data)
    print(kurs.kursnummer+' : ' + str(response.status_code))

def get_kurs(id):
    url = f'http://localhost:8080/kurs/{id}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"getKurs: {response.status_code}")
        return Kurs.from_dict(data)
    else:
        print(f"Failed to fetch Modul with ID {id}: {response.status_code}")
        return None

def get_all_kurse():
    url = "http://localhost:8080/kurs"
    response = requests.get(url)
    if response.status_code == 200:
        kurse = response.json()
        print(f"getAllKurse: {response.status_code}")
        return [Kurs.from_dict(kur) for kur in kurse]
    else:
        print(f"Error: {response.status_code}")
        return None

def get_all_kurse_studiengang(studiengang):
    url = f"http://localhost:8080/kurs/studiengang/{studiengang}"
    response = requests.get(url)

    if response.status_code == 200:
        kurse = response.json()
        print(f"getAllKurse{studiengang}: {response.status_code}")
        return [Kurs.from_dict(kurs) for kurs in kurse]
    else:
        print(f"Error: {response.status_code}")
        return None

