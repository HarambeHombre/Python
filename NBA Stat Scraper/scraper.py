import requests
from bs4 import BeautifulSoup
import datetime

dt = datetime.date.today()

# URL = 'http://localhost:5001'
URL = 'https://www.nba.com/stats'
response = requests.get(URL)

html_doc = response.text
soup = BeautifulSoup(html_doc, 'html.parser')

# FIND TABLES
sections = soup.find_all('section')
for section in sections:
    if section.find('table'):
        tables = section.find_all('table')
        title = section.find('h1')
        if title:
            print(f'\n{"-"*40} \n --{title.text.strip()}-- (Today\'s Leaders {dt}) \n{"-"*40} \n')
        for table in tables:
            rows = table.find_all('tr')
            header = table.find_previous('h2').text.strip()
            print(header)
            print('--------------------')
            for row in rows:
                a_data = row.find_all('a')
                span = a_data[0].find_next('span').text.strip()
                if len(a_data) == 2:
                    if span:
                        name =f'{a_data[0].text.strip()}-{span}'
                    else:
                        name = a_data[0].text.strip()

                    value = float(a_data[1].text.strip())
                    result = (name, value)
                    print(result)
                if len(a_data) == 1:
                    name = a_data[0].text.strip()
                    value = a_data[0].find_next('td').text.strip()
                    result = (name, value)
                    print(result)
            print('\n')