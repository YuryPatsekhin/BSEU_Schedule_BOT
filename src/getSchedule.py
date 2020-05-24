import requests
from bs4 import BeautifulSoup
import imgkit

def request(data):
    options = {
    'encoding': "UTF-8",
    }
    response = requests.post("http://bseu.by/schedule/" ,data="faculty=263&form=10&course=1&group=8064&tname=&period=2&week=15&__act=__id.25.main.inpFldsA.GetSchedule__sp.7.results__fp.4.main")
    soup = BeautifulSoup(response.text, features="html.parser")
    table = soup.find('table')
    imgkit.from_string(str(table), 'out.png', options=options)
