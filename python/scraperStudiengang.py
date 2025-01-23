from bs4 import BeautifulSoup
import requests
import re

class Studiengang:
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

    @classmethod
    def from_dict(cls, data):
        return cls(
            skz=data.get('skz'),
            name=data.get('name'),
            level=data.get('level'),
            url=data.get('url')
        )

    def __str__(self):
        return (
            f"SKZ: {self.skz}\n"
            f"Name: {self.name}\n"
            f"Level: {self.level}\n"
            f"URL: {self.url}\n"
        )
#scrap all Studiengänge by going through every entry in table in index.php
def scrap_studiengang():
    url = "https://studienhandbuch.jku.at/index.php"
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    BASE_URL = "https://studienhandbuch.jku.at/"
    data = soup.findAll('a',href=re.compile(r'^curr/'))
    for datapoint in data:
        full_url = requests.compat.urljoin(BASE_URL, datapoint['href'])
        scrap_single_studiengang(full_url)

#scrap one studiengang by getting data from heading and post to database
def scrap_single_studiengang(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    heading = soup.find('h3').text
    if heading.startswith('Bachelorstudium') or heading.startswith('Masterstudium')or heading.startswith('Doktoratsstudium'):
        level, skz, name = split_string(heading)
        print(skz+' '+name+' '+level+' '+url)
        studiengang = Studiengang(skz=skz,name=name,level=level,url=url)
        post_studiengang(studiengang)

def post_studiengang(studiengang: Studiengang):
    url = 'http://localhost:8080/studiengang'
    data = studiengang.to_dict()
    response = requests.post(url, json=data)
    print(response.status_code)

def get_studiengang(id):
    url = f'http://localhost:8080/studiengang/{id}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return Studiengang.from_dict(data)
    else:
        print(f"Failed to fetch Modul with ID {id}: {response.status_code}")
        return None

def get_all_studiengaenge():
    url = "http://localhost:8080/studiengang"
    response = requests.get(url)

    if response.status_code == 200:
        studiengaenge = response.json()  # Convert JSON response to a Python list of dictionaries
        return [Studiengang.from_dict(stg) for stg in studiengaenge]  # Convert each dictionary to a Modul object
    else:
        print(f"Error: {response.status_code}")
        return None

#spilts heading string
#input: string like Bachelorstudium Betriebswirtschaftslehre (UK 033/515)
#return: level,skz and name
def split_string(input_string):
    match = re.match(r"(\w+)\s+(.*)\s+\(([^)]+)\)", input_string)

    if not match:
        raise ValueError("Input string is not in the expected format")

    first_word = match.group(1)
    rest = match.group(2)
    in_brackets_raw = match.group(3)
    numbers_in_brackets = ''.join(filter(str.isdigit, in_brackets_raw))

    return first_word, numbers_in_brackets, rest